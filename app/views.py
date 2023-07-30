from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'mahi','age':15}
    return render(request,'data_render.html',context=d)


def if_condition(request):
    d={'a':10,'b':2000,'c':250}
    return render(request,'ifconditons.html',context=d)    
