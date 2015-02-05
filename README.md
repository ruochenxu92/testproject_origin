# testproject
This is CS410 Course Project.
All rights reserved

    Steps 
1.  Course Propursal
2.  front end bootstrap http://wsnippets.com/responsive-airbnb-style-search-box-twitter-bootstrap/
3.   https://www.airbnb.com/s/shanghai-china?price_min=730&price_max=855&sw_lat=30.71744654271819&sw_lng=121.14263084830714&ne_lat=31.31213325210683&ne_lng=121.79082420768214&zoom=10&search_by_map=true&ss_id=r218idx1
4. 


git clone https://github.com/xxu46/testproject OR if you use pycharm clone. 

0. Watch tutorial 1 and download Django 
https://www.youtube.com/watch?v=3DccH9AMwFQ

1. Download Pycharm 3.4
PyCharm-professional-3.4.1.dmg

2. Open Pycharm and typing create a project
Open the VCS and check out from github project

3. Check your Pycharm Project Interpreter is 2.7.5 python
    Django version is 1.7

4. Commit your changes also use VCS   (command + k)


5. Everyone would better his own branches and to do his own functions. 
End==============================

Useful notes

steps

6. git commands
7. git add *
8. git clone https://github.com/xxu46/testproject
9. git commit -m "message"
10. git remote add pb https://github.com/xxu46/testproject
11. git push -f pb master



Search Engine (build Index(haystack(2.4.0.dev) and Index search(Whoosh(2.5.7))
url = http://django-haystack.readthedocs.org/en/latest/tutorial.html
1. pip install -e git+https://github.com/toastdriven/django-haystack.git@master#egg=django-haystack    (2.4.0 dev)
2.
    setting.py
    import os
    HAYSTACK_CONNECTIONS = {
        'default': {
            'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
            'PATH': os.path.join(os.path.dirname(__file__), 'whoosh_index'),
        },
    }
 
3. templates/indexes/task/note_text.txt
    {{ object.title }}
    {{ object.user.get_full_name }}
    {{ object.body }}
4. urls
    (r'^search/', include('haystack.urls')),

5.  ./manage.py rebuild_index
6.  Add Haystack To INSTALLED_APPS
As with most Django applications, you should add Haystack to the INSTALLED_APPS within your settings file (usually settings.py).

Example:

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',

    # Added.
    'haystack',

    # Then your usual apps...
    'blog',
]


========================================


rm -rf foldername
