from flask import Flask, render_template, request

import random

app= Flask(__name__,template_folder='templates')



images=[
    '1.jpg',
    '2.jpg',
    '3.jpg',
    '4.jpg',
    '5.jpg',
    '6.jpg'
]



@app.route("/")
def game():
    return render_template('index.html',img=images[0])


@app.route("/roll",methods=["POST"])
def roll():
    numbers=random.randint(0,5)
    return render_template('index.html',img=images[numbers])



if __name__=="__main__":
    app.run(debug=True)