from sqlalchemy import Table, Column, Integer, ForeignKey

from Models.Base import Base

playlists = Table(
    "playlists", Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("film_id", Integer, ForeignKey("films.id")),
    )