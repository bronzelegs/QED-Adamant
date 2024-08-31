class Particle:
    def __init__(self, mass, position, velocity):
        self.mass = mass
        self.position = position
        self.velocity = velocity

    def update_position(self,   
 dt):
        self.position += self.velocity * dt

    def update_velocity(self, force, dt):
        acceleration = force / self.mass
        self.velocity += acceleration * dt

    def calculate_kinetic_energy(self):
        return 0.5 * self.mass * np.dot(self.velocity, self.velocity)

