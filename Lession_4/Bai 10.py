#Tối ưu hóa bầy đàn
import numpy as np
def rastrigin(x):
    return 10*len(x)+sum([(xi**2-10*np.cos(2*np.pi*xi)) for xi in x])
class Particle:
    def __init__(self, bounds):
        self.position = np.random.uniform(bounds[:, 0],bounds[:, 1], len(bounds))
        self.velocity = np.random.uniform(-1, 1, len(bounds))
        self.pbest_position = self.position.copy()
        self.pbest_value = float('inf')
    def update_velocity(self, pbest_position, w=0.5, c1=1.0, c2 = 1.5):
        r1 = np.random.rand(len(self.position))
        r2 = np.random.rand(len(self.position))
        cognitive_velocity = c1 * r1 * (self.pbest_position - self.position)
        social_velocity = c2 * r2 * (pbest_position - self.position)
        self.velocity = w*self.velocity+cognitive_velocity+social_velocity
    def update_position(self, bounds):
        self.position += self.velocity
        self.position = np.clip(self.position, bounds[:, 0], bounds[:, 1])
def particle_swarm_optimization(objecttive_func, bounds, n_particles=30, max_iter=100 ):
    particles = [Particle(bounds) for _ in range(n_particles)]
    gbest_position = np.random.uniform(bounds[:, 0], bounds[:, 1], len(bounds))
    gbest_value = float('inf')
    for _ in range(max_iter):
        for particle in particles:
            fitness = objecttive_func(particle.position)
            if fitness < particle.pbest_value:
                particle.pbest_value = fitness
                particle.gbest_position = particle.position.copy()
            if fitness < gbest_value:
                gbest_value = fitness
                gbest_position = particle.position.copy()

        for particle in particles:
            particle.update_velocity(gbest_position)
            particle.update_position(bounds)
    return gbest_position, gbest_value
bounds = np.array([[-5.12,5.12]]*10)

#Tối ưu hóa bầy đàn
best_solution, best_fitness = particle_swarm_optimization(rastrigin, bounds, n_particles=30, max_iter=10000)

#Giai phap va the luc tot nhat
print("Giai phap tot nhat: ", best_solution)
print("The luc tot nhat: ", best_fitness)
























