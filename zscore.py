import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics as s
import random
import pandas as pd

df = pd.read_csv("studentMarks.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot ([data], ["Math Score"] , show_hist = False )
#fig.show()
mean = s.mean(data)
std = s.stdev(data)
print("\nmean of population : ",mean)
print("std of population:", std )

def random_set_of_mean(counter):
    dataset = []
    for i in range(0,counter):  
        random_index = random.randint(0, len(data)-1) #5
        value = data[random_index] #data[5]
        dataset.append(value)
    mean = s.mean(dataset)
    return mean

meanlist = []
for i in range(0, 1000):
    sm = random_set_of_mean(100)
    meanlist.append(sm)

mean = s.mean(meanlist)
std = s.stdev(meanlist)
print("\nmean of sample data : ",mean)
print("std of sample data:", std )

fig = ff.create_distplot ([meanlist], ["Math Score"] , show_hist = False )
#fig.show()


first_std_start, first_std_end= mean-std, mean+std
second_std_start, second_std_end= mean-(2*std), mean+(2*std)
third_std_start, third_std_end= mean-(3*std), mean+(3*std)


# finding the mean of the first data(STUDENTS WHO GOT TABLET WITH LEARNING MATERIAL) and plotting it on the plot.
df = pd.read_csv("data1.csv")
data = df["Math_score"].tolist()
meansample1 = s.mean(data)
fig = ff.create_distplot ([meanlist], ["Math Score"] , show_hist = False )
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meansample1, meansample1], y=[0, 0.17], mode="lines", name="Mean of sample(iPAD)"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="first std end"))
#fig.show()


# finding the mean of the SECOND data (STUDENTS WHO HAD EXTRA CLASSES ) and plotting it on the plot.
df = pd.read_csv("data2.csv")
data = df["Math_score"].tolist()
meansample2 = s.mean(data)
fig = ff.create_distplot ([meanlist], ["Math Score"] , show_hist = False )
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meansample2, meansample2], y=[0, 0.17], mode="lines", name="Extra Classes"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="first std end"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="second std end"))#fig.show()


# finding the mean of the THIRD data (STUDENTS WHO GOT FUNSHEET) and plotting it on the plot.
df = pd.read_csv("data3.csv")
data = df["Math_score"].tolist()
meansample3 = s.mean(data)
fig = ff.create_distplot ([meanlist], ["Math Score"] , show_hist = False )
fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[meansample3, meansample3], y=[0, 0.17], mode="lines", name="Fun Worksheets"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="first std end"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="second std end"))
fig.add_trace(go.Scatter(x=[third_std_end, third_std_end], y=[0, 0.17], mode="lines", name="third std end"))
#fig.show()

#the third intervension had the best impact

zscore1 = (meansample1 - mean)/std
zscore2 = (meansample2 - mean)/std
zscore3 = (meansample3 - mean)/std
print (zscore1, zscore2, zscore3)
#the third intervensions for the zscore and using the graph gave us the same information

