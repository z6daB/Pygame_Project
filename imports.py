from csv import reader


def import_csv(path_to_folder):
    terrain_map = []
    with open(path_to_folder) as level_map:
        layout = reader(level_map, delimiter=',')
        for row in layout:
            terrain_map.append(list(row))
        return terrain_map
