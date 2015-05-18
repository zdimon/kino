# -*- coding: utf-8 -*-
from django.db import models

class BlogCategory(models.Model):
    name = models.CharField(max_length=250, verbose_name=u'Заголовок', blank=False)
    description = models.TextField(verbose_name=u'Описание')
    def __unicode__(self):
        return '%s (%s)' % (self.name,self.description)
 
class BlogTopic(models.Model):
    STATUS = (
        (u'черновик',u'черновик'),
        (u'доступен',u'доступен'),
        (u'заморожен',u'заморожен'),
    )
    category = models.ForeignKey('BlogCategory')
    title = models.CharField(max_length=250, verbose_name=u'Заголовок', blank=False)
    content = models.TextField(verbose_name=u'Содержимое')
    created_at = models.DateField(auto_now_add=True)
    status = models.CharField(choices=STATUS, verbose_name=u'Статус', max_length=250)

 
class BlogPost(models.Model):
    topic = models.ForeignKey('BlogTopic')
    author = models.CharField(verbose_name=u'Автор', blank=False, max_length=250)
    content = models.TextField(verbose_name= u'Содержимое', blank=False)

 
class BlogImages(models.Model):
    topic = models.ForeignKey('BlogTopic')
    image  = models.ImageField(upload_to='blog', verbose_name=u'Изображение')


class Tag(models.Model):
    name = models.CharField(max_length=100)
    topic = models.ManyToManyField(BlogTopic)


