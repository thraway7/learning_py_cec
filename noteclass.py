# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 12:29:48 2020

@author: CEC
"""

class Elevator:
    
    def __init__(self, floor_numbers, floor_types):
        self._floor_numbers = floor_numbers
        self._floor_types = floor_types
        self._number_to_type_dict = dict(zip(floor_numbers, floor_types)) 
        self._type_to_number_dict = dict(zip(floor_types, floor_numbers)) 
        
    def ask_which_floor(self, floor_type):    
        if floor_type in self._floor_types:
            print('The {} floor is the number: {}.'.format(floor_type, self._type_to_number_dict[floor_type]))
        else:
            print('There is no {} floor in this building.'.format(floor_type))
    
    def go_to_floor(self, floor_number):
        if floor_number in self._floor_numbers:
            print('Going to {} floor!'.format(self._number_to_type_dict[floor_number]))
        else:
            print('There is no floor number {} in this building.'.format(floor_number))
            
el=Elevator(floor_numbers, floor_types)
el.go_to_floor(1)   