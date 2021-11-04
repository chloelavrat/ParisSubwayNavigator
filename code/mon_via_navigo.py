#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################
# Institut Villebon, UE 3.1
# Projet : mon_via_navigo
# Auteur : C.Lavrat, B. Marie Joseph, S. Sonko
# Date de creation : 01/01/16
# Date de derniere modification : 01/01/16
############################################## 
#------------------------------------------------------------------------------#
#Modules used in the class :                                                   #
#------------------------------------------------------------------------------#
#home made library
from PublicTransportationNetwork import *

#platform library
import platform

#------------------------------------------------------------------------------#
#results : print all the results                                               #
#------------------------------------------------------------------------------#
def result(graph,departure_name,arrived_name):
    """
    The result function
    ===================
        
    returns a str with all the results of the shortest path. 
    the results are formated to be more readeable for a user.
    use in pair with the main() function
    
    Parameters
    ----------
    :param departure_name: name of the departure station
    :param arrived_name: name of the arrival station
    :param graph: graph
    :type departure_name: srt
    :type arrived_name: str
    :type graph: instance of PublicTransportationNetwork
        
    .. Date:: 23/01/2015
    .. author:: C.Lavrat
    """
    #this value turn to 1 if we find the instance in node (test and security)
    find_a = 0
    find_b = 0
    #we remove the firs and end node if the node are the same...
    for node in graph.network.nodes:
        if node.name == str(departure_name):
            departure_node = node
            find_a = 1
        if node.name == arrived_name:
            arrived_node = node
            find_b = 1

    if (find_a == 0)or(find_b == 0):
        raise TypeError("one of the input station isn't in the graph")

    #we use here the shortest_path in the Graph module
    path = graph.network.shortest_path(departure_node,arrived_node)
    #we create a header
    msg=[]
    msg.append("*******************************************************")
    msg.append("                     VIA_NAVIO                         ")
    msg.append("*******************************************************")
    msg.append("Depart  : "+departure_name)
    msg.append("Arrivee : "+arrived_name)
    msg.append("*******************************************************")
    
    #We detect if the path do se change in the same station at departure
    if path[0].name == path[1].name:
        path.remove(path[0])
    
    #We detect if the path do se change in the same station at arrived
    if path[-1].name == path[-2].name:
        path.remove(path[-1])
    
    #we set the line memory for futur comparaison
    line_memory = path[0].in_line.split("/")[1]
    #we add the line in the msg
    msg.append(line_memory + " : ")
    #now we gona examin all the nodes of the path
    for st in path:
        #in_line have a lot of line, we take the good
        in_line = st.in_line.split("/")
        if in_line[1] == line_memory:
            line_memory = in_line[1]
            msg.append("| "+st.name+" ")
        if in_line[1] != line_memory:
            line_memory = in_line[1]
            msg.append("v\n"+line_memory + ":" )
            msg.append("| "+st.name)
    msg.append("v")

    #Calcul of the time
    #--------------------------------------------------------------------------#
    time = 0
    node_memory = path[0] 
    for node1 in path[1:-1]:
            time += graph.network.weight[node_memory,node1]
            node_memory = node1

    #we gona change the list into a str --"
    msg_out = ""
    for string in msg:
        msg_out += string+"\n"
    #we add the footer
    msg_out += "*******************************************************\n"
    msg_out += "Duree estimee : "+graph.dec_to_hour(time)+"\n"
    #we return the msg_out :D
    return msg_out
################################################################################
#                                     MAIN                                     #
################################################################################
def main():
    """
    The main function
    =================
        
    this function is the head of this project
    it controls all the other functions!!

    RUN
    ===    
    python PublicTransportationNetwork.py Blanche Gare_du_Nord
    if you want to have a graph

    python3 PublicTransportationNetwork.py Blanche Gare_du_Nord
    otherwise

    Notta :
    if you have a " " in the name of your station use a "_" to fake it
    if you have a "'" in the name of your station use a "*" to fake it
        
    .. Date:: 23/01/2015
    .. author:: C.Lavrat
    """
    #if the user want to use the program with sys argument
    if len(sys.argv) > 2:
        #the user put in in the name of the two station
        if (sys.argv[1]!=[]) and (sys.argv[2]!=[]):
            #we extarct and change "_" to " " in the two name
            stat_1 = sys.argv[1].replace("_"," ")
            stat_2 = sys.argv[2].replace("_"," ")
            #we change the "*" into "'" in the two name
            stat_1 = stat_1.replace("*","'")
            stat_2 = stat_2.replace("*","'")
    #else the program crash ;)
    else:
        raise TypeError("No inputs")
    
    graph = PublicTransportationNetwork("Paris", 1.)
    
    #we load the graph of paris
    graph.load("Paris")
    #we connect all the station with the same name
    graph.connection_all()
    
    #we print all the results
    res = result(graph,stat_1,stat_2)
    print(res)
    
    #if we are on python 2 we plot the graph
    if platform.python_version_tuple()[0] != '3':
        graph.__plot__()
################################################################################
#                                     RUN                                      #
################################################################################
if __name__ == '__main__':
    """
    run
    python mon_via_navigo.py Blanche Gare_du_Nord
    if you want to have a graph
    
    python3 mon_via_navigo.py Blanche Gare_du_Nord
    otherwise
    
    Notta :
    if you have a " " in the name of your station use a "_" to fake it
    if you have a "'" in the name of your station use a "*" to fake it

    .. Date:: 23/01/2015
    .. author:: C.Lavrat
    """
    main()
