#!/usr/bin/env python3
# -*- coding: utf-8 -*-

##############################################
# Institut Villebon, UE 3.1
# Travaux pratique 2
# Auteur : C.Lavrat & S.Sonko
# Date de creation : 17/11/15
# Date de derniere modification : 01/12/15
##############################################

class Graph:
#------------------------------------------------------------------------------#
#initialisation of the class :                                                 #
#------------------------------------------------------------------------------#
    def __init__(self, valued):
        """
        The Graph module
        ================

        This class is made for create graph, and search in it.
        when you initialize the class a void graph is authomaticaly made.

        :Example:


        import the class:
        >>> from Graph import Graph
        >>>
        
        create a new graph:
        >>> new_graph = Graph()
        >>>


        Module atrubute
        ---------------
        :Param valued: init a valued graph if True (boolean)
        :Attribute nodes: set with all the graph's nodes in it
        :Attribute edges: list with all the graph's edges in it
        :Attribute adjacency_list: adjacency list of the graph
        :Attribute weight: dict of all the weight of the edges
                           the edge is the key and the value is the weight

        Graph getter
        ------------
        get_nodes(self): return the self.nodes value
        get_edges(self): return the self.edges value
        get_adjacency_list(self): return the self.adjacency_list value
        
        Graph print
        -----------
        __str__(self): return a str with some information about the graph struct

        Graph creation
        --------------
        add_a_node(self, node_name): add a node in the graph
        add_an_edge(self, from_node, to_node): add an edge in the graph
        
        Graph search
        ------------
        breadth_first_search(self,departure): do a BFS in the graph
        depth_first_search(self,departure): do a DFS in the graph
        dijkstra(self, departure); do a dijkstra ponderation
        
        
        Graph connected
        ---------------
        is_non_oriented(self): say if the graph is non oriented
        is_connected(self): say if the graph is connected
        connected_components(self): give the connected components of the graph
        shortest_path(self, departure, arrival): give the shortest path between 
                                                 two nodes

        Graph eulerien
        --------------
        is_eulerien(self): say if the graph is eulerien
        
        .. Warning: the value of valued is fixed when it's init
        """
        self.nodes = set()
        self.edges = []
        self.adjacency_list = {}
        self.valued_graph = valued
        self.weight = {}
################################################################################
#                            GRAPH GETTER                                      #
################################################################################
#------------------------------------------------------------------------------#
#Graph getter : nodes : give the self nodes                                    #
#------------------------------------------------------------------------------#
    def get_nodes(self):
        """ 
        The get_nodes fonction
        ======================

        This fonction return the list of nodes in the curent graph

        Parameters
        ----------
        :return: the value of self.nodes in the curent graph
        :rtype: set()

        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_node('A')
        >>> new_graph.get_nodes()
        'A'
        >>> 

        .. seealso:: GRAPH GETTER part
        """
        return self.nodes
#------------------------------------------------------------------------------#
#Graph getter : edges : give the self edges                                    #
#------------------------------------------------------------------------------#
    def get_edges(self):
        """ 
        The get_edges fonction
        ======================

        This fonction return the list of edges in the curent graph

        Parameters
        ----------
        :return: the value of self.edges in the curent graph
        :rtype: list

        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_node('A')
        >>> new_graph.add_a_node('B')
        >>> new_graph.add_an_edge('A','B')
        >>> new_graph.add_an_edge('B','A')
        >>> new_graph.get_nodes()
        [('A','B'),('B','A')]
        >>> 

        .. seealso:: GRAPH GETTER part
        """
        return self.edges
