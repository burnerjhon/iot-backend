# Basic Flask app to serve the model as an API

from flask import Flask, request

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check():
    data = request.get_json(force=True)
    print(data)
    return 'OK'

if __name__ == '__main__':
    app.run()
