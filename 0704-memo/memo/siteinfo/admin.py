from django.contrib import admin

from .models import Banner, Item, Col, Footer

# Register your models here.
class ColInline(admin.TabularInline):
    model = Col
    fields = ('title',)


class ItemInline(admin.TabularInline):
    model = Item
    fields = ('title', 'url')

@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_editable = ()
    readonly_fields = []
    inlines = [ColInline]


@admin.register(Col)
class ColAdmin(admin.ModelAdmin):
    list_display = ('title', 'footer')
    inlines = [ItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'col')


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', )