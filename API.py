
'''Q1. What is an API? Give an example, where an API is used in real life.

API stands for Application Programming Interface.

It is a set of rules and protocols that allows different software applications to communicate with each other. It defines how requests and responses should be made between systems.

Apps like Swiggy or Zomato use the Google Maps API to show you:

Your location

The restaurant's location

Real-time delivery tracking

The delivery app doesn't create its own map. Instead, it uses the Google Maps API to get location and navigation data.


'''



'''Q2. Give advantages and disadvantages of using API.
✅ Advantages of Using API:
Integration Between Systems:

APIs allow different software systems to communicate — e.g., your app talking to Google Maps or a payment gateway.

Faster Development:

You don’t have to build everything from scratch. Use existing services via APIs to save time and effort.

Automation:

APIs help automate tasks between different platforms — like syncing data between apps.

Scalability:

APIs can handle many requests, making them suitable for apps with growing users or features.

Security:

APIs can act as a gatekeeper — exposing only the necessary data/functions while hiding sensitive internal systems.

❌ Disadvantages of Using API:
Dependency on External Services:

If an external API (like Google Maps or a payment gateway) goes down or changes, your app may break.

Limited Customization:

You can only do what the API allows. You can’t modify its internal behavior.

Security Risks:

Poorly secured APIs can be a target for hacking or data breaches.

Rate Limits & Cost:

Many APIs have usage limits or paid plans — e.g., only 1000 free requests/day.

Version Compatibility:

If the API provider updates or deprecates their version, your app may need changes to keep working.'''

import requests

url= 'https://jsonplaceholder.typicode.com/users'

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    print('User List:')
    for user in users:
        print(f'{user['id']}.{user['name']} - {user['email']}')

else:
    print('Failed to retrieve data.')     



import requests

url= 'https://jsonplaceholder.typicode.com/userz'

response = requests.get(url)

if response.status_code == 200:
    users = response.json()
    print('User List:')
    for user in users:
        print(f'{user['name']}')

else:
    print(f'Error{response.status_code}: Could not fetch data')



'''Q3. What is a Web API? Differentiate between API and Web API.
A Web API is a type of API that is accessible over the internet using HTTP. It allows applications (often web or mobile) to interact with a remote server to send/receive data — usually in JSON or XML format.


Feature	          API	                                                        Web API
✅ Meaning	     Set of rules that allow two apps to communicate	           API that works over the web using HTTP/HTTPS
🌐 Network	      May or may not use a network	                                 uses a network (usually internet)
📦 Data Format	  Any format (function calls, DLLs, JSON, etc.)	                 Usually JSON or XML
💻 Access	      Local or network	                                             Over the internet
🔗 Example	      Python function API (like math.sqrt())	                      REST API like https://api.github.com/users
'''
# 💻 Code Example of a Regular (Local) API:/

import math

result = math.sqrt(16)
print('square root is:',result)

# 🌐 Code Example of a Web API:

import requests

url= 'https://jsonplaceholder.typicode.com/users/1'
response= requests.get(url)

if response.status_code == 200:
    data= response.json()
    print('User name from web API: ' ,data['name'])

else:
    print('Failed to fetch data')


'''Q4. Explain REST and SOAP Architecture. Mention shortcomings of SOAP.

🌐 REST (Representational State Transfer)
REST is a lightweight architecture for web services that uses standard HTTP methods like GET, POST, PUT, DELETE.

✅ REST Characteristics:

Stateless

Data mostly in JSON

Human-readable and easy to debug

Easily used in web/mobile apps'''

import requests

response = requests.get('https://jsonplaceholder.typicode.com/users/1')

if response.status_code == 200:
    data = response.json()
    print(f"REST API - User Name: {data['name']}")
    

'''🧼 SOAP (Simple Object Access Protocol)
SOAP is a protocol using XML for communication. It's more rigid and verbose but includes features like security, ACID transactions, and strict contracts (WSDL).

✅ SOAP Characteristics:

Uses XML only

Needs a WSDL file to define the service

Heavy and complex

Common in enterprise applications'''

from zeep import Client

wsdl = 'http://www.dneonline.com/calculator.asmx?wsdl'

client = Client(wsdl = wsdl)

result= client.service.Add(5,3)
print(f'SOAP API - Addition Result: {result}')



# ❌ Shortcomings of SOAP (Shown in Code Context)
# 🔹 1. Verbose XML (Hard to Read and Debug)

<soapenv:Envelope xmlns:soapenv ="http://schemas.xmlsoap.org/soap/envelope/">
    <soapenv:Body> 
        <Add xmlns = 'http://tempuri.org/'
            <intA>5</intA>
            <intB>3</intB>
        </Add>
    </soapenv:Body>
</soapenv:Envelope>        

# 🔹 2. Requires WSDL (Tight Coupling)
client = Client(wsdl="some_missing_or_changed.wsdl")

#  3. Slow and Complex Setup

#4. Only supports XML
