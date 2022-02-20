import numpy as np


def psi1s(x,y,z):
    r,theta,phi = convertSpherical(x,y,z)
    return psi1sSpherical(r,theta,phi)

def psi1sSpherical(r,theta,phi):
    coeff = 1 / np.sqrt(np.pi)
    expon = np.exp(-r)
    return coeff * expon

def psi2px(x,y,z):
    r,theta,phi = convertSpherical(x,y,z)
    return psi2pxSpherical(r,theta,phi)

def psi2pxSpherical(r,theta,phi):
    coeff = (1 / (4 * np.sqrt(2 * np.pi))) * r * np.sin(theta) * np.cos(phi)
    expon = np.exp(-r / 2)
    return coeff * expon

def convertSpherical(x,y,z):
    r = np.sqrt(x*x+y*y+z*z)
    theta = np.arccos(z/r)
    phi = convertPhi(x,y,z)
    return (r,theta,phi)

def convertPhi(x,y,z):
    if x > 0.0:
        return np.arctan(y/x)
    elif x < 0.0 and y >= 0.0:
        return np.arctan(y/x) + np.pi
    elif x < 0.0 and y < 0.0:
        return np.arctan(y/x) - np.pi
    elif x == 0.0 and y > 0:
        return np.pi / 2
    elif x == 0.0 and y < 0:
        return - np.pi/2
    else:
        return -1
