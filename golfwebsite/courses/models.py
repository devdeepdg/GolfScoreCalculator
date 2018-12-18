from django.db import models
from django.core import validators
from django.contrib.postgres.fields import ArrayField
#from django_mysql.models import ListCharField
import json


courseInfo = {'name': "Tollygunge Club",
              'location': ['kolkata', 'india'],
              'par': [4, 3, 4, 4, 4, 3, 5, 3, 4, 5, 3, 4, 5, 4, 4, 4, 4, 3],
              'strokeIndex': [7, 17, 3, 11, 1, 13, 9, 15, 5, 14, 16, 10, 4, 12, 6, 2, 8, 18]}

player1 = {'name': "DDG",
           'handicap': 10,
           'score': [4, 3, 4, 4, 4, 3, 5, 3, 4, 5, 3, 4, 5, 4, 4, 4, 4, 3]}


class Course(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    country = models.CharField(max_length=200)
    # par = models.CharField(max_length=200, validators=[validators.validate_comma_separated_integer_list])
    # strokeIndex = models.CharField(max_length=200, validators=[validators.validate_comma_separated_integer_list])
    strokeIndex = ArrayField(models.IntegerField(default=0), default=list)
    par = ArrayField(models.IntegerField(default=0), default=list)
    # par = models.CommaSeparatedIntegerField(max_length=200)
    # par = models.TextField(null=True)
    # strokeIndex = models.TextField(null=True)

    def set_par(self, x):
        self.par = json.dumps(x)

    def get_par(self):
        return json.loads(self.par)

    def set_strokeIndex(self, x):
        self.strokeIndex = json.dumps(x)

    def get_strokeIndex(self):
        return json.loads(self.strokeIndex)

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
        #return reverse('course-home', kwargs={'pk': self.pk})

