'''
Date: 2023-10-13 22:35:53
LastEditors: Heng-Mei l888999666y@gmail.com
LastEditTime: 2023-10-13 22:39:25
FilePath: \GMOEA\main.py
'''
from GMOEA import GMOEA
from global_parameter import GlobalParameter as GP
from IMMOEA_pro import test_problem as pro

if __name__ == "__main__":
    gp = GP(pro=pro)
    test = GMOEA(gp=gp)
    test.run()