class Task:
    def __init__(self, item_id=0, name="", desc="", status=0):
        self.id = item_id
        self.name = name
        self.description = desc
        self.status_id = status

    def to_row(self):
        return self.id, self.name, self.description, self.status_id
