# 16100415 최창현

#
# 라이브러리 임포트 , 데이터 불러오기 
#
import pandas as pd

# bike_data.csv 파일은 .py 파일과 같은 폴더에 위치
bike = pd.read_csv('bike_data.csv')

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

#
# 1. 데이터 전처리
#
bike["date"] = bike["datetime"].str.split(" ").str[0]
bike["year"] = bike["date"].str.split("-").str[0]
bike["month"] = bike["date"].str.split("-").str[1]
bike["day"] = bike["date"].str.split("-").str[2]

bike["time"] = bike["datetime"].str.split(" ").str[1]
bike["hour"] = bike["time"].str.split(":").str[0]

# holiday, workingday가 0 0 이면 주말 (쉬는날)   => weekday = 0
# holiday, workingday가 1 0 이면      (쉬는날)   => weekday = 0
# holiday, workingday가 0 1 이면      (안쉬는날) => weekday = 1
# holiday, workingday가 1 1 일 경우는 없음.
bike["weekday"] = bike["workingday"]

 
bike = bike[["year","month","day","hour","season","weekday","weather","temp","atemp","count"]]
# print(bike)

#
# 2. 데이터 분석
#

# # 그래프 1
sns.regplot(x="temp", y="atemp", data=bike)
plt.title("graph1. temp <-> atemp ")
plt.show()

#atemp 데이터 제거
bike = bike[["year","month","day","hour","season","weekday","weather","temp","count"]]


# 그래프 2
count_groupby_2018 = bike[bike["year"] == "2018"]
count_groupby_2018 = count_groupby_2018.groupby("month").sum()["count"]

count_groupby_2019 = bike[bike["year"] == "2019"]
count_groupby_2019 = count_groupby_2019.groupby("month").sum()["count"]

sns.lineplot(data=count_groupby_2018)
sns.lineplot(data=count_groupby_2019)

plt.legend(['2018','2019'])
plt.title("graph2. count groupby month ")
plt.xlabel("month")
plt.ylabel("count")
plt.show()

# 그래프 3
for i in range(1,13):
    if i < 10 :
        count_groupby_month = bike[bike["month"] == "0"+str(i)]
    else : 
        count_groupby_month = bike[bike["month"] == str(i)]

    count_groupby_month = count_groupby_month.groupby("hour").sum()["count"]
    sns.lineplot(data=count_groupby_month)
    
plt.legend([1,2,3,4,5,6,7,8,9,10,11,12])
plt.title("graph3. count groupby month ")
plt.xlabel("hour")
plt.ylabel("count")
plt.show()

# 그래프 4
bike_weekday_count = bike.loc[  bike["weekday"] == 1 , "count" ].sum() / bike["weekday"].value_counts()[1]
bike_weekend_count = bike.loc[  bike["weekday"] == 0 , "count" ].sum() / bike["weekday"].value_counts()[0]
bike_week_count = [bike_weekday_count, bike_weekend_count]
sns.barplot( x = ["weekday", "weekend+holiday"], y = bike_week_count)

plt.ylabel("one day average count")
plt.title("graph4. weekday <-> weekend, holiday")
plt.show()

# 그래프 5
sns.relplot( x ="temp", y="count", data=bike, kind= 'line', ci="sd")

plt.title("graph5. temp <-> count")
plt.grid()
plt.show()


# 그래프 6
sns.relplot( x ="month", y="season", data=bike)
plt.title("graph6. month <-> season")
plt.show()


# 그래프 7
sns.relplot( x ="month", y="temp", data=bike, kind='line', ci="sd")
plt.title("graph7. month <-> temp")
plt.grid()
plt.show()

#
# 3. 문제해결
#

# 3.1. 공유 자전거 수요량이 가장 낮은 계절은? 
print("1. 공유 자전거 수요량이 가장 낮은 계절은?")
list = []
for i in range(1,5):
    answer = bike.loc[  bike["season"] == i , "count" ].sum()
    list.append(answer)
    print( i," : ", answer)
print(np.min(list))

# 3.2. 수요량이 가장 높은 시간대는?
print("2. 수요량이 가장 높은 시간대는?")
list = []
for i in range(0,24):
    answer = bike.loc[  bike["hour"] == str(i) , "count" ].sum()
    list.append(answer)
    print( i,"시 : ", answer)
print(np.max(list))

# 3.3. 수요량이 높은 날씨 조건은?
print("3. 수요량이 높은 날씨 조건은?")
list = []
for i in range(1,5):
    answer = bike.loc[  bike["weather"] == i , "count" ].sum()
    list.append(answer)
    print( i," : ", answer)
print(np.max(list))