from django.shortcuts import render
def company(request):
    d={'rating':'1'}
    return render(request,'company.html',d)
# Create your views here.
