# import modules
from tqdm import tqdm
from transformers import pipeline
from flask import Flask, request, jsonify
import main
import re



app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>FLASK APP IS RUNNING!</h1>'

# load model, labels and functions
model = main.model
classifier = main.zero_shot_classifier
dkweb_links = main.dark_web_links
adult_cont_link = main.adult_content_sites
labels = main.labels

@app.route('/api/moderator')




if __name__ == '__main__':
    app.run()