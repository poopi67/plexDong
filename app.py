from dotenv import load_dotenv
from flask import Flask, request
from flask import render_template

from main import query, createDong

# Loads the .env file for the credentials
load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/dong', methods=['POST'])
def display_dong():
    email = request.form['email']
    num = query(email)
    # If num doesn't have a value assigned to it, return error
    if not num:
        error = 'Invalid email/username, please try again.'
        return render_template('index.html', error=error, title='| Error')
    # Else, display the Dong
    else:
        dong = createDong(num)
        statement = '{0} you have '.format(email) + num + ' plays, therefore '
        return render_template('index.html', statement=statement, dong=dong, title="| " + email)


if __name__ == '__main__':
    app.run(host='localhost', port=6942)
