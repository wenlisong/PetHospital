from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'User/sign_in.html')

def sign_up(request):
    return render(request,'User/sign_up.html')