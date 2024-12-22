# 打印工作日志目录到文件

import calendar

weeks = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]

"""
打印工作日志目录到文件函数
参数：
    year: 年份
    month: 月份
返回值：
    None
功能描述：
    该函数根据输入的年份和月份，打印一个“year-month.md”文件，文件内容为该月份的日期+星期，例如：
    2020-01.md:
    # 2020-01-01  星期一
    # 2020-01-02  星期二
    # 2020-01-03  星期三
    # 2020-01-04  星期四
"""
def print_directory(year, month):
    # 判断year和month是否为合法
    if year.isdigit() == False or month.isdigit() == False:
        print("年份和月份必须为数字")
        return
    year = int(year)
    month = int(month)
    if month < 1 or month > 12:
        print("月份必须在1-12之间")
        return

    # 打开文件
    with open(str(year) + "-" + str(month) + ".md", 'w', encoding='utf-8') as file:
        # 获取当前月份的总天数
        days = calendar.monthrange(year, month)[1]

        # 按天写入
        for i in range(1, days):
            # 日期
            date = str(year) + "-" + str(month) + "-" + str(i)
            # 星期
            week = calendar.weekday(year, month, i)
            # if week == 0:
            #     week = "星期一" 
            # elif week == 1:
            #     week = "星期二"
            # elif week == 2:
            #     week = "星期三"
            # elif week == 3:
            #     week = "星期三"
            # elif week == 4:
            #     week = "星期四"
            # elif week == 5:
            #     week = "星期五"
            # elif week == 6:
            #     week = "星期六"
            # 写入内容
            file.write(date + "  " + weeks[week] + "\n")

        print("已打印工作日志目录到文件")


if __name__ == "__main__":
    year = input("请输入年份：")
    month = input("请输入月份：")
    print_directory(year, month)