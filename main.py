from selenium import webdriver
from json import loads
from selenium.webdriver.support.select import Select
URL = 'http://class.sise.com.cn:7001/sise/'
STU_NUM = ''
PASSWORD = ''
# 加载浏览器引擎
driver = webdriver.Chrome(executable_path='./chromedriver.exe')

driver.get(URL)

with open("./sige_message","r",encoding="utf8") as f:
    stu = loads(f.read())
    STU_NUM = stu["stu_num"]
    PASSWORD = stu["password"]

# 输入学号密码
driver.find_element_by_id("username").send_keys(STU_NUM)
driver.find_element_by_id("password").send_keys(PASSWORD)

# 点击登录
driver.find_element_by_id("Submit").click()

# 跳转至教学评价
driver.get("http://class.sise.com.cn:7001/SISEWeb/pub/student/studentEvaluateAction.do?method=doNotice&evaluate=e22ewij1XIc=&gzcode=qmfRJxy3T92I2qrqyNNnCw==")
# 点击同意
driver.find_elements_by_xpath('//*[@id="form1"]/table[3]/tbody/tr[1]/td/div/label[1]/span')[0].click()
# 点击开始评估
driver.find_element_by_id("startoption").click()

sel_class = driver.find_element_by_name("courseID")
selector_class = Select(sel_class)


# 循环选择课程和老师逐一进行评价
for cls in range(len(selector_class.options)-1):
    sel_class = driver.find_element_by_name("courseID")
    selector_class = Select(sel_class)
    selector_class.select_by_index(1)
    # 选择课程对应的老师
    sel_teacher = driver.find_element_by_name("teacherID")
    selector_teacher = Select(sel_teacher)
    # 判断是否还有老师没有进行评价
    for teacher in range(len(selector_teacher.options)-1):
        selector_teacher.select_by_index(1)
        # 全部选择10分，点击确定
        for item in driver.find_elements_by_name("evaluateScore"):
            Select(item).select_by_index(1)
        driver.find_element_by_name("doSave").click()


# 关闭浏览器
driver.close()


