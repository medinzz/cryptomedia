import graphene
from graphql_schema import users

class Query(
    users.Query,
    graphene.ObjectType):
    pass

class Mutation(
    users.Mutation, 
    graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)