#------------------------------------------------------------------------------#
#Graph getter : adjacency_list : give the self adjacency_list                  #
#------------------------------------------------------------------------------#
    def get_adjacency_list(self):
        """ 
        The get_adjacency_list fonction
        ===============================

        This fonction return the adjacency_list of the edges in the curent graph

        Parameters
        ----------
        :return: the value of self.adjacency_list in the curent graph
        :rtype: dict

        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_node('A')
        >>> new_graph.add_a_node('B')
        >>> new_graph.add_an_edge('A','B')
        >>> new_graph.add_an_edge('B','A')
        >>> new_graph.adjacency_list()
        {'A':['B'], 'B':['A']}
        >>> 

        .. seealso:: GRAPH GETTER part
        """
        return self.adjacency_list
#------------------------------------------------------------------------------#
#Graph getter : get_valued_graph : give the self valued_graph                  #
#------------------------------------------------------------------------------#
    def get_valued_graph(self):
        """ 
        The get_valued_graph fonction
        =============================

        This fonction return valued_graph in the curent graph.

        Parameters
        ----------
        :return: the value of self.valued_graph in the curent graph
        :rtype: boolean

        :Example:

        >>> new_graph = Graph(True)
        >>> new_graph.get_valued_graph()
        True
        >>> 

        .. seealso:: GRAPH GETTER part
        """
        return self.valued_graph
#------------------------------------------------------------------------------#
#Graph getter : get_weight : give the self weight                              #
#------------------------------------------------------------------------------#
    def get_weight(self):
        """ 
        The get_weight fonction
        =======================

        This fonction return weight of all the edges in the curent graph.

        Parameters
        ----------
        :return: the value of self.weight in the curent graph
        :rtype: boolean

        :Example:

        >>> new_graph = Graph(True)
        >>> new_graph.add_an_edge('A','B',10)
        >>> new_graph.add_an_edge('B','A',5)
        >>> new_graph.get_weight()
        {('A','B'):10, ('B','A'):5}
        >>> 

        .. seealso:: GRAPH GETTER part
        """
        return self.weight
################################################################################
#                              GRAPH PRINT                                     #
################################################################################
#------------------------------------------------------------------------------#
#Graph print : __str__ : give a all the basics information of the graph        #
#------------------------------------------------------------------------------#
    def __str__(self):
        """
        The __str__ fonction
        ====================

        This fonction return a string with all the basics information about
        the curent graph.

        Parameters
        ----------
        :return: all the basic information about the graph
        :rtype: str

        :Example:

        >>> new_graph = Graph(True)
        >>> new_graph.add_a_node('A')
        >>> new_graph.add_a_node('B')
        >>> new_graph.add_an_edge('A','B',1.62)
        >>> new_graph.add_an_edge('B','A',3.14)
        >>> print(new_graph)
        ************************
        * Display of the graph *
        ************************
        Nodes:
        −−−−−−
        A, B
        Edges:
        ------
        A ---> B : 1.62
        B ---> A : 3.14
        =========================
        >>> 

        .. seealso:: GRAPH PRINT part
        """
        #We gona add somme string in msg (for message)
        msg  = "************************\n"
        msg += "* Display of the graph *\n"
        msg += "************************\n"
        msg += "Nodes:\n"
        msg += "−−−−−−\n"
        #add of the list nodes
        #methode 1
        for i in list(self.nodes):
            msg += str(i)+", "
        msg = msg[:-2]
        #methode 2
        #", ".join(self.nodes)
        msg += "\nEdges:\n"
        msg += "−−−−−−\n"
        #if it's a valued graph
        if not self.valued_graph: 
            #we add in msg the value of the adjacency list
            for key, value in list(self.adjacency_list.items()):
                for i in value:
                    msg += ("{} ---> {} \n".format(key, i))
        #if it's not a valued graph
        if self.valued_graph:
            #we add in msg the value of the adjacency list
            for key, value in list(self.adjacency_list.items()):
                for i in value:
                    w = self.weight[(key,i)]
                    msg += ("{} ---> {} : {}\n".format(key, i, w))
        msg+="========================="
        return msg
