import time
from BFS import *

# DFS
def dfs(initial_state, depth_limit=None, return_results=False):
    
    start_time = time.time()
    root = Node(initial_state)
    stack = [root]
    explored = set()
    nodes_expanded = 0
    
    while stack:
        node = stack.pop()
        
        if node.state in explored:
            continue
            
        explored.add(node.state)
        
        if depth_limit is not None and node.depth > depth_limit:
            continue
        
        if goal_test(node.state):
            end_time = time.time()
            path = reconstruct_path(node)
            
            if return_results: # for idfs
                return {
                    'success': True,
                    'path': path,
                    'cost': len(path),
                    'nodes_expanded': nodes_expanded,
                    'depth': node.depth,
                    'node': node,
                    'time': end_time - start_time
                }
            else:
                print("Success!\n")
                print("Path:", path)
                print("Cost:", len(path))
                print("Nodes Expanded:", nodes_expanded)
                print("Search Depth:", node.depth)
                print(f"Running Time:{end_time - start_time:.6f} seconds\n")
                print("Solution Steps:\n")
                print_solution(node)
                states = get_solution_states(node)
                visualize_solution(states)
                return
        
        nodes_expanded += 1
        
        # reverse the neighbors
        neighbors = get_neighbors(node.state)
        for move, state in reversed(neighbors):
            if state not in explored:
                child = Node(
                    state=state,
                    parent=node,
                    move=move,
                    depth=node.depth + 1,
                    cost=node.cost + 1
                )
                stack.append(child)
    
    if return_results: # for idfs
        return {
            'success': False,
            'nodes_expanded': nodes_expanded,
            'time': time.time() - start_time
        }
    else:
        print("Failure")


# Iterative DFS
def idfs(initial_state, max_depth=500):
    
    start_time = time.time()
    total_nodes_expanded = 0
    
    for depth_limit in range(max_depth + 1):
        print(f"Trying depth limit: {depth_limit}")
        
        result = dfs(initial_state, depth_limit, return_results=True) # Use DFS as DLS
        total_nodes_expanded += result['nodes_expanded']
        
        if result['success']:
            end_time = time.time()
            print(f"\nSuccess at depth {depth_limit}!\n")
            print("Path:", result['path'])
            print("Cost:", result['cost'])
            print(f"Total Nodes Expanded: {total_nodes_expanded}")
            print(f"Search Depth: {result['depth']}")
            print(f"Running Time:{end_time - start_time:.6f} seconds\n")
            print("Solution Steps:\n")
            print_solution(result['node'])
            states = get_solution_states(result['node'])
            visualize_solution(states)
            return
    
    print("Failure")