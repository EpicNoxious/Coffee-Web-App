import time
from flask import Flask, render_template, redirect, url_for, request, flash, jsonify, session
from pymongo import MongoClient
from forms import SignUp, SignIn, Menu, Buy, CheckOut
from functools import wraps
from turbo_flask import Turbo
import uuid
import smtplib



# app = Flask(__name__, static_url_path='', static_folder="./static")
app = Flask(__name__)
turbo = Turbo(app)
app.secret_key = 'Caffeine 101'
cluster = "mongodb+srv://Noxious:Ja-pp-re-et16@cluster0.p231li5.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(cluster)
db = client['brew-nation']
users = db.users
device = db.machine


def is_enough(need_water=0, need_milk=0, need_beans=0, need_cups=1):
    result = device.find_one({'name': 'caffeine 101'})
    if result['water'] < need_water:
        print('Sorry, not enough water!\n')
        raise ResourceError
    elif result['milk'] < need_milk:
        print('Sorry, not enough milk!\n')
        raise ResourceError
    elif result['beans'] < need_beans:
        print('Sorry, not enough beans!\n')
        raise ResourceError
    elif result['cups'] < need_cups:
        print('Sorry, not enough cups\n')
        raise ResourceError
    else:
        print('I have enough resources, making you a coffee!\n')


def is_not_enough(obj):
    if obj <= 0:
        print('Please add this coffee in the basket, first\n')
        raise ResourceError
    else:
        print('Coffee removed\n')

# Add functions
def add_espresso():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=50, need_beans=24)
        items['money'] += 2.50
        items['water'] -= 50
        items['milk'] -= 0
        items['beans'] -= 24
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.espresso': 1}}
        )
        flash("Espresso Added")

    except ResourceError:
        pass


def add_latte():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=50, need_milk=200, need_beans=16)
        items['money'] += 3.50
        items['water'] -= 50
        items['milk'] -= 200
        items['beans'] -= 16
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.latte': 1}}
        )
        flash("Latte Added")

    except ResourceError:
        pass

def add_cappuccino():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=90, need_milk=160, need_beans=18)
        items['money'] += 4.00
        items['water'] -= 90
        items['milk'] -= 160
        items['beans'] -= 18
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.cappuccino': 1}}
        )
        flash("Cappuccino Added")
    except ResourceError:
        pass


def add_coldbrew():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=50, need_milk=200, need_beans=14)
        items['money'] += 4.00
        items['water'] -= 50
        items['milk'] -= 200
        items['beans'] -= 14
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.coldbrew': 1}}
        )
        flash("Cold Brew Added")
    except ResourceError:
        pass

def add_americano():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=250, need_milk=0, need_beans=17)
        items['money'] += 4.00
        items['water'] -= 250
        items['milk'] -= 0
        items['beans'] -= 17
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.americano': 1}}
        )
        flash("Americano Added")
    except ResourceError:
        pass


def add_macchiato():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=0, need_milk=250, need_beans=20)
        items['money'] += 4.50
        items['water'] -= 0
        items['milk'] -= 250
        items['beans'] -= 20
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.macchiato': 1}}
        )
        flash("Macchiato Added")
    except ResourceError:
        pass


def add_flatwhite():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=0, need_milk=250, need_beans=15)
        items['money'] += 4.75
        items['water'] -= 0
        items['milk'] -= 250
        items['beans'] -= 15
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.flatwhite': 1}}
        )
        flash("Flat White Added")
    except ResourceError:
        pass


def add_affogato():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=90, need_milk=160, need_beans=18)
        items['money'] += 5.00
        items['water'] -= 30
        items['milk'] -= 220
        items['beans'] -= 15
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.affogato': 1}}
        )
        flash("Affogato Added")
    except ResourceError:
        pass


def add_tea():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=250, need_milk=0, need_beans=0)
        items['money'] += 1.75
        items['water'] -= 250
        items['milk'] -= 0
        items['beans'] -= 0
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.tea': 1}}
        )
        flash("Tea Added")
    except ResourceError:
        pass


def add_coffeemilkshake():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=0, need_milk=250, need_beans=20)
        items['money'] += 5.25
        items['water'] -= 0
        items['milk'] -= 250
        items['beans'] -= 20
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.coffeemilkshake': 1}}
        )
        flash("Coffee Milk Shake Added")
    except ResourceError:
        pass


