import time
from functools import wraps
def time_it(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        total_time = end_time - start_time
        print(f"Function '{func.__name__}' took {total_time:.4f} seconds to complete.")
        return result
    return wrapper
@time_it
def add_numbers(a, b):
    time.sleep(1)  # Simulate a short delay
    return a + b
add_numbers(3, 5)
