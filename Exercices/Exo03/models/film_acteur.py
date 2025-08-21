from sqlalchemy import Table, Integer, ForeignKey, Column

from Models.Base import Base

film_acteurs = Table(
    "film_acteurs", Base.metadata,
    Column("acteur_id", Integer, ForeignKey("acteurs.id")),
    Column("film_id", Integer, ForeignKey("films.id"))
)