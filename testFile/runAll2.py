import os
import common.HTMLTestRunner as HTMLTestRunner
import getpathInfo
import unittest
import readConfig
from common.configEmail import send_email
#from apscheduler.schedulers.blocking import BlockingScheduler
import common.Log

send_mail = send_email()
path = getpathInfo.get_Path()
report_path = os.path.join(path, 'result')
on_off = readConfig.ReadConfig().get_email('on_off')
log = common.Log.logger

class AllTest:#定义一个类AllTest
    def __init__(self):#初始化一些参数和数据
        global resultPath
        resultPath = os.path.join(report_path, "report.html")#result/report.html
        log.info('resultPath'+ resultPath)#将resultPath的值输入到日志，方便定位查看问题

    def run(self):
        case_path = os.path.join(path, 'testCase')
        print(case_path)
        discover = unittest.defaultTestLoader.discover(case_path, pattern="test01case*.py")
        #runner = unittest.TextTestRunner(verbosity=2)  # verbosity控制输出的执行结果的详细程度，可为0，1，2，其中0最简单，1是默认值，2最详细
        #runner.run(discover)
        suit = discover
        print(suit)
        if suit is not None:  # 判断test_suite是否为空
            print('if-suit')
            fp = open(resultPath, 'wb')  # 打开result/20181108/report.html测试报告文件，如果不存在就创建
            # 调用HTMLTestRunner
            runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='Test Report', description='Test Description')
            runner.run(suit)
        else:
            print("Have no case to test.")




# pythoncom.CoInitialize()
# scheduler = BlockingScheduler()
# scheduler.add_job(AllTest().run, 'cron', day_of_week='1-5', hour=14, minute=59)
# scheduler.start()

if __name__ == '__main__':
    AllTest().run()
