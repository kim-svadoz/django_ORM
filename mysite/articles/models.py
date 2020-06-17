from django.db import models

# Create your models here.
class Article(models.Model) : 
    # articles_article
    # CharField 는 글자 수 제한 할 때 사용
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)