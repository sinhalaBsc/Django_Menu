from django.db import models
class mymenu(models.Model):    

    # column name = properties
    url=models.CharField(max_length=40)
    body=models.TextField()
    date=models.DateTimeField()

    
    def __str__(self):       
        return self.url   
