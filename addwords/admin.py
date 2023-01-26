from django.contrib import admin
from .models import Language, Word


class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'type', 'translation', 'language')
    


class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Language, LanguageAdmin)
admin.site.register(Word, WordAdmin)