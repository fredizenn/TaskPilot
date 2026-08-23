from database import Base
from database import engine
import models.task

print(repr(engine.url))

Base.metadata.create_all(bind=engine)

