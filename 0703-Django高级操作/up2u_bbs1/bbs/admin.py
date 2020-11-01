from django.contrib import admin

from .models import Topic, Reply


class TopicAdmin(admin.ModelAdmin):
    list_display = ('topic_text', 'author', 'pub_date', )
    list_filter = ('topic_text', 'author', 'pub_date', )
    search_fields = ('topic_text', 'topic_description')
    list_editable = ('author',)
    # list_editable = ('topic_text', 'author')
    # list_display_links = None
    list_per_page = 10

class ReplyAdmin(admin.ModelAdmin):
    list_display = ('reply_text', 'topic', 'author', 'pub_date',)
    list_filter = ('reply_text', 'topic', 'author', 'pub_date',)
    search_fields = ('reply_text',)
    list_per_page = 10


# Register your models here.
admin.site.register(Topic, TopicAdmin)
admin.site.register(Reply, ReplyAdmin)