from django.db import models

# Create your models here.
class Article(models.Model) : 
    # articles_article
    # CharField 는 글자 수 제한 할 때 사용
    objects = models.Manager()
    title = models.CharField(max_length=150)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.id}번째 글 - {self.title} : {self.content}'