from django.db import models


class Dict(models.Model):
    word = models.CharField(max_length=20, verbose_name='단어', help_text='영단어를 입력하세요. (최대 20자)')
    mean = models.TextField(verbose_name='단어의 뜻', help_text='영단어의 뜻을 입력하세요.')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='추가일')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='수정일')

    class Meta:
        ordering = ['word']

    def __str__(self):
        return self.word
