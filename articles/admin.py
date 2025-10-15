# articles/admin.py
from django.contrib import admin
from .models import Article, Comment

#To see all comments
class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0  # No extra empty forms

class ArticleAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    
    list_display = [
    "title",
    "body",
    "author",
    ]
    
admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment)
