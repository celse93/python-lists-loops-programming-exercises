the_bools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

# Your code here

new_list = list(map(lambda item: "wiki" if item == 1 else "woko", the_bools))

print(new_list)

