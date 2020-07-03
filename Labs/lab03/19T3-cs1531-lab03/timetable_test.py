# Author: @abara15 (GitHub)
from datetime import date, time, datetime
from timetable import timetable
import pytest

def test_example_1():
    assert timetable([date(2019,9,27), date(2019,9,30)], [time(14,10), time(10,30)]) == [datetime(2019,9,27,10,30), datetime(2019,9,27,14,10), datetime(2019,9,30,10,30), datetime(2019,9,30,14,10)]

def test_example_2():
    assert timetable([date(2018,3,12), date(2019,1,31)], [time(21,50), time(21,51)]) == [datetime(2018,3,12,21,50), datetime(2018,3,12,21,51), datetime(2019,1,31,21,50), datetime(2019,1,31,21,51)]

def test_example_3():
    assert timetable([date(1976,2,21), date(1957,7,1), date(1947,12,23)], [time(23,59), time(12,25)]) == [datetime(1947,12,23,12,25),datetime(1947,12,23,23,59),datetime(1957,7,1,12,25),datetime(1957,7,1,23,59),datetime(1976,2,21,12,25),datetime(1976,2,21,23,59)]

def test_example_4():
    assert timetable([date(2003,5,16)], [time(4,44), time(13,36), time(11,23)]) == [datetime(2003,5,16,4,44),datetime(2003,5,16,11,23),datetime(2003,5,16,13,36)]
