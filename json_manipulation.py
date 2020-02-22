import json


def importToJson(lvl, name):
    with open("level_data/editor_level.json", "r") as f:
        list_levels = json.load(f)
    level = {"level_name": name, "WR": 0, "level_composition": lvl}
    list_levels.append(level)
    with open("level_data/editor_level.json", "w") as f:
        json.dump(list_levels, f)


def overwiteLevel(level, name):
    with open("level_data/editor_level.json", "r") as f:
        list_levels = json.load(f)
    for lvl in list_levels:
        if lvl["level_name"] == name:
            lvl["level_composition"] = level
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


def recupLevelNames():
    with open("level_data/editor_level.json", "r") as f:
        list_levels = json.load(f)
    listNames = []
    for lvl in list_levels:
        listNames.append(lvl["level_name"])
    return listNames


def recupTimes():
    with open("level_data/times.json", "r") as f:
        list_scores = json.load(f)
    listNames = []
    listTimes = []
    for item in list_scores:
        listNames.append(item["pseudo"])
        listTimes.append(item["time"])
    return listNames, listTimes


def saveTime(time, name, lN):
    with open("level_data/times.json", "r") as f:
        scoreboard = json.load(f)
    if name in lN:
        for item in scoreboard:
            if item["pseudo"] == name:
                item["time"] = time
    else:
        scoreboard.append({"pseudo": name, "time": time})
    orderedScoreboard = orderScoreboard(scoreboard)
    with open("level_data/times.json", "w") as f:
        json.dump(orderedScoreboard, f, indent=2)


def orderScoreboard(sb):
    return sorted(sb, key=lambda i: i["time"])


def saveLevelTime(level, time, type_):
    with open("level_data/" + type_ + "_level.json", "r") as f:
        list_levels = json.load(f)
    for lvl in list_levels:
        if lvl["level_composition"] == level:
            if lvl["WR"] > time or lvl["WR"] == 0:
                lvl["WR"] = time
    with open("level_data/" + type_ + "_level.json", "w") as f:
        json.dump(list_levels, f)

