d={}
print(type(d))

d=dict()
print(type(d))

d={1:"one",2:"two"}
print(d)

d={"name":"bincy","age":23,"marks":[40,50,60,70]}
print(d)
print(d["age"])
print(d["marks"])
print(d["marks"][2])

film={
    "name":"ok kanmani",
    "dir":"maniratnam",
    "actor":"Dq",
    "lang":{"mal","tml","tlg"}
}
print(film)

#update

film["name"]="nayakan"
print(film)

film.update({"dir":"kamal hasan"})
print(film)

#insertion

film["char_name"]="velu"
print(film)

film.update({"rating":8.5})
print(film)

# deletion

film={
    "name":"ok kanmani",
    "dir":"maniratnam",
    "actor":"Dq",
    "lang":{"mal","tml","tlg"}
}
del film['dir']
print(film)

# del d
# print(d)

# pop()

film={
    "name":"ok kanmani",
    "dir":"maniratnam",
    "actor":"Dq",
    "lang":{"mal","tml","tlg"}
}
film.pop("dir")
print(film)

#popitem()

film.popitem()
print(film)

# clear()

film.clear()
print(film)

# iteration

film={
    "name":"ok kanmani",
    "dir":"maniratnam",
    "actor":"Dq",
    "lang":{"mal","tml","tlg"}
}

# iterate keys

print(film.keys())
for i in film.keys():
    print (i)

# iterate values

print(film.values())
for i in film.values():
    print (i)

#iterate items

print(film.items())
for i,j in film.items():
    print(i,j,sep=" ")

# nested dictionary

stud={1:{"name":"bincy","age":23},2:{"name":"gowri","age":23},3:{"name":"muhsina","age":23}}
print(stud[1])
print(stud[1]["name"])
print(stud.get(3))


        




