#!flask/bin/python
from flask import Flask

app = Flask(__name__)

@app.route('/')                             # décorateur route = route par laquelle notre fonction sera accessible
def index():                                # vue index 
    return "Hello World"

@app.route('/contact')
def contact():
    mail = "jean@bon.fr"
    tel = "01 23 45 67 89"
    return "Mail: {} --- Tel: {}".format(mail, tel)


if __name__ == '__main__':
    app.run(debug=True)