class Customer:
    def __init__(self, given_name, family_name):
        self._given_name = given_name
        self._family_name = family_name
        Customer.customers.append(self)

    @property
    def given_name(self):
        return self._given_name

    @property
    def family_name(self):
        return self._family_name

    @property
    def full_name(self):
        return f"{self.given_name} {self.family_name}"
