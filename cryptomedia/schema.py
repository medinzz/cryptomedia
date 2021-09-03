import graphene
from graphql_schema import users, posts

class Query(
    users.Query,
    posts.Query,
    graphene.ObjectType):
    pass

class Mutation(
    users.Mutation,
    posts.Mutation, 
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)