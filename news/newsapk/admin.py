from django.contrib import admin
from . models import Article ,Abonnement


# Register your models here.

class ArticleAdmin(admin.ModelAdmin):
    list_display =('titre','slogan','texte','photo')
    
class AbonnementAdmin(admin.ModelAdmin):
    list_display = ('email','pays')
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Abonnement, AbonnementAdmin)
