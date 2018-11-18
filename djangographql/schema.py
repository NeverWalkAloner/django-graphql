import graphene

import posts.schema


class Mutation(graphene.ObjectType):
    create_post = posts.schema.CreatePostMutation.Field()


class Query(posts.schema.Query, graphene.ObjectType):
    # This class will inherit from multiple Queries
    # as we begin to add more apps to our project
    pass


schema = graphene.Schema(query=Query, mutation=Mutation)
