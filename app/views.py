from django.shortcuts import render

# Create your views here.
def ganesh(request):
    d={'a':100,'b':50,'c':70}
    return render(request,'ganesh.html',d)
