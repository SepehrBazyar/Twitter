from django.contrib import admin
from .models import Post, Tag, Comment, Reaction, Image

# Register your models here.
class ImageInLine(admin.StackedInline):
    model = Image
    extra = 1


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #exclude = ("is_deleted",)
    #fields = ("text", ("user", "status"), "tags")
    fieldsets = (
        (
            None, {
                'fields': ('text', ('user', 'status', 'is_deleted'), 'tags'),
            },
        ),
    )
    inlines = [ImageInLine]
    list_display = ["text", "user", "status"]
    search_fields = ["text"]
    list_filter = ["status"]
    actions = ["published_posts"]

    @admin.action(description="This Action is Published Selected Post")
    def published_posts(self, request, queryset):
        queryset.update(status=Post.Statuses.PUBLISHED)
        self.message_user(request, 'Published Successfully')


admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Reaction)
