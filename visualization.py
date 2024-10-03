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


class VisualizationData:
    def __init__(self):
        self.electron_positions = []
        self.atom_positions = []
        self.time_steps = []

    def from_dict(self, simulation_data):  # Correct method name, no data parameter
        self.electron_positions = []
        self.atom_positions = []
        self.time_steps = simulation_data['time_steps']  # Update time steps
        for molecule_data in simulation_data.get('molecules', []):
            for atom_data in molecule_data.get('atoms', []):
                self.atom_positions.append(atom_data['position'])
            for electron_data in molecule_data.get('electrons', []):
                self.electron_positions.append(electron_data['position'])
