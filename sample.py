graph = {}
S,A,B,C,D,Fin = {},{},{},{},{}, {}
S['A'] = 5
S['B'] = 2
A['C'] = 4
A['D'] = 2
B['A'] = 8
B['D'] = 7
C['Fin'] = 3
C['D'] = 6
D['Fin'] = 1
graph['S'] = S
graph['A'] = A
graph['B'] = B
graph['C'] = C
graph['D'] = D
graph['Fin'] = Fin

from djikstra_def import *

print('どの点への最短ルートとコストを求めますか。以下から選んでください')
print(graph.keys())
target = input()
costs, parents = Dijks(graph)
print('ゴールへの最短コスト:', costs[target])
print('最短経路のリスト:', shortest_root(parents, target))
