# A very simple Flask Hello World app for you to get started with...

from flask import Flask, send_file
import os

from os.path import join, dirname



app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>大鸭鸭表格生成工具</h1><p><a href="/download">下载</a></p><hr><p><a href="https://github.com/cyber-mj00/170045xyz" target="_blank">Source code</a></p>'

@app.route('/download')
def download_file():
    with open(join(dirname(__file__), "latest_file.txt"), "r") as f:
        filename = f.read()

    return send_file(filename, as_attachment=True)
