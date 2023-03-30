from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


@app.route("/")

def homepage():
    return render_template("index.html")


@app.route("/operation", methods= ["POST"])



def operation():
    if (request.method == "POST"):

        operation1 = request.form['operation']
        num1 = int(request.form['num1'])
        num2 = int(request.form['num2'])
        result = 0

        if operation1 == "add":
            result = num1 + num2
        elif operation1 == "sub":
            result = num1 - num2
        elif operation1 == "divison":
            result = num1 / num2
        elif operation1 == "multiply":
            result = num1 * num2

    return render_template("result.html", result= result)

if __name__ == "__main__":
    app.run(host= "localhost", port= 5400)