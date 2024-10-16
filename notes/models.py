from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True) #TODO: Find out the difference between auto_now and auto_now_add
    # Now we will create the foreign key to connect users to the notes they create. 
    # on_delete CASCASE means that when a user is deleted the notes will be deleted as well.
    # related_name is how we will identify this relationship on the user side
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes")