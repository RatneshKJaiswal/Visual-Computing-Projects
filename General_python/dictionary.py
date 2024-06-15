dic = {
    "Ram": "God",
    "Knife": "Object",
    124 : "System"
}
print(dic[124])
print(dic.get("Ram"))
print(dic.get(123))

print(dic.keys())

for key in dic.keys():
    print(dic[key])