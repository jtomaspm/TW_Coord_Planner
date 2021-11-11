from Functions import *
import urllib.request

class TWdata:

    WORLD = ''
    ally = {}
    player = {}
    village = {}
    compactV = {}
    compactP = {}
    compactT = {}

    def __init__(self, world):
        self.WORLD = world
        self.generate_base()
        self.generate_compactV()
        self.generate_compactP()
        self.generate_compactT()

    def generate_base(self):
        ally_txt = []
        player_txt = []
        village_txt = []

        with urllib.request.urlopen('https://'+self.WORLD+'.tribalwars.com.pt/map/ally.txt') as f:
            ally_txt = f.read().decode('utf-8').split("\n")
        with urllib.request.urlopen('https://'+self.WORLD+'.tribalwars.com.pt/map/player.txt') as f:
            player_txt = f.read().decode('utf-8').split("\n")
        with urllib.request.urlopen('https://'+self.WORLD+'.tribalwars.com.pt/map/village.txt') as f:
            village_txt = f.read().decode('utf-8').split("\n")


        ally_model = [ 'name', 'tag', 'members', 'villages', 'points', 'all_points', 'rank']
        player_model = [ 'name', 'tribe', 'villages', 'points', 'rank']
        village_model = ['id', 'name', 'x', 'y', 'player', 'points', 'rank']

        for line in ally_txt:
            line = line.split(",")
            if len(line) > 1:
                temp = {}
                for i in range(len(ally_model)):
                    temp[ally_model[i]] = line[i+1]
                self.ally[line[0]] = temp

        for line in player_txt:
            line = line.split(",")
            if len(line) > 1:
                temp = {}
                for i in range(len(player_model)):
                    temp[player_model[i]] = line[i+1]
                self.player[line[0]] = temp
                

        for line in village_txt:
            line = line.split(",")
            if len(line) > 1:
                temp = {}
                for i in range(len(village_model)):
                    temp[village_model[i]] = line[i]
                self.village[temp['x']+"|"+temp['y']] = temp
    
    def generate_compactV(self):
        for k in self.village.keys():
            v = self.village[k]
            p = v['player']
            if not p in self.player.keys():
                temp = {'x': v['x'], 'y': v['y'], 'player' : 'BB', 'tribe': ''}
            else:    
                if not self.player[p]['tribe'] in self.ally.keys():
                    temp = {'x': v['x'], 'y': v['y'], 'player' : decode(self.player[p]['name']), 'tribe': ''}
                else:
                    a = self.ally[self.player[p]['tribe']]['tag']
                    temp = {'x': v['x'], 'y': v['y'], 'player' : decode(self.player[p]['name']), 'tribe': decode(a)}
                
            
            self.compactV[temp['x']+"|"+temp['y']] = temp
    
    def generate_compactP(self):
        for k in self.compactV.keys():
            v = self.compactV[k]
            if not v['player'] in self.compactP.keys():
                self.compactP[v['player']] = {'villages': [], 'tribe': v['tribe']}

            self.compactP[v['player']]['villages'].append(v['x']+"|"+v['y'])

    def generate_compactT(self):
        for k in self.compactV.keys():
            v = self.compactV[k]
            if not v['tribe'] in self.compactT.keys():
                self.compactT[v['tribe']] = {}

            if not v['player'] in self.compactT[v['tribe']].keys():
                self.compactT[v['tribe']][v['player']] = []

            self.compactT[v['tribe']][v['player']].append(v['x']+"|"+v['y'])
