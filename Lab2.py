#Genetic Algorithms - Thuật toán di truyền

import numpy as np
#Định nghĩa hàm fitness_function - Hàm số âm
def fitness_func(individual):
    return -np.sum(individual**2)

#Tạo quần thể ban đầu ngẫu nhiên
def generate_population(size, dim):
    return np.random.rand(size, dim)
#Định nghĩa hàm Genetic Algorithm
def genetic_algorithm(individuals, fitness_func, n_generations=100, multation_rate=0.01):
    for _ in range(n_generations):
        population = sorted(individuals, key=fitness_func, reverse=True)
        next_generation = population[:len(population)//2].copy()
        while len(next_generation) < len(population):
            parents_indices = np.random.choice(len(next_generation), 2, replace= False)
            parent1, parent2 = next_generation[parents_indices[0]], next_generation[parents_indices[1]]
            crossover_point = np.random.randint(1, len(parent1))
            child = np.concatenate((parent1[:crossover_point], parent2[crossover_point:]))
            if np.random.rand() < multation_rate:
                mutation_point = np.random.randint(1, len(child))
                child[mutation_point] = np.random.rand()
            next_generation.append(child)
        population = np.array(next_generation)
    return population[0]

#Tham số
popultion_size = 10
dimension = 5
n_generations = 50
multation_rate = 0.05
#Khởi tạo quần thể
popultion = generate_population(popultion_size, dimension)
#Thuật toán di truyền, chuyển sang giá trị dương
best_individual = genetic_algorithm(popultion, fitness_func, n_generations, multation_rate)
print("Best_individual: ", best_individual)
print("Best fitness: ", -fitness_func(best_individual))
