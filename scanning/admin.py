from django.contrib import admin

<<<<<<< HEAD
from scanning.models import Category, Page, Tachymeter

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'likes')

admin.site.register(Category)
admin.site.register(Page, PageAdmin)
admin.site.register(Tachymeter, PageAdmin)
=======
from scanning.models import Category, Page

admin.site.register(Category)
admin.site.register(Page)
>>>>>>> 26b00b2f6542fe123b9fd5420c36e72e3c5dc52d
