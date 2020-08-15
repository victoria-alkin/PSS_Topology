import sys
import vtk
from PyQt5 import QtCore, QtGui
from PyQt5 import Qt
from PyQt5.QtWidgets import QShortcut ,  QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QLineEdit, QGridLayout, QMessageBox
from vtk.qt.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor
import csv
import json
import os
import pickle
import pandas as pd
import numpy as np
import trimesh
import pyglet
import meshparty
from meshparty import trimesh_io, trimesh_vtk
import sklearn
from sklearn.cluster import DBSCAN

# count and visualize the number of openings in a mesh

#shaft 1
shaft1 = trimesh.exchange.load.load_mesh(r'data\meshes\EXPT1\134025041739\spine_432.off')
shaft1broken = trimesh.repair.broken_faces(shaft1)
shaft1openings = shaft1.submesh([shaft1broken], append=True)
#shaft1_actor = trimesh_vtk.mesh_actor(shaft1)
#trimesh_vtk.render_actors([shaft1_actor])
#shaft1openings_actor = trimesh_vtk.mesh_actor(shaft1openings)
#trimesh_vtk.render_actors([shaft1openings_actor])
print(shaft1openings.body_count)

#shaft 2
shaft2 = trimesh.exchange.load.load_mesh(r'data\meshes\EXPT1\137732862037\spine_1676.off')
shaft2broken = trimesh.repair.broken_faces(shaft2)
shaft2openings = shaft2.submesh([shaft2broken], append=True)
#shaft2_actor = trimesh_vtk.mesh_actor(shaft2,color=(0,0,1),opacity=0.2)
#trimesh_vtk.render_actors([shaft2_actor])
shaft2openings_actor = trimesh_vtk.mesh_actor(shaft2openings,color=(0,0,1),opacity=0.2)
trimesh_vtk.render_actors([shaft2openings_actor])
print(shaft2openings.body_count)

#spine 1
spine1 = trimesh.exchange.load.load_mesh(r'data\meshes\EXPT1\134025041739\spine_599.off')
spine1broken = trimesh.repair.broken_faces(spine1)
spine1openings = spine1.submesh([spine1broken], append=True)
#spine1_actor = trimesh_vtk.mesh_actor(spine1)
#trimesh_vtk.render_actors([spine1_actor])
#spine1openings_actor = trimesh_vtk.mesh_actor(spine1openings)
#trimesh_vtk.render_actors([spine1openings_actor])
print(spine1openings.body_count)

#spine 2
spine2 = trimesh.exchange.load.load_mesh(r'data\meshes\EXPT1\272084747594\spine_279.off')
spine2broken = trimesh.repair.broken_faces(spine2)
spine2openings = spine2.submesh([spine2broken], append=True)
#spine2_actor = trimesh_vtk.mesh_actor(spine2)
#trimesh_vtk.render_actors([spine2_actor])
#spine2openings_actor = trimesh_vtk.mesh_actor(spine2openings)
#trimesh_vtk.render_actors([spine2openings_actor])
print(spine2openings.body_count)