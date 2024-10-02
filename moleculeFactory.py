import numpy as np

from atom import Atom
from electron import Electron
from molecule import Molecule


def create_molecules():
    """Creates a list of Molecule objects."""

    molecules = []

    # Create a hydrogen atom
    atomic_number = 1
    mass = 1.67e-27  # kg (mass of a proton)
    position = np.array([0.0, 0.0, 0.0])  # Initial position at the origin
    velocity = np.array([0.0, 0.0, 0.0])  # Initial velocity is zero
    charge = 1.6e-19  # C (charge of a proton)
    hydrogen_atom = Atom(atomic_number, mass, position, velocity, charge)

    # Create an electron
    electron_mass = 9.11e-31  # kg
    electron_position = np.array([0.529e-10, 0.0, 0.0])  # Example initial position (Bohr radius)
    electron_velocity = np.array([0.0, 0.0, 0.0])  # Initial velocity is zero
    electron_charge = -1.6e-19  # C
    electron = Electron(electron_mass, electron_position, electron_velocity, electron_charge)

    # Add the electron to the atom
    hydrogen_atom.add_electron(electron)

    # Create a molecule and add the atom
    molecule = Molecule([hydrogen_atom], [electron])  # List of atoms, list of electrons
    molecules.append(molecule)

    return molecules