def add_cafebreve():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=45, need_milk=205, need_beans=14)
        items['money'] += 3.00
        items['water'] -= 45
        items['milk'] -= 205
        items['beans'] -= 14
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.cafebreve': 1}}
        )
        flash("Cafe Breve Added")
    except ResourceError:
        pass


def add_mocha():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_enough(need_water=40, need_milk=210, need_beans=19)
        items['money'] += 4.25
        items['water'] -= 40
        items['milk'] -= 210
        items['beans'] -= 19
        items['cups'] -= 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.mocha': 1}}
        )
        flash("Cafe Breve Added")
    except ResourceError:
        pass

#  Remove functions
def remove_espresso():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['espresso'])
        items['money'] -= 2.50
        items['water'] += 50
        items['milk'] += 0
        items['beans'] += 24
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.espresso': -1}}
        )
        flash("Espresso Removed")
    except ResourceError:
        pass


def remove_latte():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['latte'])
        items['money'] -= 3.50
        items['water'] += 50
        items['milk'] += 200
        items['beans'] += 16
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.latte': -1}}
        )
        flash("Latte Removed")
    except ResourceError:
        pass


def remove_cappuccino():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['cappuccino'])
        print('latte')
        items['money'] -= 4.00
        items['water'] += 90
        items['milk'] += 160
        items['beans'] += 18
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.cappuccino': -1}}
        )
        flash("Cappuccino Removed")
    except ResourceError:
        pass


def remove_coldbrew():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['coldbrew'])
        items['money'] -= 4.00
        items['water'] += 50
        items['milk'] += 200
        items['beans'] += 14
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.espresso': -1}}
        )
        flash("Cold Brew Removed")
    except ResourceError:
        pass

def remove_americano():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['americano'])
        items['money'] -= 4.00
        items['water'] += 250
        items['milk'] += 0
        items['beans'] += 17
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.americano': -1}}
        )
        flash("Americano Removed")
    except ResourceError:
        pass

def remove_macchiato():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['macchiato'])
        items['money'] -= 4.50
        items['water'] += 0
        items['milk'] += 250
        items['beans'] += 20
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.macchiato': -1}}
        )
        flash("Macchiato Removed")
    except ResourceError:
        pass



def remove_flatwhite():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['flatwhite'])
        items['money'] -= 4.75
        items['water'] += 0
        items['milk'] += 250
        items['beans'] += 15
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.flatwhite': -1}}
        )
        flash("Flat White Removed")
    except ResourceError:
        pass

def remove_affogato():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['affogato'])
        items['money'] -= 5.00
        items['water'] += 30
        items['milk'] += 220
        items['beans'] += 15
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.affogato': -1}}
        )
        flash("Affogato Removed")
    except ResourceError:
        pass

def remove_tea():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['tea'])
        items['money'] -= 1.75
        items['water'] += 250
        items['milk'] += 0
        items['beans'] += 0
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.tea': -1}}
        )
        flash("Tea Removed")
    except ResourceError:
        pass

def remove_coffeemilkshake():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['coffeemilkshake'])
        items['money'] -= 5.25
        items['water'] += 0
        items['milk'] += 250
        items['beans'] += 20
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.coffeemilkshake': -1}}
        )
        flash("Coffee Milk Shake Removed")
    except ResourceError:
        pass

def remove_cafebreve():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['cafebreve'])
        items['money'] -= 3.00
        items['water'] += 45
        items['milk'] += 205
        items['beans'] += 14
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.cafebreve': -1}}
        )
        flash("Cafe Breve Removed")
    except ResourceError:
        pass


def remove_mocha():
    items = device.find_one({'name': 'caffeine 101'})
    user_email = session['user']['email']
    user = users.find_one({'email': user_email})
    try:
        is_not_enough(user['cart']['mocha'])
        items['money'] -= 4.25
        items['water'] += 40
        items['milk'] += 210
        items['beans'] += 19
        items['cups'] += 1
        device.update_one(
            {'name': 'caffeine 101'},
            {'$set': {'money': items['money'], 'water': items['water'], 'milk': items['milk'], \
                      'beans': items['beans'], 'cups': items['cups']}}
        )
        users.update_one(
            {'email': user['email']},
            {'$inc': {'cart.mocha': -1}}
        )
        flash("Mocha Removed")
    except ResourceError:
        pass


class ResourceError(Exception):
    pass

