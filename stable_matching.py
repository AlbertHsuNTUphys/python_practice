def stable_matching(**kwargs):
    if kwargs['who_propose'] == 'men':
        proposer = kwargs['men']
        be_proposed = kwargs['women']
    else:
        proposer = kwargs['women']
        be_proposed = kwargs['men']

    preference = kwargs['preference_dict']

    match = {}
    for person in proposer:
        match[person] = None

    while None in match.values():
        for person in match:
            #print('now in action:', person)
            if match[person] != None:
                #print('    ', person, ' is not None')
                continue
            for t in preference[person]:
                #print('    target:', t)
                if t in match.values():
                    #print('    ', t, 'is matched')
                    for p in match:
                        if match[p] == t:
                            op = p
                            #print('    opponent:', op)
                            break
                    for s in preference[t]:
                        if s == person:
                            match[person] = t
                            match[op] = None
                            #print('    found person first')
                            break
                        if s == op:
                            #print('    found op first')
                            break
                    if match[person] != None:
                        break
                else:
                    #print('    ', t, 'is not matched')
                    match[person] = t
                    break
    return match

if __name__ == '__main__':
    men_input = ['men0', 'men1', 'men2'] 
    women_input = ['women0', 'women1', 'women2']
    preference_dict_input = {
    'men0': ['women0', 'women1', 'women2'],
    'men1': ['women1', 'women2', 'women0'],
    'men2': ['women1', 'women0', 'women2'],
    'women0': ['men2', 'men0', 'men1'],
    'women1': ['men2', 'men1', 'men0'],
    'women2': ['men1', 'men2', 'men0']
    }

    #print(stable_matching(men= men_input, women=women_input, preference_dict = preference_dict_input, who_propose = "men"))
    #print(stable_matching(men= men_input, women=women_input, preference_dict = preference_dict_input, who_propose = "women"))
        
    
