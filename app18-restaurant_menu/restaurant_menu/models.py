from django.db import models
from django.contrib.auth.models import User


MEAL_TYPE = (
    ('starters', 'Starters'),
    ('salads', 'Salads'),
    ('main_dishes', 'Main Dishes'),
    ('dessert', 'Dessert'),
)


STATUS = (
    (0, 'Unavailable'),
    (1, 'Available'),
)


class Item(models.Model):
    objects = None
    meal = models.CharField(max_length=400, unique=True)
    description = models.TextField(max_length=400)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    meal_type = models.CharField(choices=MEAL_TYPE, max_length=20)
    author = models.ForeignKey(User, on_delete=models.PROTECT) # PROTECT & CASCADE & SET_NULL
    status = models.IntegerField(choices=STATUS, default=0)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.meal
