from appium import webdriver
def get_driver():
    desired_caps={}
    # 设备信息
    desired_caps['platformName']='Android'
    desired_caps['platforVersion']='5.1'
    desired_caps['deviceName']='192.168.56.101:5555'
    # 设置中文
    desired_caps['unicodeKeyboard']=True
    desired_caps['resetKeyboard']=True
    # app信息
    desired_caps['appPackage']='com.android.settings'
    desired_caps['appActivity'] = '.Settings'
    # 声明我们的driver对象
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_caps)