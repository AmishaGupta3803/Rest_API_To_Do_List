from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import ToDoReadSerializer, ToDoWriteSerializer
from .models import *

# Create your views here.
@api_view()
def api(request):
    return Response({
        "status": 200,
        "message": "Yes! Django framework is working."
    })

@api_view(["POST"])
def post_task(request):
    try: 
        data = request.data
        serializer = ToDoWriteSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                "status": True,
                "message": "Successfully added task.",
                "data": serializer.data
            })
        else:
            return Response({
                "status": False,
                "message": "invalid data",
                "data": serializer.errors
            })
    except Exception as e:
        print(e)
        return Response({
            "status": False,
            "message": "Something went wrong."
        })
    
@api_view(["GET"])
def all_tasks(request):
    tasks = Task.objects.all()
    serializer = ToDoReadSerializer(tasks, many=True)
    return Response({
        "status": True,
        "message": "Request Successful",
        "data": serializer.data
    })

@api_view(["GET"])
def get_task(request):
    try:
        data = request.data
        if not data.get('id'):
            return Response({
                "status": False,
                "message": "id is required",
                "data": {}
            })
        task = Task.objects.get(id=data.get('id'))
        serializer = ToDoReadSerializer(task)
        return Response({
            "status": True,
            "message": "Details are as follows.",
            "data": serializer.data
        })
    except Exception as e:
        print(e)
        return Response({
            "status": False,
            "message": "Something went wrong."
        })

@api_view(["PATCH"])
def update_task(request):
    try:
        data = request.data
        if not data.get('id'):
            return Response({
                "status": False,
                "message": "id is required",
                "data": {}
            })
        task = Task.objects.get(id=data.get('id'))
        serializer = ToDoWriteSerializer(task, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    "status": True,
                    "message": "Successfully added task.",
                    "data": serializer.data
                })
        else:
                return Response({
                    "status": False,
                    "message": "invalid data",
                    "data": serializer.errors
                })
    except Exception as e:
        print(e)
        return Response({
            "status": False,
            "message": "Something went wrong."
        })

@api_view(["DELETE"])
def delete_task(request):
    data = request.data
    if not data.get('id'):
            return Response({
                "status": False,
                "message": "id is required",
                "data": {}
            })
    task = Task.objects.get(id=data.get('id'))
    task.delete()
    return Response({
        "status": True,
        "message": "Successfully Deleted."
    })
