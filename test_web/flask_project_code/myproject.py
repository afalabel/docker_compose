from flask import Flask
application = Flask(__name__)

@application.route("/hello")
def hello():
    return "<h1 style='color:blue'>Hello There!</h1>"

@application.route('/test')
def test():
    return 'Hello, Test'

@application.route("/")
def main():
    return "<h1 style='color:blue'>Main!</h1>"

@application.route('/about')
def about():
    return 'The about page'

@app.route('/login')
def login():
    return 'login'

if __name__ == "__main__":
    application.run(host='0.0.0.0')
