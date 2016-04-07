"""
   Module:Dijkstra-Algorithm
          (finds shortest path between a node with others in a connected net)
   By:Ramin Dehghani
"""
import math 

class Node:
    '''Represents a node in network 
    '''
    
    def __init__(self,name):
        self.name=name 
        self.status=[math.inf,'T']
        self.from_node=None
        self.neighbors={}
    
    def __str__(self):
        return self.name
    
    @property
    def is_permanent(self):
        return self.status[1]=='P'
    
    def make_permanent(self):
        self.status[1]='P'
    
    @property
    def total_cost(self):
        return self.status[0]
    
    @total_cost.setter 
    def total_cost(self,cost):
        self.status[0]=cost
    
    def has_temporary_neighbor(self):
        """Checks if node has any temporary neighbor left"""
        if self.neighbors:
            for n in self.neighbors:
                if not n.is_permanent:
                    return True
        return False
    
    def get_min_cost_neighbor(self):
        """Finds the neighbor with min cost and mark it as permanent"""
        temp_min_cost=math.inf  
        next_node=self
        for neighbor_node,cost in self.neighbors.items():
            temp_cost=min(neighbor_node.total_cost,self.total_cost+cost)
            neighbor_node.total_cost=temp_cost
            if temp_cost==self.total_cost+cost:
                neighbor_node.from_node=self
            if temp_cost<temp_min_cost:
                temp_min_cost=temp_cost
                next_node=neighbor_node
        
        next_node.make_permanent()
        return next_node,temp_min_cost     
    
class Net:
    """A network of connected nodes"""
    def __init__(self,*nodes):
        self.nodes=list(nodes)
    
    def start(self,start_index):
        start_node=self.nodes[start_index]
        start_node.make_permanent()
        start_node.total_cost=0
        find_shortest_path(start_node)
    def results(self):
        return self.nodes
    
def find_shortest_path(node):
    """Finds shortest path from node to it's neighbors"""
    next_node,next_min_cost=node.get_min_cost_neighbor()
    if str(next_node)!=str(node):
        return find_shortest_path(next_node)
    else:
        return node
    

def main():
    node_1=Node('n_1')
    node_2=Node('n_2')
    node_3=Node('n_3')
    node_4=Node('n_4')
    node_5=Node('n_5')
    node_6=Node('n_6')
    
    #a net example
    #(node_a:3) means it has a path to node_a with weight 3
    node_1.neighbors.update({node_2:7,node_3:9,node_6:14})
    node_2.neighbors.update({node_3:10,node_4:15})
    node_3.neighbors.update({node_4:11,node_6:2})
    node_4.neighbors.update({node_5:6})
    node_6.neighbors.update({node_5:9})
    
    net=Net(node_1,node_2,node_3,node_4,node_5,node_6)
    net.start(0)
    results=net.results()
    
    #print all path after solution has been completed
    for n in results:
        if n.from_node:
            print(n.name+" <<--- "+n.from_node.name)

if __name__=='__main__':
    main()
    