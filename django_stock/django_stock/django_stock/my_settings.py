DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', #1
        'NAME': 'stock_db', #2
        'USER': 'root', #3                      
        'PASSWORD': '2000',  #4              
        'HOST': '127.0.0.1',   #5                
        'PORT': '3306', #6
    }
}

SECRET_KEY = '2000'