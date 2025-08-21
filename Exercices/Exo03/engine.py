from sqlalchemy import create_engine, select, Column, Integer, ForeignKey, Table
from sqlalchemy.orm import Session, DeclarativeBase, declarative_base
from Models.Base import Base
from Exercices.Exo03.models.film import Film
from Exercices.Exo03.models.acteur import Acteur
from Exercices.Exo03.models.film_acteur import film_acteurs
from Exercices.Exo03.models.utilisateur import User
from Exercices.Exo03.models.playlist import playlists

engine = create_engine(url='sqlite:///myfile.db', echo=True)

# Crée les tables liées à Base
# Il va récupérer toutes les classes qui sont liées à Base
# Et créer les requêtes CREATE TABLE
Base.metadata.create_all(engine)

with Session(engine) as session:
    user = User(name="qwer")
    actor = Acteur(nom="qwerasdf")
    film = Film(titre="poiqwe", annee=2025)

    film.acteurs.append(actor)
    user.films.append(film)
    

    session.add_all(
        [film, actor, user]
    )

    session.commit()



