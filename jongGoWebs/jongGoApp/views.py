from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from .models import ProductDetail

# Create your views here.


def index(request):
    #dir = db.reference()  # 기본위치 지정
    #data_1 = db.reference().child()
    posts = ProductDetail.objects.all()
    return render(request, 'jongGoApp/index.html', {'posts': posts})

def join(request):
    return render(request, 'jongGoApp/join.html')

def login(request):
    return render(request, 'jongGoApp/login.html')