from django.contrib import admin
from .models import Question, Answer
from django_summernote.admin import SummernoteModelAdmin

"""
This file is used to register the models in the admin panel.
The Question model is registered using the QuestionAdmin class.
The Answer model is registered using the AnswerAdmin class.
"""
@admin.register(Question)
class QuestionAdmin(SummernoteModelAdmin):
    list_display = ('title','user', 'created_on')
    list_filter = ('created_on',)
    search_fields = ['title', 'detail']
    summernote_fields = ('detail',)

# Register the Answer model
admin.site.register(Answer)
