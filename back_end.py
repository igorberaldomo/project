from flask import Flask, make_response,jsonify, request
from banco_dados import cores
app = Flask(__name__)
Cores = list()

@app.route('/cores', methods=['GET'])
def get_corres():
    return make_response(
    jsonify(cores)
    )
 
@app.route('/cores/', methods=['GET'])
def get_cor():
    idcores = request.args.get('id')
    return make_response(
        cores[int(idcores)-1]
    )
    
@app.route('/cores/', methods=['POST'])
def post_cor():
    cor = request.get_json()
    cores.append(cor)
    return make_response(
        jsonify(cores)
    )

@app.route('/cores/', methods=['DELETE'])
def Delete_cor():
    idcores = request.args.get('id')
    cores.remove(cores[int(idcores)-1])
    return make_response(
        jsonify(cores)
    )

app.run(port=5000, debug=True)
    