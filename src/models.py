from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Players(Base):
    __tablename__="players"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    oculus_id = Column(String, unique= True)
    highscore = Column(String, default="0")
    fastest_time = Column(String, default="0")
    coin = Column(Integer, default=0)

    darts_own = relationship("Darts")


class Darts(Base):
    __tablename__="darts"
    id = Column(Integer, primary_key=True, unique=True, index=True)
    dart_name = Column(String)
    price = Column(Integer)
    is_owned = Column(Boolean,default = False)
    owner_id = Column(Integer, ForeignKey("players.id"), nullable = True)
