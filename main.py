import qutip as qt


import Particle
import Atom
import Molecule
import DataStoreObserver
import Simulation


# Example usage
atom1 = Atom(1, 1.0, [0, 0, 0], [1, 0, 0])
atom2 = Atom(8, 16.0, [1, 1, 0], [0, 1, 0])

molecule = Molecule([atom1, atom2])
simulation = Simulation(molecule)

simulation.run(100, 0.1)
