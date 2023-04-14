from django.contrib import admin
# import models
from .models import Choice, Question

# Register your models here.

class ChoiceInline(admin.TabularInline):#StackedInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date indormation", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_field = ["question_text"]

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)