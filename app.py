from flask import Flask, request
from sens_api import SensApi

app = Flask(__name__)
sens_api = SensApi("cred.txt")


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        data = request.json

        if len(data['data']["geozones"]) > 0:
            sens_api.update_tags(
                data['data']["serial"], data['data']["geozones"])
            print(data['data']["serial"])

    return "Hello :)"


if __name__ == "__main__":
    app.run(debug=True)
