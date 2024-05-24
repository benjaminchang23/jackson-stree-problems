import datetime


def daily_task(today: datetime.date):
    print(today)
    print(today.weekday())
    if today.weekday() in [1, 2]: # 1 corresponds to Tuesday, 2 corresponds to Wednesday
        print("correct weekday")
        print(today.month)
        if today.month not in [1, 2, 3, 12]: # no street sweeping in the winter
            print("correct month")
            week_of_month = (today.day - 1) // 7 + 1
            if week_of_month == 3:
                user_ids = ["148906826790993920", "694758082479128637"]
                mentions = ""
                for user_id in user_ids:
                    mentions += "<@" + user_id + "> "
                print("Street cleanup is tomorrow!")


def week_check(datetime_today: datetime.date):
    week_of_month = (datetime_today.day - 1) // 7 + 1
    print(week_of_month)

def main():
    today = datetime.date.today()
    daily_task(today)
    print()
    week_check(today)


if __name__ == "__main__":
    main()
