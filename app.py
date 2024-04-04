from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'<h1>Welcome to 2022!</h1><p>Your user agent is: {user_agent}</p>'

if __name__ == '__main__':
    app.run(debug=True)
