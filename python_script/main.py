import os
import json
from flask import Flask, request, jsonify
from ocr import process_image

app = Flask(__name__)

@app.route('/process_image', methods=['POST'])
def process_image_route():
    data = request.get_json()
    image = data['image']
    text = process_image(image)
    return jsonify({'text': text})

if __name__ == '__main__':
    app.run(debug=True)