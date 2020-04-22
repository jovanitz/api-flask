class Config:
  pass

class DevelopmentConfig(Config):
  DEBUG = True
  SQLALCHEMY_DATABASE_URI = 'dewfew'
  SQLALCHEMY_TRACK_MODIFICATIONS = False

config = {
  'development': DevelopmentConfig
}