from django.db import models





class ESIM(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.IntegerField()
    days = models.IntegerField()
    region = models.CharField(max_length=255)
    expiration = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name



class Order(models.Model):
    esim = models.ForeignKey(ESIM, on_delete=models.CASCADE)
    user_id = models.IntegerField()

    def __str__(self):
        return self.esim.name



