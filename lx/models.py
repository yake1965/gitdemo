from django.db import models

class Reporter(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):           
        return "%s %s" % (self.first_name, self.last_name)

class Article(models.Model) :
    headline = models.CharField(max_length=100)
    content = models.TextField(blank = True, null = True)  #博客文章正文    
    reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)
    pub_date = models.DateField()
    date = models.DateField()

    def __str__(self):             
        return self.headline

    class Meta:
        ordering = ('headline',)
