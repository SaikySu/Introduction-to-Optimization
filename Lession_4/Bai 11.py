import numpy as np

class Ant:
    def __init__(self, n_cities):
        self.path = []
        self.visited = [False] * n_cities
        self.distance = 0.0
    def visit_city(self, city, distance_matrix):
        if len(self.path) > 0:
            self.distance += distance_matrix[self.path[-1]][city]
        self.path.append(city)
        self.visited[city] = True
    def path_length(self, distance_matrix):
        return self.distance + distance_matrix[self.path[-1]][self.path[0]]

def ant_colony_optimization(distance_matrix, n_ants=10, n_iterations=100, alpha=1, beta=5, rho=0.1, Q=10):
    n_cities = len(distance_matrix)
    pheromone = np.ones((n_cities, n_cities))/n_cities
    best_path = None
    best_length = float('inf')

    for _ in range(n_iterations):
        ants = [Ant(n_cities) for _ in range(n_ants)]

        for ant in ants:
            ant.visit_city(np.random.randint(n_cities), distance_matrix)

            for _ in range(n_cities - 1):
                current_city = ant.path[-1]
                probabilities = []

                for next_city in range(n_cities):
                    if not ant.visited[next_city]:
                        pheromone_level = pheromone[current_city][next_city]**alpha
                        heuristic_value = (1.0/distance_matrix[current_city][next_city])**beta
                        probabilities.append(pheromone_level * heuristic_value)
                    else:
                        probabilities.append(0)
                probabilities = np.array(probabilities)
                probabilities /= probabilities.sum()
                next_city = np.random.choice(range(n_cities), p=probabilities)
                ant.visit_city(next_city, distance_matrix)

        for ant in ants:
            length = ant.path_length(distance_matrix)
            if length < best_length:
                best_length = length
                best_path = ant.path

        pheromone *= (1-rho)
        for ant in ants:
            contribution = Q/ant.path_length(distance_matrix)
            for i in range(n_cities):
                pheromone[ant.path[i]][ant.path[(i+1)%n_cities]] += contribution
    return best_path, best_length
distance_matrix = np.array([[0, 2, 2, 5, 7],
                            [2, 0, 4, 8, 2],
                            [2, 4, 0, 1, 3],
                            [5, 8, 1, 0, 6],
                            [7, 2, 3, 6, 0]
])

#Aco - Toi uu hoa dan kien
best_path, best_length = ant_colony_optimization(distance_matrix)
#Xuat ra duong di va do dai duong di toi uu
print("Đường đi ngắn nhất: ", best_path)
print("Độ dài đường đi tối uư: ", best_length)
