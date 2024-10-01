class Particle:
    def __init__(self, mass, position, velocity, charge=0):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.charge = charge


def update_position(self, dt):
    self.position += self.velocity * dt


def update_velocity(self, force, dt):
    acceleration = force / self.mass
    self.velocity += acceleration * dt


def calculate_kinetic_energy(self):
    return 0.5 * self.mass * np.dot(self.velocity, self.velocity)


class Particle:
    def __init__(self, mass, position, velocity, atomic_number=None):
        # ... existing code ...
        self.atomic_number = atomic_number if atomic_number is not None else 0
