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

# Read data from labels file and create dataframe
labels_file = open(r"labels.pkl","rb")
labels_db = pickle.load(labels_file)
labels_file.close()
labels_df = pd.DataFrame(labels_db)

# Create dataframes for each label
spine1_df = pd.DataFrame()
shaft2_df = pd.DataFrame()
soma3_df = pd.DataFrame()
proximalprocess4_df = pd.DataFrame()
partialspine5_df = pd.DataFrame()
partialshaft6_df = pd.DataFrame()
mergedspine7_df = pd.DataFrame()
mergedshaft8_df = pd.DataFrame()
unknown9_df = pd.DataFrame()
for i in range(labels_df.shape[0]):
    if labels_df.iloc[i,4] == '1':
        spine1_df = spine1_df.append(labels_df.iloc[i])
    if labels_df.iloc[i,4] == '2':
        shaft2_df = shaft2_df.append(labels_df.iloc[i])
    if labels_df.iloc[i,4] == '3':
        soma3_df = soma3_df.append(labels_df.iloc[i])
    if labels_df.iloc[i,4] == '4':
        proximalprocess4_df = proximalprocess4_df.append(labels_df.iloc[i])
    if labels_df.iloc[i,4] == '5':
        partialspine5_df = partialspine5_df.append(labels_df.iloc[i])
    if labels_df.iloc[i,4] == '6':
        partialshaft6_df = partialshaft6_df.append(labels_df.iloc[i])
    if labels_df.iloc[i,4] == '7':
        mergedspine7_df = mergedspine7_df.append(labels_df.iloc[i])
    if labels_df.iloc[i,4] == '8':
        mergedshaft8_df = mergedshaft8_df.append(labels_df.iloc[i])
    if labels_df.iloc[i,4] == '9':
        unknown9_df = unknown9_df.append(labels_df.iloc[i])

# For each dataframe, create a list of opening counts
spine1openings = []
for i in range(spine1_df.shape[0]):
    full_path = spine1_df.iloc[i,0]
    start = full_path.find("EXPT1/")
    end = full_path.find("/spine")
    end2 = full_path.find("_ae_model")
    id = full_path[start+6 : end]
    filenumber = full_path[end+7 : end2]
    filename = r'data\meshes\EXPT1' + '/' + id + '/' + 'spine_' + filenumber + '.off'
    spine_mesh = trimesh.exchange.load.load_mesh(filename)
    spinemesh_broken = trimesh.repair.broken_faces(spine_mesh)
    spinemesh_openings = spine_mesh.submesh([spinemesh_broken], append=True)
    spine1openings.append(spinemesh_openings.body_count)
spine1_df['Openings'] = spine1openings
spine1_df.to_csv(r'spine_openings.csv')

shaft2openings = []
for i in range(shaft2_df.shape[0]):
    full_path = shaft2_df.iloc[i,0]
    start = full_path.find("EXPT1/")
    end = full_path.find("/spine")
    end2 = full_path.find("_ae_model")
    id = full_path[start+6 : end]
    filenumber = full_path[end+7 : end2]
    filename = r'data\meshes\EXPT1' + '/' + id + '/' + 'spine_' + filenumber + '.off'
    shaft_mesh = trimesh.exchange.load.load_mesh(filename)
    shaftmesh_broken = trimesh.repair.broken_faces(shaft_mesh)
    shaftmesh_openings = shaft_mesh.submesh([shaftmesh_broken], append=True)
    shaft2openings.append(shaftmesh_openings.body_count)
shaft2_df['Openings'] = shaft2openings
shaft2_df.to_csv(r'shaft_openings.csv')

proximalprocess4openings = []
for i in range(proximalprocess4_df.shape[0]):
    full_path = proximalprocess4_df.iloc[i,0]
    start = full_path.find("EXPT1/")
    end = full_path.find("/spine")
    end2 = full_path.find("_ae_model")
    id = full_path[start+6 : end]
    filenumber = full_path[end+7 : end2]
    filename = r'data\meshes\EXPT1' + '/' + id + '/' + 'spine_' + filenumber + '.off'
    proximalprocess_mesh = trimesh.exchange.load.load_mesh(filename)
    proximalprocessmesh_broken = trimesh.repair.broken_faces(proximalprocess_mesh)
    proximalprocessmesh_openings = proximalprocess_mesh.submesh([proximalprocessmesh_broken], append=True)
    proximalprocess4openings.append(proximalprocessmesh_openings.body_count)
