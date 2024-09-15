import numpy as np
def perturbation(solution, perturbation_size=0.1):
    perturbed_solution = solution + perturbation_size * np.random.rand(len(solution))
    return np.clip(perturbed_solution, -5.12, 5.12)
def local_search(solution, objective_func, max_iterations=100):
    best_solution = solution.copy()
    best_fitness = objective_func(best_solution)

    for _ in range(max_iterations):
        neighbors_solution = perturbation(solution)
        neighbors_fitness = objective_func(neighbors_solution)

        if neighbors_fitness < best_fitness:
            best_solution = neighbors_solution
            best_fitness = neighbors_fitness

    return best_solution, best_fitness

def iterated_local_search(initial_solution, objective_func, max_iterations=100, perturbation_size=0.1):
    best_solution = initial_solution.copy()
    best_fitness = objective_func(best_solution)

    for _ in range(max_iterations):
        perturbed_solution = perturbation(best_solution, perturbation_size)
        local_best_solution, local_best_fitness = local_search(perturbed_solution, objective_func)

        if local_best_fitness < best_fitness:
            best_solution = local_best_solution
            best_fitness = local_best_fitness
    return best_solution, best_fitness

def sphere_function(x):
    return np.sum(x**2) #Giai phap ban dau

initial_solution = np.random.uniform(-5.12, 5.12, size=10)

#Bai toan kich co 10 chieu
max_iterations = 100
perturbation_size = 0.1

#Tim kiem cuc bo voi so lan lap
best_solution, best_fitness = iterated_local_search(initial_solution, sphere_function, max_iterations, perturbation_size)

#Xuat ra giai phap, the luc tot nhat
print("Best solution: ", best_solution)
print("Best fitness: ", best_fitness)




















