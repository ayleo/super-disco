from django.db import models


class Form(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    date = models.DateField()
    occupation = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
"""
The models.py functions as a bluebrint for the database creation. 
Running the command python manage.py makemigrations will create a migration file 
that will be used to create the database schema under "job_application/migrations/0001_initial.py".
Than running the command python manage.py migrate will create the database.
DB refreshes can be done by reopening the same db file.
"""