from django.contrib import admin

# Register your models here.
from .models import Category
from .models import BlogPost


admin.site.register(Category)


## BlogPost
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'updated_at', 'is_published')  # fields to display
    list_filter = ('category', 'created_at', 'updated_at')  # filters in the sidebar
    search_fields = ('title',)  # search functionality

    # Publishing feature custom actions
    actions = ['publish_posts', 'unpublish_posts']

    def publish_posts(self, request, queryset):
        queryset.update(is_published=True)

    def unpublish_posts(self, request, queryset):
        queryset.update(is_published=False)

admin.site.register(BlogPost, BlogPostAdmin)



