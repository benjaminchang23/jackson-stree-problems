from calendar import Calendar
from datetime import datetime, date
from math import ceil
from typing import Dict


# april 2024 starts on a monday
def generate_april_2024():
    april_2024_dict: Dict = {}

    for x in range(1, 30 + 1):
        week_num: int = 0
        if x >= 1 and x <= 6:
            week_num = 1
        elif x >= 7 and x <= 13:
            week_num = 2
        elif x >= 14 and x <= 20:
            week_num = 3
        elif x >= 21 and x <= 27:
            week_num = 4
        elif x >= 28:
            week_num = 5
        april_2024_dict[datetime.strptime("04/" + str(x) + "/2024", "%m/%d/%Y")] = week_num

    return april_2024_dict


# may 2024 starts on a wednesday
def generate_may_2024():
    may_2024_dict: Dict = {}

    for x in range(1, 31 + 1):
        week_num: int = 0
        if x >= 1 and x <= 4:
            week_num = 1
        elif x >= 5 and x <= 11:
            week_num = 2
        elif x >= 12 and x <= 18:
            week_num = 3
        elif x >= 19 and x <= 25:
            week_num = 4
        elif x >= 26:
            week_num = 5
        may_2024_dict[datetime.strptime("05/" + str(x) + "/2024", "%m/%d/%Y")] = week_num

    return may_2024_dict


# june 2024 starts on a friday
def generate_june_2024():
    june_2024_dict: Dict = {}

    for x in range(1, 30 + 1):
        week_num: int = 0
        if x >= 1 and x <= 1:
            week_num = 1
        elif x >= 2 and x <= 8:
            week_num = 2
        elif x >= 9 and x <= 15:
            week_num = 3
        elif x >= 16 and x <= 22:
            week_num = 4
        elif x >= 23 and x <= 29:
            week_num = 5
        elif x >= 30:
            week_num = 6
        june_2024_dict[datetime.strptime("06/" + str(x) + "/2024", "%m/%d/%Y")] = week_num

    return june_2024_dict


# june 2025 starts on a sunday
def generate_june_2025():
    june_2025_dict: Dict = {}

    for x in range(1, 30 + 1):
        week_num: int = 0
        if x >= 1 and x <= 7:
            week_num = 1
        elif x >= 8 and x <= 14:
            week_num = 2
        elif x >= 15 and x <= 21:
            week_num = 3
        elif x >= 22 and x <= 28:
            week_num = 4
        elif x >= 29:
            week_num = 5
        june_2025_dict[datetime.strptime("06/" + str(x) + "/2025", "%m/%d/%Y")] = week_num

    return june_2025_dict


def daily_task(today: date):
    print(today)
    print(today.weekday())
    if today.weekday() in [1, 2]: # 1 corresponds to Tuesday, 2 corresponds to Wednesday
        print("daily_task weekday")
        print(today.month)
        if today.month not in [1, 2, 3, 12]: # no street sweeping in the winter
            print("daily_task month")
            week_of_month = (today.day - 1) // 7 + 1
            if week_of_month == 3:
                user_ids = ["148906826790993920", "694758082479128637"]
                mentions = ""
                for user_id in user_ids:
                    mentions += "<@" + user_id + "> "
                print("Street cleanup is tomorrow!")


def week_calc_calendar(datetime_today: date):
    # for a week starting on sunday like a calendar
    cal = Calendar(6)
    weeks = cal.monthdayscalendar(datetime_today.year, datetime_today.month)
    for x in range(len(weeks)):
        if datetime_today.day in weeks[x]:
            return x + 1


def week_calc_math(datetime_today: date):
    first_day = datetime_today.replace(day=1)
    dom = datetime_today.day
    adjusted_dom = dom + first_day.weekday()

    return int(ceil(adjusted_dom/7.0))


def week_check(datetime_today: date):
    week_of_month_cal = week_calc_calendar(datetime_today)
    week_of_month_math = week_calc_math(datetime_today)
    assert week_of_month_cal == week_of_month_math
    return week_of_month_cal


def check_week_dict(month_dict: Dict):
    for day_datetime in month_dict:
        week_num: int = week_calc_calendar(day_datetime)
        assert week_num == month_dict.get(day_datetime), f"{day_datetime} {week_num} {month_dict.get(day_datetime)}"


def main():
    today = date.today()
    daily_task(today)
    print()
    week_check(today)

    april_2024_datetimes = generate_april_2024()
    may_2024_datetimes = generate_may_2024()
    june_2024_datetimes = generate_june_2024()
    june_2025_datetimes = generate_june_2025()

    check_week_dict(april_2024_datetimes)
    check_week_dict(may_2024_datetimes)
    check_week_dict(june_2024_datetimes)
    check_week_dict(june_2025_datetimes)


if __name__ == "__main__":
    main()
