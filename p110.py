import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random

data = pd.read_csv("csv/110.csv")
data_list = data["temp"].tolist()

data_mean = statistics.mean(data_list)
data_stdev = statistics.stdev(data_list)

print("population mean: ", data_mean)
print("population std_dev: ", data_stdev)

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_number = random.randint(0, len(data_list)-1)
        value = data_list[random_number]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df=mean_list
    mean=statistics.mean(df)
    figure = ff.create_distplot([df], ["temp"], show_hist = False)
    figure.add_trace(go.Scatter(x=[mean, mean], y=[0, 1],mode="lines",name="MEAN"))
    figure.show()

def setup():
    mean_list=[]
    for i in range(0,1000):
       set_of_means=random_set_of_mean(100)
       mean_list.append(set_of_means)
    mean=statistics.mean(mean_list)
    print("mean of sampling_distribution",mean)
    stdev=statistics.stdev(mean_list)
    print("stdev of sampling_dsitribution",stdev)

    show_fig(mean_list)

setup()


    
     
