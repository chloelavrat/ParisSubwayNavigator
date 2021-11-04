#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################
# Institut Villebon, UE 3.1
# Projet : mon_viva_navigo
# Auteur : C.Lavrat
# Date de creation : 27/12/15
# Date de derniere modification : 19/01/16
##############################################
import sys
sys.path.append("..")

from Line import *
from Station import *

def main():
    """
    all the test of the class Line
    """
    #Header 
    print ("*******************")
    print (" Line module test")
    print ("*******************")
    #creation of 5 stations
    A = Station("A",[1.,0.])
    B = Station("B",[2.,0.])
    C = Station("C",[3.,0.])
    D = Station("D",[4.,0.])
    E = Station("E",[5.,0.])
    Line_1 = Line([A,B,C,D,E],"underground", "Line_1")
    ############################################################################
    #                           Declaration TEST                               #
    ############################################################################
    assert Line_1.station == [A,B,C,D,E]
    print("self.station    OK")
    assert Line_1.mode == "underground"
    print("self.mode       OK")
    assert Line_1.name == "Line_1"
    print("self.name       OK")
    ############################################################################
    #                               Message end                                #
    ############################################################################
    print("Line is         OK")
    print("*******************")
    print(Line_1._repr_())
    
if __name__ == '__main__':
    main()
