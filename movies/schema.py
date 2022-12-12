import graphene
import api.schema

class Query(api.schema.Query, graphene.ObjectType): # adding all the queries in the movies project as comma seperated
    pass

class Mutation(api.schema.Mutation, graphene.ObjectType): # adding all the mutation in the movies project as comma seperated
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)