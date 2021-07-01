import statistics as st
import pandas as pd

data = pd.read_csv("StudentsPerformance.csv")
Score = data["math score"].tolist()
sum = 0
mean = 0

for x in Score:
    sum += x

mean = sum/len(Score)
median = st.median(Score)
mode = st.mode(Score)
StandardDV = st.stdev(Score)

print("{} is the mean\n{} is the median\n{} is the mode".format(mean,median,mode))

#FirstRegion
FirstRegionSTDVstart , FirstRegionSTDVend = mean - StandardDV , mean + StandardDV  
FirstRegion = [Result for Result in Score if FirstRegionSTDVstart < Result < FirstRegionSTDVend]
FirstRegion_Per = len(FirstRegion)/len(Score)

#SecondRegion
SecondRegionSTDVstart , SecondRegionSTDVend = mean - 2*StandardDV , mean + 2*StandardDV  
SecondRegion = [Result for Result in Score if SecondRegionSTDVstart < Result < SecondRegionSTDVend]
SecondRegion_Per = len(SecondRegion)/len(Score)

#ThirdRegion
ThirdRegionSTDVstart , ThirdRegionSTDVend = mean - 3*StandardDV , mean + 3*StandardDV  
ThirdRegion = [Result for Result in Score if ThirdRegionSTDVstart < Result < ThirdRegionSTDVend]
ThirdRegion_Per = len(ThirdRegion)/len(Score)

print("{}% of data is in FirstRegion\n{}% of data is SecondREgion\n{}% of data is in ThirdRegion".format(FirstRegion_Per,SecondRegion_Per,ThirdRegion_Per))