import uuid


# Generate a UUID random or based at id
def uuid_generator(id):
    namespace = uuid.NAMESPACE_URL
    id = str(id)
    uuid_from_name = uuid.uuid5(namespace, id)
    return uuid_from_name
