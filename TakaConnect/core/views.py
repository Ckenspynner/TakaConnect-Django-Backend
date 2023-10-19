from django.http.response import HttpResponse , JsonResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def HomePage(request):
    return HttpResponse('<h1>Okobo</h1>')

@csrf_exempt
def UserPage(request):
    user: User = User.objects.get(pk=1)
    
    username = request.POST.get("username")
    email = request.POST.get("email")
    
    #return JsonResponse({'Username': user.username, 'Email': user.email})
    return JsonResponse({'Username': username, 'Email': email})

