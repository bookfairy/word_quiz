from django.contrib import admin
from .models import Dict


@admin.register(Dict)
class DictAdmin(admin.ModelAdmin):
    list_display = ['id', 'word', 'content_size', 'mean', 'created_at', 'updated_at']

    def content_size(self, dict):
        return '{}글자'.format(len(dict.word))

    content_size.short_description = '단어 글자수'
