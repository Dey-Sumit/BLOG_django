from django.db import models
from django.util import timezone
from django.core.urlresolvers import reverse
# Create your models here.

class Post(model.Model):
    author=models.ForeignKey('auth.User')
    title=models.CharField(max_length=100)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now())
    published_date=model.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date=timezone.now()
        self.save()

    def approve_comments(self):
        return self.comments.filter(apporoved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

class Comment(models.Model):
        post=models.ForeignKey('blog.Post',related_name='comments')
        author=models.CharField(max_length=100)
        text=models.TextField()
        create_date=models.DateTimeField(default=timezone.now())
        approved_comment=models.BooleanField(default=False)

         def approve(self):
            self.approved_comment=True;
            self.save()

        def get_absolute_url(self):
            return reverse('post_list')

        def __str__(self):
            return self.post
