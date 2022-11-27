from flask import Flask, jsonify,request,make_response,url_for,redirect
import requests, json
import model
from werkzeug.utils import secure_filename
import os

UPLOAD_FOLDER = 'chat_file/'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'GET':
        return make_response('failure')
    if request.method == 'POST':
        print(request)
    print(request.files)
    if 'form_field_name' not in request.files:
        return 'no file found'
    print("hello")
    file = request.files['form_field_name']
    filename = secure_filename(file.filename)
    file_name = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    print(file_name)
    file.save(file_name)

    
    # path = 'WhatsApp Chat with Abhishek Navadiya Cse Nitw.txt'
    x, y, z = model.emotions(file_name)
    sentiment = model.sentiment_score(x, y, z)
    return '{}'.format(sentiment)

if __name__ == '__main__':
    app.run(host='localhost',debug=True, use_reloader=True)