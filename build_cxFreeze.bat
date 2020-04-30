Rem create an empty file __init__.py in the folder of mpl_toolkits library
Rem this is du that mpl_library is an named packages
Rem for more infos : 
Rem https://stackoverflow.com/questions/18596410/importerror-no-module-named-mpl-toolkits-with-maptlotlib-1-3-0-and-py2exe

cd "%cd"

Rem creation de l'executable
python "setup.py" build

Rem déplacement des images au bon endroit -> on recré la structure
cd build/exe.win-amd64-3.6
mkdir image
move logo_add.png image/
move logo_plot.png image/
move logo_validation.png image/
move icon.png image/
PAUSE