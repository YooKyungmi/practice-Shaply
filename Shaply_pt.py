from shapely.geometry import Polygon
pol = Polygon(((6,6), (7,6), (10,4), (11,8), (6,6)))   #폴리곤 만들기

from shapely.geometry import Point
point = Point(2.0, 2.0)   # 점 만들기

from shapely.geometry import LineString
line = LineString([(0,0), (10,10)])  # 라인

from shapely.geometry import MultiPolygon
polygons = MultiPolygon([pol,pol])    #폴리곤 여러 개
