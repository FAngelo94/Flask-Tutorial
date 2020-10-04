import requests

def count_words_at_url(url):
    return len(url)

from redis import Redis
from rq import Queue

q = Queue(connection=Redis())

result = q.enqueue(count_words_at_url, 'http://nvie.com')