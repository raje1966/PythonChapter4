myDict = {
    "Pankha" : "Fan",
    "Dabba" : "Box",
    "Vastu" : "Item"
}
print("options are", myDict.keys())
a = input("Enter the Hindi word\n")
print("The meaning of your word is:", myDict.get(a))