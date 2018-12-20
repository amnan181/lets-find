from flask import Flask, redirect, url_for

#INSTALL FLASK-DANCE
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)


##################################
########## CODE START ############
##################################


app.config['SECRET_KEY'] = 'my app secrete key bro'

#client id or secret key bro google login api pr account bnany pr mily gi or y aik to https ko accept krta h or dosra domain.
google_blueprint = make_google_blueprint(client_id='client id', client_secret='secrete kry')
app.register_blueprint(google_blueprint, url_prefix="/google_login")

#ye bi bro same h facebook developer pr account bna kr new app bnana h or phir wohi secret or client id mil jayn gay
facebook_blueprint = make_facebook_blueprint(client_id='client_id', client_secret='client_secret')
app.register_blueprint(facebook_blueprint, url_prefix='/facebook_login')


@app.route('/google')
def google_login():
    if not google.authorized:
        #y jb hm domain/google lagay gay to y check kry ga ky user authorized nahi h to us ko google login page pr redirect krva daiata h
        return redirect(url_for('google.login'))

    #yaha sy data json mn milta h use ka...
    account_info = google.get('/oauth2/v2/userinfo')

    #agr status ok ho to ex 200
    if account_info.ok:
        account_info_json = account_info.json()
        return '<h1>Your facebook name is @{}'.format(account_info_json['email'])
    #agr request complete na hoi to
    return '<h1>Request failed!</h1>'





#same facebook ka bi

@app.route('/facebook')
def facebook_login():
    if not twitter.authorized:
        return redirect(url_for('facebook.login'))
    account_info = twitter.get('account/settings.json')

    if account_info.ok:
        account_info_json = account_info.json()

        return '<h1>Your facebook name is @{}'.format(account_info_json['yaha khud check kr laina bro k y json mn kia kia bhaij raha h jaisy user ka name or id wagaira'])


    return '<h1>Request failed!</h1>'

##################################
########### CODE END #############
##################################

#server route
@app.route('/')
def index():
    return "Lets find server, up and running"

if __name__ == "__main__":
    app.run(port='8080', debug=True)
