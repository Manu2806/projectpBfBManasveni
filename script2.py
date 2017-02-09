#!/usr/bin/env python
emptylist = []
#assign an empty list to store extracted values of x,y,z

variablex = "filename"
#input

variablex = raw_input("enter file name: ")
# multiple inputs by user from files downloaded using shell script

#condition to search for atomic coordinates in columns of ATOM data
with open(proteinseq) as protein:
    for lines in protein:
        if "ATOM   " in lines:
            lines = lines.split() #to split the lines of ATOM into lines seperated by white space
            emptylist.append(map(float, lines[entercolumn])) #append() function combines the coordinate data from 3 columns and assignes to list myprotein #float() converts all non-float values to float #map 


import matplotlib.pyplot as plt #pyplot is a 2D/3D plotting tool
from mpl_toolkits.mplot3d import Axes3D #axes3d creates a 3D axes

x,y,z = zip(*emptylist)
#zip function when used with * used to seperate lists of equal lengths into individual lists
#here coordinate data will get assigned to respective lists 

fig = plt.figure()
ax = Axes3D(fig)

ax.plot(x,y,z, "o") #o is a default marker 

plt.show()
