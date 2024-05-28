import datetime
from typing import Dict



# april 2024 starts on a monday
def generate_april():
    april_dict: Dict = {}

    for x in range(1, 30 + 1):
        if x >= 1 and x <= 6:
            week_num = 1
        april_dict[datetime.datetime.strptime("05/" + str(x) + "/2024", "%m/%d/%Y")] = week_num

    return april_dict


# may 2024 starts on a wednesday
def generate_may():
    may_list: List[datetime.date] = []

    for x in range(1, 31 + 1):
        may_list.append(datetime.datetime.strptime("05/" + str(x) + "/2024", "%m/%d/%Y"))

    return may_list


# june 2024 starts on a friday
def generate_june_2024():
    june_list: List[datetime.date] = []

    for x in range(1, 30 + 1):
        june_list.append(datetime.datetime.strptime("06/" + str(x) + "/2024", "%m/%d/%Y"))

    return june_list


# june 2025 starts on a sunday
def generate_june_2025():
    june_list: List[datetime.date] = []

    for x in range(1, 30 + 1):
        june_list.append(datetime.datetime.strptime("06/" + str(x) + "/2025", "%m/%d/%Y"))

    return june_list


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
        print(week_calc(may_datetime.day))


if __name__ == "__main__":
    main()