################################################################################
#                             GRAPH CREATION                                   #
################################################################################
#------------------------------------------------------------------------------#
#Graph reset : get_weight : give the self weight                              #
#------------------------------------------------------------------------------#
    def reset(self):
        """ 
        The reset fonction
        ==================

        This fonction reset all the values of the graph

        Parameters
        ----------
        :return: true if the reset is done
        :rtype: boolean

        :Example:

        >>> new_graph = Graph(True)
        >>> new_graph.add_an_edge('A','B',10)
        >>> new_graph.add_an_edge('B','A',5)
        >>> new_graph.reset()
        True
        >>> 

        .. seealso:: GRAPH CREATION part
        """
        self.nodes = set()
        self.edges = []
        self.adjacency_list = {}
        self.valued_graph = True
        self.weight = {}
        return True
#------------------------------------------------------------------------------#
#Graph creation : add_a_node : add a node in the graph                         #
#------------------------------------------------------------------------------#
    def add_a_node(self, node_name):
        """    
        The add_a_node fonction
        =======================

        This fonction add a new node in the set of nodes in the class Graph

        Parameters
        ----------
        :param node_name: name of the added node
        :type node_name: Can be a string or a value

        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_node('A',weight = 10)
        >>> 

        .. seealso:: Graph creation part
        """
        #if the not is already existed
        if node_name in self.nodes:
            msg = "the node :"+str(node_name)+": is already used!"
            raise NameError(msg)
        #we add a node
        else:
            self.adjacency_list[node_name] = []
            self.nodes.add(node_name)
#------------------------------------------------------------------------------#
#Graph creation : add_an_edge : add a edge in the graph                        #
#------------------------------------------------------------------------------#
    def add_an_edge(self, from_node, to_node, weight = 0):
        """    
        The add_an_edge fonction
        ========================

        This fonction add a new undirected edge in the curent graph

        Parameters
        ----------
        :param from_node: name of the departure node
        :param to_node: name of the arrived node
        :type from_node: Can be a string or a value
        :type to_node: Can be a string or a value

        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_edge('A')
        >>> new_graph.add_a_edge('B')
        >>> new_graph.add_an_edge('A','B')
        >>> 

        .. seealso:: Graph creation part
        """
        # add an edge
        if (from_node in self.nodes) and (to_node in self.nodes):
            # add the edge to _edges
            self.edges.append((from_node, to_node))
            # add the edge to _adjacency_list
            self.adjacency_list[from_node].append(to_node)
            #if it's a non valued graph
            if self.valued_graph == True:
                #we set the value
                self.weight[(from_node, to_node)] = weight
            else:
                if weight != 0:
                    #we set the value to 0
                    self.weight[(from_node, to_node)] = {None}
                    raise TypeError("you are in a non valued graph!!")
        else :
            raise NameError("this edges is already used!!")
################################################################################
#                              GRAPH SEARCH                                    #
################################################################################
#------------------------------------------------------------------------------#
#Graph search : breadth_first_search : do a BFS in the graph                   #
#------------------------------------------------------------------------------#
    def breadth_first_search(self,departure):
        """    
        The breadth_first_search fonction
        =================================

        This fonction do a breadth first search in the current graph 
        the departures of this search is give in parameter

        Parameters
        ----------
        :param departure: name of the departure node
        :type departure: Can be a string or a value

        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_edge('A')
        >>> new_graph.add_a_edge('B')
        >>> new_graph.add_an_edge('A','B')
        >>> new_graph.breadth_first_search('A')
        {'A': None, 'B': 'A'}
        
        .. seealso:: Graph search part
        """
        #Creation of a void dict
        colors = {}
        #We create a dict named parents
        parents = {}
        #we start the fifo list with node departures
        fifo=[departure]
        #At the begining all the nodes is white so :
        for node in self.nodes :
            colors[node] = 'white'
        #we paint in black the departure
        colors[departure] = 'black'
        parents[departure] = None
        
        while fifo :
            father = fifo.pop(0)
            #for all the nodes in the list
            for neighbors in self.adjacency_list[father]:
                #if the neighbors is not colored
                if colors[neighbors] == 'white':
                    #we add neighbors in the list
                    fifo.append(neighbors)
                    #We paint neighbors in grey
                    colors[neighbors] = 'grey'
                    #we add neighbors in father
                    parents[neighbors] = father
            #we paint father in black
            colors[father] = 'black'
        return parents
