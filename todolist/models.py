#contains fields and behaviours of the data store in app
#Each object is a row in table
#model is a single source of info about my data
#each model maps to a single database table
#model is a class that subclasses django.db.models.Model
#each attribute of the model represents a database field.
from django.db import models

# Create your models here.
class Todolist(models.Model):
    text = models.CharField(max_length=45)
    completed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.text
    
