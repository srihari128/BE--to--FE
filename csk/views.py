from django.shortcuts import render

# Create your views here.
def dhoni(request):
    d={'name':'HARI','age':23}
    return render(request,'dhoni.html',context=d)
