from django.contrib import admin
from website_app.models import Emplacement, HomePage, Media



class EmplacementAdmin(admin.ModelAdmin):
    list_display = ('emplacement_type', 'emplacement_price_a_day', 'emplacement_summary')

class HomePageAdmin(admin.ModelAdmin):
    list_display = ('header_title1', 'header_title2')

class MediaAdmin(admin.ModelAdmin):
    list_display = ('titre', 'description', 'image')

admin.site.register(Emplacement, EmplacementAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(Media, MediaAdmin)
