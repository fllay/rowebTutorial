#!/usr/bin/env python
from flask import Flask, render_template
from flask import send_from_directory
import os
from flask_cors import CORS, cross_origin

template_dir = os.path.abspath('../html')
STATIC_DIR = os.path.abspath('../html/static')
print(STATIC_DIR)
app = Flask(__name__, template_folder=template_dir, static_folder=STATIC_DIR)
cors = CORS(app)
@app.route("/static/<path:path>")
def static_dir(path):
   print(path)
   return send_from_directory("static", path)

@app.route('/')
def home():
   return render_template('index.html')
if __name__ == '__main__':
   app.run(host='0.0.0.0', port="9112")