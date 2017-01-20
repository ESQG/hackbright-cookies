"""Customers at Hackbright."""


class Customer(object):
    """Ubermelon customer."""

    # TODO: need to implement this

    def __init__(self, first_name, last_name, email, password):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = self.first_name +" "+self.last_name
        self.email = email
        self.password = password

    def __repr__(self):
        return "<customer %s %s >" %(self.first_name, self.last_name)

def read_customers_from_file(filepath):
    """Read customer data from file and populate a dictionary of customers.

    Dictionary will be {email: Customer object}
    """

    customer_dict = {}

    with open(filepath) as data_file:
        for line in data_file:
            (first_name, last_name, email, password) = line.strip().split("|")
            customer_dict[email] = Customer(first_name, last_name, email, password)

    return customer_dict

customer_dict = read_customers_from_file("customers.txt")

def get_by_email(email):
    return customer_dict.get(email)