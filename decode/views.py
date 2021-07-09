from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpResponse
import boto3
# Create your views here.

@api_view(['GET'])
def get_original_url(request):
    """
    List all code snippets, or create a new snippet.
    """
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('key_url')
    if request.method == 'GET':
        response = table.get_item(
            Key = {
                'key':'test'
            }
        )
        
        return Response(response["Item"])
