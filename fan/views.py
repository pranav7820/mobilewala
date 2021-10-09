from django.shortcuts import render
from django.http import HttpResponse
from .models import Pnna

# Create your views here.
def index(request):
    # return HttpResponse('hello world !')
    return render(request,'shop/index.html')

def python(request):
    # return HttpResponse('python')
    return render(request, 'shop/python.html')
def html(request):
    return HttpResponse('html')
def css(request):
    return render(request,'shop/css.html')
def java(request):
    return HttpResponse('java')
def contact(request):
    if request.method=='POST':
        print(request)
        name=request.POST.get('name','')
        email=request.POST.get('email','')
        phone=request.POST.get('phone','')
        pnna=Pnna(name=name,email=email,phone=phone)
        pnna.save()


    # return HttpResponse('contact')
        return render(request, 'shop/contact.html')
    else:
        return render(request, 'shop/contact.html')


def link(request):
    x=request.GET.get('text','defult')
    y=request.GET.get('chk','off')
    print(x)
    print(y)
    punc='''~!@#$%^&*()_+-={}|[]\:";'<>?,./"'''
    analized=[]
    char=[]
    if char in x:
        if char not in y:
            analized=analized+char
            PARAM={'analized':'change the caps of text'}
            return render(request,'shop/linkform.html',PARAM)
