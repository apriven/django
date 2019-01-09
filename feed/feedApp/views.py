from django.shortcuts import render
import feedparser
import ssl
# Create your views here.
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context
feed = feedparser.parse("http://feeds.feedburner.com/movieweb_news")

news = []
for i in feed.entries:
    news.append({"title": i.title, "link": i.link})


def index(request):
    context = {'news': news}
    return render(request, 'feedApp/newsfeed.html', context)
