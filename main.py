from flask import Flask, url_for, render_template, request

app = Flask(__name__, template_folder='templates')


@app.route('/', methods=["POST", "GET"])
def home():
    if request.method == "POST":
        print(request.form)
    return render_template('/home.html')


app.run(debug=True)