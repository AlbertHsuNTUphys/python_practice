class Player:
    def __init__(self):
        self.name = ''
        self.eff = float()
        self.team = None
    
    def addData(self, line, dublist):
        val = line.split(',')
        (name, team, g_s, gs_s, mp_s, fgm_s, fga_s, ftm_s, fta_s, trb_s,
                ast_s, stl_s, blk_s, tov_s, pf_s, pts_s) = tuple(val)
        g, gs, mp, fgm, fga, ftm, fta, trb, ast, stl, blk, tov, pf, pts = (
                float(g_s), float(gs_s),
                float(mp_s), float(fgm_s),
                float(fga_s), float(ftm_s),
                float(fta_s), float(trb_s),
                float(ast_s), float(stl_s),
                float(blk_s), float(tov_s), 
                float(pf_s), float(pts_s))

        self.team = team
        self.name = name
        if self.team == 'TOT':
            dublist.append(self.name)

        if (g<=10) or (mp<=5):
            return False
        else:
            self.eff = (((pts + trb + ast + stl + blk) - (fga - fgm) - (fta - ftm)
                - tov ))
            return True

    def __lt__(self, other):
        if self.eff < other.eff:
            return True
        else:
            return False

def reading_file(filename):
    with open(filename,"r",encoding='utf-8') as f: 
        f.readline()
        alllines = f.readlines()
        allplayer = [Player() for i in range(len(alllines)-1)]
        dub = []
        dellist = []
        for i in range(len(alllines)-1):
            if not allplayer[i].addData(alllines[i], dub):
                dellist.append(i)
        for i in reversed(dellist):
            del allplayer[i]

        for pl in allplayer:
            if (pl.name in dub) and (pl.team != 'TOT'):
                del pl
        allplayer.sort(reverse=True)
        return [allplayer[i].name for i in range(5)]




if __name__ == "__main__":
    print(reading_file("1819basketball_stat_dub.csv")) 
