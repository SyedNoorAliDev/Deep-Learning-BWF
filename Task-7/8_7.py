def make_album(name,title,tracks=""):
    music_album = {name:title}
    if tracks:
        music_album["tracks"]=tracks
    
    return music_album
print(make_album("Joe","Disco"))
print(make_album("Beth","Disco2"))
print(make_album("Peter","Disco3",5))
