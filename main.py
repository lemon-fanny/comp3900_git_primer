from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
   return "Welcome to COMP3900 and COMP9900"

@app.route('/calculator')
def calculator():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
    result = num1 + num2  
    return render_template('calculator.html', result=result)

    return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
