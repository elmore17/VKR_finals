from flask import  session, jsonify, request, Flask, make_response
import psycopg2
from flask_bcrypt import Bcrypt
from flask_cors import CORS
import jwt
from functools import wraps
from datetime import datetime, timedelta
from pathlib import Path
from docxcreate import read_docx
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
    
@app.route('/uploadfile', methods=['POST'])
def upload_file():
    try:
        #Загрузка файла и сохранение в директорию Downloads
        uploaded_file = request.files['file']
        downloads_directory = Path.home() / 'Downloads'
        file_path = downloads_directory / uploaded_file.filename
        uploaded_file.save(file_path)
        # output_json = 'output.json'
        data_text = read_docx(file_path)
        # create_json(data_text, output_json)

        #Добавление информиции из docx в базу данных
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT id_filepath FROM filepath WHERE filename = %s", (uploaded_file.filename,))
            existing_filepath = cursor.fetchone()
            if existing_filepath is None:
                cursor.execute("INSERT INTO filepath (filename) VALUES (%s)", (uploaded_file.filename,))
                conn.commit()
            for item in data_text:
                # Проверка наличия направления в таблице direction
                cursor.execute("SELECT id FROM direction WHERE name_direction = %s", (item[2],))
                existing_direction = cursor.fetchone()
                if existing_direction is None:
                    cursor.execute("INSERT INTO direction (name_direction) VALUES (%s)", (item[2],))
                    conn.commit()

                #Проверка наличия научного руководителя в БД
                cursor.execute("SELECT id FROM scientific_adviser WHERE name_adviser = %s AND role = %s", (item[37], item[41]))
                existing_scientific_adviser = cursor.fetchone()
                if existing_scientific_adviser is None:
                    cursor.execute("INSERT INTO scientific_adviser (name_adviser, role) VALUES (%s, %s)", (item[37], item[41]))
                    conn.commit()

                #Проверка наличия студента в БД
                cursor.execute("SELECT id FROM students WHERE name = %s AND title_gradual_work = %s", (item[26], item[29]))
                existing_student = cursor.fetchone()
                if existing_student is None:
                    cursor.execute("INSERT INTO students (name, title_gradual_work, id_scientific_adviser) VALUES (%s, %s, %s)", (item[26], item[29], existing_scientific_adviser))
                    conn.commit()
                
                #Проверка наличия квалификации в БД
                cursor.execute("SELECT id FROM level_education WHERE name_level_education = %s", (item[121], ))
                existing_level_education = cursor.fetchone()
                if existing_level_education is None:
                    cursor.execute("INSERT INTO level_education (name_level_education) VALUES (%s)", (item[121],))
                    conn.commit()

                #Проверка наличия специальностей в БД
                cursor.execute("SELECT id FROM speciality WHERE name_speciality = %s", (item[126],))
                existing_speciality = cursor.fetchone()
                if existing_speciality is None:
                    cursor.execute("INSERT INTO speciality (name_speciality) VALUES (%s)", (item[126], ))
                    conn.commit()

                #Таблица для шаблонизации
                cursor.execute("SELECT id FROM graduate_work WHERE id_student = %s", (existing_student,))
                existing_graduate_work = cursor.fetchone()
                if existing_graduate_work is None:
                    cursor.execute("INSERT INTO graduate_work (id_student, id_direction, id_scientific_adviser, id_level_education, id_speciality, id_filepath) VALUES (%s, %s, %s, %s, %s, %s)", (existing_student, existing_direction, existing_scientific_adviser, existing_level_education, existing_speciality, existing_filepath))
                    conn.commit()
        return make_response(jsonify({'status': 'success', 'message': 'File uploaded successfully', 'filePath': str(file_path)}))
    except Exception as e:
        return make_response(
                        'Could not file',
                        502,
                        {'WWW-Authenticate' : 'File !!!!"'}
                    )
            
app.run(host='0.0.0.0', port=83)