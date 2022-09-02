from crypt import methods
from flask import Flask,render_template, request
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])

def home():
    if request.method == 'POST':
        return render_template("result.html")
    else:
        print("it get in home")

        return render_template("layout.html")


@app.route("/result", methods = ['GET', 'POST'])

def result():
    if request.method == 'POST':
        text = request.files['file']
        soup = BeautifulSoup(text).get_text()
        print("it posted in request")
        return render_template("result.html", soup = soup)
    else:
        print('it get in request')


        




if __name__ == '__main__':
    app.run(debug=True)