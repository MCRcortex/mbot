
# Import flask with the request object
from flask import Flask, request
app=Flask(__name__)

# You can access demobot’s greet command via <your website>/greet
@app.route('/parse',method=["GET","POST"])
def greet_person():
    # Get the value of the 'text' query parameter
    # request.values is a dictionary (cool!)
    name = request.values.get('text')#request.values.get('code')
    # This bot says hi to every name it gets sent!
    return eval(name)

# Start the web server!
if __name__ == '__main__':
    app.run()