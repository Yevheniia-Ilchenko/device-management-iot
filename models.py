from peewee import *


db = SqliteDatabase('mydatabase.db')


class BaseModel(Model):
    class Meta:
        database = db


class ApiUser(BaseModel):
    name = CharField(max_length=100)
    email = CharField(max_length=100, unique=True)
    password = CharField(max_length=100)


class Location(BaseModel):
    name = CharField(max_length=100)


class Device(BaseModel):
    name = CharField(max_length=100)
    type = CharField(max_length=100)
    login = CharField(max_length=100)
    password = CharField(max_length=100)
    location = ForeignKeyField(Location, backref='devices', on_delete='CASCADE')
    api_user = ForeignKeyField(ApiUser, backref='devices', on_delete='CASCADE')


# def create_tables():
#     with db:
#         db.create_tables([ApiUser, Location, Device])
#
#
# if __name__ == "__main__":
#     create_tables()
