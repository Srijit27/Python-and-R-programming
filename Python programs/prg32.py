d={"Name":"Srijit","Dept":"CSE","College":"HITK"}
print("Original dictionary:",d)
print("Department is:",d["Dept"])

d["Roll"]=2351214
print("New dictionary post insertion is:",d)

del d["College"]
print("New dictionary post deletion is:",d)

d["Name"]="Aryan"
for k in d:
    print(k)
print("Dictionary length is:",len(d))