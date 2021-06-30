from flask import Flask
from flask import request
import pickle

app = Flask(__name__)
filename = "finalized_model.sav"
loaded_model = pickle.load(open(filename, 'rb'))

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/house")
def house():
    area = request.args.get('area')
    rooms = request.args.get('rooms')
    w1 = 2
    w2 = 4
    model = (int(area) * w1) + (int(rooms) * w2)
    return str(model)

@app.route("/data/<section>")
def data(section):
    section = request.view_args['section']
    return str(section)

@app.route("/house-post", methods=['POST'])
def house_post():
    area = request.form.get('area')
    return str(area)

@app.route("/iris", methods=['POST'])
def iris():
    sl = request.form.get('sl')
    sw = request.form.get('sw')
    pl = request.form.get('pl')
    pw = request.form.get('pw')
    res = loaded_model.predict([[sl, sw, pl, pw]])
    return str(res)

if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000, debug=True)
   app.run(debug=True)