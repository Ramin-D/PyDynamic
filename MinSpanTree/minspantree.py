"""
   Module: Minimum Spanning Tree
          (finds the spanning tree in a net with minimum weight)
   Author: Ramin Dehghani
"""

class Node:
    '''Represents every node in net'''
    
    def __init__(self,name):
        self.name=name
        self.resolution_nodes=[]
        self.neighbors={}
        self.resolved=False
    
    def get_min_neighbor(self):
        temp_neighbors={}
        for n,dist in self.neighbors.items():
            if not n.resolved:
                temp_neighbors.update({dist:n})
        keys=list(temp_neighbors.keys())
        if keys:
            min_key=min(keys)
            min_node=temp_neighbors[min_key]
        
            return min_key,min_node
            
    def __str__(self):
        output=''
        for reso in self.resolution_nodes:
            output+=reso.name+' , '
        return '{} -->> {}'.format(self.name,output)

def resolve_nodes(primary_resolved,n_nodes):
    if len(primary_resolved)==n_nodes:
        return primary_resolved
    
    min_nodes_track={}
    for resolved_node in primary_resolved:
        if resolved_node.get_min_neighbor()==None:
            continue
        distance,min_neighbor=resolved_node.get_min_neighbor()
        min_nodes_track.update({distance:(resolved_node,min_neighbor)})
        
    min_tuple=min_nodes_track[min(min_nodes_track.keys())]
    min_detected_neighbor=min_tuple[1]
    resolved=min_tuple[0]
    resolved.resolved=True
    min_detected_neighbor.resolved=True
    resolved.resolution_nodes.append(min_detected_neighbor)
    
    primary_resolved.append(min_detected_neighbor)
    
    return resolve_nodes(primary_resolved,n_nodes)
        

def main():
    node_a=Node('A')
    node_b=Node('B')
    node_c=Node('C')
    node_d=Node('D')
    node_e=Node('E')
    node_f=Node('F')
    node_g=Node('G')
    node_h=Node('H')
    
    #a net example
    #(node_a:3) means it connects to node_a with weight 3
    node_a.neighbors.update({node_b:3,node_d:5,node_c:2})
    node_b.neighbors.update({node_a:3,node_d:2,node_f:13})
    node_c.neighbors.update({node_a:2,node_d:2,node_e:5})
    node_d.neighbors.update({node_a:5,node_b:2,node_c:2,node_e:4,node_f:6,node_g:3})
    node_e.neighbors.update({node_c:5,node_d:4,node_g:6})
    node_f.neighbors.update({node_b:13,node_d:6,node_g:2,node_h:3})
    node_g.neighbors.update({node_e:6,node_d:3,node_f:2,node_h:6})
    node_h.neighbors.update({node_f:3,node_g:6})
    
    #start with node E
    node_e.resolved=True
    resolved_nodes=resolve_nodes([node_e],8)
    
    #prints final connected tree
    for r in resolved_nodes:
        print(r)

if __name__=="__main__":
    main()