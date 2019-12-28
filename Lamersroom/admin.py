from django.contrib import admin
from .models import Post, Profile, Rubric, Comment

admin.site.register(Post)
admin.site.register(Profile)
admin.site.register(Rubric)
admin.site.register(Comment)