class User:
    def start_session(self, user):
        del user['password']
        session['logged_in'] = True
        session['user'] = user
        return jsonify(user), 200

    def signup(self, user_data):
        user = {
            "_id": user_data['_id'],
            "name": user_data['name'],
            "email": user_data['email'],
            "password": user_data['password'],
            'cart': {
                    'espresso': 0,
                    'latte': 0,
                    'cappuccino': 0,
                    'coldbrew': 0,
                    'americano': 0,
                    'macchiato': 0,
                    'flatwhite': 0,
                    'affogato': 0,
                    'tea': 0,
                    'coffeemilkshake': 0,
                    'cafebreve': 0,
                    'mocha': 0
                }
        }
        users.insert_one(user)
        flash("User Signed Up")
        return self.start_session(user)

    def signin(self, user_data):
        user = {
            "_id": user_data['_id'],
            "name": user_data['name'],
            "email": user_data['email'],
            "password": user_data['password'],
            "cart": user_data['cart']
        }
        flash("User Signed In")
        return self.start_session(user)

    def details(self):
        return session['user']

    def signout(self):
        session.clear()
        return redirect('/')


class Machine:
    def contents(self):
        result = device.find_one({'name': 'caffeine 101'})
        return result


@app.after_request
def after_request(response):
    # if the response has the turbo-stream content type, then append one more
    # stream with the contents of the alert section of the page
    if response.headers['Content-Type'].startswith(
            'text/vnd.turbo-stream.html'):
        response.response.append(turbo.update(
            render_template('alert.html'), 'alert').encode())
        if response.content_length:
            response.content_length += len(response.response[-1])
    return response


def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return f(*args, **kwargs)
        else:
            flash("Login First")
            return redirect("/")
    return wrap


@app.route("/", methods=['GET', 'POST'])
def index():
    EMAIL = 'jappreet.016@gmail.com'
    PASSWORD = 'geymlajpkvjnnhuk'
    if request.method == 'POST' and 'send_email' in request.form:
        def send_email(email):
            with smtplib.SMTP("smtp.gmail.com", 587) as connection:
                connection.ehlo()
                connection.starttls()
                connection.ehlo()
                connection.login(EMAIL, PASSWORD)
                subject = 'Welcome to Brew Nation'
                body = f'Hi, Welcome to Brew Nation we are excited to have you on board and we would love to say thank you on behalf of our whole organisation for chosing us. We undersatnd that coffee is important in your life and thats why you are here, right? Brew Nation is an old and reputed coffee brand which started its ever long journey in 1984 and here you will experience a complete different experience to enjoy your coffee cup. To get for first free coffee cup you need to follow the following steps: \
                    \n\nSTEP-1: Capture a picture or a short video of yourself showing how much you love coffee! \
                    \n\nSTEP-2: Post it with #brewnation \
                    \n\nSTEP-3: Show it to our employee to avail your first free cup' 

                msg = f"Subject: {subject}\n\n{body}"
                connection.sendmail(EMAIL, email, msg)
                flash("Email has been sent successfully")

        email = request.form["email"]
        send_email(email)
    return render_template('index.html')


@app.route("/register/", methods=['GET', 'POST'])
def sign_up_in():
    signup = SignUp()
    signin = SignIn()
    name_error = ''
    if signup.signup.data and signup.validate():
        print('Sign Up')
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        result = users.find_one({'email': email})

        if result is not None:
            flash("User already exists")

        elif password != confirm_password:
            flash("Passwords don't match")

        else:
            user_data = {
                '_id': uuid.uuid4().hex,
                 'name': name,
                 'email': email,
                 'password': password
                 }
            user = User()
            user.signup(user_data)
            return redirect(url_for('index'))

        if turbo.can_stream():
            return turbo.stream(turbo.update(name_error, 'name_error'))

    if signin.signin.data and signin.validate():
        print('Sign In')
        email = request.form['email']
        password = request.form['password']
        user_data = users.find_one({'email': email})
        if user_data is None:
            flash("No such email exist")
        elif password != user_data['password']:
            flash("Incorrect Password")
        else:
            user = User()
            user.signin(user_data)
            return redirect(url_for('index'))

        if turbo.can_stream():
            return turbo.stream(turbo.update(name_error, 'name_error'))
    return render_template("sign_up_in.html", signup=signup, signin=signin)


