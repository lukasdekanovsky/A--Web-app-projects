from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/portfolio/desktopapp")
def desktop():
    return render_template("desktop.html")

@app.route("/portfolio/webapp")
def web():
    return render_template("web.html")

@app.route("/portfolio/ai")
def ai():
    return render_template("machine.html")


if __name__ == "__main__":
    app.run(debug=True)