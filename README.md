        https://blog.logrocket.com/creating-an-app-with-react-and-django/

Step 0: Initial setup with virtual environment activation

        virtualenv venv
        source venv/bin/activate
        pip3 install django djangorestframework django-cors-headers
        node --version
        npm --version
        
Step 1: Create django project

        django-admin startproject react_django_project
        Django project is setup as below:
            main-project-dir
                main-project-dir  - containing setups like asgi, wsgi, urls, settings
                Mutiple app directories - each created when we run "django-admin startapp app1". Each dir contain models, app, views, admin
        
        cd react_django_project
        mv venv react_django_project/
        pip3 freeze > requirements.txt
        Modify react_django_project/settings.py:
            Add to INSTALLED_APPS: 'rest_framework', 'corsheaders', 'studentsapp'
            Add to MIDDLEWARE: 'corsheaders.middleware.CorsMiddleware', 'django.middleware.common.CommonMiddleware', 
            Add CORS_ORIGIN_ALLOW_ALL = True
            Set 'default' key in DATABASES dictionary to sqllite:
                DATABASES = {
                        'default': {
                            'ENGINE': 'django.db.backends.sqlite3',
                            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                            }
                        }
            
Step 2: Create APP & DB object using models

        django-admin startapp studentsapp
        Edit models.py
        python manage.py makemigrations    
        python manage.py migrate 
        
Step 3: Create data migration file (for direct manipulation of data into the database.)

        python manage.py makemigrations  --empty --name studentsapp studentsapp
        edit 0002_studentsapp.py to give some initial data
        python manage.py migrate 

Step 4: Write endpoints inside urls.py and views.py
        
        Edit urls.py to list urlpatterns
        For the specified urlpatterns, edit views to add new methods
        python manage.py runserver
        experiment with API calls on http://localhost:8000/api/students/
        
Housekeeping:

        port 3000 --> frontend and port 8000 --> django backend
        To kill any process running on port 8000:
            lsof -P  | grep :3000 | awk '{print $2}' | xargs kill -9     
            lsof -P  | grep :8000 | awk '{print $2}' | xargs kill -9    
            
Step5: Start writing front end - create a react app named reactapp to interact with django API  

        npx create-react-app reactapp
            or npm init react-app reactapp
            or yarn create react-app reactapp
        cd reactapp
        npm install bootstrap reactstrap axios --save    # make use of Bootstrap for the styling
        
        npm start   # starts at http://localhost:3000/
        
        # Axios is the promise-based HTTP client that we’ll use to make HTTP request calls to our Django API.
        edit src/index.js to include import ‘bootstrap/dist/css/bootstrap.min.css’;
        create dir constants and a file index.js to keep a API_URL
        
Step 6: Create react components - Divide frontend into atomic components     

        Under src directory
            App.js --> acts as the main html containing react components grouped as we want. Hence here import react components form component directory.
            index.js --> performs rendering to root element

        1) Header  - logo, some text as heading
        2) Home -  main container consisting of students list as table, add/update button

Step 7: Install and play with storybook

        npx sb init
        npm run storybook 

        Resulted in main app not to work when StoryBook was installed...To fix:
        rm -rf node_modules
        rm package-lock.json
        rm src/stories
        rm -rf .stories
        remove "babel-loader": "^8.1.0", from package.json
        npm install  (outside VPN)