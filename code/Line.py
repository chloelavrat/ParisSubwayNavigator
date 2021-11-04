#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################
# Institut Villebon, UE 3.1
# Projet : mon_via_navigo
# Auteur : C.Lavrat, B. Marie Joseph, S. Sonko
# Date de creation : 27/12/15
# Date de derniere modification : 27/12/15
##############################################
#------------------------------------------------------------------------------#
#Modules used in the class :                                                   #
#------------------------------------------------------------------------------#

class Line:
    """
    The Line module
    ===============

    This class represents an oriented line of transport 

    Parameters
    ----------
    :param station: list of all the stations of the line
    :param mode: way of transport (bus, métro, RER, vélib)
    :param name: name of the line
    :type arg1: list
    :type arg2: str
    :type arg3: str

    :Example:

    >>>from Station import Station
    >>>A = Station("A",[1.,1.])
    >>>B = Station("B",[2.,2.])
    >>>Ligne_1 = Line([A,B],"métro","Ligne 1")
    >>>

    Function of Line Creation
    -------------------------
    add_all_station_in_graph(self):
    |   add all the stations in a graph

    add_a_link(self, from_station, to_station, weight = 0):
    |   add a link (an edges) between two stations

    add_all_link(self): 
    |   add all the links between the stations' in the line

    __repr__(self):
    |   gives a graphical representation of the line
    
    .. Date:: 27/12/2015
    .. author:: C.Lavrat
    """
#------------------------------------------------------------------------------#
#initialization of the class :                                                 #
#------------------------------------------------------------------------------#
    def __init__(self, station, mode, name):
        """
        The __init__ function
        =====================

        this function is the constructor of the station module

        Parameters
        ----------
        :param station: list of all the stations in the line
        :param mode: mode of transport (bus, métro, RER, vélib)
        :param name: name of the line
        :type station: list
        :type mode: str
        :type name: str

        :Example:

        >>>from Station import Station
        >>>A = Station("A",[1.,1.])
        >>>B = Station("B",[2.,2.])
        >>>Ligne_1 = Ligne([A,B],"métro","Ligne 1")
        >>>

        Module attribute
        --------------
        :param station: list of all the stations in the line
        :param mode: way of transport (bus, métro, RER, vélib)
        :param name: name of the line
        :type station: list
        :type mode: str
        :type name: str

        Function of Line Creation
        -------------------------
        add_all_station_in_graph(self): add all the stations in a graph
        add_a_link(self, from_station, to_station, weight = 0): add a link (an edges) 
                                                                between two stations
        add_all_link(self): add all the links between the stations' in the line
        _repr_(self): gives a graphical representation of the line
        
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
        #test of the type of station
        #station of the station
        if type(station) == type(list()) :
            self.station = station
        else : 
            raise TypeError(str(station)+" is not a list")
        #----------------------------------------------------------------------#
        #test of the type of mode
        #mode of the station
        if type(mode) == type(str()):
            self.mode = mode
        else :
            raise TypeError(str(mode)+" is not a str")
        #----------------------------------------------------------------------#
        #GRAPH
        self.nodes = set()
        self.link = []
        self.adjacency_list = {}
        self.weight = {}

        #Creation of the graph        
        self.add_all_station_in_graph()
        self.add_all_link()
        #======================================================================#
################################################################################
#                              LINE CREATION                                   #
################################################################################
#------------------------------------------------------------------------------#
#Graph creation : add_all_station_in_graph : all is say                        #
#------------------------------------------------------------------------------#
    def add_all_station_in_graph(self):
        """
        The add_all_station_in_graph function
        =====================================

        adds all the stations in a graph.
        used in init.
        
        .. Date:: 27/12/2015
        .. author:: C.Lavrat
        """
        for st in self.station:
            st.in_line += "/"+self.name
            self.adjacency_list[st] = []
            self.nodes.add(st)
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph creation : add_a_link : add a link in the graph                         #
#------------------------------------------------------------------------------#
    def add_a_link(self, from_station, to_station, weight = 0):
        """
        The add_a_link fonction
        =======================

        adds a link (an edges) between two stations
        used in init.
        
        Parameters
        ----------
        :param from_station: station from the class Station
        :param to_station: station from the class Station
        :param weight: weight of a link (represent a distance)
        :type from_station: station from the class Station
        :type to_station: station from the class Station
        :type weight: int

        .. Date:: 27/12/2015
        .. author:: C.Lavrat
        """
        # add the edge to _edges
        self.link.append((from_station, to_station))
        # add the edge to _adjacency_list
        self.adjacency_list[from_station].append(to_station)
        #if it's a non valued graph
        self.weight[(from_station.name, to_station.name)] = weight
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph creation : add_all_link : add all link in the graph                     #
#------------------------------------------------------------------------------#
    def add_all_link(self):
        """
        The add_all_link function
        =========================

        adds all the links in the graph as a path graph.

        .. Date:: 27/12/2015
        .. author:: C.Lavrat
        """
        #we parcourt all the station off the line and add it in the graph
        departure = self.station[0]
        for st in self.station:
            #if we are not in departure we add a link
            if st != departure:
                self.add_a_link(departure,st)
                #we set the new departure
                departure = st
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph creation : __repr__ : show the line                                     #
#------------------------------------------------------------------------------#
    def _repr_(self):
        """
        The _repr_ function
        =====================

        Gives a representation of the Line.

        :Example:

        >>>A = Station("A",[1.,1.])
        >>>B = Station("B",[2.,2.])
        >>>M1 = Line([A,B],"métro", "M1")
        >>>print(M1._repr_())
        ************************
        *  Line Informations   *
        ************************
        Name = M1
        mode = métro
        A:(M1)---> B:(M1) 
	        >>> 0 km
        ************************
        
        .. Date:: 27/12/2015
        .. author:: C.Lavrat
        """
        #creation of a msg with all the information
        #Header
        msg  = "************************\n"
        msg += "*  Line Informations   *\n"
        msg += "************************\n"
        msg += "Name = " + str(self.name) + "\n"
        msg += "mode = " + str(self.mode) + "\n"
        #for all the stations
        for key, value in self.adjacency_list.items():
            for i in value:
                w = self.weight[(key.name, i.name)]
                msg += ("{}:{}---> {}:{} \n\t>>> {} km\n".format(key.name, key.in_line, i.name, i.in_line, w))
        msg += "************************\n"        
        return msg
        #======================================================================#
################################################################################
#                                    TESTS                                     #
################################################################################     
if __name__ == '__main__':
    """
    The __main__ function
    =====================

    .. Date:: 27/12/2015
    .. author:: C.Lavrat
    """
    print("If you whant to test your program run the tests in the joined file\n")
