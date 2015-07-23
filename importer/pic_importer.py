import fake_component
import validators


datastore = fake_component
old_service = fake_component
default = u'http://giphy.com/gifs/cat-fail-cartoon-vdSCURsOBxZmM'


def picture_for(user_id):
    #if  validators.uuid(user_id):
    return datastore.fetch_user(user_id) or old_service.fetch_user(user_id) or default
    #else:
    #    raise TypeError("User IDs must be UUIDs")
