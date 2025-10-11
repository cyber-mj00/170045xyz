from flask import Flask, send_file
from apscheduler.schedulers.background import BackgroundScheduler
import csv



app = Flask(__name__)

@app.route('/')
def home():
    return '<a href="/download">Download CSV</a>'

@app.route('/download')
def download_file():
    filename = 'output.csv'
    # Generate the CSV file
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['Name', 'Age'])
        writer.writerow(['Alice', 30])
        writer.writerow(['Bob', 25])
    # Serve the file for download
    return send_file(filename, as_attachment=True)
