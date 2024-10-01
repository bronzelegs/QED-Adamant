# atom.py
from constants import COULOMB_CONSTANT  # Import Coulomb's constant


class Atom(Molecule):
    def __init__(self, atomic_number, mass, position, velocity, charge=0):
        super().__init__()
        self.atomic_number = atomic_number
        self.mass = mass
        self.position = np.array(position)  # Store position as a NumPy array
        self.velocity = np.array(velocity)  # Store velocity as a NumPy array
        self.charge = charge

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


# electron.py
import numpy as np
from eigenvector import Eigenvector


class Electron(Atom):
    def __init__(self, mass, position, velocity, charge=-1, wavefunction_coefficients=None):
        super().__init__()
        self.mass = mass
        self.position = np.array(position)  # Store position as a NumPy array
        self.velocity = np.array(velocity)  # Store velocity as a NumPy array
        self.charge = charge
        if wavefunction_coefficients is not None:
            self.eigenvector = Eigenvector(wavefunction_coefficients)

    def update(self, dt):
        # Implement the update logic for the electron based on forces and physics
        # For example, you might update position and velocity here:
        self.position += self.velocity * dt  # Update position based on velocity
        # ... (Other updates based on forces or other calculations)

        # Calculate force due to atoms
        for atom in self.atoms:
            force = atom.calculate_force_on_electron(self)
            self.velocity += force * dt / self.mass  # Apply force using Newton's second law

        # ... (other updates)
