from flask import  session, jsonify, request, Flask, make_response
import psycopg2
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import jwt
from functools import wraps
from datetime import datetime, timedelta
# instantiate the app
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.config['SECRET_KEY'] = 'your secret key'
CORS(app)

def get_db_connection():
    return psycopg2.connect(database="kisprod", user="postgres", password="", host="localhost", port="5432")


@app.route('/refreshToken', methods=['POST'])
def refresh_token():
    # Получение рефреш токена из запроса
    refresh_token = None
    if 'x-refresh-token' in request.headers:
        refresh_token = request.headers['x-refresh-token']
    if not refresh_token:
        return jsonify({'message': 'Refresh token is missing!'}), 401

    try:
        # Проверка рефреш токена
        data = jwt.decode(refresh_token, app.config['SECRET_KEY'])
        # Создание нового токена доступа
        new_token = jwt.encode({
            'public_id': data['public_id'],
            'exp': datetime.utcnow() + timedelta(minutes=30)
        }, app.config['SECRET_KEY'])

        return jsonify({'token' : new_token.decode('utf-8')}), 201
    except:
        return jsonify({'message': 'Refresh token is invalid!'}), 401

# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        # jwt is passed in the request header
        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        # return 401 if token is not passed
        if not token:
            return jsonify({'message' : 'Token is missing !!'}), 401
  
        try:
            # decoding the payload to fetch the stored details
            data = jwt.decode(token, app.config['SECRET_KEY'])
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("select user_name from adminbd where id_userbd= %s", (data['public_id'],))
                current_user = cursor.fetchone()
        except:
            return jsonify({
                'message' : 'Token is invalid !!'
            }), 401
        # returns the current logged in users context to the routes
        return  f(current_user[0], *args, **kwargs)
  
    return decorated


@app.route('/user', methods =['GET'])
@token_required
def get_all_users(current_user):
    # querying the database
    # for all the entries in it
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("select * from adminbd where user_name = %s", (current_user,))
        users = cursor.fetchall()
    # converting the query objects
    # to list of jsons
        output = []
        for user in users:
            # appending the user data json 
            # to the response list
            output.append({
                'id_userbd': user[0],
                'login' : user[1],
                'name': user[3],
            })
    
        return jsonify({'users': output})

@app.route('/login', methods=['POST'])
def login_post():
    if request.method == 'POST':
        post_data = request.get_json()
        username = post_data.get('login')
        password = post_data.get('password')
        if not username:
        # returns 401 if user does not exist
            return make_response(
                'Could not verify',
                401,
                {'WWW-Authenticate' : 'Basic realm ="User does not exist !!"'}
            )
        #Получение информации о пользователе по логину
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("select password from adminbd where user_name= %s", (username,))
            user_data = cursor.fetchone()
            cursor.execute("select id_userbd from adminbd where user_name= %s", (username,))
            user_id = cursor.fetchone()
            if user_data:
                hashed_password = user_data[0]
                if bcrypt.check_password_hash(hashed_password, password):
                    token = jwt.encode({
                        'public_id': user_id[0],
                        'exp' : datetime.utcnow() + timedelta(minutes = 30)
                    }, app.config['SECRET_KEY'])
                    refresh_token = jwt.encode({
                        'public_id': user_id[0],
                        'exp': datetime.utcnow() + timedelta(days=30)  # длинный срок действия
                    }, app.config['SECRET_KEY'])
                    return make_response(jsonify({'token' : token.decode('utf-8'), 'refresh_token': refresh_token.decode('utf-8')}), 201)
                else:
                    return make_response(
                        'Could not verify',
                        403,
                        {'WWW-Authenticate' : 'Basic realm ="Wrong Password !!"'}
                    )
                
@app.route('/registration', methods=['POST'])
def registration():
    if request.method == 'POST':
        post_data = request.get_json()
        userlogin = post_data.get('login')
        username = post_data.get('name')
        password = post_data.get('password1')
        password2 = post_data.get('password2')
        if password == password2:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            
            #Проверка наличия пользователя
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM adminbd WHERE user_name = %s", (userlogin,))
                existing_user = cursor.fetchone()

                #Обработка ошибки о наличии пользователя
                if existing_user:
                    return make_response(
                        'Could not registration',
                        403,
                        {'WWW-Authenticate' : 'User !!!!"'}
                    )
            
            #Создание нового пользователя
            with get_db_connection() as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO adminbd (user_name, password, name) VALUES (%s, %s, %s)", (userlogin, hashed_password, username))
                conn.commit()
                return make_response(jsonify({'status': 'successful'}), 201)
        else:
            return make_response(
                        'Could not registration',
                        403,
                        {'WWW-Authenticate' : 'Password !!!!"'}
                    )

@app.route('/getuserscommission', methods=['GET'])
def get_users_commission():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users_commission')
        users = cursor.fetchall()
        user_list = []
        for user in users:
            user_dict = {
                'id': user[0],
                'user_name': user[1],
                'post': user[2],
                'data_start': user[3],
                'data_end': user[4]
            }
            user_list.append(user_dict)
        return make_response(jsonify({'users_commission': user_list}))
            
app.run(host='0.0.0.0', port=83)