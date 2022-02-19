from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/cennik_nagrobki')
def cennik_nagrobki():
    return render_template('cennik_nagrobki.html')


if __name__ == '__main__':
    app.run(debug=True)