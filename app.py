from crypt import methods
from http.client import OK
from flask import Flask, request
from shadowd.flask_connector import InputFlask, OutputFlask, Connector
from flaskext.mysql import MySQL
from config import config

app = Flask(__name__)

mysql = MySQL()
app.config.from_object(config['connection'])
mysql.init_app(app)

@app.before_request
def before_req():
    input = InputFlask(request)
    output = OutputFlask()

    Connector().start(input, output)

@app.route('/consulta',methods=['GET'])
def consulta():
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        conn.commit()
        cursor.close()
        return 'ok'
    except Exception as ex:
        return 'Error'+str(ex) 

if __name__ == '__main__':

    app.run()