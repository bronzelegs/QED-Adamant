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


import threading

class Electron:
    def __init__(self, mass, position, velocity, charge=-1, wavefunction_coefficients=None):
        self.mass = mass
        self.position = np.array(position)
        self.velocity = np.array(velocity)
        self.charge = charge
        if wavefunction_coefficients is not None:
            self.eigenvector = Eigenvector(wavefunction_coefficients)

    lock = threading.Lock()  # Add a lock to protect the update method

    def update(self, dt, atoms):
        with self.lock:  # Acquire the lock before updating
            self.position += self.velocity * dt
            # ... other update logic (force calculations, etc.)

        # Calculate force due to atoms
        for atom in atoms:
            force = atom.calculate_force_on_electron(self)
            self.velocity += force * dt / self.mass
        # ... (Add other physics updates for the electron here)

    def to_dict(self):
        electron_data = {
            "electron_id": id(self),
            "mass": self.mass,
            "position": self.position.tolist(),
            "velocity": self.velocity.tolist(),
            "charge": self.charge,
            # ... any other electron properties
        }
        if hasattr(self, "eigenvector"):
            electron_data["eigenvector"] = self.eigenvector.to_dict()
        return electron_data


import numpy as np
from eigenvector import Eigenvector
import threading


class Electron:
    # ... (Existing code remains unchanged)

    lock = threading.Lock()  # Add a lock to protect the update method

    def update(self, dt, atoms):
        with self.lock:  # Acquire the lock before updating
            self.position += self.velocity * dt
            # ... other update logic (force calculations, etc.)

    # ... (Other methods remain unchanged)
