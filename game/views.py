from django.shortcuts import render
from django.http import HttpResponse

import json

from pprint import pprint

# Create your views here.
def index(request):
	data = json.loads(open("./data/game/data.json").read())
	res  = json.dumps(data)

	query_id = int(request.GET.get('id') or 0)

	if query_id != 0:
		return HttpResponse("Any data w/ this ID not exists!")

	return HttpResponse(res)

def category(request):
    return HttpResponse("Hi, welcome to geek.io. Please check our docs...")
