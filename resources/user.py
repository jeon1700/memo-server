from email_validator import EmailNotValidError, ValidatedEmail
from flask import request
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from mysql.connector import Error
from mysql_connection import get_connection

from utils import hash_password


class UserRegisterResource(Resource) :

    def post(self):

        data = request.get_json()

        try :
            ValidatedEmail( data['email'])
        except EmailNotValidError as e:
            print(e)
            return {'error' : str(e)}, 400
        
        if len(data['password']) < 4 or len(data['password']) > 300 :
            return {'error' : '비번길이를 확인하세요.'} , 400

        # 비번 암호화
        password = hash_password (data['password'])

        # DB에 회원정보를 저장한다.
        try :
            connection = get_connection()
            query = '''insert into user
                        (email, password, nickname)
                        values
                        (%s,%s,%s);'''
            record = (data['email'] , 
                      password,
                      data['nickname'])
            
            cursor = connection.cursor()
            cursor.execute(query,record)
            connection.commit()

            user_id = cursor.lastrowid

            cursor.close()
            connection.close()

        except Error as e :
            print(e)
            cursor.close()
            connection.close()
            return{'error' : str(e)}, 500
        
        access_token = create_access_token(user_id)

        return {'result' : 'success',
                'access_token' : 'access_token'} , 200



       