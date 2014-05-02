import csv

teams = csv.reader(open('CBBRootingQuiz.csv', 'rU').readlines()[1:])

stats_dict = {}
stats_dict["tempo"] = []
stats_dict["off"] = []
stats_dict["def"] = []
stats_dict["pyth"] = []
stats_dict["efg"] = []
stats_dict["ftr"] = []
stats_dict["blocks"] = []
stats_dict["assists"] = []
stats_dict["deftype"] = []
stats_dict["threes"] = []

for t in teams:
	stats_dict["tempo"].append(float(t[1]))
	stats_dict["off"].append(float(t[2]))
	stats_dict["def"].append(float(t[3]))
	stats_dict["pyth"].append(float(t[4]))
	stats_dict["efg"].append(float(t[5]))
	stats_dict["ftr"].append(float(t[6]))
	stats_dict["blocks"].append(float(t[7]))
	stats_dict["assists"].append(float(t[8]))
	stats_dict["deftype"].append(float(t[9]))
	stats_dict["threes"].append(float(t[10]))

for k in stats_dict:
	print k
	sl = sorted(stats_dict[k], reverse=True)
	print "[%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s]" %(sl[0], sl[35], sl[70], sl[105], sl[140], sl[175], sl[210], sl[245], sl[280], sl[315], sl[350]) 