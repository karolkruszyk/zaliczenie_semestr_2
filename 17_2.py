import os
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

base_op = create_engine('sqlite:///match.db')
base = declarative_base()


class Team(base):
    __tablename__ = 'teams'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    player_id = Column(Integer, ForeignKey("players.id"))
    gamed_id = Column(Integer, ForeignKey("games.id"))


class Players(base):
    __tablename__ = 'players'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    surname = Column(String, nullable=False)
    team = relationship('Team', backref='players')


class Game(base):
    __tablename__ = 'games'
    id = Column(Integer, primary_key=True)

    team1 = relationship('Team', backref='games')
    team2 = relationship('Team', backref='games')
    score = Column(String, nullable=False)


base.metadata.create_all(base_op)

dbsession = sessionmaker(bind=base_op)
session = dbsession()

if not session.query(Team).count():
    session.add(Team('LA Lakers', player_id=1, game_id=1))
    session.add(Team('Chicago Bulls', player_id=1, game_id=1))
    session.add(Team('Washington Wizards', player_id=1, game_id=1))
    session.add(Team('Brooklyn NETS', player_id=1, game_id=1))

    session.add(Players(name='Jan', surname='Kowalski'))
    session.add(Players(name='Jan1', surname='Kowalski1'))
    session.add(Players(name='Jan2', surname='Kowalski2'))
    session.add(Players(name='Jan3', surname='Kowalski3'))

    session.add(Game(score='---'))
    session.add(Game(score='---'))
    session.add(Game(score='---'))
    session.add(Game(score='---'))
session.commit()
