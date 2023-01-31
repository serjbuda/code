from datetime import datetime, timedelta, date
users = [{"name": "Alarak","birthday":datetime(year=1991, month=10, day=9)},
         {"name": "Bryan","birthday": datetime(year=1985, month=5, day=2)},
         {"name": "Cyrax","birthday": datetime(year=1982, month=6, day=5)},
         {"name": "Dante","birthday": datetime(year=1993, month=1, day=1)},
         {"name": "Eliza","birthday": datetime(year=1995, month=4, day=13)},
         {"name": "Fahkumram","birthday": datetime(year=1989, month=5, day=20)},
         {"name": "Gabriel","birthday": datetime(year=1993, month=9, day=23)},
         {"name": "Heihachi","birthday": datetime(year=1999, month=11, day=17)},
         {"name": "Ibuki","birthday": datetime(year=2001, month=8, day=24)},
         {"name": "Juri","birthday": datetime(year=1993, month=2, day=7)},
         {"name": "Kerrigan","birthday": datetime(year=1987, month=2, day=7)},
         {"name": "Lee","birthday": datetime(year=1987, month=5, day=23)},
         {"name": "Malenia","birthday": datetime(year=1986, month=12, day=30)},
         {"name": "Noob Saibot","birthday": datetime(year=1997, month=11, day=3)},
         {"name": "Orb","birthday": datetime(year=2005, month=10, day=13)},
         {"name": "Phobos","birthday": datetime(year=2002, month=3, day=19)},
         {"name": "Quan Chi","birthday": datetime(year=2003, month=12, day=1)},
         {"name": "Raiden","birthday": datetime(year=2006, month=2, day=28)},
         {"name": "Seth","birthday": datetime(year=2001, month=5, day=24)},
         {"name": "TankJR","birthday": datetime(year=2002, month=3, day=3)},
         {"name": "Uriel","birthday": datetime(year=1997, month=1, day=6)},
         {"name": "Vergil","birthday": datetime(year=1998, month=10, day=27)},
         {"name": "Wu-Ruixiang","birthday": datetime(year=1999, month=7, day=7)},
         {"name": "Xaero","birthday": datetime(year=2000, month=8, day=18)},
         {"name": "Yoshimitsu","birthday": datetime(year=2006, month=7, day=22)},
         {"name": "Zafina","birthday": datetime(year=1990, month=9, day=1)}
          ]
def get_birthdays_per_week(users):
    dict_list=[]
    mond_list=[]
    tuesd_list=[]
    wed_list=[]
    thur_list=[]
    fri_list=[]
    mond = "Monday: "
    tuesd = "Tuesday: "
    wed = "Wednesday: "
    thur = "Thursday: "
    fri = "Friday: "
    for i in users:
        dict_list = list(i.values())
        wd=dict_list[1].weekday()
        if wd == 0:
            mond_list.append(dict_list[0])
        if wd == 1:
            tuesd_list.append(dict_list[0])
        if wd == 2:
            wed_list.append(dict_list[0])
        if wd == 3:
            thur_list.append(dict_list[0])
        if wd == 4:
            fri_list.append(dict_list[0])
        if wd == 5:
            mond_list.append(dict_list[0])
        if wd == 6:
            mond_list.append(dict_list[0])
    mond = mond+', '.join(mond_list)
    tuesd = tuesd+', '.join(tuesd_list)
    wed = wed+', '.join(wed_list)
    thur = thur+', '.join(thur_list)
    fri = fri+', '.join(fri_list)
    return  print("List of users by weekdays of their birthdays (if birthday falls on Saturday or Sunday - greet on Monday):"+
                  "\n"+mond+"\n"+tuesd+"\n"+wed+"\n"+thur+"\n"+fri)
def check_if_birthday_next_week(users):
    week_greets=""
    dict_list=[]
    current_datetime = datetime.now()
    one_week_interval = timedelta(weeks=1)
    today_plus_week = date.today()+one_week_interval
    print(today_plus_week)
    for j in users:
        dict_list = list(j.values())
        birth = dict_list[1].date()
        if birth.day == today_plus_week.day and birth.month == today_plus_week.month:
            week_greets+=dict_list[0]+", "
    if week_greets !="":
        return print("In next 7 days we greet: ",week_greets)
    else:
        return print("No birthdays in next 7 days.")
def main():
    get_birthdays_per_week(users)
    check_if_birthday_next_week(users)
if __name__ == "__main__":
    main()