#------------------------------------------------------------------------------#
#Graph search : depth_first_search : do a DFS in the graph :                   #
#------------------------------------------------------------------------------#
    def depth_first_search(self,departure):
        """    
        The depth_first_search fonction
        ===============================

        This fonction do a depth first search in the current graph 
        the departures of this search is give in parameter

        Parameters
        ----------
        :param departure: name of the departure node
        :type departure: Can be a string or a value

        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_edge('A')
        >>> new_graph.add_a_edge('B')
        >>> new_graph.add_an_edge('A','B')
        >>> new_graph.depth_first_search('A')
        {'A': None, 'B': 'A'}
        
        .. seealso:: Graph search part
        """
        #we create a color dict
        colors = {}
        #we create a parents dict
        parents = {}
        #we set the departure value to None
        parents[departure] = None
        #we initialize all the node in white
        for node in self.nodes :
            colors[node] = 'white'
        #we paint departures in grey
        colors[departure] = 'grey'
        
        #we place departures on the top off the stack
        lifo=[departure]
        father = departure
        
        #while lifo is not empty
        while lifo :
            #we set br as True
            br = True
            #for all the neighbors of father
            for neighbors in self.adjacency_list[father]:
                #if neighbors is in white
                if colors[neighbors] == 'white':
                    #we set father in parents dict                    
                    parents[neighbors] = father
                    #we paint the neighbors in grey
                    colors[neighbors] = 'grey'
                    #we add neighbors in the stack
                    lifo.append(neighbors)
                    #we get father at the end off the stack
                    father = lifo[-1]
                    br = False
                    #we break because we don't want to explore other nodes yet
                    break
            #if we have breaked
            if br :
                #we remove the first node in the stack
                lifo.pop()
                #we paint father in black
                colors[father] = 'black'
                if not lifo == []:
                    father = lifo[-1]
        return parents
#------------------------------------------------------------------------------#
#Graph search : dijkstra : do a dijkstra search in the graph :                 #
#------------------------------------------------------------------------------#
    def dijkstra(self, departure):
        """    
        The dijkstra fonction
        =====================


        Parameters
        ----------
        :param departure:
        :return: 
        :type departure:
        :rtype: 
        
        :Example:

        >>>
        >>>
        >>>
                     
        .. seealso:: Graph connected part
        """
        #raise Error : 
        ## Valued graph
        if self.valued_graph == False:
            raise TypeError("you are in a non valued graph!!")
        ## Name of node
        if departure not in self.nodes:         
            msg = "the node :"+str(node_name)+": is not in the graph"
            raise NameError(msg)
        ## weight negatif
        for ed in self.edges:
            if self.weight[ed] < 0:
                raise ValueError("there are a negative weight")
            
        #initialisation of the variable
        distances = {}
        parents = {}
        non_marked_nodes = []

        #for all the nodes in nodes
        for node in self.nodes:
            #we set the distance value to the infinity
            distances[node] = float('inf')
            #we add the node in non_marked_node
            non_marked_nodes.append(node)
        
        #we set the value of the departure node
        distances[departure] = 0.0
        parents[departure] = None
        dij_node = departure
        
        #while non_marked_nodes is not emplty
        while non_marked_nodes != []:
            #we set the min to the max
            min_w = float('inf')
            #for all the nodes in non_marked_nodesde
            for node in non_marked_nodes:
                #if distance is inferieur a departure
                if distances[node] <= min_w:
                    dij_node = node
                    min_w = distances[node]

            for node in self.adjacency_list[dij_node]:
                if node in non_marked_nodes:
                    dist = self.weight[(dij_node, node)]+ distances[dij_node]
                    if dist < distances[node]:
                        distances[node] = dist
                        parents[node] = dij_node
            non_marked_nodes.remove(dij_node)
        return distances, parents
