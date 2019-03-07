from django.shortcuts import render
from article.models import Article,Article_type
from theme.models import Theme

# Create your views here.
def index(request):
	return_content = {}
	articles = Article.objects.all().order_by('-release_time')[0:5]
	theme = Theme.objects.all()
	return_content['articles'] = articles
	return_content['theme'] = theme
	return render(request,'index/index.html',return_content)

def all_article(request):
	return_content = {}
	articles = Article.objects.all().order_by('-release_time')
	return_content['articles'] = articles
	return render(request,'article/all_article.html',return_content)

def article(request,id):
	return_content = {}
	article = Article.objects.get(id=id)
	statistical_visits(article)
	return_content['article'] = article
	return render(request,'article/article.html',return_content)

def about(request):
	return render(request,'about/about.html',{})

def statistical_visits(article):
	article.visits += 1
	article.save()