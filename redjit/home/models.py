from django.db import models

class Post(models.Model):
  username = models.CharField(max_length=255)
  title = models.CharField(max_length=255)
  slug = models.SlugField()
  content = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-date_added']

class Comment(models.Model):
  post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
  username = models.CharField(max_length=255)
  body = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['date_added']