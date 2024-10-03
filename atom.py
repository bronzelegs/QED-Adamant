import numpy as np

from constants import COULOMB_CONSTANT


class Atom:
    def __init__(self, atomic_number, mass, position, velocity, charge=0):
        self.atomic_number = atomic_number
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.charge = charge
        self.electrons = []

    def update(self, dt):
        self.position += self.velocity * dt
        # ... (Add other physics updates for the atom here, e.g., force calculations)

    def calculate_force_on_electron(self, electron):
        distance_vector = electron.position - self.position
        distance = np.linalg.norm(distance_vector)
        force_magnitude = COULOMB_CONSTANT * self.charge * electron.charge / distance ** 2
        force_direction = distance_vector / distance  # Ensure correct normalization
        force = force_magnitude * force_direction  # Calculate force vector
        return force


    def add_electron(self, electron):
        self.electrons.append(electron)

    def to_dict(self):
        return {
            "atom_id": id(self),
            "atomic_number": self.atomic_number,
            "mass": self.mass,
            "position": self.position.tolist(),
            "velocity": self.velocity.tolist(),
            "charge": self.charge,
            # ... any other relevant properties
        }
