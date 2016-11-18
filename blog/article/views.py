from django.shortcuts import render

from article.models import Article, Comment

# Create your views here.
def article(request):
    '''
    Render the article page
    '''
    articles = Article.objects.all()
    itemArray = []
    for article in articles:
        items = [article]
        items.extend(list(Comment.objects.filter(article=article)))
        itemArray.append(items)
    context = {'itemArray':itemArray}
    return render(request, 'article/article.html', context)