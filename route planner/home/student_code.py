def shortest_path(M,start,goal):

    out=[start]
    travelled_dist=0
    if start==goal:
        return [goal]
    frontier={start:{'path':[start]}}
    explored={}
    possible_out=None

    while bool(frontier):
        data=frontier[start]
        frontier.pop(start)
        if start==goal:
            if possible_out is None:
                possible_out={'path':out, 'cost':travelled_dist}
            elif travelled_dist<possible_out['cost']:
                possible_out={'path':out, 'cost':travelled_dist}
        adj_points=M.roads[start]
        print("adj_points is {}".format(adj_points))
        for adj_point in adj_points:
            if adj_point in explored:
                continue

            path=data['path']+[adj_point]
            path_cost=travelled_dist+estimated_dist(M.intersections[start],M.intersections[adj_point])
            estimated_cost=estimated_dist(M.intersections[adj_point],M.intersections[goal])
            f=path_cost+estimated_cost

            if frontier.get(adj_point,None) is None:
                frontier[adj_point]={'path':path,'path_cost':path_cost,'f':f}
                print("checkingg for {}, old {}, new {}".format(adj_point,frontier.get(adj_point,None)['f'],f))                
            elif frontier.get(adj_point,None)['f'] > f:
                frontier[adj_point]={'path':path,'path_cost':path_cost,'f':f}
                
        for adj_point in adj_points:
            explored[start]=True

        out,travelled_dist = find_min_cost_path_in_frontier(frontier)
        if len(out)>0:
            start=out[-1]
    return possible_out.get('path')
            
def find_min_cost_path_in_frontier(data):
    min_dist=None
    index=0
    cost=0
    path=''
    for idx, val in data.items():
        f=val.get('f')
        if min_dist is None or min_dist > f :
            min_dist=f
            path=val.get('path')
            cost=val.get('path_cost')
    return (path,cost)
        
import math        
def estimated_dist(a, b):
    x1=a[0]
    y1=a[1]
    x3=b[0]
    y3=b[1]
    x2=x3
    y2=y1
    
    dist=math.sqrt((x2-x1)**2 + (y3-y2)**2)
    return dist