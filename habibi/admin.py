from django.contrib import admin
from habibi.models import *
# Register your models here.
class KiyimlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','content','size','number')
    list_display_links = ('name',)
    search_fields = ('name', 'image')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )
    list_display_links = ('name',)
    search_fields = ('name',)

class AloqaAdmin(admin.ModelAdmin):
    list_display = ('name','Email','subject','Email')
    list_display_links = ('name',)
    search_fields = ('name',)

admin.site.register(Kiyimlar,KiyimlarAdmin)
admin.site.register(Category,CategoryAdmin)
admin.site.register(Aloqa, AloqaAdmin)