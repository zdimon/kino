# -*- coding: utf-8 -*-
import logging
from optparse import make_option
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand
from blog.models import BlogCategory
from page.models import Page

#logger = logging.getLogger(__name__)


class Command(BaseCommand):

    def handle(self, *args, **options):
        BlogCategory.objects.all().delete()
        print 'start'
        from django_faker import Faker
        populator = Faker.getPopulator()

        
        populator.addEntity(BlogCategory,5)
        insertedPks = populator.execute()
        print insertedPks
        #import pdb; pdb.set_trace()
        for i,d in insertedPks:
            print i,d
        
        
        

        print 'Done' 
