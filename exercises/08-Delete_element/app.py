people = ['juan','ana','michelle','daniella','stefany','lucy','barak']

def delete_person(person_name):
    # Your code here
    people_copy = people.copy()
    for i in people:
        if i == person_name:
            people_copy.remove(i)
    return people_copy

    
# Don't delete anything below
print(delete_person("daniella"))
print(delete_person("juan"))
print(delete_person("emilio"))
