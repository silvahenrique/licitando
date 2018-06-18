import os
from dotenv import load_dotenv
load_dotenv()

ENV = os.environ.get('ENV', 'dev')

SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY', '')

EMAIL_HOST = os.environ.get('EMAIL_HOST', '')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD', '')
EMAIL_PORT = os.environ.get('EMAIL_PORT', '')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS', '')


print('RUNNING THIS APP IN ENVIRONMENT: {}'.format(ENV))
