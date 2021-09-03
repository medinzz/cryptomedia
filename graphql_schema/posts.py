import graphene

from helpers.graphql.post_mutation_handlers import mutation_handler
from .users import UserType
from posts.models import Post
from graphql import GraphQLError
from graphql_jwt.decorators import login_required
from graphene_django.types import (
	DjangoObjectType,
	ObjectType
	)


class PostType(DjangoObjectType):
  '''
  # PostType
  
  A django object type that can be use to return an object in graphql
  '''
  class Meta:
    model = Post
    fields = '__all__'
  owner = graphene.Field(
    UserType
  )

  def resolve_owner(self, info):
    return self.user
    


class PostInput(graphene.InputObjectType):
  '''
  # PostInput

  Is an input object type in django to be used in graphql mutations
  '''
  content = graphene.String(required=True)
  user_id = graphene.ID(required=True)


class Query(ObjectType):
  posts = graphene.List(
    PostType
  )

  post = graphene.Field(
    PostType,
    id=graphene.ID(required=True)
  )

  @login_required
  def resolve_posts(self, *qrgs, **kwargs):
    return Post.objects.all()

  @login_required
  def resolve_post(self, *args, **kwargs):
    post_id = kwargs.get('id')
    return Post.objects.get(pk=id)


class CreatePost(graphene.Mutation):
  
  class Arguments:
    input = PostInput()

  post = graphene.Field(PostType)
  success = graphene.Boolean()

  @login_required
  def mutate(self, info, input=None):
    post = mutation_handler(input)
    print(input)
    success = True if(post) else False

    return CreatePost(post, success)


class UpdatePost(graphene.Mutation):

  class Arguments:
    input = PostInput()
    id = graphene.ID(required=True)

  post = graphene.Field(PostType)
  success = graphene.Boolean()

  @login_required
  def mutate(self, info, id, input=None):
    try:
      if(Post.objects.get(pk=id)):
        post = mutation_handler(input)
        success = True if(post) else False

        return UpdatePost(post, success)
      else:
        raise Exception('No existing post')
    except Exception as e:
      raise GraphQLError(e)


class Mutation(graphene.ObjectType):
  create_post = CreatePost.Field()
  update_post = UpdatePost.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)


