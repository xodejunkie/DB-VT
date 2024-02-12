from flask import request, render_template, redirect, url_for, flash, redirect
from app import app
from app.services.db_service import create_user, insert_document, get_user
from app.services.visualization_service import generate_sample_plot
import json
import pandas as pd
from werkzeug.utils import secure_filename
import os

@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/create_user', methods=['POST'])
def user_creation():
    username = request.form['username']
    create_user(username)
    return redirect(url_for('home'))

@app.route('/insert_document', methods=['POST'])
def document_insertion():
    document = request.form['document']
    try:
        document_json = json.loads(document)
        insert_document('myCollection', document_json)
    except json.JSONDecodeError as e:
        return f"Invalid JSON format: {str(e)}", 400
    return redirect(url_for('home'))

@app.route('/sample_visualization')
def sample_visualization():
    plot_html = generate_sample_plot()
    return render_template('index.html', plot_html=plot_html)

@app.route('/upload-csv', methods=['POST'])
def upload_csv():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and file.filename.endswith('.csv'):
        filename = secure_filename(file.filename)
        file_path = os.path.join('uploads', filename)
        file.save(file_path)
        
        # Use Pandas to read the CSV file
        df = pd.read_csv(file_path)
        
        # Here you can process the DataFrame as needed and insert it into your database
        # For example, inserting into MongoDB or SQL database
        
        return 'File uploaded and processed successfully'
    else:
        return 'Invalid file type'