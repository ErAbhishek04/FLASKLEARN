

from flask import Flask, redirect, url_for , render_template ,request

app = Flask(__name__)

@app.route('/')

def welcome():

    return render_template("index.html")

@app.route('/success/<int:score>')
def success(score):
    if score>=50:
        res = "Pass"

    else:
        res = "Fail"

    expr ={'score' :score , 'res' : res}

    return render_template("result.html", result = expr)

@app.route('/fail/<int:score>')
def fail(score):
    return "Failing with " + str(score) + " Marks"

@app.route('/results/<int:marks>')
def results(marks):
    if marks > 50:
        return redirect(url_for('success', score=marks))
    else:
        return redirect(url_for('fail', score=marks))
    

@app.route('/submit', methods=['POST' ,'GET'])

def submit():

    if request.method == 'POST':

        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience =float(request.form['datascience'])
        total = (science+maths+c+datascience)//4

    if total>=50:

        return redirect(url_for("success", score = total ))
    
    else:

        return redirect(url_for("fail" , score = total))

if __name__ == '__main__':
    app.run(debug=True)
