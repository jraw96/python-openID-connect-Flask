# Import flask and declare the app
from flask import Flask
# Import the render_template module to open and read html files
from flask import Flask, render_template
# Import the flask oidc library and declare an instance of the openID object
from flask_oidc import OpenIDConnect

# Declare the app
app = Flask(__name__)

# Attach the client_secrets.json file and configure other parameters
app.config.update({
    'SECRET_KEY': 'notSureWhatThisIs',
    'TESTING': True,
    'DEBUG': True,
    'OIDC_CLIENT_SECRETS': 'client_secrets.json',
    'OIDC_ID_TOKEN_COOKIE_SECURE': False,
    'OIDC_REQUIRE_VERIFIED_EMAIL': False
})


# Create an instance of the OpendID Connect object
oidc = OpenIDConnect(app)


# Require authentication at for the home page
@app.route('/')
def theMain():
    return render_template('index.html')


@app.route('/private')
@oidc.require_login
def hello_me():
     return render_template('secure.html')


if __name__ == '__main__':
    app.run(port=8080, debug=True)