#------------------------------------------------------------------------------#
#Graph search : shortest_path : find the shortest path between two node        #
#------------------------------------------------------------------------------#
    def shortest_path(self, departure, arrival):
        """
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAA AAAAAAAAA   AAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAA AAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAABA AAAAAAA AAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAA AAAAAAA AAAAAAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAA AAAAAAAA AAAA AAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAA AAAAAAAAA   AAAAAAAA AAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
        """
        #is the departure or the graph isn't in the graph
        if (departure or arrival) not in self.nodes:
            raise NameError("the node '"+str(departure)+"' or '"+str(arrival)+"' isn't in the graph")
        
        #if departure is the same as arrival
        if departure is arrival:
            return ([arrival])
        
        #we did the dijksta algorithm
        distances, parents = self.dijkstra(departure)

        #if there are no way to go to the arrival node
        if arrival not in parents:
            raise TypeError("the node '" +str(arrival) +"' is not accessible :-(")
        
        #initialisation of the path
        path=[]
        
        #while we aren't arrived
        while arrival != departure:
            #we add the departure node in path
            path.append(arrival)
            #we set the new departure
            arrival = parents[arrival]
        path.append(departure)
        path.reverse()

        return path        
        
################################################################################
#                              GRAPH CONNECTED                                 #
################################################################################
#------------------------------------------------------------------------------#
#Graph connected : is_non_oriented : say if a graph is oriented                #
#------------------------------------------------------------------------------#
    def is_non_oriented(self):
        """    
        The is_non_oriented fonction
        ============================

        This fonction say if the current graph is or not oriented

        Parameters
        ----------
        :return: True if the graph is unoriented False else
        :rtype: boolean
        
        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_edge('A')
        >>> new_graph.add_a_edge('B')
        >>> new_graph.add_an_edge('A','B')
        >>> new_graph.add_an_edge('B','A')
        >>> new_graph.is_non_oriented()
        True   
             
        .. seealso:: Graph connected part
        """
        #this variable compte the unoriented_edges
        unoriented_edges = 0
        #we can all the nodes
        for node_1 in self.nodes:
            for node_2 in self.nodes:
                #if there are tow edges in oposites way between two nodes 
                #this nodes is link by a unoriented edge
                if node_2 in self.adjacency_list[node_1]:
                    if node_1 in self.adjacency_list[node_2]:
                        #we compte teh number of unoriented_edges
                        unoriented_edges += 1

        #if the number of unoriented_edges is egual to the number of edge
        #the graph is unoriented
        if (unoriented_edges == len(self.edges)):
            return True
        else :
            return False
#------------------------------------------------------------------------------#
#Graph connected : connected_component : give the connected coponent off graph #
#------------------------------------------------------------------------------#
    def connected_components(self):
        """    
        The connected_components fonction
        =================================

        This fonction give all the connected components of a graph in a list

        Parameters
        ----------
        :return: all the parent of a connected components
        :rtype: list of set
        
        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_edge('A')
        >>> new_graph.add_a_edge('B')
        >>> new_graph.add_an_edge('A','B')
        >>> new_graph.add_an_edge('B','A')
        >>> new_graph.connected_components()
        [set(['A', 'B'])]
        
        .. Warnings:: this fonction work just for non_oridented graphs
        .. seealso:: Graph connected part
        """
        #if the graph is non_oriented
        if self.is_non_oriented() == True:
            seen = []
            c_compo  = []
            #this code find connected component for a undirected graph
            #we take a node
            for node in self.nodes:
                #if we haven't seen the node
                if node not in seen:
                    #we add it in seen 
                    c=set(self.breadth_first_search(node))
                    seen.append(c)
            #now ye have a list with doublon 
            #so we must delet the undoubon of the liste
            #indeed if there are a doublon it is a conncted graph
            for x in seen:
                for y in seen:
                    if x == y:
                        if x not in c_compo:
                            c_compo.append(x)
            return c_compo
            
        #if the graph is oriented
        else :
            raise TypeError("this graph is oriented!")
