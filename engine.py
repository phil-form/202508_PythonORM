from sqlalchemy import create_engine, select, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import Session, DeclarativeBase, declarative_base
from Models.user import User
from Models.role import Role
from Models.BasketItem import BasketItem
from Models.user_roles import user_roles
from Models.Item import Item
from Models.Base import Base

DATABASE_URL = "sqlite:///database.db"
engine = create_engine(url=DATABASE_URL, echo=True)

# Base.metadata.drop_all(engine)
# Pour drop tout les tables de la DB
# Base.metadata.drop_all(engine)
# Crée les tables liées à Base
# Il va récupérer toutes les classes qui sont liées à Base
# Et créer les requêtes CREATE TABLE
# Base.metadata.create_all(engine)

# with Session(engine) as session:
#     # Créer les nouveau utilisateurs
#     # Sans le session.add(user), l'utilisateur ne sera pas ajouté
#     user1 = User(username="user1", password="<PASSWORD>")
#     user2 = User(username="user2", password="<PASSWORD>")
#
#     # Ajouter un utilisateur dans DB
#     # session.add(user1)
#     # session.add(user2)
#
#     # ajoute plusieurs éléments en DB
#     session.add_all([user1, user2])
#     # Commit la transaction
#     session.commit()
#
# with Session(engine) as session:
#     # Me permet de sélectionner des éléments en DB
#     stmt = select(User).where(User.username.in_(['user1', 'user2']))
#     # récuperer plusieurs entités en DB
#     users = session.scalars(stmt)
#     for user in users:
#         print(user.username)
#
#     stmt = select(User).where(User.username == 'user1')
#     # Récupérer une entité en DB
#     user = session.scalars(stmt).one()
#     print(user.username)
#
#     # dès que je modifie mon entité, l'ORM va détecter automatiquement
#     # que celle-ci a été modifiée, et la mettra à jour lors du prochain commit.
#     user.username = 'nouveau'
#     session.commit()
#
#     # Permet de supprimer une entité en DB
#     session.delete(user)
#     session.commit()
#
#     user1 = User(username="user1", password="<PASSWORD>")
#     session.add(user1)
#     session.commit()
#
#     session.flush()


