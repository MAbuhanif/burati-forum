from django.contrib import admin
from .models import Question, Answer


# Register the Answer model
admin.site.register(Question)
admin.site.register(Answer)
