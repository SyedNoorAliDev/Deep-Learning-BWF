def make_album(name,title,tracks=""):
    music_album = {name:title}
    if tracks:
        music_album["tracks"]=tracks
    
    return music_album
i=0
while i < 5:
    name = input("Enter your name: ")
    title = input("Enter the title of the track: ")
    track = int(input("Enter Number of tracks: "))
    print(make_album(name,title,track))
    i+=1
