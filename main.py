from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/Solarsystem')
def Solarsystem():
    return render_template("Solarsystem.html")


@app.route('/Sun')
def Sun():
    return render_template("Sun.html")


@app.route('/Mercury')
def Mercury():
    return render_template("Mercury.html")


@app.route('/Venus')
def Venus():
    return render_template("Venus.html")


@app.route('/Earth')
def Earth():
    return render_template("Earth.html")


@app.route('/Mars')
def Mars():
    return render_template("Mars.html")


@app.route('/Jupiter')
def Jupiter():
    return render_template("Jupiter.html")


@app.route('/Saturn')
def Saturn():
    return render_template("Saturn.html")


@app.route('/Uranus')
def Uranus():
    return render_template("Uranus.html")


@app.route('/Neptune')
def Neptune():
    return render_template("Neptune.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')