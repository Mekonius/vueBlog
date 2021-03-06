from django.contrib import admin
from blog.models import Profile, Post, Tag, Ingredients, Brand, Series


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag

@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    model = Ingredients
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    model = Brand
@admin.register(Series)
class BrandAdmin(admin.ModelAdmin):
    model = Series

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post

    list_display = (
        "id",
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    list_filter = (
        "published",
        "publish_date",
    )
    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )
    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }

    
    date_hierarchy = "publish_date"
    save_on_top = True