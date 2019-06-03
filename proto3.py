# -*- coding: utf-8 -*-
"""
Przybliżone koordynaty możliwych punktów będących wierzchołkami prostokąta zawierającego badany region:

(50.108, 19.846)
(50.008, 20.056)

Przybliżenie do 3 miejsc * 10000:
    501080-500080=1000
    200560-198460=2100

Rejon: 1000x2100 = 2100000 komórek (po około 11 m x 7 m)
(11,12 km x 14,98 km)

"""


import prototyp2


a=Map(1000,2100)
a.simulate()


