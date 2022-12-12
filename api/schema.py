import graphene
import graphql_jwt

from graphene_django.types import DjangoObjectType
from .models import Movie, Director

from graphql_jwt.decorators import login_required

class MovieType(DjangoObjectType):
    class Meta:
        model = Movie

    movie_age = graphene.String()

    def resolve_movie_age(self, info):
        return "Old Movie" if self.date < 2000 else "New Movie"

class DirectorType(DjangoObjectType):
    class Meta:
        model = Director

class Query(graphene.ObjectType):
    all_movies = graphene.List(MovieType)
    movie = graphene.Field(MovieType, id=graphene.Int(), title=graphene.String())

    all_directors = graphene.List(DirectorType)
    director = graphene.Field(DirectorType, id=graphene.Int())
    
    @login_required
    def resolve_all_movies(self, info, **kwargs):
        return Movie.objects.all()

    @login_required
    def resolve_movie(self, info, **kwargs):
        id = kwargs.get('id')
        title=kwargs.get('title')

        if id is not None:
            return Movie.objects.get(pk=id)
        
        if title is not None:
            return Movie.objects.get(title=title)

    @login_required
    def resolve_all_directors(self, info):
        return Director.objects.all()
    
    @login_required
    def resolve_director(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Director.objects.get(id=id)

class DirectorCreateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        surname = graphene.String()

    director = graphene.Field(DirectorType)

    @login_required
    def mutate(self, info, name, surname):
        director = Director.objects.create(name=name, surname=surname)

        return DirectorCreateMutation(director=director)

class DirectorUpdateMutation(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        surname = graphene.String()
        id = graphene.ID(required=True)

    director = graphene.Field(DirectorType)

    @login_required
    def mutate(self, info, id, name, surname):
        director = Director.objects.get(pk=id)

        if name is not None:
            director.name=name
        if surname is not None:
            director.surname=surname
        director.save()

        return DirectorUpdateMutation(director=director)

class DirectorDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    director = graphene.Field(DirectorType)

    @login_required
    def mutate(self, info, id):
        director = Director.objects.get(pk=id)
        director.delete()
        
        return DirectorDeleteMutation(director=None)

class MovieCreateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        date= graphene.Int(required=True)
        director_id = graphene.Int(required=True)
    
    movie = graphene.Field(MovieType)

    @login_required
    def mutate(self, info, title, date, director_id):
        director = Director.objects.get(id=director_id)
        movie = Movie.objects.create(title=title, date=date, director=director)

        return MovieCreateMutation(movie=movie)

class MovieUpdateMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String()
        date = graphene.Int()
        id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)

    @login_required
    def mutate(self, info, id, title, date):
        movie = Movie.objects.get(pk=id)

        if title is not None:
            movie.title=title
        if date is not None:
            movie.date=date
        movie.save()

        return MovieUpdateMutation(movie=movie)

class MovieDeleteMutation(graphene.Mutation):
    class Arguments:
        id = graphene.ID(required=True)

    movie = graphene.Field(MovieType)

    @login_required
    def mutate(self, info, id):
        movie = Movie.objects.get(pk=id)
        movie.delete()
        
        return MovieDeleteMutation(movie=None)

class Mutation:
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()

    create_movie = MovieCreateMutation.Field()
    update_movie = MovieUpdateMutation.Field()
    delete_movie = MovieDeleteMutation.Field()

    create_director = DirectorCreateMutation.Field()
    update_director = DirectorUpdateMutation.Field()
    delete_director = DirectorDeleteMutation.Field()