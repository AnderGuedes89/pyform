from django.contrib import admin
from evaluation.models import Evaluation, Instructor, Training

admin.site.register(Training)
admin.site.register(Instructor)
admin.site.register(Evaluation)
