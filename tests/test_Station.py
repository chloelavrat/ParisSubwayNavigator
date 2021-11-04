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

from Station import *

def main():
    """
    all the test of the class Station
    """
    #Header 
    print ("*******************")
    print ("Station module test")
    print ("*******************")
    #creation of 3 stations
    orsay_ville  = Station("Orsay Ville",[1.5,3.14],"RER B")
    orsay_ville2 = Station("Orsay",[1.5,3.14],"RER B")
    orsay = Station("Orsay Ville",[1.5,3.14],"RER B")
    gare_est = Station("Gare de l'est",[1.5,3.14],"RER P")
    ############################################################################
    #                           Declaration TEST                               #
    ############################################################################
    assert gare_est.name == "Gare de l'est"
    print("self.name       OK")
    assert gare_est.position == [1.5,3.14]
    print("self.position   OK")
    assert gare_est.in_line == "RER P"
    print("self.in_line    OK")
    ############################################################################
    #                                __eq__ TEST                               #
    ############################################################################
    assert orsay_ville._eq_(orsay) == True
    print("self._eq_       OK")
    ############################################################################
    #                                __lt__ TEST                               #
    ############################################################################
    A = Station("aaaab",[1.5,3.14],"RER B")
    B = Station("aaaaa",[1.5,3.14],"RER B")
    C = Station("aaaab",[1.5,3.14],"RER B")
    D = Station("aaaab",[1.5,3.14],"RER P")
    assert A._lt_(B) == "aaaaa"
    assert D._lt_(C) == "aaaab"
    print("self._lt_       OK")
    ############################################################################
    #                              __hash__ TEST                               #
    ############################################################################    
    assert orsay_ville._hash_() ==  orsay._hash_()
    print("self._hash_     OK")
    ############################################################################
    #                               __str__ TEST                               #
    ############################################################################
    msg  = "************************\n"
    msg += "* Station Informations *\n"
    msg += "************************\n"
    msg += "Name     = " + str(gare_est.name) + "\n"
    msg += "Position = " + str(gare_est.position) + "\n"
    msg += "Line     = " + str(gare_est.in_line) + "\n"
    msg += "************************"
    assert gare_est._str_() == msg
    print("self._str_      OK")
    ############################################################################
    #                               Message end                                #
    ############################################################################
    print ("Station is      OK")
    print ("*******************")

if __name__ == '__main__':
    main()
