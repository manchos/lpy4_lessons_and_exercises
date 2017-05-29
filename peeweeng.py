from peewee import *
from datetime import date

db = SqliteDatabase('files/people.db')

class Person(Model):
    name = CharField()
    birthday = DateField()
    is_relative = BooleanField()

    class Meta:
        database = db # This model uses the "people.db" database.


class Pet(Model):
    owner = ForeignKeyField(Person, related_name='pets')
    name = CharField()
    animal_type = CharField()

    class Meta:
        database = db # this model uses the "people.db" database

db.connect()
db.create_tables([Person, Pet], safe=True)

# uncle_bob = Person(name='Bob', birthday=date(1960, 1, 15), is_relative=True)
# grandma = Person.create(name='Grandma', birthday=date(1935, 3, 1), is_relative=True)
# herb = Person.create(name='Herb', birthday=date(1950, 5, 5), is_relative=False)
# grandma.name = 'Grandma L.'
# grandma.save()
# aa = uncle_bob.save()  # bob is now stored in the database
# print(aa)