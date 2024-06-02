from flask import Flask

application = Flask(__name__)

@application.route('/')
def hello():
    return 'Hello, This is Binaya Timsina and this is his website!'

if __name__ == '__main__':
    application.run(debug=True)
