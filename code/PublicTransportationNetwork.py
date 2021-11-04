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
#home made library
from Station import Station
from Line import Line
from Graph import Graph

#used library
from math import sqrt, pi, cos, sin
import os
import sys
import platform
#This is just for the plot of the graph
if platform.python_version_tuple()[0] != '3':
    import numpy as np
    import matplotlib.pyplot as plt

class PublicTransportationNetwork:
    """
    The PublicTrasportationNetwork module
    =====================================

    This module represents a graph of a public transportation network.
    
    Notta : all the stations with the same name are linked.

    Parameters
    ----------
    :param name: name of the network
    :param scale: scale of the map
    :type name: str
    :type scale: int

    :Example:
    
    >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
    >>>

    Line creation
    ----------------
    add_a_line(self, line): 
    |   adds a new line in the network

    distances(self, from_station, to_station): 
    |   calculates distances between two stations
    
    set_all_distances(self, line): 
    |   sets all the distances between all the station of the line
    
    duration(self,station_1, station_2, mode): 
    |   gives the time between two stations 
    |   in function of the way of transportation of the line
    
    dec_to_hour(self, time):
    |   takes the hour in base 10 and gives the hour in base 60 
    
    reset_network(self): 
    |   resets all the variables of the network
    
    connection(self, couple):
    |   connects two points of a network 
    |   and adds a new line "tunnel"
    
    connection_all(self):
    |   connects all point with the same name in the network 
    
    create_straight_line(self,line_name, stations_names, from_x, from_y, to_x, to_y, mode):
    |    this function creates a straight line between two stations
    
    create_circular_line(self,line_name, stations_names, center_x, center_y, radius, mode):
    |   this function creates a circular line with a radius of radius and 
    |   line_name as a departure station
    
    
    Graph print
    -----------
    __str__(self): 
    |   gives a visualisation of the network
    
    __plot__(self, legend = True):
    |   Gives a representation of the network with matplotlib. 
    |   /!\ : ONLY ON PYTHON 2.7!
    |   take False in argument if we want legend
        
    Graph data
    ----------
    save(self, file_name): saves all the data of the graph in a file
    load(self, file_name): loads a graph from a file

    .. Date:: 28/12/2015
    .. author:: C.Lavrat
    """
