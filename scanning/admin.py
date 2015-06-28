from django.contrib import admin

from scanning.models import Category, Page, Tachymeter

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'likes')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(Tachymeter, PageAdmin)
