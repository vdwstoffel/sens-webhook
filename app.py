import os
from flask import Flask, request
from sens_api import SensApi

app = Flask(__name__)
try:
    with open("cred.txt") as f:
        api_key = f.read()
except:
    api_key = os.environ["API_KEY"]

sens_api = SensApi(api_key)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.json

        sens_api.update_tags(
            data['data']["serial"], data['data']["geozones"], data["data"]["address"])

    return "Hello :)"


if __name__ == "__main__":
    app.run(debug=True)
