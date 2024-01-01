from django.db import models


class User(models.Model):
    name = models.CharField(max_length=255)
    server = models.CharField(max_length=255)
    player_id = models.IntegerField()
    nickname = models.CharField(max_length=255)

class Order(models.Model):
    total_diamond = models.IntegerField()
    price = models.IntegerField()
    payment_method = models.CharField(max_length=255, default="DANA")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class Games(models.Model):
    name = models.CharField(max_length=255, default="Untitled")
    image = models.FileField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name