from django.db import models
from django.contrib.auth.models import User

class Character(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    system = models.CharField(max_length=100)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    last_update = models.DateTimeField(auto_now=True)
    # Other data
    # ...

    def __str__(self):
        #result_str = f'author: {self.author}\n character: {self.name}\n system: {self.system}\n ' \
        #             f'description: {self.description}\n' f'created: {self.date_created}\n last updated: {self.last_update}'
        return f'{self.name} | {self.author}'