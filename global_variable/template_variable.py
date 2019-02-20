from article.models import Article_type

def show_article_type(request):
	content ={}
	article_type = Article_type.objects.all()
	content['article_type'] = article_type
	return content