from Coord import *
from TWdata import *
from Functions import *
from make_file import *
from csv_handler import *

PARTICIPANTS = read_participants()
ZONES = read_zones()
TARGETS = read_targets()
SETTINGS = read_settings()
DATA = TWdata(SETTINGS['world'])

def organize_plans(plan_array, zones):
    res = {}
    for plan in plan_array:
        for player in list(plan.keys()):
            if player not in res.keys():
                res[player] = {}
                for zone in list(zones.keys()):
                    res[player][zone] = ''
    i = 0
    zones = list(zones.keys())
    for plan in plan_array:
        for player in plan.keys():
            res[player][zones[i]] += plan[player]
        i += 1
    return res

def main():
    #Set fulls per village

    coord_plans = []
    for zone in ZONES.keys():
        print(zone)
        coord_plans.append(gerar_coord(TARGETS[zone], PARTICIPANTS[zone], DATA, SETTINGS['max_distance'], ZONES[zone][0],ZONES[zone][1],ZONES[zone][2],ZONES[zone][3]))
    organized = organize_plans(coord_plans, ZONES)

    build_send_msgs_script(organized, SETTINGS)
    build_preview_file(organized, ZONES, SETTINGS)

main()