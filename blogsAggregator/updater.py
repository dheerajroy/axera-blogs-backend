from apscheduler.schedulers.background import BackgroundScheduler
from .blogs_aggregator import BlogsAggregator
from django.conf import settings
from datetime import datetime

def start():
    scheduler = BackgroundScheduler()
    blogs_aggregator = BlogsAggregator()
    scheduler.add_job(blogs_aggregator.delete_old_blogs, 'interval', hours=settings.JOB_EVERY, next_run_time=datetime.now())
    scheduler.add_job(blogs_aggregator.set_blogs, 'interval', hours=settings.JOB_EVERY, next_run_time=datetime.now())
    scheduler.start()
