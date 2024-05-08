import uuid


def uuid_generator(id: str) -> uuid.UUID:
    """
    Generate a UUID based on the given ID using UUID version 5.

    Args:
        id (str): The input ID to generate the UUID.

    Returns:
        UUID: The UUID generated based on the input ID.
    """
    namespace = uuid.NAMESPACE_URL
    id = str(id)
    uuid_from_name = uuid.uuid5(namespace, id)
    return uuid_from_name
