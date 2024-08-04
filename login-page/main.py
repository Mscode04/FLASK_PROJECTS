from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates')


@app.route("/")
def game():
    return render_template('index.html') 

@app.route("/login",methods=["POST",'GET'])
def loginform():
    if request.form['email']=='ms.shaheenkp@gmail.com' and request.form['pass']=="1234":
        return render_template('dashbord.html')
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)