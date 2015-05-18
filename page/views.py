from django.shortcuts import render
from blog.models import *
# Create your views here.

def home(request):
    context = {'blog_category': BlogCategory.objects.all(), 'd': 'dddddddddd'}
    import pdb; pdb.set_trace()
    return render(request, 'home.html', context)
