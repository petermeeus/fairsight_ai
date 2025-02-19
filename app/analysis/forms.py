from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import SubmitField

class ContractUploadForm(FlaskForm):
    contract_file = FileField('Upload Contract', validators=[
        FileRequired(),
        FileAllowed(['txt', 'doc', 'docx', 'pdf'], 'Documents only!')
    ])
    submit = SubmitField('Analyze')
