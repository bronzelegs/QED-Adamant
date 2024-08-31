from particle import Particle

class Atom(Particle):
    def __init__(self, atomic_number, mass, position, velocity, charge=0):
        super().__init__(mass, position, velocity, charge)
        self.atomic_number = atomic_number

    def calculate_potential_energy(self, other_atoms):
        # Implement potential energy calculation based on inter atomic forces
        # ...
        return 0
