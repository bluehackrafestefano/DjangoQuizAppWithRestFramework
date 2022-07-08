How to use docker image:
1. Pull the image;
```cmd
docker pull stefanorafe/djangoquizappwithrestframework:v0.2
```
2. Run the image;
```cmd
docker run --name my-django-app -w /flight -p 8000:8000 -d stefanorafe/djangoquizappwithrestframework:v0.2 sh -c "python manage.py runserver 0.0.0.0:8000"
```
3. Check the app on localhost:8000