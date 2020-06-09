"""生成一个HTML的测试报告"""
#1.导入unittest
import unittest
import time
import HTMLTestRunnerPlugins
#2.确定测试用例的存放路径
case_path="./script"
#3.将需要执行的用例添加到测试套件中
discover=unittest.defaultTestLoader.discover(start_dir=case_path)
#4.确定存放测试报告的路径
report_path="./report"
#5.给测试报告命名
#以当前时间命名
now=time.strftime("%Y-%m-%d %H_%M_%S")
report_name=now + "report.html"   #报告名称
with open(report_path+"/"+report_name,"wb") as fp:
    runner=HTMLTestRunnerPlugins.HTMLTestRunner(
        title="unittest自动化测试",  #写项目名称
        description="使用unittest框架执行用例",  #对项目描述
        stream=fp
    )
    runner.run(discover)