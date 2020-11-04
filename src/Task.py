class Task:
    def __init__(self, id=0, nm="", ds="", st=0):
        self.id = id
        self.name = nm
        self.description = ds
        self.status_id = st

    def to_row(self):
        return self.id, self.name, self.description, self.status_id
