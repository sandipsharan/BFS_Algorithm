import numpy as np
import copy

path_dict = {}
visited_nodes = []
queue_nodes = []
best_path = []


# To get initial state from the user
def input_initial_state():
    Ri = 3
    Ci = 3
    # Initialize matrix
    print("Enter the entries column wise one by one:")
    mat_initial = [[int(input()) for x in range (Ri)] for y in range(Ci)]
    mat_initial = np.array(mat_initial).transpose()
    print(mat_initial)
    return mat_initial.tolist()

# To get goal state from the user
def input_goal_state():
    Rg = 3
    Cg = 3
    # Initialize matrix
    print("Enter the entries column wise one by one:")
    mat_goal = [[int(input()) for x in range (Cg)] for y in range(Rg)]
    mat_goal = np.array(mat_goal).transpose()
    print(mat_goal)
    return mat_goal.tolist()

# To find transpose state got from the user
def transpose_node(copied_list):
    T_queue = [list(i) for i in zip(*copied_list)]
    return T_queue

# To find the position of zero
def find_blank_tile(queue):
    value = 0
    blank = [(pos, row.index(value)) for pos, row in enumerate(queue) if value in row]

    for y in blank:
        a = y[0]
        b = y[1]
    location = a,b
    return location

# To move up
def ActionMoveUp(a,b, queue):
    queue_copy = copy.deepcopy(queue)
    # Swapping the position of the blank tile

    temp = queue_copy[a][b]
    queue_copy[a][b] = queue_copy[a-1][b]
    queue_copy[a-1][b] = temp

    if queue_copy not in visited_nodes:
        visited_nodes.append(queue_copy)
        queue_nodes.append(queue_copy)
        queue_parent = tuple([tuple(x) for x in queue])
        queue_child = tuple([tuple(x) for x in queue_copy])
        path_dict[queue_child] = queue_parent
    return queue_copy

# To move down
def ActionMoveDown(a,b, queue):
    queue_copy = copy.deepcopy(queue)
    # Swapping the position of the blank tile

    temp = queue_copy[a][b]
    queue_copy[a][b] = queue_copy[a+1][b]
    queue_copy[a+1][b] = temp

    if queue_copy not in visited_nodes:
        visited_nodes.append(queue_copy)
        queue_nodes.append(queue_copy)
        queue_parent = tuple([tuple(x) for x in queue])
        queue_child = tuple([tuple(x) for x in queue_copy])
        path_dict[queue_child] = queue_parent
    return queue_copy

# To move right
def ActionMoveRight(a,b, queue):
    queue_copy = copy.deepcopy(queue)
    # Swapping the position of the blank tile

    temp = queue_copy[a][b]
    queue_copy[a][b] = queue_copy[a][b+1]
    queue_copy[a][b+1] = temp

    if queue_copy not in visited_nodes:
        visited_nodes.append(queue_copy)
        queue_nodes.append(queue_copy)
        queue_parent = tuple([tuple(x) for x in queue])
        queue_child = tuple([tuple(x) for x in queue_copy])
        path_dict[queue_child] = queue_parent
    return queue_copy

# To move left
def ActionMoveLeft(a,b, queue):
    queue_copy = copy.deepcopy(queue)
    # Swapping the position of the blank tile
    
    temp = queue_copy[a][b]
    queue_copy[a][b] = queue_copy[a][b-1]
    queue_copy[a][b-1] = temp
    
    if queue_copy not in visited_nodes:
        visited_nodes.append(queue_copy)
        queue_nodes.append(queue_copy)
        queue_parent = tuple([tuple(x) for x in queue])
        queue_child = tuple([tuple(x) for x in queue_copy])
        path_dict[queue_child] = queue_parent
    return queue_copy

# For back tracking to initial position
def back_tracking(path, initial_state, pre_queue):
    queue_pop_tup = tuple([tuple(x) for x in pre_queue])
    queue_pop_initial = tuple([tuple(x) for x in initial_state])
    best_path.append(queue_pop_tup)
    parent_node = path[queue_pop_tup]
    best_path.append(parent_node)
    # Finding the parent of parent to back track

    while parent_node != queue_pop_initial:  
        parent_node = path[parent_node]
        best_path.append(parent_node)
        if pre_queue == queue_pop_initial:
            parent_node = path[queue_pop_tup]
            best_path.append(parent_node)
            break
    best_path.reverse()
    print("Path Taken: ")
    for i in best_path:
        print(i)
    return best_path

# For getting the value of index, parent index, value of the parent
def nodes_info(visited, path, initial):
    nodes = []
    for i in visited:
        if i == initial:
            continue
        else:
            child = visited.index(i)
            goal_state = tuple([tuple(x) for x in i])
            parent = path[goal_state]
            parent = visited.index(list([list(x) for x in parent]))
            nodes.append([child, parent, i])
    return nodes

# To write in Nodes.txt
def nodes_write(visited):
    for i in visited:
        a = list(map(list,zip(*i)))
        b = list(np.concatenate(a))
        c = ' '.join(str(i) for i in b)
        n.write(c)
        n.write('\n')

# To write in nodePath.txt
def nodePath_write(path):
    for i in path:
        a = list(map(list,zip(*i)))
        b = list(np.concatenate(a))
        c = ' '.join(str(i) for i in b)
        p.write(c)
        p.write('\n')


# To write in NodesInfo.txt
def nodes_info_write(NI):
    for i in NI:
        node = list(map(list, zip(*i[2])))
        node_conc = list(np.concatenate(node))
        joined_node = ' '.join(str(i) for i in node_conc)
        node_index = str(i[0])
        parent_node_index = str(i[1])
        info_node = node_index + "   "+parent_node_index+"   "+joined_node
        node_info.append(info_node)
    f.write('\n'.join('%s' % x for x in node_info))

node_state_i = input_initial_state()
node_state_it = transpose_node(node_state_i)

node_state_g = input_goal_state()
node_state_gt = transpose_node(node_state_g)

queue_nodes.append(node_state_i)
visited_nodes.append(node_state_i)
print("Start Position =", node_state_it)

while True: 
    queue_pop = queue_nodes.pop(0)
    position = find_blank_tile(queue_pop)
    i, j = position
    if queue_pop != node_state_g:
        if i-1 >= 0:
            ActionMoveUp(i,j, queue_pop)
        if i+1 < 3:
            ActionMoveDown(i,j, queue_pop)
        if j-1 >= 0:
            ActionMoveLeft(i,j, queue_pop)
        if j+1 < 3:
            ActionMoveRight(i,j, queue_pop)

    else:
        p = open('nodePath.txt', 'w')
        n = open('Nodes.txt', 'w')
        f = open('NodesInfo.txt', 'w')
        node_info =[]
        d = back_tracking(path_dict, node_state_i, queue_pop)
        print("Goal Reached: ", node_state_gt)
        nodes_write(visited_nodes)
        nodePath_write(best_path)
        info = nodes_info(visited_nodes, path_dict, node_state_i)
        nodes_info_write(info)
        break


