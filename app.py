from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/cennik_nagrobki')
def cennik_nagrobki():

    with open('static//baza_produktow.csv', encoding='UTF-8') as f:
        produkty = []
        for produkt in f.readlines():
            if produkt.split(";")[0].strip() == 'NAGROBKI':
                produkty.append(produkt)


    return render_template('cennik_nagrobki.html', produkty=produkty)


if __name__ == '__main__':
    app.run(debug=True)