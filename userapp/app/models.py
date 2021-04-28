from django.db import models

# Create your models here.

class CoreUsers(models.Model):
    first_name = models.CharField(max_length = 10)
    last_name = models.CharField(max_length =10)
    user_id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.first_name

class UserLogs(models.Model):
    user_id_log = models.ForeignKey(CoreUsers, on_delete=models.CASCADE,)
    actions = models.CharField(max_length=50)
    service = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_id_log +" "+ self.actions +" "+ self.service