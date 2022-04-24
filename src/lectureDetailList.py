import json
import re
from copy import deepcopy

def convert(classtime):
    detailList = []

    for i in range(len(classtime)):
        # Initial data struct
        detail = {
            "isSingWeek": False,
            "isEvenWeek": False,
            "weekBegin": 0,
            "weekEnd": 0,
            "week": "",
            "periodBegin": "0",
            "periodEnd": "0",
            "classroom": ""
        }

        # only singular week
        if "单" in classtime[i]:
            detail["isSingWeek"] = True
        # only even week
        if "双" in classtime[i]:
            detail["isEvenWeek"] = True
        # both singular week and even week
        if "单" not in classtime[i] and "双" not in classtime[i]:
            detail["isSingWeek"], detail["isEvenWeek"] = True, True

        # matching week period and class period
        weekperiod = re.findall("[0-9]{1,2}-[0-9]{1,2}.周", classtime[i])
        if weekperiod != []:
            weekBegin = int(re.findall("[0-9]{1,2}-", weekperiod[0])[0][:-1])
            weekEnd = int(re.findall("-[0-9]{1,2}", weekperiod[0])[0][1:])
        classperiod = re.findall("[0-9]{1,2}-[0-9]{1,2}节", classtime[i])
        if classperiod != []:
            classBegin = re.findall("[0-9]{1,2}-", classperiod[0])[0][:-1]
            classEnd = re.findall("-[0-9]{1,2}", classperiod[0])[0][1:]
        week = re.findall("星期.", classtime[i])
        try:
            classroom = re.findall("[^/]+(?!.*/)", classtime[i])[0]
        except:
            classroom = ""
        if weekperiod == []:
            singw = re.findall("[0-9]{1,2}周", classtime[i])
            if singw == []:
                detail["classroom"] = "该课程暂无上课时间及上课地点"
                detailList.append(deepcopy(detail))
                continue
            else:
                singw = int(singw[0][:-1])
                classBegin = re.findall("[0-9]{1,2}-", classperiod[0])[0][:-1]
                classEnd = re.findall("-[0-9]{1,2}", classperiod[0])[0][1:]
                detail["weekBegin"] = singw
                detail["weekEnd"] = singw
                detail["periodBegin"] = classBegin
                detail["periodEnd"] = classEnd
                detail["classroom"] = classroom
                detail["week"] = week[0]
                detailList.append(deepcopy(detail))
        else:
            detail["weekBegin"] = weekBegin
            detail["weekEnd"] = weekEnd
            detail["periodBegin"] = classBegin
            detail["periodEnd"] = classEnd
            detail["classroom"] = classroom
            detail["week"] = week[0]
            detailList.append(deepcopy(detail))

    return detailList


with open("lectureList.json", "r") as f:
    content = f.read()[8:-1]
    print(content)
    lectureDetailList = json.loads(content)

for i, item in enumerate(lectureDetailList):
    lectureDetailList[i]["classTimeList"] = convert(lectureDetailList[i]["classTimeList"])

with open("lectureDetailList.json", "w", encoding="utf-8") as f:
    f.write("{\"list\":")
    f.write(json.dumps(lectureDetailList, indent=4, sort_keys=True, ensure_ascii=False)+"\n")
    f.write("}")


# Debug print
for lecture in lectureDetailList:
    print(lecture["classTimeList"], "\n")
