import json


def importToJson(lvl, name):
    with open("level_data/editor_level.json", "r") as f:
        list_levels = json.load(f)
    level = {"level_name": name, "level_composition": lvl}
    list_levels.append(level)
    with open("level_data/editor_level.json", "w") as f:
        json.dump(list_levels, f)


def deleteLevel(listLevels, i):
    with open("level_data/editor_level.json", "w") as f:
        listLevels.pop(i)
        json.dump(listLevels, f)
    i = 0
    for lvl in listLevels:
        lvl.i = i
        i += 1
    return listLevels
