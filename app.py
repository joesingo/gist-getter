import requests
from flask import Flask, abort, make_response

from get_gist import get_gist_url, get_raw_url

app = Flask(__name__)

@app.route("/<filename>", methods=["GET"])
def get_gist(filename):
    try:
        gist_url = get_gist_url(filename)
    except ValueError as ex:
        abort(404)

    raw_url = get_raw_url(gist_url)
    response = make_response(requests.get(raw_url).text)
    response.headers["Content-Type"] = "Raw"
    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0")