#------------------------------------------------------------------------------#
#Graph connected : is_connected : say if the graph is connected                #
#------------------------------------------------------------------------------#
    def is_connected(self):
        """    
        The is_connected fonction
        =========================

        Say if the current graph il connected
        Return True if the graph is connected, false otherwise.
         
        Parameters
        ----------
        :return: Return True if the graph is connected, false otherwise.
        :rtype: boolean
        
        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_edge('A')
        >>> new_graph.add_a_edge('B')
        >>> new_graph.add_an_edge('A','B')
        >>> new_graph.add_an_edge('B','A')
        >>> new_graph.is_connected()
        True
        
        .. Warnings:: this fonction work just for non_oridented graphs
        .. seealso:: Graph connected part
        """
        #if the graph is non_oriented
        if self.is_non_oriented() == True:
            #we take all the connected components
            connect_compo = self.connected_components()
            #if the variable connect compo is non empty
            if connect_compo != None:
                cpt = 0
                for i in connect_compo:
                    cpt+=1
                if cpt == 1 :
                    return True
                else :
                    return False
            else :
                return False
        #if the graph is oriented
        else :
            raise TypeError("this graph is oriented!")
################################################################################
#                               GRAPH EULERIEN                                 #
################################################################################
#------------------------------------------------------------------------------#
#Graph eulerien : is_eulerien : say if the graph is eulerien :                 #
#------------------------------------------------------------------------------#
    def is_eulerien(self):
        """
        The is_eulerien fonction
        =========================

        Say if the current graph is eulerien
        Return True if the graph is eulerien, false otherwise.
         
        Parameters
        ----------
        :return: Return True if the graph is eulerien, false otherwise.
        :rtype: boolean
        
        :Example:

        >>> new_graph = Graph()
        >>> new_graph.add_a_edge('A')
        >>> new_graph.add_a_edge('B')
        >>> new_graph.add_a_edge('C')
        >>> new_graph.add_an_edge('A','B')
        >>> new_graph.add_an_edge('B','A')
        >>> new_graph.add_an_edge('A','C')
        >>> new_graph.add_an_edge('C','A')
        >>> new_graph.add_an_edge('C','B')
        >>> new_graph.add_an_edge('B','C')
        >>> new_graph.is_eulerien()
        True
        
        .. Warnings:: this fonction work just for non_oridented graphs
        .. seealso:: Graph eulerien part
        """
        #if the graph is non_oriented
        if self.is_non_oriented() == True:
            #for all the nodes
            for node_1 in self.nodes:
                cpt = 0
                #we compte the value degre
                for node_2 in self.adjacency_list[node_1]:
                    cpt += 1
                #we test if the value is pair
                if not cpt %2 == 0:
                    return False
            return True
        
        else:
            #we create a dict with all the node's degre
            degre_add = {}
            #we initialize the dict
            for node in self.nodes:
                degre_add[node] = 0
            #for all the nodes
            for node_1 in self.nodes:
                #we are gona compte the node degre in end out off a node
                cpt_in = 0
                cpt_ex = 0
                for node_2 in self.adjacency_list[node_1]:
                    #Degre in
                    cpt_in += 1
                    #Degre out
                    cpt_ex  = self.adjacency_list[node_1].count(node_2)
                    print (cpt_ex)
                    #if the sum off all the degre off a node isent pair
                    if not (cpt_ex + cpt_in) %2 == 0:
                        #we return False
                        return False
            return True

