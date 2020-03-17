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
