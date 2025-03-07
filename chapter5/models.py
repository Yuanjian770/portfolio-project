from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float
from sqlalchemy.orm import relationship
from database import base

class Player(base):
    __tablename__ = "player"

    player_id = Column(Integer, primary_key=True, index=True)
    gsis_id = Column(String, nullable=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    position = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)
    # Player.performances attribute will return all the related rows from the performance
    # tablefor each row in the player table
    performances = relationship("Performance", back_populates="player")
    # Many to Many relationship between Player and team tables

    '''
    there is another kind of relationship, which uses the team_player association table to 
    connect player to team. by defining secondary = "team_player", this relationship 
    alls a Player record to have an attribute named Player.teams, this is the many-to-many relationship 
    that was discussed when creating the database tables. 
    '''
    teams = relationship("Team", secondary='team_player', back_populates="players")
    relationship()

class Performance(base):
    __tablename__ = "performance"
    performance_id = Column(Integer, primary_key=True)
    week_number = Column(String, nullable=False)
    fantasy_points = Column(Float, nullable=False)
    last_changed_date = Column(Date, nullable=False)
    player_id = Column(Integer, ForeignKey("player.player_id"))
    player = relationship("Player", back_populates="performances")

class League(base):
    __tablename__ = "league"
    league_id = Column(Integer, primary_key=True, index=True)
    league_name = Column(String, nullable=False)
    scoring_type = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)
    teams = relationship("Team",  back_populates="league")

class Team(base):
    __tablename__ = "team"
    team_id = Column(Integer, primary_key=True, index=True)
    team_name = Column(String, nullable=False)
    last_changed_date = Column(Date, nullable=False)
    league_id = Column(Integer, ForeignKey("league.league_id"))
    league = relationship("League", back_populates="teams")
    players = relationship("Player", secondary="team_player", back_populates="teams")

class TeamPlayer(base):
    __tablename__ = "team_player"
    team_id = Column(Integer, ForeignKey("team.team_id"), primary_key=True, index=True)
    player_id = Column(Integer, ForeignKey("player.player_id"), primary_key=True, index=True)
    last_changed_date = Column(Date, nullable=False)


