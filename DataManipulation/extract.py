import pandas
import numpy as np
from sklearn.naive_bayes import GaussianNB


fileName ="PathaoFoodDeliveryData"

data = pandas.read_csv(fileName)

sorted_data = data.sort_values(['item_id'] , ascending=False)

print(len(sorted_data))

# Setting values of user_id , item_id, restaurant_id
'''
Data Description:
columns :

user_id
item_id
day_of_week
hour_of_day
category
cuisine_id
resturant_id
item_count

'''

setUid = set(data["user_id"])
setItemID = set(data["item_id"])
setRestaurantID = set(data["restaurant_id"])

print(len(setUid))

print(len(data["user_id"]))

uids = list(setUid)
itemID = list(setItemID)
restaurantID = list(setRestaurantID)

# print(data.loc[(data["item_id"]=="fffe5f4c-384")])

itemDayHour = data.values[:, [1, 2, 3]]

itemID_len = len(itemID)
for i in range(itemID_len):
    _index = np.where(itemDayHour[:, 0] == itemID[i])
    #print(itemDayHour[_index])
    itemDayHour[_index, 0] = i
    #print(itemDayHour[_index])

itemID_len = len(itemID)
for i in range(itemID_len):
    data['item_id'].replace(
        to_replace=[itemID[i]],
        value=i,
        inplace=True
    )

print(data)

#pandas.DataFrame(itemDayHour).to_csv("data_2_.csv")
pandas.DataFrame(data.values).to_csv("data_2_.csv")

clf = GaussianNB()