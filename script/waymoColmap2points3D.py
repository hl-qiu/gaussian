import numpy as np
from plyfile import PlyData, PlyElement


def storePly(path, xyz, rgb):
    # Define the dtype for the structured array
    dtype = [('x', 'f4'), ('y', 'f4'), ('z', 'f4'),
             ('nx', 'f4'), ('ny', 'f4'), ('nz', 'f4'),
             ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')]

    normals = np.zeros_like(xyz)

    elements = np.empty(xyz.shape[0], dtype=dtype)
    attributes = np.concatenate((xyz, normals, rgb), axis=1)
    elements[:] = list(map(tuple, attributes))

    # Create the PlyData object and write to file
    vertex_element = PlyElement.describe(elements, 'vertex')
    ply_data = PlyData([vertex_element])
    ply_data.write(path)


def fetchPly(path):
    plydata = PlyData.read(path)
    vertices = plydata['vertex']
    positions = np.vstack([vertices['x'], vertices['y'], vertices['z']]).T
    # 手动生成rgb
    colors = np.ones_like(positions)
    return positions, colors


if __name__ == '__main__':
    path = '/data/qhl/data/waymo/seg1/sparse/0/points3D_before.ply'
    # 读取ply的xyz
    xyz, colors = fetchPly(path)

    # 调用storePly生成完整ply文件
    storePly('/data/qhl/data/waymo/seg1/sparse/0/points3D.ply', xyz, colors)
