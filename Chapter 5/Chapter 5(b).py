a={
    "fast":"Very Quick",
    "shivesh":"A guy",
    "marks":[1,2,3],
    "anotherdict":{"shivesh":"nice guy"},
    1:2
}

print(a.keys())
print(type(a.keys()))
print(list(a.keys()))

print(a.values())
print(a.items())

print(a)
updated_a={
    "Lovish":"Me",
    "marks":[45,56,67]
}
a.update(updated_a)
print(a)
 
print(a.get("shivesh")) 
print(a.get("shivesh2")) #---> Get doesn't throw an error whereas print(a["shivesh2"]) throws an error

