from django.contrib import admin
from habibi.models import Kiyimlar
# Register your models here.
class KiyimlarAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','content','size','number')
    list_display_links = ('name',)
    search_fields = ('name', 'image')

admin.site.register(Kiyimlar)