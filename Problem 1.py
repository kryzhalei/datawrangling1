# -*- coding: utf-8 -*-
"""
Created on Wed Nov 27 22:32:52 2019

@author: Kryzha Lei Aguilar
"""

import pandas as pd

Bears_Math = pd.DataFrame ({'Student' : ['Ice Bear','Panda','Grizzly'],
                            'Math' : [80,95,79] })

Bears_Electronics = pd.DataFrame ({'Student' : ['Ice Bear','Panda','Grizzly'],
                                   'Electronics' : [85,95,83] })

Bears_GEAS = pd.DataFrame ({'Student' : ['Ice Bear','Panda','Grizzly'],
                            'GEAS' : [90,79,93] })

Bears_ESAT = pd.DataFrame ({'Student' : ['Ice Bear','Panda','Grizzly'],
                            'ESAT' : [93,89,88] })

mrgA = pd.merge(Bears_Math, Bears_Electronics, how = 'right', on = 'Student')
mrgB = pd.merge(mrgA, Bears_GEAS, how = 'right', on = 'Student')
mrgC = pd.merge(mrgB, Bears_ESAT, how = 'right', on = 'Student')

mlt1 = pd.melt(mrgC, id_vars = 'Student', value_vars = ['Math','Electronics','GEAS','ESAT'])
mlt2 = mlt1.rename(columns = {'variable' : 'Subject', 'value' : 'Grades'})
