from django.contrib import admin
from .models import Question, Answer
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):

    list_display = ('title','user', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['title', 'detail']
    summernote_fields = ('detail',)

# Register your models here.


admin.site.register(Answer)
