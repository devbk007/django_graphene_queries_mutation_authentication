GraphQL APIs for adding, deleting and updating movie and director details. Every API is authenticated using JWT.

# Operations handled by APIs
1. Add, Update, Delete and Read details of a single director.
2. Add, Update, Delete and Read details of a single movie.
3. Read details of all movies.
4. Read details of all directors.
5. Read details of all movies and directors.
6. User login.
7. JWT token verification.
8. JWT token refresh

# Steps to install application
1. Install packages    
    ```
    pipenv install
    ```

2. Activate virtual environment
    ```
    pipenv shell
    ```

3. Perform migrations.
    ```
    python manage.py makemigrations
    ```
    ```
    python manage.py migrate --run-syncdb
    ```

4. Create a superuser
     ```
    python manage.py createsuperuser
    ```
  
5. Run the command 
    ```
    python manage.py runserver
    ```
# API's to test
Download [django-graphene.postman_collection](https://github.com/devbk007/django_graphene_queries_mutation_authentication/blob/master/django-graphene.postman_collection.json) and import the file in Postman as a collection to test the APIs.

# Demo Video
[![Video Thumbnail](https://github.com/devbk007/django_graphene_queries_mutation_authentication/blob/master/youtube_thumbnail.png)](https://youtu.be/_434Dub-kC8)