################################################################################
#                                    TESTS                                     #
################################################################################
if __name__ == '__main__':
    """
    The __name__ fonction
    ===================================

    Quick test on a simple graph. 
    Who looks like :
    
                ---A-----B-----C---
                |        |        |
                I        |        D
                |        |        |
                H---     ---------E
                |  |              |
                |--G-----------F--|

    :Example:

    how to run this test?
    >>>execfile("Graph.py")
    >>>
    """
    #init of the graph
    graph = Graph(True)
    #we add 6 nodes
    graph.add_a_node('A')
    graph.add_a_node('B')
    graph.add_a_node('C')
    graph.add_a_node('D')
    graph.add_a_node('E')
    graph.add_a_node('F')
    graph.add_a_node('G')
    graph.add_a_node('H')
    graph.add_a_node('I')
    
    #we add an edge between the nodes
    graph.add_an_edge('A','B',1)
    graph.add_an_edge('B','A',2)
    graph.add_an_edge('B','C',3)
    graph.add_an_edge('C','B',4)
    graph.add_an_edge('C','D',1)
    graph.add_an_edge('D','C',2)
    graph.add_an_edge('D','E',3)
    graph.add_an_edge('E','D',4)
    graph.add_an_edge('E','F',1)
    graph.add_an_edge('F','E',2)
    graph.add_an_edge('F','G',3)
    graph.add_an_edge('G','F',4)
    graph.add_an_edge('G','H',1)
    graph.add_an_edge('H','G',2)
    graph.add_an_edge('H','I',3)
    graph.add_an_edge('I','H',4)
    graph.add_an_edge('I','A',1)
    graph.add_an_edge('A','I',2)
    ############################################################################
    #                         GRAPH GETTER TEST CREATION                       #
    ############################################################################
    assert graph.get_nodes() == {'G', 'D', 'F', 'H', 'A', 'B', 'I', 'C', 'E'}
    assert graph.get_edges() == [('A', 'B'), ('B', 'A'), ('B', 'C'), ('C', 'B'), 
                                 ('C', 'D'), ('D', 'C'), ('D', 'E'), ('E', 'D'), 
                                 ('E', 'F'), ('F', 'E'), ('F', 'G'), ('G', 'F'), 
                                 ('G', 'H'), ('H', 'G'), ('H', 'I'), ('I', 'H'), 
                                 ('I', 'A'), ('A', 'I')]
    assert graph.get_adjacency_list() == {'F': ['E', 'G'], 'G': ['F', 'H'], 
                                          'A': ['B', 'I'], 'H': ['G', 'I'], 
                                          'B': ['A', 'C'], 'I': ['H', 'A'], 
                                          'D': ['C', 'E'], 'C': ['B', 'D'], 
                                          'E': ['D', 'F']}
    ############################################################################
    #                         GRAPH PRINT TEST                                 #
    ############################################################################
    print(graph)
    ############################################################################
    #                         GRAPH SEARCH TEST                                #
    ############################################################################
    assert graph.depth_first_search('A') ==   {'D': 'C', 'I': 'H', 'E': 'D', 
                                               'G': 'F', 'H': 'G', 'F': 'E', 
                                               'C': 'B', 'B': 'A', 'A': None}
    assert graph.breadth_first_search('A') == {'I': 'A', 'D': 'C', 'H': 'I',
                                               'G': 'H', 'E': 'D', 'F': 'G',
                                               'C': 'B', 'B': 'A', 'A': None}
    assert graph.shortest_path('A','E') == ['A', 'B', 'C', 'D', 'E']
    ############################################################################
    #                         GRAPH CONNECTED TEST                             #
    ############################################################################
    assert graph.is_non_oriented() == True
    assert graph.connected_components() == [{'E', 'H', 'F', 'D', 'C', 'G', 'A', 
                                             'B', 'I'}]
    assert graph.is_connected() == True
    ############################################################################
    #                         GRAPH EULERIEN TEST                              #
    ############################################################################
    assert graph.is_eulerien() == True
    

    
