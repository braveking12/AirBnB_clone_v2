#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Represents an Amenity entity for a MySQL database.

    Inherits from the SQLAlchemy Base and establishes a connection
    to the MySQL table named "amenities."

    Characteristics::
        __tablename__ (str): The identifier for the MySQL table
        used to store information about Amenities.
        name (sqlalchemy String): The name of the amenity.
        place_amenities (sqlalchemy relationship): Relationship between
        Place and Amenity.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
