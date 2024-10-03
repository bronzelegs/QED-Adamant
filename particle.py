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


class Particle:
    def __init__(self, mass, position, velocity, charge=0):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.charge = charge


def update_position(self, dt):
    self.position += self.velocity * dt


def update_velocity(self, force, dt):
    acceleration = force / self.mass
    self.velocity += acceleration * dt


def calculate_kinetic_energy(self):
    return 0.5 * self.mass * np.dot(self.velocity, self.velocity)


class Particle:
    def __init__(self, mass, position, velocity, atomic_number=None):
        # ... existing code ...
        self.atomic_number = atomic_number if atomic_number is not None else 0
