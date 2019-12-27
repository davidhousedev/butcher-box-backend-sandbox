def enum_as_choices(enum):
    """
    Represents a standard library Enum in a data format
    which can be supplied to Django as a list of choices.
    """
    return ((tag.name, tag.value) for tag in enum)
