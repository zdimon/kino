from django.shortcuts import render
from blog.models import BlogCategory

def category_detail(request, id):
    category = BlogCategory.objects.get(pk=id)
    topics = BlogTopic.objects.filter(category=category, )
    context = {'category': category )}
    #import pdb; pdb.set_trace()
    return render(request, 'blog_detail.html', context)
