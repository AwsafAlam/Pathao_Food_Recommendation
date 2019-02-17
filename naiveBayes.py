#%%
import pandas
import numpy as np

fileName ="PathaoFoodDeliveryData"

data= pandas.read_csv(fileName)
data_sorted = data.sort_values(['restaurant_id'], ascending=False)
print(data_sorted)

setUid = set(data["user_id"])
setItemID = set(data["item_id"])
setRestaurantID = set(data["restaurant_id"])

uids = list(setUid)
itemID = list(setItemID)
restaurantID = list(setRestaurantID)

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

#itemDayHour
print(data)


#pandas.DataFrame(itemDayHour).to_csv("data_2_.csv")
pandas.DataFrame(data.values).to_csv("data_2_.csv")


from sklearn.naive_bayes import GaussianNB
clf = GaussianNB()

X = itemDayHour[:,[1,2]].astype(np.int)


#%%
X


#%%
Y = itemDayHour[:,0].astype(np.int)


#%%
Y


#%%
clf.fit(X, Y)


#%%
print(clf.predict_proba([[ 7,  3]]))


#%%
clf.classes_


