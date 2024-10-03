class Molecule:
    # ... (Existing __init__ remains unchanged)

    def simulate_step(self, step, dt):
        # ... existing simulate_step code
        pass  # Remove existing implementation

    def to_dict(self):  # Add the to_dict() method
        return {
            "molecule_id": id(self),
            "atoms": [atom.to_dict() for atom in self.atoms],
            "electrons": [electron.to_dict() for electron in self.electrons]
        }
