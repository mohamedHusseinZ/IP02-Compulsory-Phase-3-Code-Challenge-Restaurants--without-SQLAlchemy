class Customer:
    customers = []

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

    @classmethod
    def all(cls):
        return cls.customers


class Restaurant:
    def __init__(self, name):
        self._name = name
        self._reviews = []

    @property
    def name(self):
        return self._name

    @property
    def reviews(self):
        return self._reviews

    @property
    def customers(self):
        return list(set(review.customer for review in self.reviews))

    def average_star_rating(self):
        if not self.reviews:
            return 0
        total_ratings = sum(review.rating for review in self.reviews)
        return total_ratings / len(self.reviews)


class Review:
    reviews = []

    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.reviews.append(self)
        restaurant.reviews.append(self)
        customer.reviews.append(self)

    @property
    def rating(self):
        return self._rating

    @property
    def customer(self):
        return self._customer

    @property
    def restaurant(self):
        return self._restaurant

    @classmethod
    def all(cls):
        return cls.reviews
