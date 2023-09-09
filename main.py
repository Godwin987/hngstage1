from flask import Flask, request
from datetime import datetime


app = Flask(__name__)
response = {
    'current_day': f'{datetime.day}',
    'utc_time': f'{datetime.time()}',
    'github_file_url':
}
@app.route('/get/<slack_name>')
def index():
    return "hello"




if __name__ == '__main__':
    app.run(debug=True)
