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
    all_user = get_all()
    # If num doesn't have a value assigned to it, return error
    if not username:
        error = 'Invalid email/username, please try again.'
        return render_template('index.html', error=error, title='| Error')
    # Else, display the Dong
    else:
        statement = '{0} you have '.format(username) + plays + ' plays, therefore '
        return render_template('index.html', statement=statement, dong=dong, title="| " + email, alluser=all_user, isIndex=False)


@app.errorhandler(500)
def internal_error(error):
    msg = '<p style="color:red;">Invalid email/username, please try again.</p><br />'
    return render_template('index.html', error=error, msg=msg, title='| Error')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8787)
