from app import db_uri
from app.models import Event, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

notebook_id = 'postman_python'

if __name__ == '__main__' :

    engine = create_engine(db_uri)
    Base.metadata.bind = engine 

    Session = sessionmaker(bind=engine)
    session = Session()

    events = session.query(Event).filter(Event.notebook_id == notebook_id).all()
    print('Number of events :',len(events))
    
    session.close()