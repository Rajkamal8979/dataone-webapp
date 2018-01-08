from django.db import models
#from django.contrib.admin import widgets

class leadactors(models.Model):
    name=models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.name

class director(models.Model):
    name=models.CharField(max_length=100)
    #movie =models.ForeignKey(to='movie',related_name="in_movie",blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return self.name




class movie(models.Model):
    name = models.CharField(max_length=100)
    actors = models.ManyToManyField(leadactors)
    release_date=models.DateField()
    genre=models.CharField(max_length=100)
    director=models.ForeignKey(director,blank=False,on_delete=models.CASCADE)

    def __str__(self):
        return '%s %s %s %s'%(self.name,self.release_date,self.genre,self.director)





# Create your models here.
