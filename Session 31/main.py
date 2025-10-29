from datetime import datetime
from typing import List

import bcrypt
from sqlalchemy import create_engine, Integer, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Session, Mapped, mapped_column, relationship, declarative_base

from urllib.parse import quote_plus
import random

Base = declarative_base()


class SpeciesModel(Base):
    __tablename__ = "zoo_app"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    category: Mapped[str] = mapped_column(String(64))
    description: Mapped[str] = mapped_column(String(256), nullable=True)
    animals: Mapped[List["AnimalModel"]] = relationship("AnimalModel", back_populates="zoo_app")

    def __repr__(self):
        return f"Species('{self.name}', '{self.category}')"


class AnimalModel(Base):
    __tablename__ = "animal"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(64), nullable=False)
    birthday: Mapped[datetime] = mapped_column(TIMESTAMP, unique=True, nullable=False)
    species_id: Mapped[int] = mapped_column(ForeignKey("zoo_app.id"), nullable=False)
    species: Mapped["SpeciesModel"] = relationship("SpeciesModel", back_populates="animals")
    users: Mapped[List["UserModel"]] = relationship("UserModel", back_populates="animal")

    def __repr__(self):
        return f"Animal('{self.name}', '{self.species.name}')"


class UserModel(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(64), unique=True)
    hashed_password: Mapped[str] = mapped_column(String(64), nullable=False)
    animal_id: Mapped[int] = mapped_column(ForeignKey("animal.id"), default=None)
    animal: Mapped["AnimalModel"] = relationship("AnimalModel", back_populates="users")

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


SPECIES = [
    {"name": "African Elephant", "category": "Mammal",
     "description": "The largest land animal, known for its trunk, tusks, and strong social bonds."},
    {"name": "Great White Shark", "category": "Fish",
     "description": "A powerful predator with sharp teeth, found in coastal surface waters worldwide."},
    {"name": "Bald Eagle", "category": "Bird",
     "description": "A majestic bird of prey, symbol of the USA, known for its white head and tail."},
    {"name": "Green Sea Turtle", "category": "Reptile",
     "description": "A large marine turtle that migrates long distances between feeding and nesting sites."},
    {"name": "Emperor Penguin", "category": "Bird",
     "description": "The tallest and heaviest penguin, living in large Antarctic colonies."},
    {"name": "Bengal Tiger", "category": "Mammal",
     "description": "A striking orange-and-black striped big cat native to the Indian subcontinent."},
    {"name": "Blue Whale", "category": "Mammal",
     "description": "The largest animal on Earth, feeding mainly on tiny krill."},
    {"name": "Komodo Dragon", "category": "Reptile",
     "description": "The world’s largest lizard, native to Indonesian islands."},
    {"name": "Clownfish", "category": "Fish",
     "description": "Bright orange with white bands, famous for living among sea anemones."},
    {"name": "Giant Panda", "category": "Mammal",
     "description": "A bear native to China, known for its black-and-white fur and bamboo diet."},
    {"name": "Red Kangaroo", "category": "Mammal",
     "description": "The largest marsupial, native to Australia, known for powerful hind legs."},
    {"name": "Humpback Whale", "category": "Mammal",
     "description": "A baleen whale famous for its songs and acrobatic breaches."},
    {"name": "Snow Leopard", "category": "Mammal",
     "description": "A rare big cat adapted to cold mountainous regions of Central Asia."},
    {"name": "King Cobra", "category": "Reptile",
     "description": "The world’s longest venomous snake, known for its hood and hiss."},
    {"name": "Atlantic Puffin", "category": "Bird",
     "description": "A seabird with a colorful beak, excellent at both flying and diving."},
    {"name": "Cheetah", "category": "Mammal",
     "description": "The fastest land animal, capable of speeds up to 70 mph."},
    {"name": "Axolotl", "category": "Amphibian",
     "description": "A neotenic salamander from Mexico, known for its regenerative abilities."},
    {"name": "Orca", "category": "Mammal",
     "description": "Also called killer whale, a social and intelligent marine predator."},
    {"name": "Flamingo", "category": "Bird",
     "description": "A pink wading bird that feeds by filtering water with its beak."},
    {"name": "Green Anaconda", "category": "Reptile",
     "description": "One of the largest snakes, found in South American swamps and rivers."}
]

ANIMAL_NAMES = [
    "Simba", "Nala", "Garfield", "Tom", "Jerry", "Lassie", "Rex", "Buddy", "Max", "Bella", "Charlie", "Lucy", "Daisy",
    "Milo", "Luna", "Rocky", "Coco", "Shadow", "Smokey", "Oreo", "Chloe", "Molly", "Sasha", "Tiger", "Oscar", "Leo",
    "Ziggy", "Toby", "Ruby", "Ginger", "Sammy", "Jack", "Sophie", "Riley", "Pumpkin", "Peanut", "Zeus", "Lilly",
    "Lucky", "Penny", "Marley", "Simone", "Frankie", "Tigger", "Bentley", "Gracie", "Scout", "Buster", "Rosie",
    "Maggie", "Winston", "Poppy", "Jasper", "Rocco", "Harley", "Cleo", "Shadowfax", "Finn", "Duke", "Misty", "Samson",
    "Athena", "Gus", "Hercules", "Muffin", "Bandit", "Benny", "Cinnamon", "Pepper", "Nico", "Fiona", "Chester", "Belle",
    "Hunter", "Toby", "Sable", "Mocha", "Cookie", "Trixie", "Ranger", "Loki", "Zephyr", "Amber", "Boo", "Blue",
    "Diesel", "Honey", "Pip", "Rudy", "Sable", "Cuddles", "Spike", "Nemo", "Simone", "Pixie", "Rufus", "Marigold",
    "Thor", "Mochi", "Gizmo"
]

