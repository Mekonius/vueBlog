import graphene
from django.contrib.auth import get_user_model
from graphene_django import DjangoObjectType

from blog import models


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


class AuthorType(DjangoObjectType):
    class Meta:
        model = models.Profile


class PostType(DjangoObjectType):
    class Meta:
        model = models.Post

class TagType(DjangoObjectType):
    class Meta:
        model = models.Tag


class Ingredients(DjangoObjectType):
    class Meta:
        model = models.Ingredients


class BrandType(DjangoObjectType):
    class Meta:
        model = models.Brand
        
class SeriesType(DjangoObjectType):
    class Meta:
        model = models.Series

class Query(graphene.ObjectType):
    all_posts = graphene.List(PostType)
    author_by_username = graphene.Field(AuthorType, username=graphene.String())
    post_by_slug = graphene.Field(PostType, slug=graphene.String())
    posts_by_author = graphene.List(PostType, username=graphene.String())
    posts_by_tag = graphene.List(PostType, tag=graphene.String())
    posts_by_ingredients = graphene.List(PostType, ingredients=graphene.String())
    posts_by_brands = graphene.List(PostType, brands=graphene.String())
    posts_by_series = graphene.List(PostType, series=graphene.String())

    def resolve_all_posts(root, info):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .all()
        )

    def resolve_author_by_username(root, info, username):
        return models.Profile.objects.select_related("user").get(
            user__username=username
        )

    def resolve_post_by_slug(root, info, slug):
        return (
            models.Post.objects.prefetch_related("author")
            .select_related("author")
            .get(slug=slug)
        )

    def resolve_posts_by_author(root, info, username):
        return (
            models.Post.objects.prefetch_related("username")
            .select_related("author")
            .filter(author__user__username=username)
        )

    def resolve_posts_by_tag(root, info, tag):
        return (
            models.Post.objects.prefetch_related("tags")
            .select_related("author")
            .filter(tags__name__iexact=tag)
        )

    def resolve_posts_by_ingredients(root, info, ingredients):
        return (
            models.Post.objects.prefetch_related("ingredients")
            .select_related("author")
            .filter(ingredients__name__iexact=ingredients)
        )

    def resolve_posts_by_brand(root, info, brand):
        return (
            models.Post.objects.prefetch_related("brands")
            .select_related("author")
            .filter(brand__name__iexact=brand)
        )

    def resolve_posts_by_series(root, info, series):
        return (
                models.Post.objects.prefetch_related("series")
                .select_related("author")
                .filter(series_name__iexact=series)
        )


schema = graphene.Schema(query=Query)
