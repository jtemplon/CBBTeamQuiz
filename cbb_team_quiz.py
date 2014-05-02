import csv

#Quiz Intro
def ask_question(question):
    val = input(question)
    if 1 <= val <= 8:
        return val
    else:
        print "Please enter valid value"
        val = ask_question(question)
        return val

print "For the following statements select on a scale of 1 (strongly disagree) to 8 (strongly agree) how much the qualities of the team would affect your enjoyment when watching them play"
print ""
print ""

care_vals = {}

care_vals["pyth"] = ask_question("1. Is Really Good: ")
care_vals["tempo"] = ask_question("2. Plays Fast: ")
care_vals["off"] = ask_question("3. Plays Great Offense: ")
care_vals["def"] = ask_question("4. Plays Great Defense: ")
care_vals["threes"] = ask_question("5. Shoots A Lot of Threes: ")
care_vals["assists"] = ask_question("6. Moves The Ball Well: ")
care_vals["blocks"] = ask_question("7. Blocks A Lot of Shots: ")
care_vals["efg"] = ask_question("8. Shoots The Ball Well: ")
care_vals["ftr"] = ask_question("9. Has A Lot of Free Throws: ")
care_vals["deftype"] = ask_question("10. Plays Man Defense: ")

data_vals = {}

data_vals["tempo"] = [58.5, 63.5, 64.9, 65.8, 66.8, 67.8, 69.3, 75.6]
data_vals["off"] = [87.7, 96.6, 100.1, 103.1, 105.3, 108.2, 111.3, 124.1]
data_vals["def"] = [121.9, 111.6, 109.0, 106.3, 104.1, 101.6, 97.8, 88.5]
data_vals["pyth"] = [0.054, 0.192, 0.314, 0.406, 0.514, 0.631, 0.771, 0.952]
data_vals["efg"] = [42.1, 46.5, 47.7, 48.9, 49.9, 51.2, 52.4, 58.9]
data_vals["ftr"] = [58.9, 72.9, 76.3, 79.8, 82.6, 85.0, 89.4, 113.0]
data_vals["blocks"] = [3.4, 6.5, 7.7, 9.0, 10.1, 11.3, 12.6, 19.9]
data_vals["assists"] = [37.2, 46.1, 48.6, 50.3, 52.3, 54.5, 57.5, 65.8]
data_vals["deftype"] = [-9.2, -1, 2, 4.1, 6.3, 8.7, 11.4, 20.4]
data_vals["threes"] = [19.3, 27.5, 29.7, 31.7, 33.8, 35.4, 38.4, 47.8]

ideal_vals = {}
for key in data_vals:
    ideal_vals[key] = data_vals[key][care_vals[key]-1]

top_team = ""
top_score = 100

#print ideal_vals.keys()

teams = csv.reader(open('CBBRootingQuiz.csv', 'rU').readlines()[1:])
for row in teams:
    #print row
    team_name = row[0]
    team_score = abs(float(row[1])-ideal_vals["tempo"])/2.7+ \
                 abs(float(row[2])-ideal_vals["off"])/6.7+ \
                 abs(float(row[3])-ideal_vals["def"])/6.3+ \
                 abs(float(row[4])-ideal_vals["pyth"])/0.239+ \
                 abs(float(row[5])-ideal_vals["efg"])/2.8+ \
                 abs(float(row[6])-ideal_vals["ftr"])/8.6+ \
                 abs(float(row[7])-ideal_vals["blocks"])/2.9+ \
                 abs(float(row[8])-ideal_vals["assists"])/5.4+ \
                 abs(float(row[9])-ideal_vals["deftype"])/5.9
    if team_score < top_score:
        top_score = team_score
        top_team = team_name
    else:
        pass

print "You should watch %s" %(top_team)