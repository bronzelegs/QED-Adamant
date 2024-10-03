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

from constants import COULOMB_CONSTANT


class Atom:
    def __init__(self, atomic_number, mass, position, velocity, charge=0):
        self.atomic_number = atomic_number
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.charge = charge
        self.electrons = []

    lock = threading.Lock()  # Add a lock to protect the update method

    def update(self, dt):
        with self.lock:  # Acquire the lock before updating
            self.position += self.velocity * dt
            # ... other update logic
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
