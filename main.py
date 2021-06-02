from flask import Flask, request, redirect
from flask import render_template
from dotenv import load_dotenv
import os
import requests
import json
import math

# Loads the .env file for the credentials
load_dotenv()

app = Flask(__name__)

# Handles the query to the API
def query(user):
    # Takes in the Tautulli API/Server credentials from the .env file
    api_token = os.environ.get('api_token')
    server_url = os.environ.get('server_url')
    user = user
    api_url_base = '{0}/api/v2?apikey={1}&cmd=get_users_table&order_column=plays&search={2}'.format(server_url, api_token, user)
    headers = {'Content-Type': 'application/json'}
    response = requests.get(api_url_base, headers=headers)
    users = json.loads(response.text)
    for user in users['response']['data']['data']:
        # If the record does not exist, continue
        if 'recordsFiltered' == 0 in users:
            continue
        # Otherwise, return the value
        else:
            return str(user['plays'])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dong', methods=['POST'])
def displayDong():
    email = request.form['email']
    num = query(email)
    # If num doesn't have a value assigned to it, return error
    if not num:
        error = 'Invalid email/username, please try again.'
        return render_template('index.html', error=error, title='| Error')
    # Else, display the Dong
    else:
        # The variables to create the dong
        # Gets the total watch amount and divides it by 5 then displays the, uh, shaft
        # using the newCount number with "="'s
        dongDigit = math.trunc(int(num) / 5)
        dong =  '8' + '='*dongDigit + 'D'
        statement = '{0} you have '.format(email) + num + ' plays, therefore '
        return render_template('index.html', statement=statement, dong=dong, title="| " + email)
        return redirect('/')


if __name__ == '__main__':
    app.run(host='localhost', port=6942)
