import os
import xml.etree.ElementTree as ET

'''Lendo o XML'''

arquivo = "entrada.xml"
tree =  ET.parse(arquivo)

root = tree.getroot()

#viewport
#vpmin
for vpmin in root.findall('viewport/vpmin'):
    x_vpmin = vpmin.get('x')
    y_vpmin = vpmin.get('y')
    print(x_vpmin, y_vpmin)
    print('\n')

#vpmax
for vpmax in root.findall('viewport/vpmax'):
    x_vpmax = vpmax.get('x')
    y_vpmax = vpmax.get('y')
    print(x_vpmax, y_vpmax)
    print('\n')

#window
#wmin
for wmin in root.findall('window/wmin'):
    x_wmin = wmin.get('x')
    y_wmin = wmin.get('y')
    z_wmin = wmin.get('z')
    print(x_wmin, y_wmin, z_wmin)
    print('\n')
    
#wmax
for wmax in root.findall('window/wmax'):
    x_wmax = wmax.get('x')
    y_wmax = wmax.get('y')
    z_wmax = wmax.get('z')
    print(x_wmax, y_wmax, z_wmax)
    print('\n')
    
#ponto
xp = []
yp = []
zp = []

for ponto in root.findall('ponto'):
    for i in range():
        xp[i].append(ponto.get('x'))
        yp[i].append(ponto.get('y'))
        zp[i].append(ponto.get('z'))
        
        print(xp[i], yp[i], zp[i])
        print('\n')

#reta
