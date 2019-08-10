# Problem name: Bot Saves Princess

def get_corner_indices(dim: int) -> list:
    return [[0,0], [0,dim-1], [dim-1,0], [dim-1,dim-1]] 

def get_princess_location(dim: int, grid: list) -> list:
    corners = get_corner_indices(dim)        
    for cidx in range(4):
        loc = corners[cidx]
        ploc = cidx
        if grid[loc[0]][loc[1]] == 'p':                                        
            break
    return ploc

def displayPathtoPrincess(dim: int, grid: list) -> None: 
    if len(grid) != dim:
        return

    corner_dict = {
        0 : ['UP', 'LEFT'],
        1 : ['UP', 'RIGHT'],
        2 : ['DOWN', 'LEFT'],
        3 : ['DOWN', 'RIGHT']
    }  

    def get_path_to_target(dim: int, target_ref: int) -> list:
        num_steps = dim // 2
        steps_to_tgt = corner_dict[target_ref]
        path = []
        for i in range(num_steps):
            path.append(steps_to_tgt[0])
            path.append(steps_to_tgt[1])
        return path
    
    ploc = get_princess_location(dim, grid)    
    path = get_path_to_target(dim, ploc)

    for step_direction in range(len(path)):
        print(path[step_direction])