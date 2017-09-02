from models import *
from flask_restful import marshal, fields
from app import db


marshal_project_fields = {
	'name': fields.String
}
def list_projects():
	projects = Projects.query.all()
	txt = "Here are Projects that you have open: \n "
	for row in projects:
		txt = txt + "*id:* "+str(row.id)+" \t *Name:* "+row.name + '\n '
	if len(projects)== 0:
		return "Sorry, :sob: Seems You have not added any projects yet"
	return txt


def create_project(p):
	project_name = p[p.rfind('project')+8:]
	new_project = Projects(name = project_name)
	db.session.add(new_project)
	db.session.commit()
	return project_name

def delete_project(p):
	project_name = p[p.rfind('project')+8:]
	proj = Projects.query.filter_by(id=int(project_name)).delete()
	db.session.commit()