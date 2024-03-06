import os
import sys

def load_map(file_path):
#    room_question = input("what room you are in now? ")
    new_dict = dict()
    filename = os.path.join(sys.path[0], file_path + ".txt")
    open(filename,"r")
    with open(filename, "r") as f:
        for line in f:
            lines = line.split(":")
            new_dict[lines[0]]=lines[1]

        #for x in new_dict.keys():
        #  print(x +": ["+new_dict[x].split("\n")[0]+"]")

    return new_dict


def simplify_testimony(chat, rooms):
    c = ["red", "blue", "green", "yellow", "brown", "pink", "orange"]
    if ("voted" in chat) or ("vote" in chat):
        return chat.strip("\n")

    x = chat.split(":")
    r = 0
    l = 0
    color = ""
    room = ""
    new_words=[]
    for words in x[1].split():
        new_words.append(words.strip(".,?!"))
    for y in new_words:
        if y in c:
            color = y
            l = 1
        if y in rooms.keys():
            room = y
            r = 1

    if r != 1:
        return ""
    if l ==1 and r == 1: 
        return str(x[0]) + ": " + color + " in " + room
    else: 
        return str(x[0]) + ": " + str(x[0]) + " in " + room

def load_chat_log(filename, rooms):
    x = []
    filename = os.path.join(sys.path[0], filename+ ".txt")
    open(filename,"r")
    with open(filename, "r") as f:
        for line in f:
            
            if x != "":
                x.append(simplify_testimony(line,rooms))
            else:
                pass
    return x

def tally_votes(chat_log):
    votes = dict(red = 0, blue = 0, green = 0, yellow = 0, brown= 0, pink = 0, orange = 0, skip = 0)
    y = chat_log
    #Who voted who?!
    for x in y:
        if "voted" in x:
            #Who skiped?!
            if "skip" not in x:
                votes[(x.split()[2])] += 1
            else:
                votes[(x.split()[2])] += 1
    return votes

def get_paths(chat_log):
    y = chat_log
    paths = dict(red = [], blue = [], green = [], yellow = [], brown= [], pink = [], orange = [] )
    for x in y:

        z = x.split(":")
        if "voted" in x:
            pass
        elif z[0] not in paths.keys():
            pass
        else:
            if z[0] == z[1].split()[0]:
                paths[z[0]].append(z[1].split()[2])
            else:
                pass
    
    return paths

def get_sus_paths(path_dict, rooms):
    z = 0
    sus = []
    for x in path_dict.keys():
        for y in path_dict[x]:
            if z == (len(path_dict[x])-1):
                break
            elif y in rooms[(path_dict[x])[z+1]]:
                #print("not sus")
                pass
            else:
                #Here where do we find the sus
                sus.append(x)
            z+=1
        z = 0
    return sus

def main():
    mapLocation = "skeld"
    chatlogLocation = "chatlog" 
    skeld_rooms = load_map(mapLocation)
    loadChatLog= load_chat_log(chatlogLocation,skeld_rooms)
    votes = tally_votes(loadChatLog)
    paths = get_paths(loadChatLog)
    get_sus = get_sus_paths(paths, skeld_rooms)
    
    #Problem 1: Loading the Map
    print("the maps where you can go: "+ str(skeld_rooms) + '\n')
    #Problem 3: Loading Chat from a File
    print("A little chat: " + str(loadChatLog) +'\n')
    #Problem 4: Tallying Votes
    print("Who voted: " + str(votes) +'\n')
    #Problem 5: Identifying Paths
    print("Colours paths: " + str(paths) + '\n')
    #Problem 6: Who is Lying?
    print("List of Sus : " + str(get_sus) + "\n")
main() 
