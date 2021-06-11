import requests
from flask import Flask, request
from flask import render_template

from main import single_query, create_dong, get_all

app = Flask(__name__)


@app.route('/')
def index():
    default = "Enter a Username/Email &#128522;"
    return render_template('index.html', default=default, isIndex=True)


@app.route('/dong', methods=['POST'])
def display_dong():
    email = request.form['email']
    plays, username = single_query(email)
    dong = create_dong(plays)
    all_names, all_dongs = get_all()
    # If num doesn't have a value assigned to it, return error
    if not username:
        error = 'Invalid email/username, please try again.'
        return render_template('index.html', error=error, title='| Error')
    # Else, display the Dong
    else:
        statement = '{0} you have '.format(username) + plays + ' plays, therefore '
        return render_template('index.html', statement=statement, dong=dong, title="| " + email, all_names=all_names,
                               all_dongs=all_dongs,
                               isIndex=False)


# Handles an error that is produced when an invalid email/username is entered
@app.errorhandler(500)
def internal_error(error):
    msg = '<p style="color:red;">Invalid email/username, please try again.</p><br />'
    return render_template('index.html', error=error, msg=msg, title='| Error', isIndex=True)


# Handles an error that is produced when the URL is invalid
@app.errorhandler(requests.exceptions.ConnectionError)
def connection_error(error):
    msg = '<p style="color:red;">The credentials you entered were incorrect, please try again.</p><br />'
    return render_template('index.html', error=error, msg=msg, title='| Error', isIndex=True)


# Allows for values to be zipped in the flask for-loop templates
@app.template_global(name='zip')
def _zip(*args, **kwargs):
    return __builtins__.zip(*args, **kwargs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8787)
