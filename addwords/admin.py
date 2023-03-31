from django.contrib import admin
from .models import Language, Word, Exchange


class WordAdmin(admin.ModelAdmin):
    list_display = ('word', 'type', 'translation', 'language', 'rate', 'add_date', 'author', 'archived')
    list_filter = ('archived', 'add_date')
    
class ExchangeAdmin(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'word', 'status')

class LanguageAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Language, LanguageAdmin)
admin.site.register(Word, WordAdmin)
admin.site.register(Exchange, ExchangeAdmin)