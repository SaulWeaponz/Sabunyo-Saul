#Exercise
#submit your work to github for method overriding, method overloading and MRO
#MRO is Method Resolution Order.
# Two real world examples are neede for the above concepts. 

# 2.Method overloading
# Real World Example: Delivery Service
from multipledispatch import dispatch

class DeliveryService:
    @dispatch(float)
    def calculate_shipping_cost(self, weight_kg):
        """Calculates shipping cost based on weight only."""
        return 5 + weight_kg * 2

    @dispatch(float, float)
    def calculate_shipping_cost(self, weight_kg, distance_km):
        """Calculates shipping cost based on weight and distance."""
        return 10 + weight_kg * 2 + distance_km * 0.5

    @dispatch(float, float, str)
    def calculate_shipping_cost(self, weight_kg, distance_km, delivery_type):
        """Calculates shipping cost based on weight, distance, and delivery type."""
        cost = 10 + weight_kg * 2 + distance_km * 0.5
        if delivery_type == "express":
            cost += 15
        elif delivery_type == "fragile":
            cost += 10
        return cost

# Usage
delivery_service = DeliveryService()

# Calculate shipping cost based on weight only
cost1 = delivery_service.calculate_shipping_cost(5.0)
print(f"Shipping cost (weight only): ${cost1}")

# Calculate shipping cost based on weight and distance
cost2 = delivery_service.calculate_shipping_cost(5.0, 20.0)
print(f"Shipping cost (weight and distance): ${cost2}")

# Calculate shipping cost based on weight, distance, and delivery type
cost3 = delivery_service.calculate_shipping_cost(5.0, 20.0, "express")
print(f"Shipping cost (weight, distance, and express delivery): ${cost3}")

cost4 = delivery_service.calculate_shipping_cost(5.0, 20.0, "fragile")
print(f"Shipping cost (weight, distance, and fragile delivery): ${cost4}")