@app.route("/menu/", methods=['POST', 'GET'])
def menu():
    buy = Buy()
    menu = Menu()

    if turbo.can_stream():
        if menu.add_es and request.form['btn'] == '+ Espresso':  # espresso
            if 'logged_in' in session:
                add_espresso()
            else:
                flash("Login First")
        if menu.remove_es() and request.form['btn'] == '- Espresso':  # espresso
            if 'logged_in' in session:
                remove_espresso()
            else:
                flash("Login First")
        if menu.add_la() and request.form['btn'] == '+ Latte':  # latte
            if 'logged_in' in session:
                add_latte()
            else:
                flash("Login First")
        if menu.remove_la() and request.form['btn'] == '- Latte':  # latte
            if 'logged_in' in session:
                remove_latte()
            else:
                flash("Login First")
        if menu.add_ca() and request.form['btn'] == '+ Cappuccino':  # cappuccino
            if 'logged_in' in session:
                add_cappuccino()
            else:
                flash("Login First")
        if menu.remove_ca() and request.form['btn'] == '- Cappuccino':  # cappuccino
            if 'logged_in' in session:
                remove_cappuccino()
            else:
                flash("Login First")
        if menu.add_cb() and request.form['btn'] == '+ Brew':  # cold brew
            if 'logged_in' in session:
                add_coldbrew()
            else:
                flash("Login First")
        if menu.remove_cb() and request.form['btn'] == '- Brew':  # cold brew
            if 'logged_in' in session:
                remove_coldbrew()
            else:
                flash("Login First")
        if menu.add_am() and request.form['btn'] == '+ Americano':  # americano
            if 'logged_in' in session:
                add_americano()
            else:
                flash("Login First")
        if menu.remove_am() and request.form['btn'] == '- Americano':  # americano
            if 'logged_in' in session:
                remove_americano()
            else:
                flash("Login First")
        if menu.add_ma() and request.form['btn'] == '+ Macchiato':  # macchiato
            if 'logged_in' in session:
                add_macchiato()
            else:
                flash("Login First")
        if menu.remove_ma() and request.form['btn'] == '- Macchiato':  # macchiato
            if 'logged_in' in session:
                remove_macchiato()
            else:
                flash("Login First")
        if menu.add_fw() and request.form['btn'] == '+ FlatWhite':  # flat white
            if 'logged_in' in session:
                add_flatwhite()
            else:
                flash("Login First")
        if menu.remove_fw() and request.form['btn'] == '- FlatWhite':  # flat white
            if 'logged_in' in session:
                remove_flatwhite()
            else:
                flash("Login First")
        if menu.add_af() and request.form['btn'] == '+ Affogato':  # affogato
            if 'logged_in' in session:
                add_affogato()
            else:
                flash("Login First")
        if menu.remove_af() and request.form['btn'] == '- Affogato':  # affogato
            if 'logged_in' in session:
                remove_affogato()
            else:
                flash("Login First")
        if menu.add_te() and request.form['btn'] == '+ Tea':  # tea
            if 'logged_in' in session:
                add_tea()
            else:
                flash("Login First")
        if menu.remove_te() and request.form['btn'] == '- Tea':  # tea
            if 'logged_in' in session:
                remove_tea()
            else:
                flash("Login First")
        if menu.add_cm() and request.form['btn'] == '+ Shake':  # coffee milk shake
            if 'logged_in' in session:
                add_coffeemilkshake()
            else:
                flash("Login First")
        if menu.remove_cm() and request.form['btn'] == '- Shake':  # coffee milk shake
            if 'logged_in' in session:
                remove_coffeemilkshake()
            else:
                flash("Login First")
        if menu.add_cr() and request.form['btn'] == '+ Breve':  # cafe breve
            if 'logged_in' in session:
                add_cafebreve()
            else:
                flash("Login First")
        if menu.remove_cr() and request.form['btn'] == '- Breve':  # cafe breve
            if 'logged_in' in session:
                remove_cafebreve()
            else:
                flash("Login First")
        if menu.remove_cr() and request.form['btn'] == '- Mocha':  # mocha
            if 'logged_in' in session:
                add_mocha()
            else:
                flash("Login First")
        if menu.remove_cr() and request.form['btn'] == '- Mocha':  # mocha
            if 'logged_in' in session:
                remove_mocha()
            else:
                flash("Login First")

        if buy.checkout() and request.form['btn'] == 'Proceed Cart':  # buy button
            if 'logged_in' in session:
                return redirect(url_for('cart'))
            else:
                flash("Login First")
        
        if buy.contents() and request.form['btn'] == 'Show Content':  # buy button
            if 'logged_in' in session:
                print(1111)
            else:
                flash("Login First")

        return turbo.stream([
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='money'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='water'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='milk'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='beans'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='cups'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='espresso'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='latte'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='cappuccino'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='coldbrew'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='americano'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='macchiato'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='flatwhite'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='affogato'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='tea'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='coffeemilkshake'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='cafebreve'),
            turbo.replace(render_template('menu.html', menu=menu, buy=buy), target='mocha')
        ])
    else:
        return render_template('menu.html', menu=menu, buy=buy)


