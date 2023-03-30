from flask import Flask, request



app = Flask(__name__)   #initialize with the flask


# Routes

@app.route("/")
def hello_world():
    return "hello world"


@app.route("/about us")
def about_us():
    return "we are ineuron"


@app.route("/demo", methods= ["POST"])
def math_operation():
    if (request.method == "POST"):
        operation = request.json['operation']
        num1 = int(request.json['num1'])
        num2 = int(request.json['num2'])

        if operation == "add":
            result = num1 + num2
        elif operation == "multiply":
                result = num1 * num2
        elif operation == "divison":
                result = num1 / num2
        else:
             result = num1 - num2
        return f"the operation is {operation} and the result is {result}"

@app.route("/multiply", methods= ["POST"])
def math_multiply():
    if (request.method == "POST"):
        operation = request.json['operation']
        num1 = request.json['num1']
        num2 = request.json['num2']
        result = num1 * num2

        return f"the operation is {operation} and the result is {result}"

if __name__ == "__main__":
    app.run(host= "localhost", port= 5302)   # host is where the application is running
                                            #port shows through which port we have ato access this application.
    