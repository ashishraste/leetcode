from bot_saves_princess import *

def get_5x5_grid():
    dim = 5
    grid = []
    for i in range(2):
        grid.append('-----')
    grid.append('--m--')
    grid.append('-----')
    grid.append('----p')
    return [grid, 5]

def test_corner_indices():
    dim = 5
    assert get_corner_indices(dim) == [[0,0], [0,4], [4,0], [4,4]]
    assert get_corner_indices(dim) != [[0,0], [0,4], [4,4], [0,4]]

def test_princess_location():
    grid, dim = get_5x5_grid()
    assert get_princess_location(dim, grid) == 3
    assert get_princess_location(dim, grid) != 0

# def test_path_to_princess():
#     grid, dim = get_5x5_grid()
#     assert displayPathtoPrincess(dim, grid) == ['DOWN', 'RIGHT', 'DOWN', 'RIGHT']
#     assert displayPathtoPrincess(dim, grid) != ['DOWN', 'LEFT', 'DOWN', 'LEFT']
#     assert displayPathtoPrincess(dim, grid) != ['UP', 'LEFT', 'UP', 'LEFT']
#     assert displayPathtoPrincess(dim, grid) != ['UP', 'RIGHT', 'UP', 'RIGHT']
