import os


class Config:
    SECRET_KEY = '365eec3a8b482c9ac0051bd02581aa27'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'densis.dtech@gmail.com'
    MAIL_PASSWORD = 'simsidben1'