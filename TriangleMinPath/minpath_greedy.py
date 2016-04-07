"""
   Module:Greedy Min Cost Path Finder
         a greedy solution to find minimum cost path in a triangle
         not efficient for large triangles
   Author:Ramin-Dehghani
"""
from operator import attrgetter

class Row:
    """A row is an array of values indicating costs"""
    def __init__(self,costs):
        self.costs=costs
    def __getitem__(self,item):
        return self.costs[item]
    def __len__(self):
        return len(self.costs)

class Path:
    """Connects rows through a special path"""
    def __init__(self):
        self.position=0
        self.total_cost=0
        self.indicated_path=[]
    
    def forward(self,next_row):
        """going down in triangle to next row"""
        return self._populate_new_pathes(next_row)
    
    def _populate_new_pathes(self,next_row):
        left_path=Path()
        right_path=Path()
        
        left_path.position=self.position
        right_path.position=self.position+1
        
        left_path.indicated_path=self.indicated_path+[0]
        right_path.indicated_path=self.indicated_path+[1]
        
        left_path.total_cost=self.total_cost+next_row[self.position]
        right_path.total_cost=self.total_cost+next_row[self.position+1]
        
        return left_path,right_path

class Triangle:
    """A triangle is some rows on top of each other which we want to
       find the min path from top to bottom of it
    """
    def __init__(self,rows):
        self.rows=rows
    def find_min_path(self):
        all_pathes=self._find_all_pathes()
        min_path=min(all_pathes,key=attrgetter('total_cost'))
        
        return min_path
    
    def _find_all_pathes(self):
        path=Path()
        path.total_cost=2
        pathes=[path]
        for index,r in enumerate(self.rows):
            if index==len(self.rows):
                break
            if len(r)<2:
                continue
            
            new_pathes=[]
            for p in pathes:
                pl,pr=p.forward(r)
                new_pathes.extend([pl,pr])
                
            pathes=new_pathes
        
        return pathes

#simple test
row1=[2]
row2=[3,4]
row3=[6,5,7]
row4=[4,1,8,3]     
rows_a=[row1,row2,row3,row4]
