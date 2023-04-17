userDict = {
0: "beginner",
1: "average",
2: "pro"
}

userLie = {
0: "Fairway",
1: "Rough",
2: "Sand"
}

clubDict = {
0: "Driver",
1: "3 wood",
2: "Hybrid",
3: "3 Iron",
4: "4 Iron",
5: "5 Iron",
6: "6 Iron",
7: "7 Iron",
8: "8 Iron",
9: "Pitching Wedge",
10: "Sand Wedge"
}

distDict = {
0 : {
(190, 300) : 0,
(170,189) : 1,
(125,169) : 4,
(120, 124) : 5,
(115, 119) : 6,
(105, 114) : 7,
(95, 104): 8,
(70, 94) : 9,
(55, 69) : 10,
},
1: {
(220, 300) : 0,
(210, 219) : 1,
(160, 209) : 4,
(155, 159) : 5,
(145, 154) : 6,
(140, 144) : 7,
(130, 139) : 8,
(100, 129) : 9,
(80, 99) : 10
},
2: {
(250, 330): 0,
(225, 249): 1,
(205, 224): 2,
(180, 204): 3,
(170, 179): 4,
(165, 169): 5,
(160, 164): 6,
(150, 159): 7,
(140, 149): 8,
(100, 139): 9,
(95, 109): 10
}}

print( "****** WELCOME TO VIRTUAL CADDY! ******")
print("I will help you choose the appropriate club based on how far you are from the pin (yards)")
userLevel = int(input("What is your skill level? Select 0: Beginner, 1: Average, 2: Pro = " ))
userRange = int(input("How far are you from the pin in yards? "))
userLie = input("What is your lie? Select 0: Fairway, 1: Rough, 2: Sand, 3: Other = ")

lie_options = [("1", "club up"), ("2", "use a sandwedge if near the green, otherwise use the club below"), ("3", "Punch out and get it back on the fairway the best you can")]

for option in lie_options:
    if userLie == option[0]:
        print("Recommendation:", option[1])
        if option[0] == "1":
            userRange += 15
            print("Distance adjustment: +15 yards")
        break

"""if userLie == "1":
    userRange += 15
    print("I suggest clubbing up based on your lie.")
elif userLie == "2":
    print("If your near the green, I would use a sandwedge, if not use the club below!")
elif userLie == "3":
    print("I would suggest get it back on the fairway the best you can!")"""

for key, value in distDict[userLevel].items():
    if userRange >= key[0] and userRange <= key[1]:
        print("The club that you should be using is ", clubDict[value])
