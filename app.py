from flask import Flask
from flask import request, jsonify
from flask_cors import CORS


import os
from supabase import create_client, Client

#TODO: errors

url: str = os.environ.get("SUPABASE_URL")
#key: str = os.environ.get("SUPABASE_ANON_KEY")
key: str = os.environ.get("SUPABASE_KEY")

supabase: Client = create_client(url, key)

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return "Hello world"

@app.route('/create', methods=["POST"])
def create_note():    
    data = supabase.table("notes").insert(request.json).execute().dict()

    created_note = data['data'][0] #FIXME:

    return jsonify(created_note), 201

@app.route('/notes', methods=["GET"])
def get_notes():
    data = supabase.table("notes").select("*").execute().dict()
    notes = data['data']
    return jsonify(notes), 200 

@app.route('/update/<id>', methods=["PUT"])
def update_note(id: int):

    data = supabase.table("notes").update(request.json).eq("id", id).execute().dict()
    updated_note = data['data'][0] #FIXME:

    return jsonify(updated_note), 200

@app.route('/delete/<id>', methods=["DELETE"])
def delete_note(id: int):

    data=supabase.table("notes").delete().eq("id", id).execute().dict()
    deleted_note = data['data'][0] #FIXME:

    return jsonify(deleted_note), 200
