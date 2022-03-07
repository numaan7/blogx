from atexit import register
from django.contrib import admin
from .models import Post,Categorie,Conatct,Comments,Page



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')
admin.site.register(Categorie)
@admin.register(Conatct)
class ContactAdmin(admin.ModelAdmin):
    list_display=('fname','lname','email','question')
    list_filter = ('date', 'email', 'question')

@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):
    list_display=('user', 'comment', 'post', 'created', 'active')
    list_filter = ('created', 'post', 'user')

    search_fields = ('name', 'email', 'comment')
@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display=('ptitle', 'slug', 'status')
    list_filter = ('ptitle', 'pbody', 'status')
    prepopulated_fields = {'slug': ('ptitle',)}
    search_fields = ('ptitle', 'pbody', 'slug')


