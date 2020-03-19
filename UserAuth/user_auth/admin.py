from django.contrib import admin
from .models import Question, Choice

# Register your models here.
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class ChoicesAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    search_fields = ['choice_text']

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields':['question_text']}),
        ('Date information', {'fields':['pub_date']})
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoicesAdmin)
