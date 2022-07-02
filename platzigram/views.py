"""Platzigram views."""

#Django
from curses.ascii import HT
from django.http import HttpResponse

#Utils
from datetime import datetime
import json

import platzigram

def hello(request):
    """return greeting"""
    return HttpResponse('Oh, hi! current server time is {now}'. format(
        now=datetime.now().strftime("%b %dth, %Y - %H:%M hrs")
    ))

def sort_integers(request):
    """return a JSON response with sorted integer"""
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    data= {
        'status': 'ok',
        'numbers': sorted_numbers,
        'message': 'Integers sorted successfully'
    }
    # import pdb; pdb.set_trace()
    return HttpResponse(
        json.dumps(data, indent=4), 
        content_type='application/json'
        )

def say_hi(request, name, age):
    if age<12:
        message = 'Sorry {}, you are not allowed here.'.format(name)
    else: 
        message = 'Hello {}!, Welcome to platzigram'. format(name)
    return HttpResponse(message)
