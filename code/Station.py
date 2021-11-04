#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################
# Institut Villebon, UE 3.1
# Projet : mon_via_navigo
# Auteur : C.Lavrat, B. Marie Joseph, S. Sonko
# Date de creation : 27/12/15
# Date de derniere modification : 27/12/15
##############################################

class Station:
    """
    The Station module
    ==================

    This class creates stations and contains all the informations of the stations

    Parameters
    ----------
    :param name: name of the station
    :param position: position of the station
    :param in_line: line of the station
    :type name: str
    :type position: list format [x,y]
    :type in_line: str

    :Example:

    >>>Orsay_Ville = Station("Orsay Ville",[1.5,3.14],"RER B")
    >>>

    Function of information
    -----------------------
    _eq_(self, station):
    |   tells if two stations are the same or not

    _lt_(self, station):
    |   gives the first station in the alphabeter range

    _hash_(self):
    |   returns hash(self.name + self.in_line)

    _str_(self):
    |   Prints a textual representation of the current station
        
    .. Date:: 27/12/2015
    .. author:: C.Lavrat
    """
#------------------------------------------------------------------------------#
#initialisation of the class :                                                 #
#------------------------------------------------------------------------------#
    def __init__(self, name, position, in_line=""):
        """
        The __init__ fonction
        =====================

        this function is the constructor of the station's module

        Parameters
        ----------
        :param name: name of the station
        :param position: position of the station
        :param in_line: line of the station
        :type name: str
        :type position: list format [x,y]
        :type in_line: str

        :Example:

        >>>Orsay_Ville = Station("Orsay Ville",[1.5,3.14],"RER B")
        >>>

        Module attribute
        --------------
        :param name: name of the station
        :param position: position of the station
        :param in_line: line of the station
        :type name: str
        :type position: list format [x,y]
        :type in_line: str

        .. Date:: 27/12/2015
        .. author:: C.Lavrat
        """
        #INPUT TESTS
        #----------------------------------------------------------------------#
        #name of the station
        #test of the type of name
        if type(name) == type(str()) :
            self.name = name
        else :
            raise TypeError(str(name)+" is not a str")
        #----------------------------------------------------------------------#
        #test of the type of position
        #position of the station
        if type(position) == type(list()) :
            self.position = position
        else : 
            raise TypeError(str(position)+" is not a list")
        #----------------------------------------------------------------------#
        #test of the type of in_line
        #line of the station
        if type(in_line) == type(str()):
            self.in_line = in_line
        else :
            raise TypeError(str(in_line)+" is not a str")
        #======================================================================#
################################################################################
#                           Fonction of information                            #
################################################################################
#------------------------------------------------------------------------------#
# __eq__(self, station) : Say if two station are the same or not               #
#------------------------------------------------------------------------------#
    def _eq_(self, station):
        """
        The _eq_ function
        ===================

        Tells if two stations are the same or not, using the hash value.
        
        :Example:

        >>>Orsay_Ville = Station("Orsay Ville",[1.5,3.14],"RER B")
        >>>Orsay = Station("Orsay Ville",[1.5,3.14],"RER B")
        >>>Orsay_Ville._eq_("Orsay")
        True
        
        .. Date:: 27/12/2015
        .. Author:: C.Lavrat
        """
        #if the hash value of the station is the same
        if self._hash_() == hash(station.name + station.in_line):
            #the station is the same
            return True
        else:
            #the station is not the same
            return False
        #======================================================================#
#------------------------------------------------------------------------------#
# __lt__(self, station) : Return the first station in the alphabetical order.  #
#------------------------------------------------------------------------------#
    def _lt_(self, station):
        """
        The _lt_ function
        ===================

        Returns the first station in the alphabetical order.
        
        :Example:

        >>>Palaiseau = Station("Palaiseau",[1.4,15.7],"RER B")
        >>>Palaiseau_villebon = Station("Palaiseau Villebon",[1.4,18.14],"RER B")
        >>>Orsay_Ville._lt_()
        Palaiseau
        
        .. Date:: 27/12/2015
        .. author:: C.Lavrat
        """
        #----------------------------------------------------------------------#
        #if the station are not the same
        if not self._eq_(station):
            if not str(station.name) > str(self.name):
                if not str(station.in_line) > str(self.in_line):
                    return station.name
                else:
                   #print(self.name)
                    return self.name
            else:
                return self.name
        #----------------------------------------------------------------------#
        #if the station are the same
        else:
            raise ValueError("/!\ : this station are the same")
        #======================================================================#
#------------------------------------------------------------------------------#
# __hash__(self) : Return a hash value for the station and line.               #
#------------------------------------------------------------------------------#
    def _hash_(self):
        """
        The _hash_ function
        =====================

        Returns a hash value for the station and line.
        Two stations with the same informations have the same hash value.
        The reverse is not necessarily true, but it can be true.
        /!\ warning : the hash value is different between two runs
        
        :Example:

        >>>Orsay_Ville = Station("Orsay Ville",[1.5,3.14],"RER B")
        >>>Orsay_Ville._hash_()
        -4599906160503219187
        
        .. Date:: 27/12/2015
        .. author:: C.Lavrat
        """
        return hash(self.name + self.in_line)
        #======================================================================#
#------------------------------------------------------------------------------#
# __str__(self) : return a textuel representation of the current station       #
#------------------------------------------------------------------------------#
    def _str_(self):
        """
        The _str_ function
        ====================

        returns a textual representation of the current station
        
        :Example:

        >>>orsay_ville = Station("Orsay Ville",[1.618,3.141],"RER B")
        >>>print(orsay_ville._str_())
        ************************
        * Station Informations *
        ************************
        Name     = Orsay Ville
        Position = [1.618,3.141]
        Line     = RER B
        ************************

        .. Date:: 27/12/2015
        .. author:: C.Lavrat
        """
        #creation of a msg with all the information
        msg  = "************************\n"
        msg += "* Station Informations *\n"
        msg += "************************\n"
        msg += "Name     = " + str(self.name) + "\n"
        msg += "Position = " + str(self.position) + "\n"
        msg += "Line     = " + str(self.in_line) + "\n"
        msg += "************************"
        
        return msg
        #======================================================================#

if __name__ == '__main__':
    """
    The __main__ function
    =====================

    .. Date:: 27/12/2015
    .. author:: C.Lavrat
    """
    print("If you whant to test your programm run the tests in the joigned file \n")
