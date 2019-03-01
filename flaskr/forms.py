from wtforms import Form, StringField, TextAreaField, HiddenField, validators

class ProjectCreateForm(Form):
	name = StringField('Name', [validators.Length(min=1, max=50)])
	client = StringField('Client', [validators.Length(min=1, max=100)])
	technology = StringField('Technology', [validators.Length(min=1, max=50)])
	status = StringField('Status', [validators.Length(min=1, max=15)])

class TaskCreateForm(Form):
	title = StringField('Title', [validators.Length(min=1, max=50)])
	description = TextAreaField('Description')
	project_id = HiddenField("project_id")