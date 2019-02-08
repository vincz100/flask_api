#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

territoires = [
    {
        'codgeo': '76120',
        'libgeo': 'Grand-Quevilly',
        'population': 17500,
    },
    {
        'codgeo': '76000',
        'libgeo': 'Rouen',
        'population': 56000,
    }
]

@app.route('/')                             # décorateur route = route par laquelle notre fonction sera accessible
def index():                                # vue index
    return "Hello World"

@app.route('/api/territoires', methods=['GET'])
def get_territoires():
    return jsonify({'territoires': territoires})

@app.route('/contact')
def contact():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


if __name__ == '__main__':
    app.run(debug=True)