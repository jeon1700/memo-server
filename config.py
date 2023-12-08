



class Config :
    HOST = 'yhdb.cdy5sr538fxl.ap-northeast-2.rds.amazonaws.com'
    DATABASE = 'memo'
    DB_USER = 'memo_user'
    DB_PASSWORD = '1212'



    PASSWORD_SALT = 'yh1206hello'


    ### JWT 관련 변수 셋팅  => 셋팅 후 
    ### app.py 파일에서, 설정해줘야한다.
    JWT_SECRET_KEY = 'yh1206hello##bye~~'
    JWT_ACCESS_TOKEN_EXPIRES = False
    PROPAGATE_EXCEPTIONS = True