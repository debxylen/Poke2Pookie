import re, json


fcatches = open("log_catches.json","r")
catches = json.loads(fcatches.read())
fcatches.close()

with open("legendary.txt", "r", encoding='utf8') as f:
    legendaries = f.read().split("\n")
with open("mythical.txt", "r", encoding='utf8') as f:
    mythics = f.read().split("\n")

def jsonwriter(i,fn):
    status = 0
    try:
        with open(fn, "w") as fw:
            fw.write(json.dumps(i, indent=1))
        status = 1
    except:
        status = 0
    return status


def congrats(text,username,log=True):
    global catches
    p1 = r"(You caught.*)"
    textp1 = re.search(p1,text).group(1)
    pattern = r"You\s+caught\s+a\s+Level\s+(\d+)\s+(\w+:\w+:)\s+\((\d+\.\d+)%\)"
    match = re.search(pattern, textp1)
    if match:
        level = match.group(1)
        pokemon = match.group(2).replace(":female:","♀️").replace(":male:","♂️")
        percentage = match.group(3)
        datadict = {"name": pokemon, "level": level, "iv": percentage}
        if log==False:
            return {"user": username, "name": pokemon, "level": level, "iv": percentage}
        try:
            catches[username].append(datadict)
        except:
            catches[username] = []
            catches[username].append(datadict)
        rs = jsonwriter(catches, "log_catches.json")
        return {"user": username, "name": pokemon, "level": level, "iv": percentage}

def get_catches(user):
    global catches
    try:
        cn = len(catches[user])
    except:
        return 0 
    return cn

def extract_alphanumeric(text):
    res = "".join(re.split("[^a-zA-Z]*", text))
    return res

def israre(name):
    if name in legendaries:
        return ["Legendary",True]
    elif name in mythics:
        return ["Mythical",True]
    else:
        return ["Common",True]

def format_catch(c):
    r = f"[Added to user's caught list]\n**{israre(c['name'])[0]}**\nPokemon caught: {c['name']}\nLevel: {c['level']}\nIV: {c['iv']}\n\nTotal catches by <@{c['user']}> logged: {get_catches(c['user'])}"
    return r

