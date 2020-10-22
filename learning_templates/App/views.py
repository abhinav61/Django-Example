from django.shortcuts import render


# Create your views here.
def index(request):
    context_dict = {'text': 'Hello_World','number':100}
    return render(request,'App/index.html', context_dict)

def other(request):
    return render(request,'App/other.html')

def relative(request):
    return render(request,'App/Relative_url_templates.html')