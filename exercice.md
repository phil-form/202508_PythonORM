# 1) Créer un model BasketItem qui contient les données suivantes :
```sql
CREATE TABLE basketitems (
    id int PRIMARY KEY,
    itemname VARCHAR(255) NOT NULL,
    price int NOT null
)
```

# 2) Reproduire avec SQLAlchemy

```sql
CREATE TABLE auteurs (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

CREATE TABLE livres (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    auteur_id INT NOT NULL REFERENCES auteurs(id) ON DELETE CASCADE
);

CREATE TABLE exemplaires (
    id SERIAL PRIMARY KEY,
    livre_id INT NOT NULL REFERENCES livres(id) ON DELETE CASCADE,
    etat VARCHAR(50) NOT NULL
);

CREATE TABLE lecteurs (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

CREATE TABLE emprunts (
    id SERIAL PRIMARY KEY,
    lecteur_id INT NOT NULL REFERENCES lecteurs(id) ON DELETE CASCADE,
    exemplaire_id INT NOT NULL REFERENCES exemplaires(id) ON DELETE CASCADE,
    date_emprunt DATE NOT NULL,
    date_retour DATE
);

INSERT INTO auteurs (nom) VALUES ('Victor Hugo'), ('Jules Verne');

INSERT INTO livres (titre, auteur_id) VALUES
                                          ('Les Misérables', 1),
                                          ('Notre-Dame de Paris', 1),
                                          ('Vingt mille lieues sous les mers', 2);

INSERT INTO exemplaires (livre_id, etat) VALUES
                                             (1, 'bon'), (1, 'abîmé'), (2, 'bon'), (3, 'bon'), (3, 'neuf');

INSERT INTO lecteurs (nom) VALUES ('Alice'), ('Bob');

INSERT INTO emprunts (lecteur_id, exemplaire_id, date_emprunt) VALUES
                                                                   (1, 1, '2025-08-01'),
                                                                   (2, 5, '2025-08-05');

```

# 3) Reproduire
```sql
CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    titre VARCHAR(200) NOT NULL,
    annee INT
);

CREATE TABLE acteurs (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

-- Relation Film ↔ Acteur
CREATE TABLE films_acteurs (
    film_id INT REFERENCES films(id) ON DELETE CASCADE,
    acteur_id INT REFERENCES acteurs(id) ON DELETE CASCADE,
    PRIMARY KEY (film_id, acteur_id)
);

CREATE TABLE utilisateurs (
    id SERIAL PRIMARY KEY,
    nom VARCHAR(100) NOT NULL
);

-- Relation Utilisateur ↔ Film
CREATE TABLE playlists (
    utilisateur_id INT REFERENCES utilisateurs(id) ON DELETE CASCADE,
    film_id INT REFERENCES films(id) ON DELETE CASCADE,
    PRIMARY KEY (utilisateur_id, film_id)
);
```