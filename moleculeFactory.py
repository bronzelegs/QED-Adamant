# Copyright (c) 2024 Terrance Alan Davis
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


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
