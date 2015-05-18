# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Page'
        db.create_table(u'page_page', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=30, db_index=True, blank=True)),
            ('content', self.gf('django.db.models.fields.TextField')(max_length=30)),
            ('release_date', self.gf('django.db.models.fields.DateField')()),
            ('num_stars', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'page', ['Page'])


    def backwards(self, orm):
        # Deleting model 'Page'
        db.delete_table(u'page_page')


    models = {
        u'page.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_stars': ('django.db.models.fields.IntegerField', [], {}),
            'release_date': ('django.db.models.fields.DateField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['page']