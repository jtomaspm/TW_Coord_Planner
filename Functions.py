from os import terminal_size
import urllib.parse
from Coord import *


def get_closest_per_target(target, origin):
    res = {}
    for t in target:
        cd = 0
        for o in origin:
            d = Coord(o).distance(Coord(t))
            if cd == 0 or d < cd:
                cd=d
        res[t] = cd
    return res

def get_min_distance(target, origin):
    cd = 0
    for t in target:
        for o in origin:
            d = Coord(o).distance(Coord(t))
            if cd == 0 or d < cd:
                cd=d
    return cd

def get_average_distance(coords1, coords2):
    count1 = 0
    count2 = 0
    dist1 = 0
    dist2 = 0
    for coord1 in coords1:
        for coord2 in coords2:
            dist2 += Coord(coord1).distance(Coord(coord2))
            count2 += 1
        dist1 += dist2/count2
        count1 += 1
        count2 = 0
        dist2 = 0
    return round(dist1/count1, 3)

def encode(s):
    return urllib.parse.quote_plus(s)

def decode(s):
    return urllib.parse.unquote_plus(s)


def get_aldeias_zona(player, DATA, above='None', under='None', left='None', right='None'):
    if above == under == left == right == 'None':
        return DATA.compactP[player]['villages']
    else:
        res = []
        if not above == 'None':
            for v in DATA.compactP[player]['villages']:
                if Coord(v).above(Coord('111|'+ above)):
                    res.append(v)
        if not under == 'None':
            for v in DATA.compactP[player]['villages']:
                if Coord(v).under(Coord('111|'+ under)):
                    res.append(v)
        if not left == 'None':
            for v in DATA.compactP[player]['villages']:
                if Coord(v).left(Coord(left+'|111')):
                    res.append(v)
        if not right == 'None':
            for v in DATA.compactP[player]['villages']:
                if Coord(v).right(Coord(right+'|111')):
                    res.append(v)
        return res

def get_general_priority(participants): #{player: general_priority}
    max_num_fulls = max(participants.values())
    res = {}
    for player in participants.keys():
        res[player] = (10*participants[player])/max_num_fulls
    return res

def get_priorityV(fulls_needed_per_target, general_priority, max_distance, DATA, above='None', under='None', left='None', right='None'):
    res = {}
    for target in fulls_needed_per_target.keys():
        res[target] = {}
        for player in general_priority.keys():
            vills = get_aldeias_zona(player, DATA, above, under, left, right)
            invalid = (get_average_distance([target], vills) > max_distance and fulls_needed_per_target[target]['from'][0] == 'None')
            if len(vills) < 1:
                res[target][player] = 0
            elif invalid:
                res[target][player] = general_priority[player]
            else:
                if fulls_needed_per_target[target]['from'][0] == 'None':
                    res[target][player] = general_priority[player] - ((get_min_distance([target], vills) + 2*get_average_distance([target], vills))/3)
                    res[target][player] += max_distance
                    res[target][player] = round(res[target][player],3)
                else:
                    from_list = fulls_needed_per_target[target]['from']
                    i = max_distance
                    for f in from_list:
                        temp = get_average_distance([f], vills)
                        if i > temp:
                            i = temp
                    if i >= max_distance:
                        res[target][player] = general_priority[player]
                    else:    
                        res[target][player] = general_priority[player] - i
                        res[target][player] += max_distance
                        res[target][player] = round(res[target][player],3)
        print(target + " : " + str(res[target]))
    return res

def get_highest_priority(village):
    if list(village.keys()) == []:
        return ""
    return max(village, key=village.get)

def gerar_coord(fulls_needed_per_target, participants, DATA, max_distance=50, above='None', under='None', left='None', right='None'):
    avalible_fulls = participants
    general_priority = get_general_priority(participants)
    priorityV = get_priorityV(fulls_needed_per_target, general_priority, max_distance, DATA)
    #calculate fulls
    plan = {}
    for village in priorityV.keys():
        while not fulls_needed_per_target[village]['fulls'] == 0:
            highest_priority = get_highest_priority(priorityV[village])
            if highest_priority == "":
                fulls_needed_per_target[village]['fulls'] = 0
            else:
                if avalible_fulls[highest_priority] == 0:
                    priorityV[village].pop(highest_priority)
                else:
                    if priorityV[village][highest_priority] <= 10:
                        print("WARNING: NO MORE FULLS WITHIN MAX_DISTANCE!, filling with fulls from:\n" + highest_priority + " > " + village)
                    if fulls_needed_per_target[village]['fulls'] >= avalible_fulls[highest_priority]:
                        send = avalible_fulls[highest_priority]
                        fulls_needed_per_target[village]['fulls'] = fulls_needed_per_target[village]['fulls'] - avalible_fulls[highest_priority]
                        avalible_fulls[highest_priority] = 0
                        priorityV[village].pop(highest_priority)
                        if not highest_priority in plan.keys():
                            plan[highest_priority] = {}
                        plan[highest_priority][village] = send
                    else:
                        send = fulls_needed_per_target[village]['fulls']
                        avalible_fulls[highest_priority] = avalible_fulls[highest_priority] - fulls_needed_per_target[village]['fulls']
                        fulls_needed_per_target[village]['fulls'] = 0
                        priorityV[village].pop(highest_priority)
                        if not highest_priority in plan.keys():
                            plan[highest_priority] = {}
                        plan[highest_priority][village] = send
    result = {}   
    for pl in plan.keys():
        result[pl] = ""
        for tg in plan[pl].keys():
            result[pl] += str(tg) + " : " + str(plan[pl][tg]) + " fulls \\n"
    return result


