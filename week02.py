def greet(name):
    return f"Hello {name}. How are you?"
print(greet("Cesar"))
# Step 1: Define the greet function
def greet(name):
    return f"Hello {name}. How are you?"
my_friends = ["Juan", "John", "Ari"]
def greet_friends(friend_list):
    for friend in friend_list:
        print(greet(friend))
greet_friends(my_friends)
import math

def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant < 0:
        print("no real solutions")
    else:
        x1 = (-b - math.sqrt(discriminant)) / (2 * a)
        x2 = (-b + math.sqrt(discriminant)) / (2 * a)
        print("Solutions:")
        print("x1 =", x1)
        print("x2 =", x2)
solve_quadratic(1, -3, 2)  # This will solve x^2 - 3x + 2 = 0



