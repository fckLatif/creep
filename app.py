from flask import Flask, render_template, redirect

app = Flask(__name__)
app.secret_key = "dev"

@app.errorhandler(404)
def page_not_found_redirect(e):
    return render_template('404.html'), 404   

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/downloads")
def downloads():
    return render_template("downloads.html")

if __name__ == "__main__":
    app.run(debug=True)