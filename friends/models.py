from django.db import models
from users.models import Profile
from django.contrib.auth.models import User


# Create your models here.

class Friend(models.Model):
    user1 = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
    user2 = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user1)+" "+str(self.user2)


class Request(models.Model):
    requested_by = models.ForeignKey(User, related_name='%(class)s_requests_created', on_delete=models.CASCADE)
    requested_to = models.ForeignKey(User,  on_delete=models.CASCADE)

    def __str__(self):
        return str(self.requested_by)+" Requested: "+str(self.requested_to)