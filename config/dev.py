APP_DEBUG = True


DATABASE_HOST = '127.0.0.1'
DATABASE_PORT = 3306
DATABASE_USER = 'root'
DATABASE_PASSWORD = '123456'
DATABASE_NAME = 'dev'


REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0
REDIS_URL = f'redis://{REDIS_HOST}:{REDIS_PORT}/{REDIS_DB}'


MONGO_HOST = '127.0.0.1'
MONGO_PORT = '27017'
MONGO_DB = 'dev'
MOTOR_URI = f'mongodb://{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB}'
