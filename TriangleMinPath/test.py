import unittest

from minpath_dynamic import Triangle as dy_triangle
from minpath_greedy import Triangle as gr_triangle

from minpath_greedy import rows_a
from minpath_dynamic import all_rows as dy_rows

from minpath_dynamic import find_min_path

class MinPathFinder(unittest.TestCase):
    '''class for testing our finders'''
    
    def test_greedy_min_path(self):
        triangle=gr_triangle(rows_a)
        min_path=triangle.find_min_path()
        
        self.assertEqual(min_path.indicated_path, [0,1,0])
        self.assertEqual(min_path.total_cost, 11)
    
    def test_dynamic_min_path(self):
        t=dy_triangle(dy_rows)
        rows=t.calculate_new_costs()
        min_costs=[]
        for elem in rows:
            min_costs.append(elem.min_costs)
        rotate_bits,cost=find_min_path(min_costs)
        
        self.assertEqual(cost, 494)
        self.assertEqual(rotate_bits, [0, 1, 0, 0, 0, 1, 1, 0,
                                        0, 1, 1, 1, 1, 1, 1, 0, 1, 1,
                                         0, 1, 1, 1, 1, 1, 1, 1, 0, 1,
                                          1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0])

if __name__=='__main__':
    unittest.main()
    