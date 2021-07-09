# from django.shortcuts import render
# from django.http import HttpResponse
# import boto3 
# def say_hello(request):
#     dynamodb = boto3.resource('dynamodb')
#     table = dynamodb.Table('key_url')
#     print(table.creation_date_time)
#     return HttpResponse(table.creation_date_time,s)

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
import boto3 
# Create your views here.

@api_view(['POST'])
def create_short_url(request):
    """
    List all code snippets, or create a new snippet.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('key_url')
    if request.method == 'POST':
        return HttpResponse(table.creation_date_time)

    else:
        return HttpResponse('Hello World222')
