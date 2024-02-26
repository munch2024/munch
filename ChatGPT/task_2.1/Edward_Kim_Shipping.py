#2.1
def calculate_shipping_cost(weight, distance):
    rate = 5  # Rate per kg-km
    cost = weight * distance * rate
    return cost

def calculate_discounted_cost(weight, distance, discount):
    rate = 5  # Rate per kg-km
    cost = weight * distance * rate
    discounted_cost = cost * (1 - discount)
    return discounted_cost
