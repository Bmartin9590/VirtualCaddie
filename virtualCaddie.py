userDict = {
0: "beginner",
1: "average",
2: "pro"
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
print("I will help you choose the right club based on how far you are from the pin (yards)")
userLevel = int(input("What is your skill level? Select 0: Beginner, 1: Average, 2: Pro : " ))
userRange = int(input("How far are you from the pin in yards? "))

for key, value in distDict[userLevel].items():
    if userRange >= key[0] and userRange <= key[1]:
        print("The club that you should be using is " , clubDict[value])