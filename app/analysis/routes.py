import os
from flask import render_template, flash, redirect, url_for, request, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename
from . import analysis
from .forms import ContractUploadForm

# Allowed file extensions and file size limit (16MB)
ALLOWED_EXTENSIONS = {'txt', 'doc', 'docx', 'pdf'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@analysis.route('/upload', methods=['GET', 'POST'])
@login_required
def upload_contract():
    form = ContractUploadForm()
    if form.validate_on_submit():
        file = form.contract_file.data
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            upload_dir = os.path.join(current_app.root_path, 'uploads')
            os.makedirs(upload_dir, exist_ok=True)
            file_path = os.path.join(upload_dir, filename)
            file.save(file_path)
            
            # Placeholder for ML analysis integration:
            # Insert your ML model here to process file_path.
            risk_score = 42  # Dummy risk score for now
            findings = [
                {'clause': 'Clause 1', 'explanation': 'Explanation for clause 1'},
                {'clause': 'Clause 2', 'explanation': 'Explanation for clause 2'},
            ]
            return render_template('analysis_results.html', title='Analysis Results',
                                   risk_score=risk_score, findings=findings)
        else:
            flash('Invalid file format.', 'danger')
    return render_template('analysis_upload.html', title='Contract Analysis', form=form)
