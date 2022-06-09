a = {"AGG":{"ATA":1}}


# print(a)
# a.setdefault("AGG", {})["ATA"] = 2
# print(a)
# a.setdefault("ATA", {})["ATC"] = 1
# print(a)

# for key in a.get("AGG").keys():
#     print(a[key])


mylist = ["a", "b", "a", "c", "c"]
mylist = list(dict.fromkeys(mylist))
print(mylist)