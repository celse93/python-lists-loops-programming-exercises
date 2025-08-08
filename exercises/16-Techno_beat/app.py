def lyrics_generator(list):
    lyric = ""
    counter = 0

    for x in list:
        if x == 0:
            lyric += "Boom "
            counter = 0
        elif x == 1:
            lyric += "Drop the bass "
            counter += 1
            if counter == 3:
                lyric += "!!!Break the bass!!! "
        
    return lyric
        


# Your code above, nothing to change after this line
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
