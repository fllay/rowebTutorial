#!/usr/bin/env python
from flask import Flask, request, render_template, jsonify, make_response
from flask import send_from_directory
import subprocess 
import signal
import os
import os.path
from flask_cors import CORS, cross_origin

template_dir = os.path.abspath('../html')
STATIC_DIR = os.path.abspath('../html/static')
print(STATIC_DIR)
app = Flask(__name__, template_folder=template_dir, static_folder=STATIC_DIR)
cors = CORS(app)
pp = None
@app.route("/static/<path:path>")
def static_dir(path):
   print(path)
   return send_from_directory("static", path)

@app.route('/<path:path>')
def static_file(path):
   return app.send_static_file(path)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/blck')
def blck():
   return render_template('blck.html')

@app.route('/run', methods=['GET', 'POST'])
def run_python():
    content_type = request.headers.get('Content-Type')
    global pp
    if (content_type == 'application/json'):
        json = request.json
        print(json["code"])
        save_path = '/home/pi/tutorial'
        name_of_file = "test1"
        completeName = os.path.join(save_path, name_of_file+".py")         
        file1 = open(completeName, "w")
        #toFile = raw_input(json["code"])
        file1.write(json["code"])
        file1.close()
        pp = subprocess.Popen(['python %s'%(completeName)],stdout = subprocess.PIPE,stderr = subprocess.PIPE,shell=True, preexec_fn=os.setsid)
        out = pp.communicate()[0]
        output = str(out)
        print(output)
        return make_response(jsonify(status="OK"), 200)
    else:
        return 'Content-Type not supported!'

@app.route('/stop', methods=['GET', 'POST'])
def stop_python():
   os.killpg(os.getpgid(pp.pid),  signal.SIGTERM)
   return make_response(jsonify(status="OK"), 200)

@app.route('/save', methods=['GET', 'POST'])
def save_blockly():
    content_type = request.headers.get('Content-Type')
    global pp
    if (content_type == 'application/json'):
        json = request.json
        print(json["code"])
        save_path = '/home/pi/tutorial'
        name_of_file = "test1"
        completeName = os.path.join(save_path, name_of_file+".xml")         
        file1 = open(completeName, "w")
        file1.write(json["code"])
        file1.close()
        return make_response(jsonify(status="OK"), 200)
    else:
        return 'Content-Type not supported!'

@app.route('/load', methods=['GET', 'POST'])
def load_blockly():
    content_type = request.headers.get('Content-Type')
    global pp
    if (content_type == 'application/json'):
        json = request.json
        save_path = '/home/pi/tutorial'
        name_of_file = "test1"
        completeName = os.path.join(save_path, name_of_file+".xml")         
        with open(completeName) as f:
           contents = f.read()
           print(contents)
        return make_response(jsonify(status="OK", code=contents), 200)
    else:
        return 'Content-Type not supported!'



if __name__ == '__main__':
   app.run(host='0.0.0.0', port="9112")