from die import Die
import pygal
die1=Die()
die2=Die()
results=[]
for roll in range(1000):
    result1=die1.roll()
    result2=die2.roll()    
    results.append(result1+result2)
#print(results)

frequencies=[]
for value in range(1,die1.num_sides+die2.num_sides+1):
    frequency=results.count(value)
    frequencies.append(frequency)
#print(frequencies)

hist=pygal.Bar()

hist.title="this is Bar"
hist.x_labels=[1,2,3,4,5,6,7,8,9,10,11,12]
hist.x_title="结果"
hist.y_title="结果2"

hist.add('D12',frequencies)
hist.render_to_file('result.svg')