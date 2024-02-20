# Axera Blogs API

This repo holds the backend source code for an application which aggregates news as well as provides a platform to publish own articles

Django was used to build the backend hence the following steps needs to be followed in order to setup the project

## Setup
1. Clone the repo
2. Move inside the project folder
3. Install dependencies `pip install -r requirements.txt`
4. Run the following commands
   1. `python manage.py makemigrations`
   2. `python manage.py migrate`
   3. `python manage.py createsuperuser` and follow the prompts
   4. `python manage.py runserver` to start the server
   5. Visit  [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin) and login. Create some blog posts, add some topics and RSS feed links of your favorite websites to include it in the explore page of the platform
5. You're done!

## This is how the admin panel looks like
![admin panel](/readme_media/admin.png)