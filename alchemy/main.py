from app import db_uri
from app.models import Base, Event
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine(db_uri, echo=True)
Base.metadata.create_all(engine)

nb_entries = 50000
notebook_id = 'postman_python'
content = "wngfiwrhguirehgiuerhgiuthiuthbirubntruituihthbrtwngfiwrhguirehgiuerhgiuthiuthbirubntruituihthbrtwngfiwrhguirehgiuerhgiuthiuthbirubntruituihthbrtwngfiwrhguirehgiuerhgiuthiuthbirubntruituihthbrtwng"

if __name__ == "__main__":

    engine = create_engine(db_uri)
    Base.metadata.bind = engine 

    Session = sessionmaker(bind=engine)
    session = Session()

    for n in range(nb_entries) :

        new_event = Event(
            notebook_id=notebook_id,
            col_1=content
        )

        session.add(new_event)
        session.commit()
    
    session.close()

    # keep the container alive
    while True:
        pass
