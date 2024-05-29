from datetime import datetime, date
from calendar import Calendar
from typing import Dict



# april 2024 starts on a monday
def generate_april_2024():
    april_dict: Dict = {}

    for x in range(1, 30 + 1):
        if x >= 1 and x <= 6:
            week_num = 1
        april_dict[datetime.strptime("05/" + str(x) + "/2024", "%m/%d/%Y")] = week_num

    return april_dict


# may 2024 starts on a wednesday
def generate_may_2024():
    may_list: List[dt.date] = []

    for x in range(1, 31 + 1):
        may_list.append(datetime.strptime("05/" + str(x) + "/2024", "%m/%d/%Y"))

    return may_list


# june 2024 starts on a friday
def generate_june_2024():
    june_list: List[date] = []

    for x in range(1, 30 + 1):
        june_list.append(datetime.strptime("06/" + str(x) + "/2024", "%m/%d/%Y"))

    return june_list


# june 2025 starts on a sunday
def generate_june_2025():
    june_list: List[date] = []

    for x in range(1, 30 + 1):
        june_list.append(dt.datetime.strptime("06/" + str(x) + "/2025", "%m/%d/%Y"))

    return june_list


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


def week_calc(datetime_today: date):
    # for a week starting on sunday like a calendar
    cal = Calendar(6)
    weeks = cal.monthdayscalendar(datetime_today.year, datetime_today.month)
    for x in range(len(weeks)):
        if datetime_today.day in weeks[x]:
            return x + 1


def week_check(datetime_today: date):
    week_of_month = week_calc(datetime_today)
    print(week_of_month)
    return week_of_month


def main():
    today = date.today()
    daily_task(today)
    print()
    week_check(today)
    print()

    may_2024_datetimes = generate_may_2024()
    for may_2024_datetime in may_2024_datetimes:
        print(week_calc(may_2024_datetime))


if __name__ == "__main__":
    main()
