import graphene
import tourism.schema

class Query(tourism.schema.Query,graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=None)
