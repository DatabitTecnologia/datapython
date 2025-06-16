from flask import Flask, render_template, url_for

app = Flask(__name__, template_folder='templates', static_url_path='/static')


@app.route("/")
def iniciar():
    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True, port=8878)
