from flask import Flask, request
from flask import render_template

from main import query, create_dong

app = Flask(__name__)


@app.route('/')
def index():
    default = "Enter a Username/Email &#128522;"
    return render_template('index.html', default=default)


@app.route('/dong', methods=['POST'])
def display_dong():
    email = request.form['email']
    plays, username = query(email)
    # If num doesn't have a value assigned to it, return error
    if not username:
        error = 'Invalid email/username, please try again.'
        return render_template('index.html', error=error, title='| Error')
    # Else, display the Dong
    else:
        dong = create_dong(plays)
        statement = '{0} you have '.format(username) + plays + ' plays, therefore '
        return render_template('index.html', statement=statement, dong=dong, title="| " + email)


@app.errorhandler(500)
def internal_error(error):
    msg = '<p style="color:red;">Invalid email/username, please try again.</p><br />'
    return render_template('index.html', error=error, msg=msg, title='| Error')


if __name__ == '__main__':
    app.run(host='localhost', port=8787)
