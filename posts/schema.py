from django.contrib.auth import get_user_model

import graphene

from graphene_django.types import DjangoObjectType

from .models import Comment, Post


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment


class PostType(DjangoObjectType):
    class Meta:
        model = Post


class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()
        only_fields = ['id', 'username', 'first_name', 'last_name']


class Query(object):
    all_comments = graphene.List(CommentType)
    all_posts = graphene.List(PostType)

    def resolve_all_comments(self, info, **kwargs):
        return Comment.objects.all()

    def resolve_all_posts(self, info, **kwargs):
        return Post.objects.prefetch_related('comment_set').all()


class CreatePostMutation(graphene.Mutation):
    post = graphene.Field(PostType)

    class Arguments:
        title = graphene.String()
        content = graphene.String()

    def mutate(self, info, title, content):
        user = info.context.user
        return CreatePostMutation(
            post=Post.objects.create(title=title, content=content, author=user)
        )
