from django.shortcuts import render

# Create your views here.
def data_render(request):
    d={'name':'mahi','age':15}
    return render(request,'data_render.html',context=d)


def if_condition(request):
    d={'a':10,'b':2000,'c':250,'hobbies':['dancing','sleeping','eating','listening stories','mostly watching zain immam']}
    return render(request,'if_conditions.html',context=d)    
