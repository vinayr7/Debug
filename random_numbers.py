import random
import numpy as np

def generate_random_numbers():
    # Generate a random integer between 1 and 100
    random_int = random.randint(1, 100)
    print(f"Random integer between 1 and 100: {random_int}")
    
    # Generate a random float between 0 and 1
    random_float = random.random()
    print(f"Random float between 0 and 1: {random_float}")
    
    # Generate a random float in a specific range
    random_float_range = random.uniform(10.5, 20.5)
    print(f"Random float between 10.5 and 20.5: {random_float_range}")
    
    # Generate multiple random numbers using numpy
    random_array = np.random.rand(5)  # 5 random numbers between 0 and 1
    print(f"Array of 5 random numbers: {random_array}")
    
    # Generate random integers using numpy
    random_integers = np.random.randint(1, 100, size=5)  # 5 random integers between 1 and 100
    print(f"Array of 5 random integers: {random_integers}")

if __name__ == "__main__":
    print("Generating random numbers using different methods:")
    generate_random_numbers() 