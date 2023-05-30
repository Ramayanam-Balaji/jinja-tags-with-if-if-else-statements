from django.shortcuts import render

# Create your views here.
def prabhas(request):
    d={'a':10,'b':7}
    return render(request,'prabhas.html',context=d)
