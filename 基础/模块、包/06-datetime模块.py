import datetime as dt

# 以一个下划线 _ 开始  _x
# 以两个下划线 _ 开始  __x
# 以两个下划线开始，再以两个下划线结束 __x__


# 涉及到四个类 datetime/date/time/timedelta
# 获取当前的日期时间
print(dt.datetime.now())

# 创建一个日期
dt.date(2020, 1, 1)

# 创建一个时间
dt.time(18, 12, 45)

# 计算3天以后的日期
print(dt.datetime.now() + dt.timedelta(3))