USERS = [
    {"username": "alice_w", "email": "alice.williams@example.com", "password": "P@ssw0rd!23"},
    {"username": "bob89", "email": "bob89@mail.com", "password": "SunnyDay2024"},
    {"username": "charlie.pet", "email": "charlie.peterson@example.org", "password": "Ch@rlie_77"},
    {"username": "dana.k", "email": "dana.keller@mail.com", "password": "Blue!Sky#9"},
    {"username": "ethan91", "email": "ethan91@example.com", "password": "echo%1991"},
    {"username": "fionaF", "email": "fiona.foster@mail.com", "password": "Fiona#Love4"},
    {"username": "george_r", "email": "george.ramsey@example.com", "password": "G3orge-Rox"},
    {"username": "hannah.m", "email": "hannah.miller@mail.com", "password": "HannahM*88"},
    {"username": "ivan_ivan", "email": "ivan.ivanov@example.org", "password": "Passw0rdIvan!"},
    {"username": "juliaG", "email": "julia.green@mail.com", "password": "Jules@2022"},
    {"username": "kevinX", "email": "kevin.xu@example.com", "password": "Kev!nX_5"},
    {"username": "lola.l", "email": "lola.lopez@mail.com", "password": "L0la.L0ves"},
    {"username": "matthewG", "email": "matt.gibson@example.com", "password": "MattG#321"},
    {"username": "nora_s", "email": "nora.santos@mail.com", "password": "Nora_Sun!7"},
    {"username": "oliverB", "email": "oliver.barnes@example.org", "password": "OliveR-88*"},
    {"username": "paulaP", "email": "paula.perez@mail.com", "password": "PaulaP@2020"},
    {"username": "quentinQ", "email": "quentin.quinn@example.com", "password": "QQuinn!42"},
    {"username": "rileyR", "email": "riley.rose@mail.com", "password": "R1ley.Rocks"},
    {"username": "sophieS", "email": "sophie.stewart@example.org", "password": "S0phie$mile"},
    {"username": "tommyT", "email": "tommy.tucker@mail.com", "password": "Tuck3r#Safe"}
]


def random_datetime(start: datetime, end: datetime = None) -> datetime:
    if end is None:
        end = datetime.now()

    start_ts = start.timestamp()
    end_ts = end.timestamp()

    random_ts = random.uniform(start_ts, end_ts)
    return datetime.fromtimestamp(random_ts)


def hash_password(password: str) -> str:
    password = password.encode('utf-8')
    hashed = bcrypt.hashpw(password, bcrypt.gensalt())
    return hashed.decode('utf-8')


def add_species(session: Session, name: str, category: str, description: str = None):
    species = SpeciesModel(name=name, category=category, description=description)
    session.add(species)


def add_animal(session: Session, name: str, birthday: datetime, species: SpeciesModel):
    animal = AnimalModel(name=name, birthday=birthday, species=species)
    session.add(animal)


def add_user(session: Session, username: str, email: str, password: str, animal: AnimalModel = None):
    user = UserModel(username=username, email=email, hashed_password=hash_password(password), animal=animal)
    session.add(user)


def add_all_species(session: Session):
    for species in SPECIES:
        if random.random() > 0.3:
            add_species(session, name=species["name"], category=species["category"],
                        description=species["description"])
        else:
            add_species(session, name=species["name"], category=species["category"])

    session.commit()


def add_all_animals(session: Session):
    species_all = session.query(SpeciesModel).all()

    for animal_name in ANIMAL_NAMES:
        birthday = random_datetime(datetime(2000, 1, 1, 0, 0, 0))
        species = random.choice(species_all)
        add_animal(session, name=animal_name, birthday=birthday, species=species)

    session.commit()


def add_all_users(session: Session):
    animals = session.query(AnimalModel).all()

    for user in USERS:
        if random.random() > 0.5:
            animal = random.choice(animals)
            add_user(session, username=user["username"], email=user["email"], password=user["password"], animal=animal)
        else:
            add_user(session, username=user["username"], email=user["email"], password=user["password"])

    session.commit()


def main():
    engine = create_engine(f'mysql://root:{quote_plus("%1TcEzxuzkpz1NUoqd@G4iMt")}@localhost:3306/zoo')
    with Session(engine) as session:
        add_all_species(session)
        add_all_animals(session)
        add_all_users(session)


if __name__ == '__main__':
    main()
