import csv

def read_zones():
    res = {}
    with open('input/zones.csv', mode='r') as zones_csv:
        csv_dict = csv.DictReader(zones_csv)
        for row in csv_dict:
            res[row['Zone']] = [row['above'],row['under'],row['left'],row['right']]
    return res

def read_participants():
    res = {}
    with open('input/participants.csv', mode='r') as participants_csv:
        csv_dict = csv.DictReader(participants_csv)
        first = True
        for row in csv_dict:
            if first:
                first = False
                for k in row.keys():
                    if not k == 'Nome':
                        res[k] = {}
            for k in res.keys():
                res[k][row['Nome']] = int(row[k])
    return res

def read_targets():
    res = {}
    with open('input/targets.csv', mode='r') as targets_csv:
        csv_dict = csv.DictReader(targets_csv)
        for row in csv_dict:
            zone = row['Zone']
            if not zone in res.keys():
                res[zone] = {}
            targets = row['Targets'].split(" ")
            for target in targets:
                fulls = row['Fulls']
                res[zone][target] = {}
                res[zone][target]['fulls'] = int(fulls)
                res[zone][target]['from'] = ['None']

    return res

def read_settings():
    res = {}
    with open('input/settings.csv', mode='r') as settings_csv:
        csv_dict = csv.DictReader(settings_csv)
        for row in csv_dict:
            res['date'] = row['date']
            res['time'] = row['time']
            res['title'] = row['title']
            res['world'] = row['world']
            res['max_distance'] = int(row['max_distance'])
    return res
