#!/bin/bash

# Install dependencies
pip install -r requirements.txt
pip install -r python_script/requirements.txt

# Run the Flask app
cd python_script
python main.py &
cd ..

# Run the Google App Script (not possible in a Unix script, as it's a Google Apps Script)
# You need to deploy the script to Google Apps Script and set up the SCRIPT_ID

# Wait for the Flask app to start
sleep 2

# You can test the app by sending a POST request to http://localhost:5000/process_image
# with a JSON body containing an "image" key with a base64 encoded image value
