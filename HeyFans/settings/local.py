
# 本機（開發機）用的設定。
from .base import *

SECRET_KEY = 'la1fk1p9ksy!e#i(k2@(nz#q8w&yuh2-0(gpww@g0@#ekb_p=9'
DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'heyfans',  # 建立的資料庫
        'USER': 'root',  # mysql使用者名稱
        'PASSWORD': 'joanna10544218',  # mysql密碼
        'HOST': '127.0.0.1',  # IP
        'PORT': '3306',  # 埠號
    }
}
