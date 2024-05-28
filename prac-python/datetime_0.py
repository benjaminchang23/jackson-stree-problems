import datetime
from typing import List

def generate_may():
    may_list: List[datetime.date] = []

    for x in range(1, 31 + 1):
        may_list.append(datetime.datetime.strptime("05/" + str(x) + "/2024", "%m/%d/%Y"))

    return may_list


def daily_task(today: datetime.date):
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


def week_calc(day: int):
    return (day - 1) // 7 + 1


def week_check(datetime_today: datetime.date):
    week_of_month = week_calc(datetime_today.day)
    print(week_of_month)
    return week_of_month


def main():
    today = datetime.date.today()
    daily_task(today)
    print()
    week_check(today)
    print(week_calc(7))
    print()

    may_datetimes = generate_may()
    for may_datetime in may_datetimes:
        print(may_datetime)


if __name__ == "__main__":
    main()
