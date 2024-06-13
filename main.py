<<<<<<< HEAD
from flask import Flask, render_template, request
=======
from flask import Flask, render_template,request
>>>>>>> incorrect_branch_name

app = Flask(__name__)

@app.route('/')
def home():
<<<<<<< HEAD
   return "Welcome to COMP3900 and COMP9900"
=======

>>>>>>> incorrect_branch_name

@app.route('/calculator')
def calculator():
    num1 = int(request.form['num1'])
    num2 = int(request.form['num2'])
<<<<<<< HEAD
    result = num1 + num2  
    return render_template('calculator.html', result=result)

    return render_template('calculator.html')
=======
>>>>>>> incorrect_branch_name

if __name__ == '__main__':
    app.run(debug=True)
