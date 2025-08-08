par = "Lorem ipsum dolor sit amet consectetur adipiscing elit Curabitur eget bibendum turpis Curabitur scelerisque eros ultricies venenatis mi at tempor nisl Integer tincidunt accumsan cursus"

counts = {}

# Your code here
lower_case_string = par.casefold()
for letter in lower_case_string:
    if letter in counts:
        counts[letter] += 1
    elif letter == " ":
        None
    else: 
        counts[letter] = 1

print(counts)
