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
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Create dataframes for each PSS type
spine1_df = pd.read_csv(r'spine_openings.csv')
shaft2_df = pd.read_csv(r'shaft_openings.csv')
proximalprocess4_df = pd.read_csv(r'proximalprocess_openings.csv')
partialspine5_df = pd.read_csv(r'partialspine_openings.csv')
partialshaft6_df = pd.read_csv(r'partialshaft_openings.csv')
mergedspine7_df = pd.read_csv(r'mergedspine_openings.csv')
mergedshaft8_df = pd.read_csv(r'mergedshaft_openings.csv')

print(shaft2_df)
# Make 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

for i in range(len(spine1_df)):
    ax.scatter(spine1_df.iloc[i,4],spine1_df.iloc[i,5],spine1_df.iloc[i,6],c="red",s=20,alpha=0.1)
for i in range(len(shaft2_df)):
    ax.scatter(shaft2_df.iloc[i,4],shaft2_df.iloc[i,5],shaft2_df.iloc[i,6],c="limegreen",s=20,alpha=0.1)
for i in range(len(proximalprocess4_df)):
    ax.scatter(proximalprocess4_df.iloc[i,4],proximalprocess4_df.iloc[i,5],proximalprocess4_df.iloc[i,6],c="orange",s=20,alpha=0.1)
for i in range(len(partialspine5_df)):
    ax.scatter(partialspine5_df.iloc[i,4],partialspine5_df.iloc[i,5],partialspine5_df.iloc[i,6],c="lightcoral",s=20,alpha=0.1)
for i in range(len(partialshaft6_df)):
    ax.scatter(partialshaft6_df.iloc[i,4],partialshaft6_df.iloc[i,5],partialshaft6_df.iloc[i,6],c="palegreen",s=20,alpha=0.1)
for i in range(len(mergedspine7_df)):
    ax.scatter(mergedspine7_df.iloc[i,4],mergedspine7_df.iloc[i,5],mergedspine7_df.iloc[i,6],c="maroon",s=20,alpha=0.1)
for i in range(len(mergedshaft8_df)):
    ax.scatter(mergedshaft8_df.iloc[i,4],mergedshaft8_df.iloc[i,5],mergedshaft8_df.iloc[i,6],c="darkgreen",s=20,alpha=0.1)

ax.set_xlabel('X Coordinate')
ax.set_ylabel('Y Coordinate')
ax.set_zlabel('Number of Openings')

plt.show()