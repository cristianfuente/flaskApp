from flask import Flask, request
from shadowd.flask_connector import InputFlask, OutputFlask, Connector

app = Flask(__name__)

@app.before_request
def before_req():
    input = InputFlask(request)
    output = OutputFlask()

    Connector().start(input, output)


if __name__ == '__main__':

	app.run(debug=True)