proximalprocess4_df['Openings'] = proximalprocess4openings
proximalprocess4_df.to_csv(r'proximalprocess_openings.csv')

partialspine5openings = []
for i in range(partialspine5_df.shape[0]):
    full_path = partialspine5_df.iloc[i,0]
    start = full_path.find("EXPT1/")
    end = full_path.find("/spine")
    end2 = full_path.find("_ae_model")
    id = full_path[start+6 : end]
    filenumber = full_path[end+7 : end2]
    filename = r'data\meshes\EXPT1' + '/' + id + '/' + 'spine_' + filenumber + '.off'
    partialspine_mesh = trimesh.exchange.load.load_mesh(filename)
    partialspinemesh_broken = trimesh.repair.broken_faces(partialspine_mesh)
    partialspinemesh_openings = partialspine_mesh.submesh([partialspinemesh_broken], append=True)
    partialspine5openings.append(partialspinemesh_openings.body_count)
partialspine5_df['Openings'] = partialspine5openings
partialspine5_df.to_csv(r'partialspine_openings.csv')

partialshaft6openings = []
for i in range(partialshaft6_df.shape[0]):
    full_path = partialshaft6_df.iloc[i,0]
    start = full_path.find("EXPT1/")
    end = full_path.find("/spine")
    end2 = full_path.find("_ae_model")
    id = full_path[start+6 : end]
    filenumber = full_path[end+7 : end2]
    filename = r'data\meshes\EXPT1' + '/' + id + '/' + 'spine_' + filenumber + '.off'
    partialshaft_mesh = trimesh.exchange.load.load_mesh(filename)
    partialshaftmesh_broken = trimesh.repair.broken_faces(partialshaft_mesh)
    partialshaftmesh_openings = partialshaft_mesh.submesh([partialshaftmesh_broken], append=True)
    partialshaft6openings.append(partialshaftmesh_openings.body_count)
partialshaft6_df['Openings'] = partialshaft6openings
partialshaft6_df.to_csv(r'partialshaft_openings.csv')

mergedspine7openings = []
for i in range(mergedspine7_df.shape[0]):
    full_path = mergedspine7_df.iloc[i,0]
    start = full_path.find("EXPT1/")
    end = full_path.find("/spine")
    end2 = full_path.find("_ae_model")
    id = full_path[start+6 : end]
    filenumber = full_path[end+7 : end2]
    filename = r'data\meshes\EXPT1' + '/' + id + '/' + 'spine_' + filenumber + '.off'
    mergedspine_mesh = trimesh.exchange.load.load_mesh(filename)
    mergedspinemesh_broken = trimesh.repair.broken_faces(mergedspine_mesh)
    mergedspinemesh_openings = mergedspine_mesh.submesh([mergedspinemesh_broken], append=True)
    mergedspine7openings.append(mergedspinemesh_openings.body_count)
mergedspine7_df['Openings'] = mergedspine7openings
mergedspine7_df.to_csv(r'mergedspine_openings.csv')

mergedshaft8openings = []
for i in range(mergedshaft8_df.shape[0]):
    full_path = mergedshaft8_df.iloc[i,0]
    start = full_path.find("EXPT1/")
    end = full_path.find("/spine")
    end2 = full_path.find("_ae_model")
    id = full_path[start+6 : end]
    filenumber = full_path[end+7 : end2]
    filename = r'data\meshes\EXPT1' + '/' + id + '/' + 'spine_' + filenumber + '.off'
    mergedshaft_mesh = trimesh.exchange.load.load_mesh(filename)
    mergedshaftmesh_broken = trimesh.repair.broken_faces(mergedshaft_mesh)
    mergedshaftmesh_openings = mergedshaft_mesh.submesh([mergedshaftmesh_broken], append=True)
    mergedshaft8openings.append(mergedshaftmesh_openings.body_count)
mergedshaft8_df['Openings'] = mergedshaft8openings
mergedshaft8_df.to_csv(r'mergedshaft_openings.csv')