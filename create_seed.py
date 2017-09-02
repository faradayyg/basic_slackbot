from app import db

db.create_all()
print(db)

from models import Projects



i = 1
while i < 10:
	p = Projects(name = 'test project %d ' % i)
	i = i+1
	db.session.add(p)

db.session.commit()