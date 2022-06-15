from bs4 import BeautifulSoup
import feedparser
from datetime import timedelta
from django.utils import timezone
from .models import RSSLink, Blog
import django.db
import re


class BlogsAggregator:
    def get_image(self, data):
        link = re.search(r"""(http)?s?:?(\/\/[^"']*\.(?:png|jpg|jpeg|gif|png|svg))""", data)
        if link is not None:
            link = link.group(0)
            
        elif link is None:
            soup = BeautifulSoup(data, 'html.parser')
            a = soup.find('img')
            if a is not None:
                link = a.get('src')
        return link
    def clean_summary(self, summary):
        soup = BeautifulSoup(summary, 'html.parser')
        return soup.get_text()

    def set_blogs(self):
        django.db.close_old_connections()
        rss_link = RSSLink.objects.all().order_by('?')
        for link in rss_link:
            blogs = feedparser.parse(link.link)['entries']
            for blog in blogs:
                try:
                    Blog.objects.create(topic=link.topic,
                                        title=blog.title,
                                        cover_image=self.get_image(str(blog)),
                                        summary=self.clean_summary(blog.summary),
                                        link=blog.link)
                except Exception:
                    pass

    def delete_old_blogs(self):
        django.db.close_old_connections()
        current_datetime = timezone.now()
        Blog.objects.filter(uploaded_datetime__lte=current_datetime-timedelta(hours=24)).delete()
