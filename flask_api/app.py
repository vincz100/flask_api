#!flask/bin/python
# coding: utf-8

from flask import Flask, jsonify, abort, make_response

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
    },
    {
        'codgeo': '93200',
        'libgeo': 'Saint-Denis',
        'population': 67000,
    }
]

@app.route('/')                             # décorateur route = route par laquelle notre fonction sera accessible
def index():                                # vue index
    return "Hello World"

@app.route('/api/territoires', methods=['GET'])
def get_territoires():
    return jsonify({'territoires': territoires})

@app.route('/api/territoires/<string:codgeo>', methods=['GET'])                                     # on récupère un string et pas un int
def get_territoire(codgeo):
    territoire = [territoire for territoire in territoires if territoire['codgeo'] == codgeo]
    if len(territoire) == 0:
        abort(404)
    return jsonify({'territoires': territoire[0]})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

# fonction équivalents mais plus verbeuse
# def get_territoire(codgeo):
#     territoire = []
#     for el in territoires:
#         if el['codgeo'] == codgeo:
#             territoire.append(el)
#             return jsonify({'territoires': territoire[0]})
#         if len(territoire) == 0:
#             abort(404)


@app.route('/contact')
def contact():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


if __name__ == '__main__':
    app.run(debug=True)