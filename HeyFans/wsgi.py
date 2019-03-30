"""
WSGI config for HeyFans project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

# 當應用程式啟動後，讀取我們設定此專案的環境變數，HeyFans資料夾底下的settings.py檔案
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'HeyFans.settings')

application = get_wsgi_application()
