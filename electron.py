import numpy as np

from eigenvector import Eigenvector


class Electron:
    def __init__(self, mass, position, velocity, charge=-1, wavefunction_coefficients=None):
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.charge = charge
        if wavefunction_coefficients is not None:  # Corrected conditional check
            self.eigenvector = Eigenvector(wavefunction_coefficients)

    def update(self, dt, atoms):  # Add atoms as a parameter
        self.position += self.velocity * dt

        # Calculate force due to atoms
        for atom in atoms:  # Iterate over the provided atoms list
            force = atom.calculate_force_on_electron(self)
            self.velocity += force * dt / self.mass
