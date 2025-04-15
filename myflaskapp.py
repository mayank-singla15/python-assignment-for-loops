# Q1. What is Flask Framework? What are the advantages of Flask Framework?
'''Flask is a lightweight and flexible web framework written in Python. It is classified as a micro-framework because it does not require particular tools or libraries. Flask is designed to be simple and easy to get started with, but it's also highly extensible, allowing developers to add extensions as needed.

It is widely used to build web applications and REST APIs and is known for its simplicity, flexibility, and fine-grained control over components.

🔥 Key Features of Flask:
Lightweight and modular

Built-in development server and debugger

RESTful request dispatching

Supports secure cookies (client-side sessions)

WSGI compliant (uses Werkzeug)

Integrated support for unit testing

Jinja2 templating engine

✅ Advantages of Flask Framework:
Simplicity and Flexibility – Easy to learn and understand.

Minimal Setup – No boilerplate code to start a project.

Modular – Add only what you need using extensions.

Easy to Debug – Comes with a built-in debugger and interactive shell.

RESTful request handling – Ideal for building APIs.

Scalable – While it’s minimal, it can scale with your app’s needs.'''

# Q2. Create a simple Flask application to display ‘Hello World!!’.


from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello,Flask!'

if __name__ == '__main__':
    
    app.run(debug = True)


# Q3. What is App routing in Flask? Why do we use app routes?
'''App Routing in Flask is the process of binding a URL to a specific function. This means when a user visits a specific URL (like /home or /about), Flask will run the function you associated with that route and return its output to the browser.

In Flask, this is done using the @app.route() decorator.

🔥 Why Do We Use App Routes?
To connect URLs with specific functions (views)

To handle different web pages or API endpoints

To create clean, readable, and RESTful URLs

To make your web application interactive and navigable'''

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the home page!'

@app.route('/about')
def about():
    return 'This is the about page!' 

@app.route('/contact')
def contact():
    return 'Contact us at contact@example.com'

if __name__ == 'main':
    app.run(debug=True)           
        
'''Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”
route to show the following details:
Company Name: ABC Corporation
Location: India
Contact Detail: 999-999-9999'''

from flask import Flask

app=Flask(__name__)

@app.route('/welcome')
def welcome():
    return 'Welcome to ABC Corporation'

@app.route('/')
def company_details():
    return """
    <h2>Company Name: ABC Corporation</h2>
    <h2>Location: India</h2>
    <h2>Contact Detail:999-999-9999</h2>
    """ 

if __name__ == '__main__':
    app.run(debug=True)       

'''Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the
url_for() function.
 Purpose of url_for():
Dynamically builds URLs for functions linked with routes.

Makes your app more maintainable — you don’t need to hard-code URLs.

It ensures URLs are always correct, even if routes are changed.

'''
from flask import Flask,url_for


app = Flask(__name__)

@app.route('/')
def home():
    return f"""
        <h2>Welcome!</h2>
        <a href = "{url_for('about')}">About</a><br>
        <a href=  "{url_for('user_profile',username = 'mayank')}">User Profile </a> 
    """
@app.route('/about')
def about():
    return 'This is the about page' 

@app.route('/user/<username>')
def user_profile(username):
    return f'Hello,{username}! This is your profile.'

if __name__ =='__main__':
    app.run(debug=True)                
