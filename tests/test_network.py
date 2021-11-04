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
from PublicTransportationNetwork import *


def main():
    """
    all the test of the class PublicTransportationNetwork
    """
    #Header 
    print ("*****************************************")
    print (" PublicTransportationNetwork module test")
    print ("*****************************************")
    ############################################################################
    #                           Declaration TEST                               #
    ############################################################################
    graph_test = PublicTransportationNetwork("graph_test",1./500.)
    assert graph_test.name == "graph_test"
    print("self.name                       OK")
    assert graph_test.scale == 1./500.
    print("self.scale                      OK")
    assert graph_test.lines == []
    print("self.lines                      OK")
    ############################################################################
    #                           Creation TEST                               #
    ############################################################################
    graph_test.create_straight_line("line 1", ["S1","S2","S3","S4","S5"], 5., 0., 10., 0., "underground")
    graph_test.create_circular_line("circular 1", ["C1","C2","C3","C4","C5","C6","C7","C8"], 0., 0., 5., "kayak")
    assert len(graph_test.lines) == 2
    print("self.add_a_line                 OK")
    assert graph_test.lines[0].name == "line 1"
    assert graph_test.lines[0].mode == "underground"
    assert graph_test.lines[1].name == "circular 1"
    assert graph_test.lines[1].mode == "kayak"
    print("self.create_straight_line       OK")
    print("self.create_circular_line       OK")
    assert graph_test.lines[0].weight[("S1","S2")] == 0.0025
    ############################################################################
    #                                _plot_ TEST                               #
    ############################################################################
    graph_test.__plot__()
    print("self.__plot__()                 OK")
    ############################################################################
    #                               Message end                                #
    ############################################################################
    print("PublicTransportationNetwork is  OK")
    print("*****************************************")

def vic_test():
    """
    creation of a network as below, with random position.
    
    A---B---C---D---E   (line_1)
     \     / \     /
      \   /   \   /     (line_3)
       \ /     \ /
    F---G---H---I---J   (line_2)
    
    """
    
    print("\n")
    print("*******************************************************************")
    print("**************************   OTHER   ******************************")
    print("*******************************************************************")
    print("\n")
    ############################################################################
    #                                Methode 1                                 #
    ############################################################################
    #Creation of some stations
    A = Station("A",[1.,2.])
    B = Station("B",[2.,2.])
    C = Station("C",[3.,2.])
    D = Station("D",[4.,2.])
    E = Station("E",[5.,2.])
    F = Station("F",[1.,1.])
    G = Station("G",[2.,1.])
    H = Station("H",[3.,1.])
    I = Station("I",[4.,1.])
    J = Station("J",[5.,1.])
    #creation of the network    
    test_network = PublicTransportationNetwork("test_network",1./25000.)
    #creation of some line
    line_1 = {"mode": "underground","name": "line 1", "stations":[A,B,C,D,E]}
    line_2 = {"mode": "underground","name": "line 2", "stations":[F,G,H,I,J]}
    line_3 = {"mode": "underground","name": "line 3", "stations":[A,G,C,I,E]}
    test_network.add_a_line(line_1)
    test_network.add_a_line(line_2)
    test_network.add_a_line(line_3)
    #save of the network
    test_network.save("test_network")
    print(test_network.__str__())
    test_network.__plot__()
    
    #--------------------------------------------------------------------------#
    #we reset the network
    test_network.reset_network()
    #--------------------------------------------------------------------------#
    print("*******************************************************************")
    print("*************************   RESET_1   *****************************")
    print("*******************************************************************")
    ############################################################################
    #                                Methode 2                                 #
    ############################################################################
    #we load a new network (same as over)
    test_network.load("test_network")
    print(test_network.__str__())
    test_network.__plot__()

    #--------------------------------------------------------------------------#
    #we reset the network
    test_network.reset_network()
    #--------------------------------------------------------------------------#
    print("*******************************************************************")
    print("*************************   RESET_2   *****************************")
    print("*******************************************************************")
    ############################################################################
    #                                Methode 3                                 #
    ############################################################################
    #straight_line creation
    test_network.create_straight_line("straight", ["H","E","L","L","O"], 1., 2., 5., 2., "")
    test_network.create_circular_line("circular", ["W","O","R","L","D"], 0., 0., 5., "bus")
    print(test_network.__str__())
    test_network.__plot__()
    print("*******************************************************************")
    print("*************************   ALL OK   ******************************")
    print("*******************************************************************")

if __name__ == '__main__':
    main()
    vic_test()

