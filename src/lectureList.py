from copy import deepcopy
import json

data = []

# read file line by line
for line in open('lecture.txt'):
    data.append(line)
data = data[2:-1]

# remove \n in line
for line in range(len(data)):
    data[line] = data[line].replace("\n", "")

lecture = {
    "name": "",
    "score": "",
    "type": "",
    "teacher": "",
    "classNum": "",
    "className": "",
    "selectLimit": "",
    "selected": "",
    "selectble": "",
    "classTimeList": []
}
lectureList = []

# convert lecture txt to lecture data struct
for line in data:
    line = line.split(",")

    lecture["name"] = line[0][9:]
    lecture["score"] = line[1]
    lecture["type"] = line[2]
    lecture["teacher"] = line[3]
    lecture["classNum"] = line[4]
    lecture["className"] = line[5]
    lecture["selectLimit"] = line[6]
    lecture["selected"] = line[7]
    lecture["selectble"] = line[8]

    # save classtime list into data struct
    lecture["classTimeList"] = []
    for i in range(9, len(line)):
        line[i] = line[i].replace("\"", "")
        line[i] = line[i].replace("节1", "节]")
        if line[i] == "":
            line[i] = "该课程暂无上课时间"
        lecture["classTimeList"].append(line[i])

    lectureList.append(deepcopy(lecture))

with open("lectureList.json", 'w', encoding="utf-8") as f:
    f.write("{\"list\":")
    f.write(json.dumps(lectureList, indent=4, sort_keys=True,  ensure_ascii=False)+"\n")
    f.write("}")

# Debug print
print(lectureList)
