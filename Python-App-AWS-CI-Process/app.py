from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, This is my first python app using CI process and AWS'

if __name__ == '__main__':
    app.run()
