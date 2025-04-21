'''Q1. Explain GET and POST methods.
In Flask, routes can handle different HTTP methods like GET and POST.

GET is used to retrieve data (e.g., visit a webpage, fetch an API response).

POST is used to submit data (e.g., form submission, sending JSON to an API).'''

from flask import Flask, request, jsonify

app = Flask(__name__)
@app.route('/greet',methods = ['GET','POST'])
def greet():
    if request.method == 'GET':
        name = request.args.get('name','Guest')
        return jsonify({'message':f'Hello {name}! (from GET)'})

    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name','Guest')
        return jsonify({'message':f'Hello,{name}! (from POST)'})

if __name__ == '__main__':
    app.run(debug= True)      

'''Q2. Why is request used in Flask?

The request object in Flask is used to access incoming data from the client — whether it's coming from:

URL parameters (GET)

Form inputs

JSON data

Headers

Cookies

Basically, anytime someone sends something to your server (like filling a form or calling your API), request helps you read that data.''' 

# Getting Data from a POST Request

from flask import Flask,request

app = Flask(__name__)

@app.route('/login',methods = ['POST'])
def login():

    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    return jsonify({
        'message':f"Received credentials for {username}"
    })

if __name__ == '__main__':
    app.run(debug= True)

'''Q3. Why is redirect() used in Flask?

In Flask, redirect() is used to redirect the user to a different route or URL after something happens.
Common Use Cases:
After logging in, redirect to a dashboard

After submitting a form, redirect to a thank-you page

Redirect from an old page to a new one'''

from flask import Flask,request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return  '''
        <form method="POST" action="/login">
            <input type="text" name="username" placeholder="Enter username">
            <button type="submit">Login</button>
        </form>
    '''

@app.route('/login',methods = ['POST'])
def login():
    username = request.form.get('username')
    print(f'User logged in: {username}')
    return redirect(url_for('welcome'))

@app.route('/welcome')
def welcome():
    return 'Welcome to ypur dashboard!'

if __name__ == '__main__':
    app.run(debug = True) 
       
'''Q4. What are templates in Flask? Why is the render_template() function used?
Templates in Flask are HTML files that let you separate your web page design from your Python logic.

Instead of returning a plain string like "Hello, World!", you can return a full HTML page using Jinja2 templating — which Flask uses by default.

🎯 Why Use render_template()?
render_template() is used to:

Load an HTML file from the templates folder

Inject dynamic content (like names, lists, etc.)

Render it into a complete HTML response''' 

from flask import Flask,request, render_template

app = Flask(__name__)

@app.route('/greet',methods = ['GET'])
def greet():
    name= request.args.get('name','Guest')
    return render_template('greet.html', name= name)

if __name__ == '__main__':
    app.run(debug=True) 
       

