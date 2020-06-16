from django.shortcuts import render, redirect
import requests
# 모델 가져오기
from articles.models import Article

# Create your views here.
def index(request):
    # 전체 데이터 가져오기
    # 그 데이터 템플릿에게 넘겨주기
    # 템플릿에서 반복문으로 각각의 게시글 pk, title 보여주기
    article = Article.objects.all()
    context = {
        'articles' : article
    }
    return render(request, 'articles/index.html', context)

def new(request):
    return render(request, 'articles/new.html')

def create(request):
    title = request.POST.get('title')
    text = request.POST.get('text')
    Article.objects.create(title=title, content=text)
    
    return redirect('articles:index')

def introduce(request):
    return render(request, 'articles/introduce.html')


# 1. 상세 페이지를 보기위한 경로
# 1-1. 특정 게시글에 대한 고유 값
# 1-2. /articles/1/, /articles/2/...
# 2. 해당 게시글에 대한 상세 내용
# 2-1. 게스글의 pk, title, ...
# 3. 인덱스 페이지로 돌아가는 링크
def detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/detail.html', context)

# 1. 특정 글 삭제를 위한 경로 작성
# 1.1 /articles/delete/
# 2. 글 삭제 처리를 해주는 view 작성
# 3. 글 삭제 후, index page로 redirect
# 4. 글 삭제를 위한 링크 detail에 작성
def delete(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    article.delete()
    return redirect('articles:index')

# 1. 특정 글 수정을 위한 경로 생성
# 1-1. /articles/1/edit
# 2. 글 수정 template를 render하는 edit view 작성
# 2-1. 해당 template에 form tag 생성
# 2-2. 각 input tag 내부에 기존 내용이 들어있어야 함.
# 3. edit 보낸 데이터 처리를 위한 경로 생성
# 3-1. /articles/1/update
# 4. 글 수정 처리를 하는 update view 작성
# 5. 해당 글 상세 페이지로 redirect
# 6. 글 수정을 위한 edit 링크 해당 글 상세 페이지에 생성
# 6-1. {% url 'articles:edit' articles.pk %}

def edit(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    context = {
        'article' : article
    }
    return render(request, 'articles/edit.html', context)

def update(request, article_pk):
    edit_title = request.POST.get('edit_title')
    edit_content = request.POST.get('edit_content')
    article = Article.objects.get(pk=article_pk)
    article.title = edit_title
    article.content = edit_content
    article.save()
    return redirect('articles:detail', article_pk)