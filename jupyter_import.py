
#%%
fileName ="PathaoFoodDeliveryData"


#%%
import pandas


#%%
data= pandas.read_csv(fileName)


#%%
data_sorted = data.sort_values(['item_id'], ascending=False)


#%%
data_sorted


#%%
setUid = set(data["user_id"])
setItemID = set(data["item_id"])
setRestaurantID = set(data["restaurant_id"])


#%%
len(setUid)


#%%
len(data["user_id"])


#%%
uids = list(setUid)
itemID = list(setItemID)
restaurantID = list(setRestaurantID)


#%%
data.loc[(data["item_id"]=="fffe5f4c-384")]


#%%
anomalyItemID = []
for item in itemID:
    #print(item, data[(data["item_id"]==item)]["restaurant_id"])
    #size = len(data[(data["item_id"]==item) & (data["restaurant_id"]!=res_id)])
    #print(size)
    size = len(set(data[(data["item_id"]==item)]["restaurant_id"]))
    print(size)
    if size > 1:
        anomalyItemID.append(item)


#%%
set(data[(data["item_id"]=="fffe5f4c-384")]["restaurant_id"])


