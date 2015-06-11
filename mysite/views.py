import os,sys
from django.http import HttpResponse
import datetime

def current_datetime(request):
	now = datetime.datetime.now()
	html = "<html><body>The time is now %s </html></body>" % now
	return HttpResponse(html)