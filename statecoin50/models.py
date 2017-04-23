from django.db import models
from django.utils import timezone
# Create your models here.
class Coin(models.Model):
    #owner = models.ForeignKey('auth.User')
    state = models.CharField(max_length = 250)
    stAbbr= models.CharField(max_length = 2)
    owned= models.BooleanField(default=False)
    dateOwned= models.DateField(blank= True, null=True)
    stURL=models.URLField(max_length= 250)
    dates = models.CharField(blank = True, max_length = 250)
    details = models.CharField(blank= True, max_length = 500)


    def obtained(self):
        self.owned = True
        self.dateOwned=(timezone.now())
        self.save()


    def __str__(self):
        return self.state
