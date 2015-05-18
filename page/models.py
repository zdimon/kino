from django.db import models


class Page(models.Model):
    title = models.CharField(max_length=30, blank = True, default='', verbose_name = 'Name', db_index = True)
    content = models.TextField(max_length=30, blank = True, null = True)
    release_date = models.DateField(auto_now_add = True)
    num_stars = models.IntegerField(blank = True, null = True)
    num_stars2 = models.IntegerField(blank = True, null = True)
