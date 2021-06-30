from flask import Flask
from flask import request

app = Flask(__name__)

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

if __name__ == '__main__':
#    app.run(host='0.0.0.0', port=5000, debug=True)
   app.run(debug=True)