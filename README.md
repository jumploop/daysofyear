![Image](https://pic1.zhimg.com/v2-7302e7611df7f1e4a4d87e8d6d0f19e9_r.jpg)

# 每天一个python小程序

## 背景

最近，没有多少时间去写代码，为了不让自己的编码能力下降，我决定抽时间会写一些短小的python代码，来巩固自己的所学。

## 开发环境

- python版本：3.6

- 开发工具：Pycharm

- Windows10 操作系统

## 代码及思路

该程序的功能主要是根据输入的年月日计算该日是这一年中的第多少天

代码如下：

```python

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/16 21:49
# @Author  : 一叶知秋
# @File    : dayofyear.py
# @Software: PyCharm
import sys
from datetime import datetime


def is_leap(year):
    """
    判断是否是闰年
    :param year: 年份
    :return: 布尔值
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def get_days(year, month):
    """
    获取这一年中这个月份的天数
    :param year: 年份
    :param month: 月份
    :return: 该月的天数
    """
    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    elif month == 2:
        return 29 if is_leap(year) else 28
    else:
        return 30


def main():
    if len(sys.argv) == 4:
        year = int(sys.argv[1])
        month = int(sys.argv[2])
        day = int(sys.argv[3])
    else:
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
    total = 0
    for m in range(1, month):
        total += get_days(year, m)
    total += day
    print(f'{year}年{month}月{day}日是{year}年的第{total}天')


if __name__ == '__main__':
    main()
```

代码思路：

1. 通过位置传参，依次输入年月日 ，如果参数不足，则默认计算当前系统时间是该年的第多少天

2. 根据月份计算该年到当前月的上一个月为止经过了多少天

3. 计算月份的天数的时候，要考虑以下几个条件：

    - 根据is_leap函数判断该年是闰年还是平年，如果是平年的2月是28天，闰年的2月是29天，

    - 判断该月是否在31天所在的月份

    - 该月如果不是2月且不在31天所在的月份，该月就是30天

4. 累加该月之前所有月份的天数，并加上该月的天数，就是你输入年月日对应该年的第多少天。

5. 输出结果

项目地址：https://github.com/jumploop/daysofyear
