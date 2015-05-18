# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Page.num_stars'
        db.alter_column(u'page_page', 'num_stars', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Page.num_stars2'
        db.alter_column(u'page_page', 'num_stars2', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Page.release_date'
        db.alter_column(u'page_page', 'release_date', self.gf('django.db.models.fields.DateField')(auto_now_add=True))

        # Changing field 'Page.content'
        db.alter_column(u'page_page', 'content', self.gf('django.db.models.fields.TextField')(max_length=30, null=True))

    def backwards(self, orm):

        # Changing field 'Page.num_stars'
        db.alter_column(u'page_page', 'num_stars', self.gf('django.db.models.fields.IntegerField')(default=2))

        # Changing field 'Page.num_stars2'
        db.alter_column(u'page_page', 'num_stars2', self.gf('django.db.models.fields.IntegerField')(default=2))

        # Changing field 'Page.release_date'
        db.alter_column(u'page_page', 'release_date', self.gf('django.db.models.fields.DateField')())

        # Changing field 'Page.content'
        db.alter_column(u'page_page', 'content', self.gf('django.db.models.fields.TextField')(default=2, max_length=30))

    models = {
        u'page.page': {
            'Meta': {'object_name': 'Page'},
            'content': ('django.db.models.fields.TextField', [], {'max_length': '30', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'num_stars': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'num_stars2': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'release_date': ('django.db.models.fields.DateField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '30', 'db_index': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['page']