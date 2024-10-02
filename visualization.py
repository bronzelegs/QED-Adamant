# visualization.py
import mayavi.mlab as mlab


def visualize_data(visualization_data):
    mlab.clf()  # Clear previous plot
    mlab.points3d(visualization_data.electron_positions[:, 0],
                  visualization_data.electron_positions[:, 1],
                  visualization_data.electron_positions[:, 2],
                  scale_factor=0.1, color=(1, 0, 0))
    mlab.points3d(visualization_data.atom_positions[:, 0],
                  visualization_data.atom_positions[:, 1],
                  visualization_data.atom_positions[:, 2],
                  scale_factor=0.2, color=(0, 1, 0))
    mlab.show()
