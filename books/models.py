from django.db import models

# Create your models here.
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    stat_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()
    
    def __unicode__(self):
        return unicode(self.name)
    
    class Meta:
        ordering=["name"]


class Auther(models.Model):
    first_name = models.CharField(max_length=30,verbose_name="first_name_")
    last_name = models.CharField(max_length=40,verbose_name="last_name_")
    #set filed can be empty
    email = models.EmailField(blank=True,verbose_name="e-mail")
    
    def __unicode__(self):
        return u'%s %s %s' % (self.id,self.first_name, self.last_name)

    
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Auther)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField(blank=True,null=True)
    
    def __unicode__(self):
        return self.title
