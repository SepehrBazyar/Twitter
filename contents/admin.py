from django.contrib import admin
from .models import Post, Tag, Comment, Reaction, Image

# Register your models here.
class ImageInLine(admin.StackedInline):
    model = Image
    extra = 5


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    #exclude = ("is_deleted",)
    #fields = ("text", ("user", "status"), "tags")
    fieldsets = (
        ('details', {
        'fields': ('text', ('user', 'status'), 'tags'),
        }),
    )
    inlines = [ImageInLine]


admin.site.register(Tag)
admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(Reaction)