#------------------------------------------------------------------------------#
#initialisation of the class :                                                 #
#------------------------------------------------------------------------------#
    def __init__(self,name, scale):
        """
        The PublicTrasportationNetwork module
        =====================================

        This module represents a graph of a public transportation network

        Parameters
        ----------
        :param name: name of the network
        :param scale: scale of the map
        :type name: str
        :type scale: int

        :Example:

        >>>network = PublicTransportationNetwork("Network_1", 1./25000)
        >>>

        Module attribute
        --------------
        :param name: name of the network
        :param scale: scale of the map
        :param lines: lines in the network
        :type name: str
        :type scale: int
        :type lines: list

        .. Date:: 20/01/2015
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
        #scale of the graph
        #test of the type of scale
        if type(scale) == type(float()) :
            self.scale = scale
        else :
            raise TypeError(str(scale)+" is not a float")
        #----------------------------------------------------------------------#
        #LINES
        self.lines = []
        #GRAPH
        self.network = Graph(True)
        self.dist = {}
        #======================================================================#
################################################################################
#                              LINE CREATION                                   #
################################################################################
#------------------------------------------------------------------------------#
#------------------------------------------------------------------------------#
#Graph creation : add_a_line                                                   #
    def add_a_line(self, line):
        """
        The add_a_line function
        =======================

        adds a new line in the network

        Parameters
        ----------
        :param line: dictionary with the format
                     dict = {"mode": "","name": "", "stations":[]}
                     the value in "station" is a graph module
        :type arg3: dict

        :Example:

        >>>A = Station("A",[1.,1.])
        >>>B = Station("B",[2.,2.])
        >>>C = Station("C",[3.,3.])
        >>>D = Station("D",[4.,4.])
        >>>E = Station("E",[5.,5.])
        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>Line_A={"mode": "métro","name": "L_A", "stations":[A,B,C,D,E]}
        >>>network.add_a_line(Line_A)
        >>>

        .. Date:: 23/01/2015
        .. author:: C.Lavrat
        """
        #We add the line in the visual variables
        #----------------------------------------------------------------------#
        #we create a line with all the informations
        new_line = Line(line["stations"],line["mode"],line["name"])
        #we add the line in the line's list
        self.lines.append(new_line)
        #We set all the distances 
         
        #we add the stations in nodes
        #----------------------------------------------------------------------#
        #we add the stations in nodes
        #we set the departure node
        self.network.add_a_node(line["stations"][0])
        for st in line["stations"]:
            #if the stations is not the departure station
            if st != line["stations"][0]:
                #we add the station in the nodes
                self.network.add_a_node(st)

        #we add the edges the graph
        #----------------------------------------------------------------------#
        #we add all the edges
        #we set the departure node
        departure = line["stations"][0]
        #for all the stations
        for st in line["stations"]:
            #if the station is not the departure station
            if st != departure:
                #we calculate the weight in time 
                weight = self.duration(departure,st,line["mode"])
                #and add an edge between departure and st
                self.network.add_an_edge(departure,st,weight)
                #the new node is the departure
                departure = st
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph creation : calculate distances                                          #
#------------------------------------------------------------------------------#
    def distances(self, from_station, to_station):
        """
        The distances function
        ======================

        Calculates the distance between two stations of a map.

        Parameters
        ----------
        :param from_station: station of departure
        :param to_station: station of arrival
        :type from_station: class Station
        :type to_station: class Station
        :return: distance between the two stations
        :rtype: float

        :Example:

        >>>A = Station("A",[1.,1.])
        >>>B = Station("B",[2.,2.])
        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>Line_A={"mode": "métro","name": "L_A", "stations":[A,B]}
        >>>network.add_a_line(Line_A)
        >>>network.distances(A,B)
        1.4142135623730951
        
        .. Date:: 28/12/2015
        .. author:: C.Lavrat
        """
        #this used pythagore
        #we take the from_station positions
        [x1,y1] = from_station.position
        #we take the to_station positions
        [x2,y2] = to_station.position
        #we return the pythagore value
        return sqrt((abs(x1-x2))**2 + (abs(y1-y2))**2) * self.scale
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph creation : duration                                                     #
#------------------------------------------------------------------------------#
    def duration(self,station_1, station_2, mode):
        """
        The duration function
        =====================

        gives the time between two stations in function of the way the
        transportation in the given line.
        
        way and speed
        --------------
        RER: 40 km/h
        Underground:25 km/h
        Tramway: 22 km/h
        Bus: 14 km/h
        Piéton: 4.5 km/h
        
        Parameters
        ----------
        :param station_1: station of departure
        :param station_2: station of arrival
        :type station_1: class Station
        :type station_2: class Station
        :return: time in minutes between the two stations
        :rtype: float

        :Example:

        >>>A = Station("A",[1.,1.])
        >>>B = Station("B",[2.,2.])
        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>Line_A={"mode": "Underground","name": "L_A", "stations":[A,B]}
        >>>network.add_a_line(Line_A)
        >>>network.duration(A,B)
        1.4142135623730951
        
        .. Date:: 22/01/2015
        .. author:: C.Lavrat

        """
        #all the type of name of the stations
        #----------------------------------------------------------------------#
        rer   = ["RER","rer"]
        under = ["Underground","underground","subway",
                 "métro","Métro","metro","Metro"]
        tram  = ["Tramway","tramway"]
        bus   = ["Bus","bus"]
        foot  = ["Piéton","piéton","Pieton","pieton"]
        #Speed Selection
        #----------------------------------------------------------------------#
        #RER speed selection
        if mode in rer:
            v = 40. #km/h
        #subway speed selection
        if mode in under:
            v = 25. #km/h
        #Tramway speed selection
        if mode in tram:
            v = 22. #km/h
        #Tramway speed selection
        if mode in bus:
            v = 14. #km/h
        #pieton speed selection
        if mode in foot:
            v = 4.5 #km/h
        #----------------------------------------------------------------------#
        #Time between station_1 and station_2 in minutes
        #----------------------------------------------------------------------#
        return self.distances(station_1, station_2)*60./v
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph creation : decimal to hours                                             #
#------------------------------------------------------------------------------#
    def dec_to_hour(self, time):
        """
        The dec_to_hour function
        ========================

        takes the hour in base 10 and give the hour in base 60 

        :Example:

        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>network.dec_to_hour(0.5)
        30 Min
        >>>
                
        .. Date:: 30/12/2015
        .. author:: C.Lavrat
        """
        #MINS
        mins = time%1*60
        mins = mins - mins%1
        #HOURS
        hours = time - time%1
        if hours == 0:
            return str(mins)+" Min"
        if hours != 0:
            return str(hours)+" heure "+str(mins)+" Min"
#------------------------------------------------------------------------------#
#Graph creation : reset_network                                                #
#------------------------------------------------------------------------------#
    def reset_network(self):
        """
        The reset_network function
        ==========================

        resets all the network

        :Example:

        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>network.reset_network()
        >>>
                
        .. Date:: 23/12/2015
        .. author:: C.Lavrat
        """
        #we put nothing in all the global variable 
        self.lines = []
        self.name = ""
        self.scale = 1
        #this function have been added in the Graph module
        self.network.reset()
        self.dist = {}
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph creation : connection                                                   #
#------------------------------------------------------------------------------#
    def connection(self, couple):
        """
        The connection function
        =======================

        connects two points of a network 
        and adds a new line "tunnel"

        Parameters
        ----------
        :Param couple: two station to link
        :type : instance of station
        
        .. Date:: 23/01/2015
        .. author:: C.Lavrat
        """
        #We add the line in the visual variables
        #----------------------------------------------------------------------#
        #we create a line with all the in informations in ---->
        new_line = Line(couple,"piéton","tunnel")
        #we add the line in the line lsit
        self.lines.append(new_line)
        
        #we add all the edges
        weight = self.duration(couple[0],couple[1],"piéton")
        self.network.add_an_edge(couple[0],couple[1],weight)
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph creation : connection_all                                                   #
#------------------------------------------------------------------------------#
    def connection_all(self):
        """
        The connection_all function
        ===========================

        connects all points with the same name in the network 

        .. Date:: 23/01/2015
        .. author:: C.Lavrat
        """
        #we connect all the station with the same name 
        #----------------------------------------------------------------------#
        #for all the node in the network
        
        for node1 in self.network.nodes:
            #for all the node in the network
            for node2 in self.network.nodes:
                #if the instance of the two node are different
                if node1 != node2:
                    #if the name are the same
                    if node1.name == node2.name:
                        #we connect the two nodes
                        self.connection([node1,node2])
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph creation : create_straight_line                                         #
#------------------------------------------------------------------------------#
    def create_straight_line(self,line_name, stations_names, from_x, from_y, to_x, to_y, mode):
        """
        The create_straight_line function
        =================================
        
        this function creates a straight line between two stations
        
        :Example:

        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>network.create_straight_line("line 1", ["S1","S2","S3","S4","S5"], 5., 0., 10., 0., "underground")
        >>>
        
        Parameters
        ----------
        :param line_name: name of the line
        :param stations_names: list of the name of all the stations
        :param from_x: position in x of the from station
        :param from_y: position in y of the from station
        :param to_x: position in x of the two stations
        :param to_y: position in y of the two stations
        :param mode: mode of the station (bus...)
        :type line_name: srt
        :type from_x: float
        :type from_y: float
        :type to_x: float
        :type to_y: float
        :type mode: str
        
        .. Date:: 22/01/2015
        .. author:: C.Lavrat
        """
        station_s_line = []
        i=0
        
        nb_station = len(stations_names)
        
        dx = float(to_x-from_x)/float(nb_station -1)
        dy = float(to_y-from_y)/float(nb_station -1)
        
        for st in stations_names:
            x = float(i*dx)+from_x
            y = float(i*dy)+from_y
            station_s_line.append(Station(st,[x,y]))
            i += 1

        line_new_s = {"mode": mode,"name": line_name, "stations":station_s_line}
        self.add_a_line(line_new_s)
#------------------------------------------------------------------------------#
#Graph creation : create_circular_line                                         #
#------------------------------------------------------------------------------#
    def create_circular_line(self,line_name, stations_names, center_x, center_y, radius, mode):
        """
        The create_straight_line function
        =================================
        
        this function creates a circular line with a radius of radius and 
        line_name as a departure station
        
        :Example:

        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>network.create_circular_line("circular 1", ["C1","C2","C3"], 0., 0., 5., "kayak")
        >>>
        
        Parameters
        ----------
        :param line_name: name of the line
        :param stations_names: list of the name of all the stations
        :param center_x: position in x of the from station
        :param center_y: position in y of the from station
        :param radius: position in x of the to station
        :param mode: way of transportation of the station (bus...)
        :type line_name: srt
        :type center_x: float
        :type center_y: float
        :type radius: float
        :type mode: str
        
        .. Date:: 22/01/2015
        .. author:: C.Lavrat
        """
        station_s_line = []
        i=0

        d_alpha = float(2*pi)/float(len(stations_names))
        
        for st in stations_names:
            x = radius*cos(i*d_alpha) + center_x
            y = radius*sin(i*d_alpha) + center_y
            station_s_line.append(Station(st,[x,y]))
            i += 1
        station_s_line.append(station_s_line[0])
        
        line_new_s = {"mode": mode,"name": line_name, "stations":station_s_line}
        self.add_a_line(line_new_s)
################################################################################
#                              GRAPH PRINT                                     #
################################################################################
#------------------------------------------------------------------------------#
#Graph print : __str__                                                         #
#------------------------------------------------------------------------------#
    def __str__(self):
        """
        The __str__ function
        ====================

        Gives a representation of the network. 
        prints the representation of all the lines

        :Example:

        >>>A = Station("A",[1.,1.])
        >>>B = Station("B",[2.,2.])
        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>Line_A={"mode": "métro","name": "L_A", "stations":[A,B]}
        >>>network.add_a_line(Line_A)
        >>>print(network.__repr__())
        ************************
        *  Line Informations   *
        ************************
        Name = L_A
        mode = métro
        A:(M1)---> B:(M1) 
	        >>> 35355.33905932738 km
        ************************
        
        .. Date:: 28/12/2015
        .. author:: C.Lavrat
        """
        msg = str()
        for line in self.lines:
            msg += line._repr_()
        return msg
        #======================================================================#
#------------------------------------------------------------------------------#
#Graph print : __plot__                                                        #
#------------------------------------------------------------------------------#
    def __plot__(self, legend = True):
        """
        The __plot__ function
        =====================

        Gives a representation of the network with matplotlib. 
        /!\ : ONLY ON PYTHON 2!
        takes False in argument if we want legend
    
        :Example:

        >>>A = Station("A",[1.,1.])
        >>>B = Station("B",[2.,2.])
        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>Line_A={"mode": "métro","name": "L_A", "stations":[A,B]}
        >>>network.add_a_line(Line_A)
        >>>network.__plot__()
        >>>
                
        .. Date:: 23/01/2015
        .. author:: C.Lavrat        """
        if platform.python_version_tuple()[0] == '3':
            raise IOError("only on python 2")        
        else :
            for line in self.lines:
                if line.name != "tunnel":
                    position_st_x = []
                    position_st_y = []

                    for st in line.station:
                        x = st.position[0]
                        y = st.position[1]
                        position_st_x.append(float(x))
                        position_st_y.append(float(y))
                    plt.plot(np.array(position_st_x),np.array(position_st_y),linestyle='-',marker='o',label=line.name)
                
            plt.title(self.name)
            plt.xlabel("km")
            plt.ylabel("km")
            if legend == True:
                plt.legend(bbox_to_anchor=(1,1), loc=2, borderaxespad = 0.)
            plt.show()
            return "plot of " + str(self.name)
        #======================================================================#
################################################################################
#                              GRAPH DATA                                      #
################################################################################
#------------------------------------------------------------------------------#
#Graph creation : save                                                         #
#------------------------------------------------------------------------------#
    def save(self, file_name):
        """
        The save function
        =================

        Saves the network in a csv file.
        the format of the csv file is :
        mode:line:station name:position x:position y

        :Example:

        >>>A = Station("A",[1.,1.])
        >>>B = Station("B",[2.,2.])
        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>Line_A={"mode": "métro","name": "L_A", "stations":[A,B]}
        >>>network.add_a_line(Line_A)
        >>>network.save()
        >>>
        
        .. Date:: 22/01/2015
        .. author:: C.Lavrat
        """
        #if there are a extantion in the file name
        if ".csv" in file_name:
            file_name = file_name[:-4]

        #if the directory file_name is existant
        if file_name in os.listdir(os.getcwd()):
            #we delet this directory hahahahahahhaha!!!
            os.system("rm -r "+file_name)

        #we make a directory with all the data of the graph
        os.makedirs(file_name)
        #----------------------------------------------------------------------#
        # opening of the file                                                  #
        #----------------------------------------------------------------------#
        file_data = open(file_name+"/"+file_name+".csv","w")
        #----------------------------------------------------------------------#
        # save of the scale                                                    #
        #----------------------------------------------------------------------#
        msg  = "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
        msg += "%%%%%%%%%%%%%%%%%%%%scale%%%%%%%%%%%%%%%%%%%%\n"
        msg += "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
        msg += "scale\n"
        msg += str(self.scale)+"\n"
        msg += "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
        msg += "%%%%%%%%%%%%%%%%lines/stations%%%%%%%%%%%%%%%\n"
        msg += "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
        msg += "mode:line:station name:position x:position y\n"
        #----------------------------------------------------------------------#
        # save of the lines                                                    #
        #----------------------------------------------------------------------#
        #this function save all the "tunnel" link as special connection
        msg_tunnel = ""
        msg_temp = ""
        #we write in the file
        for line in self.lines:
            #we open the file
            for st in line.station:
                #we write the mode of the line (metro for example)
                msg += str(line.mode) + ":"
                #we write le name of the line
                msg += str(line.name) + ":"
                #we write all the stations of the line
                msg += str(st.name) + ":"
                for po in st.position:
                    msg += str(po) + ":"
                msg  = msg[:-1] 
                msg += "\n"
        #----------------------------------------------------------------------#
        # save of the special connections                                      #
        #----------------------------------------------------------------------#
        msg += "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
        msg += "%%%%%%%%%%%%%%special connections%%%%%%%%%%%%\n"
        msg += "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
        msg += "line 1:station name 1:line 2:station name 2\n"
        #we write the message in the file
        file_data.write(msg)
        file_data.close()
        #----------------------------------------------------------------------#
        # save of the network's information                                    #
        #----------------------------------------------------------------------#
        #we write in the file
        #file_data = open(file_name+"/"+file_name+"_info.csv","w")
        #msg  = str()
        #msg += self.name+":"+str(self.scale)+"\n"
        #file_data.write(msg)
        #file_data.close()
#------------------------------------------------------------------------------#
#Graph creation : load                                                         #
#------------------------------------------------------------------------------#
    def load(self, file_name):
        """
        The load function
        =================

        loads the network from a csv file to the program.
        the format of the csv file is :
        name_line;name_station;position_station;mode_of_transport;

        :Example:

        >>>network = PublicTrasportationNetwork("Network_1", 1/25000)
        >>>network.load()
        >>>
        
        .. Date:: 23/12/2015
        .. author:: C.Lavrat
        """
        #----------------------------------------------------------------------#
        #Recuperation of the data                                              #
        #----------------------------------------------------------------------#
        if ".csv" in file_name:
            file_name = file_name[:-4]
        files = os.listdir(file_name)
        #we open the file_info file and we extract the information form if
        file_dat = open(file_name+"/"+file_name+".csv","r")
        #we read all the data of the file
        data_raw = file_dat.read()
        #we split all the data of the file
        data = data_raw.split("\n")
        #we set the name of the graph
        self.name = file_name + "graph"
        
        #test of the format
        #----------------------------------------------------------------------#
        msg = []
        msg.append("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        msg.append("%%%%%%%%%%%%%%%%%%%%scale%%%%%%%%%%%%%%%%%%%%")
        msg.append("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        if data[0:3] != msg:
            raise TypeError("the Header 'Scale' have not the right format!")
        #----------------------------------------------------------------------#

        #we set the scale of the graph
        self.scale = float(data[4])
        #we can know create all the graph...
        #we create a dictionnary
        dict_line={}

        #test of the format
        #----------------------------------------------------------------------#
        msg = []
        msg.append("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        msg.append("%%%%%%%%%%%%%%%%lines/stations%%%%%%%%%%%%%%%")
        msg.append("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        msg.append("mode:line:station name:position x:position y")
        if data[5:9] != msg:
            raise TypeError("the Header 'lines/stations' have not the right format!")
        #----------------------------------------------------------------------#

        line_dat=9
        #for all the data lines
        for dat in data[9:]:
            #if it is the end of the data line, we break (no more data)
            if "%" in dat :
                break
            #we split all the line to extract the in data
            st_info = dat.split(":")
            #we create a station with all the data informations
            station = Station(st_info[2],[float(st_info[3]),float(st_info[4])],st_info[0])
            #if the keys is not in the data we add it
            if st_info[1] not in dict_line.keys():
                dict_line[st_info[1]]=[st_info[0]]
            #we add the station i the list of the value of the key
            dict_line[st_info[1]].append(station)
            line_dat += 1

        #Creation of the graph!!
        for keys, values in dict_line.items():
            self.add_a_line({"mode": values[0],"name": keys, "stations":values[1:]})

        #----------------------------------------------------------------------#
        #special connections
        #----------------------------------------------------------------------#
        #test of the format
        #----------------------------------------------------------------------#
        msg = []
        msg.append("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        msg.append("%%%%%%%%%%%%%%special connections%%%%%%%%%%%%")
        msg.append("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
        msg.append("line 1:station name 1:line 2:station name 2")
        if data[line_dat:line_dat+4] != msg:
            raise TypeError("the Header 'special connections' have not the right format!")
        #----------------------------------------------------------------------#

        #Extraction of the couple of destination of the tunnel
        #----------------------------------------------------------------------#
        tunnel_couple = []
        #for all the data after the ### header
        for dat in data[line_dat+4:]:
            #we split all the data
            link_info = dat.split(":")
            #there are sometimes a glitch, the data is [""] we delet this gkitch
            if link_info != [""]:
                #we want to find the instance with the good name to finde the two 
                #we gona compare the line and the name in data
                for lin in self.lines:
                    #if the line read is the same as in the graph
                    if lin.name == link_info[0]:
                        #we take the goos staion in the good line
                        for st in lin.station:
                            #we compare to take the good station
                            if st.name == link_info[1]:
                                #we add the station in our tunnel
                                tunnel_couple.append(st)
                    #we did the same for the other side of the tunnel
                    if lin.name == link_info[2]:
                        for st in lin.station:
                            if st.name == link_info[3]:
                                tunnel_couple.append(st)
                if len(tunnel_couple) == 2:
                    self.connection(tunnel_couple)
if __name__ == '__main__':
    """
    run
    python PublicTransportationNetwork.py Blanche Gare_du_Nord
    if you want to have a graph

    python3 PublicTransportationNetwork.py Blanche Gare_du_Nord
    if not

    Notta :
    if you have a " " in the name of your station use a "_" to fake it
    if you have a "'" in the name of your station use a "*" to fake it

    .. Date:: 23/01/2015
    .. author:: C.Lavrat
    """
