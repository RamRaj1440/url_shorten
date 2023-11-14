from flask import Flask, render_template, request, redirect, jsonify
import hashlib
import json

app = Flask(__name__)

# File to store the mapping between short and original URLs
URL_MAPPING_FILE = 'url_mapping.json'

# Dictionary to store the mapping between short and original URLs
url_mapping = {}

def generate_short_url(original_url):
    # Generate a unique hash for the original URL
    hash_object = hashlib.md5(original_url.encode())
    short_url = "www." + hash_object.hexdigest()[:6]
    return short_url

def save_url_mapping():
    # Save the mapping to the JSON file
    with open(URL_MAPPING_FILE, 'w') as json_file:
        json.dump(url_mapping, json_file)

def load_url_mapping():
    # Load existing URL mapping from JSON file
    try:
        with open(URL_MAPPING_FILE, 'r') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        return {}

# Load URL mapping on application startup
url_mapping = load_url_mapping()

@app.route('/')
def index():
    return render_template('index.html', url_mapping=url_mapping)

@app.route('/shorten', methods=['POST'])
def shorten_url():
    original_url = request.form.get('url')

    if original_url:
        short_url = generate_short_url(original_url)
        url_mapping[short_url] = original_url
        save_url_mapping()
        return redirect('/')
    
    return "Invalid input"

@app.route('/<short_url>')
def redirect_to_original(short_url):
    original_url = url_mapping.get(short_url)
    if original_url:
        return redirect(original_url, code=302)
    else:
        return "Short URL not found"

if __name__ == '__main__':
    app.run(debug=True)
