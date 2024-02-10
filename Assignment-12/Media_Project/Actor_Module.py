class Actor:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def show_full_name(self):
        return f"{self.firstname} {self.lastname}"

    def __str__(self):
        return f"Firstname: {self.firstname}\t|Lastname: {self.lastname}"
