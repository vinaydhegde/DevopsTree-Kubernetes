import os

POSTGRES_USER = os.environ.get('POSTGRES_USER')
print(POSTGRES_USER)
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
DATABASE_URL = f'postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@devopstree-postgres:5432/devopstree'


class BaseConfig:
    """Base configuration"""
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """Development configuration"""
    SQLALCHEMY_DATABASE_URI = DATABASE_URL


class ProductionConfig(BaseConfig):
    """Production configuration"""
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
