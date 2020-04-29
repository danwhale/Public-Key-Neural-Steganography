from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_form():
    return render_template("form.html")

@app.route("/form", methods=["POST"])
def post_form():
  return render_template("results.html", context="", message="", method="")

if __name__ == '__main__':
    app.run()