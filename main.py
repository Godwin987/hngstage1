from flask import Flask, request, jsonify
from datetime import datetime

app = Flask(__name__)


@app.route('/api/')
def index():
    response = {
        'slack_name': request.args.get('slack_name'),
        'current_day': f'{datetime.now().strftime("%A")}',
        'utc_time': f'{datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")}',
        'track': request.args.get('track'),
        'github_file_url': 'https://github.com/Godwin987/hngstage1/blob/master/main.py',
        'github_repo_url': 'https://github.com/Godwin987/hngstage1',
        'status_code': 200
    }
    response = jsonify(response)
    return response


if __name__ == '__main__':
    app.run(debug=True)
