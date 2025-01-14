import graphene
from typing import Any

class Person(graphene.ObjectType):
    name: Any = ...
    age: Any = ...

class PersonInput(graphene.InputObjectType):
    name: Any = ...
    age: Any = ...

class CreatePerson(graphene.Mutation):
    class Input:
        person_data: Any = ...
    ok: Any = ...
    person: Any = ...
    def mutate(self, args: Any, context: Any, info: Any): ...

class LatLngInput(graphene.InputObjectType):
    lat: Any = ...
    lng: Any = ...

class LocationInput(graphene.InputObjectType):
    name: Any = ...
    latlng: Any = ...

class MyMutations(graphene.ObjectType):
    create_person: Any = ...

schema: Any
query_string: str
result: Any
