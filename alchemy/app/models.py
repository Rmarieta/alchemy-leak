from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class EventParent(Base):
    __tablename__ = 'EventParent'

    id = Column(Integer, primary_key=True)
    notebook_id = Column(String(100), nullable=False)
    event_type = Column(String(32), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'EventParent',
        'polymorphic_on': event_type
    }

class Event(EventParent):
    __tablename__ = 'Event'

    id = Column(Integer, ForeignKey('EventParent.id'), primary_key=True)
    col_1 = Column(String(200), nullable=False)

    __mapper_args__ = {
        'polymorphic_identity': 'Event'
    }
