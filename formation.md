# 1) Créer la classe de Base

=> Fichier Models/Base.py

Ici on doit créer une classe de base pour nos entités, qui nous servira pour créer
de nouvelles classes dérivée qui pourront être liées à une DB.

```python
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass
```

# 2) Créer vos entités : 

=> Fichiers Models/user.py Models/Basket.py

Ici on va déclarer des variables static qui vont définir les différents parametres 
de notre table : 

__tablename__ => nom de la table

pour les champs : 
nomDuChamp: Mapped[TYPE] = mapped_column(?contraintes?)

id: Mapped[int] = mapped_column(primary_key=True)

Crée un champ username d'une longueur max de 50 et avec le flag unique

username: Mapped[str] = mapped_column(length=50, unique=True)
```python
from sqlalchemy.orm import Mapped
from sqlalchemy.testing.schema import mapped_column
from Models.Base import Base

class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column()
```

# 3) créer l'engine et manipuler nos entités 

=> Fichier engine.py

Dans celui-ci je vais devoir créer l'engine de la DB via la fonction create_engine, 
attention que la DB doit être créée au préalable

```python
from sqlalchemy import create_engine

# url = connection string
# echo = afficher les informations de transaction avec la DB dans le terminal
engine = create_engine(url='sqlite:///myfile.db', echo=True)
```
Créer les tables 
```python
from Models.Base import Base

Base.metadata.create_all(engine)
```
Drop les tables
```python
from Models.Base import Base

Base.metadata.drop_all(engine)
```

## Ajouter des informations en DB :

Pour ce faire on utiliser une sesssion, pour passer automatiquement par des transactions
```python
from sqlalchemy.orm import Session
from Models.user import User

with Session(engine) as session:
    # Créer les nouveau utilisateurs
    # Sans le session.add(user), l'utilisateur ne sera pas ajouté
    user1 = User(username="user1", password="<PASSWORD>")
    user2 = User(username="user2", password="<PASSWORD>")

    # Ajouter un utilisateur dans DB
    # session.add(user1)
    # session.add(user2)

    # ajoute plusieurs éléments en DB
    session.add_all([user1, user2])
    # Commit la transaction
    session.commit()
```

## Récupérer et manipuler des informations en DB
```python
with Session(engine) as session:
    # Me permet de sélectionner des éléments en DB
    stmt = select(User).where(User.username.in_(['user1', 'user2']))
    # récuperer plusieurs entités en DB
    users = session.scalars(stmt)
    for user in users:
        print(user.username)

    stmt = select(User).where(User.username == 'user1')
    # Récupérer une entité en DB
    user = session.scalars(stmt).one()
    print(user.username)

    # dès que je modifie mon entité, l'ORM va détecter automatiquement
    # que celle-ci a été modifiée, et la mettra à jour lors du prochain commit.
    user.username = 'nouveau'
    session.commit()

    # Permet de supprimer une entité en DB
    session.delete(user)
    session.commit()

    user1 = User(username="user1", password="<PASSWORD>")
    session.add(user1)
    session.commit()
```

# One to many
```python
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship
    
    # On définit la clé étrangère !! users.id = nom_de_la_table.nom_colonne
    user_id = Column(Integer, ForeignKey('users.id'))
    # Optionel On défini la relation des objets entre eux
    # Ici je dis que l'objet BasketItem contient une relation qui cible l'objet User
    # le back_population est optionel
    # !! Le back_population est le nom du champ dans l'objet !!
    # Pour la relationship, je passe le nom de l'objet sous forme de string,
    # pour éviter les boucles d'import example : 
    #   Le fichier user.py qui import la classe BasketItem de basket_item.py
    #   et le fichier basket_item.py qui importe la classe User de user.py
    user = relationship('User', back_populates='basket_items')
```
```python
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    user = relationship('User', back_populates='basket_items')
```

Du coté de l'entité ciblée :
```python
# l'option cascade va me permettre de dire comment et quels opération faire en cascade 
#   - all => toutes les opération, insert, update, delete
#   - save-update => on cascade les insert et update
#   - delete => uniquement cascade les delete
#   - delete-orphan => supprime les éléments qui ne sont plus lié à un parent automatiquement.
basket_items = relationship('BasketItem', back_populates='user', cascade='all, delete-orphan')
```

# Many to many
Créer une table d'association
```python
from sqlalchemy import Table, Integer, Column, ForeignKey
from Models.Base import Base

user_roles = Table('user_roles', Base.metadata,
                   Column('user_id', Integer, ForeignKey('users.id')),
                   Column('role_id', Integer, ForeignKey('roles.id'))
                   )
```

Faire les relations dans les entités respectives.

```python
    roles = relationship('Role', back_populates='users', secondary='user_roles')
```

```python
    users = relationship('User', back_populates='roles', secondary='user_roles')
```
## Si j'ai des informations supplémentaires dans ma relation

Dans ce cas ci il faut faire une entité supplémentaires, stockant les données
```python
from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from Models.Base import Base


class BasketItem(Base):
    __tablename__ = 'basketitems'

    id = Column(Integer, primary_key=True)
    quantity = Column(Integer, nullable=False)

    item_id = Column(Integer, ForeignKey('items.id'))
    user_id = Column(Integer, ForeignKey('users.id'))

    user = relationship('User', back_populates='basket_items')
    item = relationship('Item', back_populates='basket_items')
```