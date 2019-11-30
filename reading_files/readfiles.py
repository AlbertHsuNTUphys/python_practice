import decimal
def reading_file(filename):
    with open(filename,"r",encoding='utf-8') as f:
        f.readline()
        line = f.readline().strip()
        top5 = [(-9999999999999999999999, 'name') for i in range(5)]
        skip = []
        while line != '':
            val = line.split(',')
            (name, team, g_s, gs_s, mp_s, fgm_s, fga_s, ftm_s, fta_s, trb_s,
                    ast_s, stl_s, blk_s, tov_s, pf_s, pts_s) = tuple(val)
            g, gs, mp, fgm, fga, ftm, fta, trb, ast, stl, blk, tov, pf, pts = (
                    decimal.Decimal(g_s), decimal.Decimal(gs_s),
                    decimal.Decimal(mp_s), decimal.Decimal(fgm_s),
                    decimal.Decimal(fga_s), decimal.Decimal(ftm_s),
                    decimal.Decimal(fta_s), decimal.Decimal(trb_s),
                    decimal.Decimal(ast_s), decimal.Decimal(stl_s),
                    decimal.Decimal(blk_s), decimal.Decimal(tov_s), 
                    decimal.Decimal(pf_s), decimal.Decimal(pts_s))
            if (name in skip) or (g<=10) or (mp<=5):
                line = f.readline()
                continue
            eff = ((pts + trb + ast + stl + blk) - (fga - fgm) - (fta - ftm)
                    - tov )
            if team == 'TOT':
                if (eff, name) in top5:
                    top5.remove((eff, name))
                    top5.append((-99999999999999999999999999, 'name'))
                skip.append(name)
            # if name == 'Karl-Anthony Towns':
                # print(line)
                # print(pts, trb, ast, stl, blk, fga, fgm, fta, ftm, tov )
                # print(eff)
            record = (eff, name)
            if record > min(top5):
                top5.remove(min(top5))
                top5.append(record)
            line = f.readline().strip()
    top5.sort()
    # print(top5)
    return [top5[4-i][1] for i in range(5)]

if __name__ == "__main__":
    print(reading_file('./1819basketball_stat_dub.csv'))
    # reading_file('./1819basketball_stat_dub.csv')
