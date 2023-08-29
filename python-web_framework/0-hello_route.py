"""here we import the flask module"""
from flask import Flask

"""we intialise the Flask module"""
app = Flask(__name__)


"""we declare the route of the resource"""
@app.route("/",strict_slashes = False)
def main():
    """here is the function that executes when that route is hit"""
    return "Hello HBNB!";

if __name__ == "__name__":
    app.run(host="0.0.0.0",port = 5000)