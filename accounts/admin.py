from django.contrib import admin

from .models import Post,Like,EditProfile

@admin.register(Post)
class ImageAdmin(admin.ModelAdmin):
    list_display=['title','body']

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display=['user','value']


@admin.register(EditProfile)
class EditAdmin(admin.ModelAdmin):
    list_display=['name']
    