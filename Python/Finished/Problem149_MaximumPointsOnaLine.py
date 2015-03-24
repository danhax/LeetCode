"""
Given n points on a 2D plane, find the maximum number of points that lie on the same straight line.
"""
# Definition for a point
class Point:
	def __init__(self, a=0, b=0):
		self.x = a
		self.y = b

def Compare(p1,p2):
	return p1.x-p2.x

class Solution:
	# @param points, a list of Points
	# @return an integer
	def maxPoints(self, points):
		n=len(points)
		if(n<3):return n
		result=2
		points=sorted(points,cmp=Compare)
		#points=sorted(points,key=lambda point:point.x)
		for i in range(n):
			p1=points[i]
			print p1.x,p1.y
			slope={}
			same_points=1;local_max=1
			for j in range(i+1,n):
				p2=points[j]
				m=0.0
				if(p1.x==p2.x and p1.y==p2.y):
					same_points+=1
					local_max=max(local_max,same_points)
					continue
				elif(p1.x==p2.x):
					m=0xfffffff+0.1
				else:
					m=float(p1.y-p2.y)/(p1.x-p2.x)
				if(not(m in slope)):slope[m]=same_points
				slope[m]+=1
				local_max=max(local_max,slope[m])
			result=max(result,local_max)
		return result


s=Solution()
p=[(40,-23),(9,138),(429,115),(50,-17),(-3,80),(-10,33),(5,-21),(-3,80),(-6,-65),(-18,26),(-6,-65),(5,72),(0,77),(-9,86),(10,-2),(-8,85),(21,130),(18,-6),(-18,26),(-1,-15),(10,-2),(8,69),(-4,63),(0,3),(-4,40),(-7,84),(-8,7),(30,154),(16,-5),(6,90),(18,-6),(5,77),(-4,77),(7,-13),(-1,-45),(16,-5),(-9,86),(-16,11),(-7,84),(1,76),(3,77),(10,67),(1,-37),(-10,-81),(4,-11),(-20,13),(-10,77),(6,-17),(-27,2),(-10,-81),(10,-1),(-9,1),(-8,43),(2,2),(2,-21),(3,82),(8,-1),(10,-1),(-9,1),(-12,42),(16,-5),(-5,-61),(20,-7),(9,-35),(10,6),(12,106),(5,-21),(-5,82),(6,71),(-15,34),(-10,87),(-14,-12),(12,106),(-5,82),(-46,-45),(-4,63),(16,-5),(4,1),(-3,-53),(0,-17),(9,98),(-18,26),(-9,86),(2,77),(-2,-49),(1,76),(-3,-38),(-8,7),(-17,-37),(5,72),(10,-37),(-4,-57),(-3,-53),(3,74),(-3,-11),(-8,7),(1,88),(-12,42),(1,-37),(2,77),(-6,77),(5,72),(-4,-57),(-18,-33),(-12,42),(-9,86),(2,77),(-8,77),(-3,77),(9,-42),(16,41),(-29,-37),(0,-41),(-21,18),(-27,-34),(0,77),(3,74),(-7,-69),(-21,18),(27,146),(-20,13),(21,130),(-6,-65),(14,-4),(0,3),(9,-5),(6,-29),(-2,73),(-1,-15),(1,76),(-4,77),(6,-29)]
p=[(0,0),(1,1),(0,0)]
points=[]
for x in p:
	points.append(Point(x[0],x[1]))
print s.maxPoints(points),"== 25"
