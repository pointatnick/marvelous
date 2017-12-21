class Character:
    def __init__(self, id=None, name=None):
        self.id = 0 if id is None else id
        self.name = "" if name is None else name


class Comic:
    def __init__(self, id=None, title=None, description=None):
        self.id = 0 if id is None else id
        self.title = "" if title is None else title
        self.description = "" if description is None else description