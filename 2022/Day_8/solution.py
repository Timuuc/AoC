doc = open('Day_8/input.txt', 'r')
content = doc.readlines()
doc.close()
score:int = 0

for li in range(0, len(content)):
    if li == len(content) - 1:
        content[li] += '\n'

    for ci in range(0, len(content[li]) - 1):
        tree_h = int(content[li][ci])

        n_x = 0 + ci
        p_x = (len(content[li]) - 2) - ci
        p_y = 0 + li
        n_y = len(content) - li - 1
        
        if n_x < p_x: max_x = p_x
        else:         max_x = n_x
        if n_y < p_y: max_y = p_y
        else:         max_y = n_y
        if max_x < max_y: max = max_y
        else:             max = max_x
        
        xp_vis = True
        xp_trees = 0
        xn_vis = True
        xn_trees = 0
        yp_vis = True
        yp_trees = 0
        yn_vis = True
        yn_trees = 0

        for r in range(1, max + 1):
            if xp_vis:
                if r <= p_x:
                    tree_v = int(content[li][ci + r])
                    if tree_h <= tree_v:
                        xp_vis = False 
                        xp_trees = r
            
            if xn_vis:
                if r <= n_x:
                    tree_v = int(content[li][ci - r])
                    if tree_h <= tree_v:
                        xn_vis = False
                        xn_trees = r

            if yp_vis:
                if r <= p_y:
                    tree_v = int(content[li - r][ci])
                    if tree_h <= tree_v:
                        yp_vis = False
                        yp_trees = r

            if yn_vis:
                if r <= n_y:
                    tree_v = int(content[li + r][ci])
                    if tree_h <= tree_v:
                        yn_vis = False
                        yn_trees = r
            
            test_b = (xp_vis or xn_vis or yp_vis or yn_vis) 
            if not test_b: break

        if test_b:
            if xp_vis: xp_trees = p_x
            if xn_vis: xn_trees = n_x
            if yp_vis: yp_trees = p_y
            if yn_vis: yn_trees = n_y
        
        scenic_score = xp_trees * xn_trees * yp_trees * yn_trees
        if score < scenic_score: score = scenic_score
        

print("The score is: " + str(score))