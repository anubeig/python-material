import Json
import datetime

#if our data stucture contains a datetime object we'll get an exception:
d = {
    'name': 'Foo'
}
print(Json.dumps(d))  # {"name": "Foo"}

d['date'] = datetime.datetime.now()
print(Json.dumps(d))  # TypeError: datetime.datetime(2016, 4, 8, 11, 22, 3, 84913) is not JSON serializable


d = {
    'name': 'Foo'
}
print(Json.dumps(d))  # {"name": "Foo"}

d['date'] = datetime.datetime.now()


def myconverter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()


print(Json.dumps(d, default=myconverter))  # {"date": "2016-04-08 11:43:36.309721", "name": "Foo"}
