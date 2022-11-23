def solution(id_pw, db):
    d=dict()
    
    for item in db:
        id,pw=item[0],item[1]
        d[id]=pw
    
    id,pw=id_pw[0],id_pw[1]
    
    if id not in d:
        return "fail"
    elif d[id]!=pw:
        return "wrong pw"
    else:
        return 'login'