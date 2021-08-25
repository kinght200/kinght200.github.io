import json
import requests

usertoken = ""
cookies = {}
courselist = []
TeachList = []


def login(userName, userPwd):
    global usertoken, cookies
    url = "https://zjyapp.icve.com.cn/newMobileAPI/MobileLogin/newLogin"
    data = {
        "appVersion": "2.8.20",
        "clientId": "04fbaf3b874041b68db529f24b5aa86b",
        "sourceType": 3,
        "userName": userName,
        "userPwd": userPwd
    }
    res = requests.post(url, data=data)
    userifo = json.loads(res.text)
    if (userifo['code'] != 1):
        print("账号或密码错误")
        return 0
    usertoken = userifo['token']
    cookies = requests.utils.dict_from_cookiejar(res.cookies)


def getCourseList():
    global courselist
    url = "https://zjyapp.icve.com.cn/newMobileAPI/Student/getCourseList?isPass=0&sourceType=3&stuId=" + usertoken
    res = requests.get(url, cookies=cookies)
    course = json.loads(res.text)
    index = 0
    if (course['code'] == 1):
        courselist = course['dataList']
        print("账号下共有" + str(len(courselist)) + "门课程")
    for item in courselist:
        print(str(index) + ". " + item['courseName'])
        index += 1
    c_index = input("课程序号:")


def getDate():
    url = "https://zjyapp.icve.com.cn/newMobileAPI/FaceTeach/getFaceTeachDate?courseOpenId=&faceTeachType=4&openClassId=&sourceType=3&userId=" + usertoken
    res = requests.get(url, cookies=cookies)
    course = json.loads(res.text)
    index = 0
    if (course['code'] == 1):
        datelist = course['dateList']
    for item in datelist:
        print(str(index) + ". " + item)
        index += 1
    c_index = input("日期序号:")
    getTeachList(datelist[int(c_index)])


def getTeachList(date):
    global TeachList
    url = "https://zjyapp.icve.com.cn/newMobileAPI/FaceTeach/getStuFaceTeachList?courseOpenId=&faceDate=" + date + "&openClassId=&sourceType=3&stuId=" + usertoken
    res = requests.get(url, cookies=cookies)
    course = json.loads(res.text)
    index = 0
    if (course['code'] == 1):
        TeachList = course['dataList']
    for item in TeachList:
        print(str(index) + ". " + item['Title'] + " 课程:" + item['courseName'])
        index += 1
    c_index = input("请输入课程序号:")
    getActivityList(TeachList[int(c_index)]['Id'], TeachList[int(c_index)]['state'],
                    TeachList[int(c_index)]['openClassId'])


def getActivityList(activityId, classState, openClassId):
    url = "https://zjyapp.icve.com.cn/newMobileAPI/faceTeach/newGetStuFaceActivityList"
    data = {
        "activityId": activityId,
        "classState": 2,
        "openClassId": openClassId,
        "sourceType": 3,
        "stuId": usertoken
    }
    res = requests.post(url, data=data)
    Activit = json.loads(res.text)
    index = 0
    if (Activit['code'] == 1):
        ActivityList = Activit['dataList']
    for item in ActivityList:
        print(str(index) + ". " + item['Title'] + " 类型:" + item['DataType'])
        index += 1
    c_index = input("补签的任务序号:")
    changeSignType(openClassId, ActivityList[int(c_index)]['Id'])


def changeSignType(OpenClassId, SignId):
    url = "https://zjyapp.icve.com.cn/newMobileAPI/FaceTeach/changeSignType"
    data = 'data={"SignResultType" : 1,"StuId" :\"' + usertoken + '\","OpenClassId" :\"' + OpenClassId + '\","SignId" :\"' + SignId + '\","Id" : \"' + usertoken + '\","SourceType" : 3}&sourceType=3'
    headers = {
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
    }
    res = requests.post(url, data=data, headers=headers)
    resjson = json.loads(res.text)
    if (resjson['code'] == 1):
        print("修改成功!")
    getDate()


if __name__ == "__main__":
    account = input("账号: ")
    password = input("密码: ")
    login(account, password)
    getDate()
