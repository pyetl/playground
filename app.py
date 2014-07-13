#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jaik
#
# Created:     21/06/2014
# Copyright:   (c) jaik 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# This route will show a form to perform an AJAX request
# jQuery is loaded to execute the request and update the
# value of the operation
@app.route('/')
@app.route("/home")
def index():
    print ' Called Index'
    return render_template('index.htm')

@app.route("/signup")
def signup():
    return render_template('signup.htm')

@app.route("/signme" , methods=['POST','GET'])
def signme():
    email = request.args.get('email')
    passw = request.args.get('password')
    return "Login-To" + email + passw


# Route that will process the AJAX request, sum up two
# integer numbers (defaulted to zero) and return the
# result as a proper JSON response (Content-Type, etc.)
@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

if __name__ == '__main__':
    print 'Running App'
    app.run( debug=True)

