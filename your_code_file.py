from flask import Flask, Response, render_template, jsonify, request, make_response, session, redirect, url_for, stream_with_context, send_file
import pyaudio
import wave
import os
from dotenv import load_dotenv
import openai
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from flask_cors import CORS
import wave
from datetime import datetime
from threading import Lock
from io import BytesIO
import gridfs
import zipfile

app = Flask(__name__)


@app.route('/transcript/<code>')
def get_transcript(code):
    entry = db.transcripts.find_one({"id": code})
    if not entry:
        return("No transcript found.")
    else:
        return entry["transcript"]

@app.route("/trans")
def trans():
    return render_template("transcript.html")

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, threaded=True, port=5000)