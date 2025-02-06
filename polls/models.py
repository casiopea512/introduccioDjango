from django.db import models

# para el was_published_recently
import datetime
from django.utils import timezone

# para el decorator
from django.contrib import admin

# Esta clase te creará tanto las tablas de la bd como acceder a ellas

class Question(models.Model):
    question_text = models.CharField(max_length=200) # dices el varchar, los nombres de la columna es el nombre de la variable
    pub_date = models.DateTimeField("date published")

    # esto es para que se printee de manera bonita el objeto en el front
    def __str__(self):
        return self.question_text

    # es un decorator, que dice que es un boolean. Es una función que hace de wraper, y modificas el comportamiento de la otra función a través de ésta. El @admin es una librería
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )

    # añadimos un método, es decir una función, que se verá reflejada en el front
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
    
class Votes(models.Model):
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)
    vote_date = models.DateTimeField("date voted")