from django.contrib import admin

from .models import Test, User, Post, Image
# Register your models here.

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    exclude = ('image_width', 'image_height',)

admin.site.register(Test)
admin.site.register(Post)

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = ('avatar_width', 'avatar_height','salt',)
