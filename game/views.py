from django.shortcuts import render
from django.http import HttpResponse

import json
# import os

from pprint import pprint

# Create your views here.
def index(request):
    return HttpResponse("Welcome to GeekData Api v1. Check docs to use Game API")

def game(request):
	data = json.loads(open("./data/game/data.json").read())
	res  = json.dumps(data)

	query_id = int(request.GET.get('id') or 0)

	# print query_id

	if query_id != 0:
		return HttpResponse("Any data w/ this ID not exists!")

	return HttpResponse(res)

def user(request):
    return HttpResponse("User")
