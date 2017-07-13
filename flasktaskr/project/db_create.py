from views import db
from models import Task, User
from datetime import date

db.create_all()

db.session.add(Task("Finish this tutorial", date(2016, 9, 22), 10, 1))
db.session.add(Task("Finish Real Python Course 2", date(2015, 3, 25), 10, 1))

db.session.add(User("Sanghoon Lee", "orcpunch@gmail.com", "1234"))
db.session.add(User("Jisun Kim", "eldldk@gmail.com", "1234"))

db.session.commit()