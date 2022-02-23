from flask import Flask
from flask import render_template

app = Flask(__name__)

path = 'static//'
file = 'baza_produktow.csv'

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/cennik_nagrobki')
def cennik_nagrobki():

    with open(path + file, encoding='UTF-8') as f:
        produkty = []
        for produkt in f.readlines():
            if produkt.split(";")[0].strip() == 'NAGROBKI':
                produkty.append(produkt)

    return render_template('cennik_nagrobki.html', produkty=produkty)

@app.route('/cennik_ksiazki')
def cennik_ksiazki():

    with open(path + file, encoding='UTF-8') as f:
        produkty = []
        for produkt in f.readlines():
            if produkt.split(";")[0].strip() == 'KSIAZKI':
                produkty.append(produkt)

    return render_template('cennik_ksiazki.html', produkty=produkty)


@app.route('/cennik_blaty')
def cennik_blaty():

    with open(path + file, encoding='UTF-8') as f:
        produkty = []
        for produkt in f.readlines():
            if produkt.split(";")[0].strip() == 'BLATY':
                produkty.append(produkt)

    return render_template('cennik_blaty.html', produkty=produkty)

@app.route('/cennik_schody')
def cennik_schody():

    with open(path + file, encoding='UTF-8') as f:
        produkty = []
        for produkt in f.readlines():
            if produkt.split(";")[0].strip() == 'SCHODY':
                produkty.append(produkt)

    return render_template('cennik_schody.html', produkty=produkty)

@app.route('/cennik_elewacje')
def cennik_elewacje():

    with open(path + file, encoding='UTF-8') as f:
        produkty = []
        for produkt in f.readlines():
            if produkt.split(";")[0].strip() == 'ELEWACJE':
                produkty.append(produkt)

    return render_template('cennik_elewacje.html', produkty=produkty)

@app.route('/cennik_kostka')
def cennik_kostka():

    with open(path + file, encoding='UTF-8') as f:
        produkty = []
        for produkt in f.readlines():
            if produkt.split(";")[0].strip() == 'KOSTKA':
                produkty.append(produkt)

    return render_template('cennik_kostka.html', produkty=produkty)

if __name__ == '__main__':
    app.run(debug=True)