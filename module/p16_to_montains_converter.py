from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

file_import = open('ME-SSEP1-270-sensperpendiculaire.txt', 'r')
lignes = file_import.readlines()
file_import.close()

file_export = open('EXPORT_NiW2DDCL2.txt', 'w')

# repr is used to visualise specials caracters
#print(repr(file.readlines()[15]))

# extraction of first data
for i in range(11):
    line = lignes[i]
    line_l = line.split('\t')
    if line_l[0] == 'Number of Points':
        nb_points = int(line_l[1])
    elif line_l[0] == 'Number of Traces':
        nb_traces = int(line_l[1])
    elif line_l[0] == 'X-Resolution':
        x_res = int(float(line_l[1]))
    elif line_l[0] == 'Y-Resolution':
        y_res = int(float(line_l[1]))

l_x_plot = []
l_y_plot = []
l_z_plot = []

for i in range(nb_points):
    #print(i, '=>', lignes[11+i])
    ligne = lignes[11+i].split('\t')[1::] # delete first number which is line number
    for j, point in enumerate(ligne):
        #print('point', point)
        X = x_res*i
        Y = y_res*j
        Z = float(point) # TODO conversion amstrum->micron
        new_line = str(X) + ',' + str(Y) + ',' + str(Z) + '\n'

        file_export.write(new_line) #write new line
        l_x_plot.append(X)
        l_y_plot.append(Y)
        l_z_plot.append(Z)

file_export.close()

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_trisurf(np.array(l_x_plot), np.array(l_y_plot), np.array(l_z_plot), cmap=cm.coolwarm, linewidth=0.2, antialiased=True)

plt.savefig('temp_profile.png')
#plt.show()
