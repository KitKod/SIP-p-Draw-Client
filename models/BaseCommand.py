

class BaseCommand:

    #: str:the value to be displayed in the construct table.
    display_name = None
    #: dict: contains map of attribute name to its value.
    #: attribute -> value (None if this attribute has no default value).
    attributes_map = None
    #: str?: contains data that located in command.
    content = None

    def __init__(self):
        self.attributes_map = {
            'start_rtd': ,
            '': ,
            '': ,
            '': ,
            '': ,
        }
