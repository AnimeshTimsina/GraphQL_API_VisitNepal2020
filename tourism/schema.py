import graphene
from graphene_django.types import DjangoObjectType, ObjectType
from .models import attractions,festivals,pubs,restaurants,cafe,hotels

#Create a GraphQL type for the actor model
class AttractionType(DjangoObjectType):
    class Meta:
        model = attractions

class FestivalType(DjangoObjectType):
    class Meta:
        model = festivals

class PubType(DjangoObjectType):
    class Meta:
        model = pubs

class restaurantType(DjangoObjectType):
    class Meta:
        model = restaurants

class cafeType(DjangoObjectType):
    class Meta:
        model = cafe

class HotelType(DjangoObjectType):
    class Meta:
        model = hotels
#Create a query type
class Query(ObjectType):
    attraction = graphene.Field(AttractionType, id=graphene.Int())
    attraction_list = graphene.List(AttractionType)
    attraction_by_province = graphene.List(AttractionType,id=graphene.Int())

    festival = graphene.Field(FestivalType,id=graphene.Int())
    festival_list = graphene.List(FestivalType)

    pub = graphene.Field(PubType,id=graphene.Int())
    pub_list = graphene.List(PubType)

    restaurant = graphene.Field(restaurantType,id=graphene.Int())
    restaurant_list = graphene.List(restaurantType)

    cafe = graphene.Field(cafeType,id=graphene.Int())
    cafe_list = graphene.List(cafeType)

    hotel = graphene.Field(HotelType,id=graphene.Int())
    hotel_list = graphene.List(HotelType)

    def resolve_attraction(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return attractions.objects.get(pk=id)

        return None

    def resolve_attraction_list(self, info, **kwargs):
        return attractions.objects.all()

    def resolve_attraction_by_province(self,info,**kwargs):
        id = kwargs.get('id')

        if id is not None:
            return attractions.objects.filter(province=id)

        return None

    def resolve_festival(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return festivals.objects.get(pk=id)

        return None

    def resolve_festival_list(self, info, **kwargs):
        return festivals.objects.all()

    def resolve_pub(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return pubs.objects.get(pk=id)

        return None

    def resolve_pub_list(self, info, **kwargs):
        return pubs.objects.all()

    def resolve_restaurant(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return restaurants.objects.get(pk=id)

        return None

    def resolve_restaurant_list(self, info, **kwargs):
        return restaurants.objects.all()

    def resolve_cafe(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return cafe.objects.get(pk=id)

        return None

    def resolve_cafe_list(self, info, **kwargs):
        return cafe.objects.all()

    def resolve_hotel(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return hotels.objects.get(pk=id)

        return None

    def resolve_hotel_list(self, info, **kwargs):
        return hotels.objects.all()


schema=graphene.Schema(query=Query,mutation=None)