@app.route("/about/", methods=['GET', 'POST'])
def about():
    if turbo.can_stream():
        print(1)
        return "1"
    return render_template('about.html')


@app.route("/success/", methods=['GET', 'POST'])
@login_required
def success():
    return render_template('success.html')


@app.route("/cart/", methods=['GET', 'POST'])
@login_required
def cart():
    machine = Machine()
    checkout = CheckOut()
    cart = users.find_one({'email': session['user']['email']})
    result = machine.contents()
    products = cart['cart']
    qty_list = products
    cost = 0
    number = 0

    for k, v in qty_list.items():
        if(k == 'espresso'):
            cost += 2.50*v
            number += v
        if(k == 'latte'):
            cost += 3.50*v
            number += v
        if(k == 'cappuccino'):
            cost += 4.00*v
            number += v
        if(k == 'coldbrew'):
            cost += 4.00*v
            number += v
        if(k == 'americano'):
            cost += 4.00*v
            number += v
        if(k == 'macchiato'):
            cost += 4.50*v
            number += v
        if(k == 'flatwhite'):
            cost += 4.75*v
            number += v
        if(k == 'affogato'):
            cost += 5.00*v
            number += v
        if(k == 'tea'):
            cost += 1.75*v
            number += v
        if(k == 'coffeemilkshake'):
            cost += 5.25*v
            number += v
        if(k == 'cafebreve'):
            cost += 3.00*v
            number += v
        if(k == 'mocha'):
            cost += 4.25*v
            number += v
    print(number, cost)
    print(result)

        
    if checkout.validate_on_submit():
        checkout_cart = {
                'espresso': 0,
                    'latte': 0,
                    'cappuccino': 0,
                    'coldbrew': 0,
                    'americano': 0,
                    'macchiato': 0,
                    'flatwhite': 0,
                    'affogato': 0,
                    'tea': 0,
                    'coffeemilkshake': 0,
                    'cafebreve': 0,
                    'mocha': 0
                }
        users.update_one(
            {'email': cart['email']},
            {'$set': {'cart': checkout_cart}}
        )
        flash('Checked Out successfully')
        return redirect(url_for('index'))
    return render_template('cart.html', products=products, checkout=checkout, result=result, qty_list=qty_list, cost=cost, number=number)



@app.route("/signout/", methods=['GET', 'POST'])
def signout():
    user = User()
    return user.signout()


@app.context_processor
def inject_load():
    if 'logged_in' in session:
        machine = Machine()
        cart = users.find_one({'email': session['user']['email']})
        result = machine.contents()
        money = result['money']
        water = result['water']
        milk = result['milk']
        beans = result['beans']
        cups = result['cups']
        espresso = cart['cart']['espresso']
        latte = cart['cart']['latte']
        cappuccino = cart['cart']['cappuccino']
        coldbrew = cart['cart']['coldbrew']
        americano = cart['cart']['americano']
        macchiato = cart['cart']['macchiato']
        flatwhite = cart['cart']['flatwhite']
        affogato = cart['cart']['affogato']
        tea = cart['cart']['tea']
        coffeemilkshake = cart['cart']['coffeemilkshake']
        cafebreve = cart['cart']['cafebreve']
        mocha = cart['cart']['mocha']

        return {'money': money, 'water': water, 'milk': milk, 'beans': beans, 'cups': cups, 'espresso': espresso, 'latte': latte, 'cappuccino': cappuccino, 'coldbrew': coldbrew, \
                'americano': americano, 'macchiato': macchiato, 'flatwhite': flatwhite, 'affogato': affogato, \
                'tea': tea, 'coffeemilkshake': coffeemilkshake, 'cafebreve': cafebreve, 'mocha': mocha}
    else:
        return {}


if __name__ == "__main__":
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug=True)

