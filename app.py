from crypt import methods
from flask import Flask,render_template, request
from bs4 import BeautifulSoup


app = Flask(__name__)

@app.route("/", methods = ['GET', 'POST'])

def home():
    if request.method == 'POST':
        text_file = open('file','r')
        text = text_file.read()
        soup = BeautifulSoup(text).get_text()
        print("it posted in home")
        return render_template("result.html",soup = soup)
    else:
        return render_template("layout.html")


@app.route("/result", methods = ['GET', 'POST'])

def result():
    print('hello')
    if request.method == 'POST':
        text_file = open('file','r')
        text = text_file.read()
        soup = BeautifulSoup(text).get_text()
        print("it posted in results")
        return render_template("result.html",soup = soup)
    else:
        print('poop')


        




if __name__ == '__main__':
    app.run(debug=True)