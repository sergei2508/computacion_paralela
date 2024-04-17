import random
import time

def monte_carlo_pi(points):
    inside_circle = 0
    for _ in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        if x**2 + y**2 <= 1:
            inside_circle += 1
    return inside_circle

def calculate_pi(num_points):
    total_inside_circle = monte_carlo_pi(num_points)
    return 4 * total_inside_circle / num_points

if __name__ == "__main__":
    num_points = 1000000  # Número total de puntos a generar

    start_time = time.time()
    pi_estimate = calculate_pi(num_points)
    end_time = time.time()

    print(f"Estimación de PI: {pi_estimate}")
    print(f"Tiempo de ejecución: {end_time - start_time} segundos")
