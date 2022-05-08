from collections import defaultdict
from heapq import *


def solution(n, paths, gates, summits):
    answer = []
    result = None
    mxx = 10000001
    for i in range(len(gates)):
        mst, mx = prim(gates[i], paths, gates, summits)
        if mxx > mx:
            mxx = mx
            result = mst
    print("Result ", result)
    print("intense :", mxx)
    sm = []
    flag = False
    for j in result:
        if j[2] == mxx:
            flag = True
        if flag == True and j[1] in summits:
            sm.append(j[1])
            flag = False
    print(" min : ", min(sm))
    answer.append(mst[-1][1])
    return answer


def prim(start_node, edges, gates, summits):
    mst = []
    li = []
    mx = 0
    connected_nodes = set()
    adjacent_edges = defaultdict(list)
    for n1, n2, weight in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))
    print(start_node)
    connected_nodes.add(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        li.append(weight)
        if n2 in summits and mx == 0:
            mx = max(li)
        elif mx != 0 and n2 in summits:
            if mx > max(li):
                mx = max(li)
        print(li, mx)
        if n2 not in connected_nodes and n2 not in gates:
            connected_nodes.add(n2)
            mst.append((n1, n2, weight))
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst, mx


# solution(
#     6,
#     [
#         [1, 2, 3],
#         [2, 3, 5],
#         [2, 4, 2],
#         [2, 5, 4],
#         [3, 4, 4],
#         [4, 5, 3],
#         [4, 6, 1],
#         [5, 6, 1],
#     ],
#     [1, 3],
#     [5],
# )


# solution(
#     7,
#     [[1, 4, 4], [1, 6, 1], [1, 7, 3], [2, 5, 2], [3, 7, 4], [5, 6, 6]],
#     [1],
#     [2, 3, 4],
# )

solution(
    7,
    [[1, 2, 5], [1, 4, 1], [2, 3, 1], [2, 6, 7], [4, 5, 1], [5, 6, 1], [6, 7, 1]],
    [3, 7],
    [1, 5],
)
