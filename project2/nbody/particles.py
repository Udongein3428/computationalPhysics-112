import numpy as np
import matplotlib.pyplot as plt


class Particles:
    """
    Particle class to store particle properties
    """
    
    def __init__(self, N:int=0):
    
        self.nparticles = N
        self._masses = np.ones((N,1))
        self._positions = np.zeros((N,3))
        self._velocities = np.zeros((N,3))
        self._accelerations = np.zeros((N,3))
        self._tags = N
        self._times = 0.0
        return
    
    @property
    def masses(self):
        return self._masses
    
    @property
    def positions(self):
        return self._positions
    
    @property
    def velocities(self):
        return self._velocities
        
    @property
    def accelerations(self):
        return self.accelerations
    
    @property
    def tags(self):
        return self._tags
    
    @property
    def times(self):
        return self._times
        
    @masses.setter
    def masses(self, m: np.ndarray):
        if m.shape != np.zeros((self.nparticles,1)).shape:
            print("the number of particles is not match.")
            raise ValueError
        self._masses = m
        return
    
    @positions.setter
    def positions(self, pos: np.ndarray):
        if pos.shape != np.zeros((self.nparticles,3)).shape:
            print("the number of particles is not match.")
            raise ValueError    
        self._positions = pos
        return
    
    @velocities.setter
    def velocities(self, vel: np.ndarray):
        if vel.shape != np.zeros((self.nparticles,3)).shape:
            print("Number of particles does not match!")
            raise ValueError
        
        self._velocities = vel
        return
    
    @accelerations.setter
    def accelerations(self, acc: np.ndarray):
        if acc.shape != np.zeros((self.nparticles,3)).shape:
            print("Number of particles does not match!")
            raise ValueError
        
        self._accelerations = acc
        return
    
    @tags.setter
    def tags(self, tag: np.ndarray):
        if tag.shape != np.arange(self.nparticles).shape:
            print("Number of particles does not match!")
            raise ValueError
        
        self._tags = tag
        return
    
    
    
    pass

