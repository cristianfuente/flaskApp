from flask import Flask, request
from shadowd.flask_connector import InputFlask, OutputFlask, Connector
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

conexion=MySQL(app)

@app.before_request
def before_req():
    input = InputFlask(request)
    output = OutputFlask()

    Connector().start(input, output)


if __name__ == '__main__':
    app.config.from_object(config['connection'])
    app.run()