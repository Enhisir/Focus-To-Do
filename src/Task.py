from datetime import date


class Task:
    def __init__(self, item_id: int = 0, name: str = "", desc: str = "",
                 status: int = 0, is_imp: int = 0, have_dt: int = 0, dt: str = "1970-1-1"):
        self.id = item_id
        self.name = str(name)
        self.description = desc
        self.status_id = status
        self.is_imp = is_imp
        self.have_dt = have_dt
        self.date = dt
        if self.have_dt:
            self.date = date(*map(int, dt.split('-')))
        else:
            self.date = date(1971, 1, 1)
        if self.have_dt and self.status_id == 0 and self.date == date.today():
            self.is_imp = 1
        elif self.have_dt and self.status_id == 0 and self.date < date.today():
            self.status_id = 2

    def to_row(self):
        if self.have_dt:
            self.date = '-'.join(map(str, [self.date.year, self.date.month, self.date.day]))
        else:
            self.date = "1-1-1970"
        return self.id, self.name, self.description, self.status_id, self.is_imp, self.have_dt, self.date
