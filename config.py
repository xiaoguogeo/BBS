# 配置数据库信息
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'personalblog'
USERNAME = 'root'
PASSWORD = 'xgg925'
DB_URI = f'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8'
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = True

# 配置邮箱信息
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = 'xiaoguogeo@qq.com'
MAIL_PASSWORD = 'vrnkwsqidsygdeeg'
MAIL_DEFAULT_SENDER = 'xiaoguogeo@qq.com'


SECRET_KEY = "xgg"
