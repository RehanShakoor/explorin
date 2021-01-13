from django.db import models

from django.contrib.auth.models import User


class EditProfile(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.name) 

class Post(models.Model):
    photo = models.ImageField(null=True,blank=True,upload_to="myimage")
    title = models.CharField(max_length=255)
    liked=models.ManyToManyField(User,default=None,blank=True,related_name='liked')   
    body = models.TextField()

    def __str__(self):
        return str(self.title)  

    @property
    def num_likes(self):
        return self.liked.all().count()
 
LIKE_CHOICES=(
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)   
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    value = models.CharField(choices = LIKE_CHOICES,default='Like',max_length=10)     

    def __str__(self):
        return str(self.post)


