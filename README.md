# PSS_Topology
Using PSS mesh topology to count the number of openings and distinguish spines form shafts

bodycount.py - program to count (and visualize) the number of openings in a mesh (with four examples)

openings.py - for a list of classified PSS meshes (in this case, the 1000 classified points from PSS machine learning model training), creates dataframe for each PSS class (spine, shaft, soma, proximal process, partial spine, partial shaft, merged spine, merged shaft) with number of openings for each PSS in that class

3Dplot.py - code to create a 3D plot with X and Y coordinates being the (x,y) coordinates of the 2D UMAP "creature" and the Z coordinate as number of openings

quantized3Dplot.py - code to create a 3D plot with X and Y coordinates being the (x,y) coordinates of the 2D UMAP "creature" and the Z coordinate as number of openings with three levels - one opening, two openings, and greater than two openings