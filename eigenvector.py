import numpy as np

class Eigenvector:
    def __init__(self, wavefunction_coefficients):
        self.coefficients = np.array(wavefunction_coefficients)  # Store as numpy array

    def calculate_energy(self, hamiltonian):
        eigenvalue = hamiltonian.dot(self.coefficients)  # Use NumPy's dot product
        return eigenvalue

    def calculate_probability_density(self, position):
        probability_density = np.abs(self.coefficients[position]) ** 2
        return probability_density

    # ... other methods for Eigenvector ...

    def to_dict(self):
        return {
            "coefficients": self.coefficients.tolist()
        }
