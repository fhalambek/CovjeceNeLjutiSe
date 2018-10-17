from time import sleep

def main(board, dice, color, pieces_s):

    start = color * 10 + 1
    if(color == 0): start = 41
    positions = board[color]

    danger = [0, 0, 0, 0]
    danger_opt = [0, 0, 0, 0]
    
    pieces = []                                                                 #pretvorba ulaza u brojeve
    if 'M' in pieces_s:
        pieces += [0]
    if 'I' in pieces_s:
        pieces += [1]
    if 'O' in pieces_s:
        pieces += [2]
    if 'C' in pieces_s:
        pieces += [3]


    
    
    options = []
    positions_relative = []
    for i in range(4):                                                          #polja na koja je moguce doci
        if(i in pieces): options += [positions[i] + dice]
        else: options += [0]

        if(positions[i] < 0):
            options[i] = positions[i] - dice
        if(positions[i] == 0 and dice == 6):
            options[i] = 10*color+1
        
        if(options[i] > 40):
            options[i] -= 40

        if(positions[i] >= 1): positions_relative += [positions[i] - start + 1]                        #relativna pozicija
        else: positions_relative += [positions[i]]
        if(positions_relative[i] < 1 and positions[i] >= 1): positions_relative[i] += 40              #(u odnosu na vlastito startno polje)

        if(positions_relative[i] < start and positions_relative[i] + dice >= start and i in pieces):       #spas
            options[i] = -(positions_relative[i] + dice - 40)
            #print(options)
            return("MIOC"[i])
    

    #print(options, pieces, positions, positions_relative)
    
    optmx = -5
    for i in pieces:                                                            #odabir najudaljenije figure
        if(positions_relative[i] >= optmx):
            optmx = positions_relative[i]
            pref = i;


    for i in range(4):
        for j in range(4):                                                      #ofenziva
            if(j == color): continue
            for k in range(4):
                if(board[j][k] == options[i] and i in pieces):
                    #print("pojeo")
                    return("MIOC"[i])
                                                        
    
    for i in range(4):
        if(i == color): continue                                                #defenziva - analiza
        for j in range(4):
            for k in range(4):
                if (k in pieces) == False: continue
                oppstart = i*10+1
                
                a = board[i][j]
                b = positions[k]

                if(a <= 0):
                    if(b == oppstart):
                        danger[k] = 1
                    continue
                if(b <= 0):
                    danger[k] = 0
                    continue
                
                difr = b - a;
                if(difr < 1): difr += 40
                
                if(difr <= 6):
                    #print("opasno", i, j, k)
                    trig = 0
                    
                    if(i != 0):
                        if(b >= oppstart and a < oppstart and danger[k] == 0):
                            danger[k] = 0
                            trig = 1
                    else:
                        if(b < 10 and a > 30 and danger[k] == 0):
                            danger[k] = 0
                            trig = 1
                            
                    if(trig == 0):
                        danger[k] = 1
                    
                
                #print(i, j, k, difr, "MIOC"[k], end = "-->")
                
                b = options[k]

                if(a <= 0):
                    if(b == oppstart):
                        danger_opt[k] = 1
                    continue
                if(b < 0):
                    danger_opt[k] = 0
                    continue
                
                difr = b - a;
                if(difr < 1): difr += 40
                
                if(difr <= 6):
                    trig = 0
                    
                    if(i != 0):
                        if(b >= oppstart and a < oppstart and danger_opt[k] == 0):
                            danger_opt[k] = 0
                            trig = 1
                    else:
                        if(b < 10 and a > 30 and danger_opt[k] == 0):
                            danger_opt[k] = 0
                            trig = 1
                            
                    if(trig == 0):
                        danger_opt[k] = 1
                #print(difr, "MIOC"[k])

    #print(danger, danger_opt)
                
    for i in range(3, -1, -1):                                                  #defenziva - akcija
        if(danger_opt[i] == 1):
            continue
        if(danger[i] == 1 and (i in pieces)):      
            return("MIOC"[i])
    

    active = 0
    for i in range(4):
        if(positions[i] >= 1): active += 1
        
    if(dice == 6 and active < 2):
        for i in range(3, -1, -1):                                              #izlaz novih figura
            if positions[i] == 0 and i in pieces:
                return("MIOC"[i])
    
    for i in range(4):                                                          #oslobadjanje pocetnog polja
        if(positions_relative[i] == 1 and (i in pieces)): return("MIOC"[i])

    

    #print(dice, "d   ", danger, "dopt", danger_opt)
    #sleep(10)


    #print("tu sam")
    return("MIOC"[pref])
    return(pieces_s[-1])


#print(main([[-1, -2, 10, 0], [-1, 39, 22, 34], [0, -2, -3, -4], [0, 0, 3, -4]], 2, 1, "IOC"))
