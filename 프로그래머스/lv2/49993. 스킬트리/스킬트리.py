def solution(skill, skill_trees):

    ans=0
    for item in skill_trees:
        level=0
        for s in item:
            req=skill.find(s)
            if level<req:
                break
            elif level==req:
                level+=1
        else:
            ans+=1
    return ans