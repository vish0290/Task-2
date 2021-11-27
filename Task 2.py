import pandas as pd

# pd.read_csv is used to make them as pandas dataframe 
data  = pd.read_csv("ZAPPOS_OOS_DISCARDED_DUMP_2021-11-23.csv")
data2 = pd.read_csv("ZAPPOS_OOS_DISCARDED_DUMP_2021-11-24.csv")
data3 = pd.read_csv("ZAPPOS_OOS_DISCARDED_DUMP_2021-11-25.csv")

data_22  = {}
data_23 = {}
data_24 = {}

a = list(data['retailer'])
b = list(data2['retailer'])
c = list(data3['retailer'])


# the below function take the retailer list and an dictionary as arguements to calculate the occurance of the retailer and update it ,retailer is the key and the count is the value

def countings(x,main_data):
    for i in range(len(x)):
        if x[i] in main_data.keys():
            main_data[x[i]]+=1
        else:
            main_data.update({x[i]:0})        
#     for i in sorted(main_data.keys()):
#         print(f"{i} : {main_data[i]}")

countings(a,data_22)
countings(b,data_23)
countings(c,data_24)


#the final dict is initalized with some data which will act as the column head
final_data = {'sources':[22112021,23112021,24112021,'3_day_average',24112021,'24th_value_as_a_percentage_of_the_3_day_average']}

# final_data.update({i:[data_22[i],data_23[i],data_24[i],round((data_22[i]+data_23[i]+data_24[i])/3,2),data_22[i],round((data_22[i]/avg) * 100,2)] for i in sorted(data_22.keys())})
#finding the average of 3 days and considering the 24th as the current date and passing it to caluclate the today's percentage over the 3 days average
for i in sorted(data_22.keys()):
    avg = round((data_22[i]+data_23[i]+data_24[i])/3,2)
    val = round((data_24[i]/avg) * 100,2)
    final_data.update({i:[data_22[i],data_23[i],data_24[i],avg,data_24[i],val]})

#converting the dictionary to pandas dataframe and using ths dataframe to write over a CSV file

df =  pd.DataFrame.from_dict(final_data,orient='index')
df.to_csv('out_table.csv',header=False)
# print(final_data)
    




