import os
import processing
import json

from flask import Flask, request, jsonify
import google_service_api
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


def _valid_secret_key(method=None):
    sk = request.headers.get('secret_key')
    if method == "POST":
        sk = request.json.get('secret_key')

    if sk == os.getenv("secret_key"):
        return True
    else:
        return False


@app.route("/")
def view_index():
    req = request
    env = os.environ

    if not _valid_secret_key():
        return "Secret key not valid"

    return "Completed"


@app.route('/enterHours', methods=['POST'])
def view_submit_invoices():
    res = request
    if not _valid_secret_key('POST'):
        return "Secret key not valid"

    _json_data = request.json
    processing.log_hours(_json_data)

    return "Success"


if __name__ == "__main__":
    app.run()
    # app.run(host='0.0.0.0')
