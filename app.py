from flask import Flask
from flask import request, jsonify
import datetime
import uuid

app = Flask(__name__)

notes = []

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/create', methods=["POST"])
def create_note():
    title, body = request.json.get('title'), request.json.get('body')
    
    notes.append({
        "title": title,
        "body": body,
        "id":uuid.uuid4(),
        "created_at": datetime.datetime.now()
	})

    return jsonify(notes), 201

@app.route('/notes', methods=["GET"])
def get_notes():
    return jsonify(notes), 200 

@app.route('/update/<id>')
def update_note(id: int):
    #TODO: get id, modify note, return updated note -> easier with models
    pass

@app.route('/delete/<id>', methods=["DELETE"])
def delete_note():
    #TODO: get id, delete note, return list of updated notes -> easier with models
    pass
