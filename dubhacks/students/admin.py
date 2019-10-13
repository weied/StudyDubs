from django.contrib import admin

from .models import *
# Register your models here.
class QuestionInline(admin.StackedInline):
    model = Question.options.through
    extra = 1

class OptionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

class QuestionAdmin(admin.ModelAdmin):
    filter_horizontal = ("options",)

admin.site.register(Option)
admin.site.register(Question, QuestionAdmin)
