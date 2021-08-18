import graphene

from graphql_auth.schema import UserQuery, MeQuery
from graphql_auth import mutations

class Query(
    UserQuery, 
    MeQuery, 
    graphene.ObjectType):
    pass

class Mutation(graphene.ObjectType):
  register = mutations.Register.Field()
  verify_account = mutations.VerifyAccount.Field()
  resend_activation_email = mutations.ResendActivationEmail.Field()
  send_password_reset_email = mutations.SendPasswordResetEmail.Field()
  password_reset = mutations.PasswordReset.Field()
  password_change = mutations.PasswordChange.Field()
  update_account = mutations.UpdateAccount.Field()

  # django-graphql-jwt inheritances
  token_auth = mutations.ObtainJSONWebToken.Field()
  verify_token = mutations.VerifyToken.Field()
  refresh_token = mutations.RefreshToken.Field()
  revoke_token = mutations.RevokeToken.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)