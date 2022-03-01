from crypt import methods
from http.client import OK
import json
from flask import Flask, request,jsonify
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

@app.route('/consultaByDoc',methods=['GET'])
def consulta():
    try:
        conn = mysql.connect()
        cursor=conn.cursor()
        docFind=request.args.get('doc')
        placa=request.args.get('placa')
        query="SELECT * from Users WHERE documento = '{}' and placa = {}".format(docFind,placa)
        cursor.execute(query)
        data=cursor.fetchall()
        json_data=[]
        for r in data:
            cons={'nombre':r[1],'documento':r[2],'correo':r[3],'telfono':r[4]}
            json_data.append(cons)
        return jsonify(json_data)
    except Exception as ex:
        return 'Error'+str(ex) 

if __name__ == '__main__':

    app.run()