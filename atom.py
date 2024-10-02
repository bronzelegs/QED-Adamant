import numpy as np

from constants import COULOMB_CONSTANT  # Import Coulomb's constant


class Atom:
    def __init__(self, atomic_number, mass, position, velocity, charge=0):
        self.atomic_number = atomic_number
        self.mass = mass
        self.position = np.array(position)  # Store position as a NumPy array
        self.velocity = np.array(velocity)  # Store velocity as a NumPy array
        self.charge = charge
        self.electrons = []  # Initialize list of electrons

    def update(self, dt):
        # Implement the update logic for the atom based on forces and physics
        # For example, you might update position and velocity here:
        self.position += self.velocity * dt  # Update position based on velocity
        # ... (Other updates based on forces or other calculations)

    def calculate_force_on_electron(self, electron):
        """Calculates the electrostatic force between the atom and an electron."""
        distance_vector = electron.position - self.position
        distance = np.linalg.norm(distance_vector)
        force_magnitude = COULOMB_CONSTANT * self.charge * electron.charge / distance ** 2
        force_direction = distance_vector / distance
        force = force_magnitude * force_direction
        return force

    def add_electron(self, electron):
        self.electrons.append(electron)
