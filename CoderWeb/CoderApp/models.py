from django.db import models

class Terror(models.Model):
    titulo = models.CharField(max_length=40)
    año = models.IntegerField()
    director = models.CharField(max_length=40)
    
    
class Comedia(models.Model):
    titulo = models.CharField(max_length=40)
    año = models.IntegerField()
    director = models.CharField(max_length=40)

class Cienciaficcion(models.Model):
    titulo = models.CharField(max_length=40)
    año = models.IntegerField()
    director = models.CharField(max_length=40)
    

    



    

    