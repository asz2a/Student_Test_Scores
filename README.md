# Student_Test_Scores
<h2>Scatter Plot and Bar Plot of students test scores <h2/>
<br/>
<img src="img/bar_chart.png" alt="Bar Chart">
<br/>
<p> The Bar Chart is a visual representation of the Math, Reading, and Writing scores of different ethnic groups <p/>
<br/>
<img src="img/scatter_plot.png" alt="Scatter Plot">
<br/>
<p> The Scatter Plot is a visual representation of Math scores vs Reading scores <p/>


<b/>

<h3>Explaining the code</h3>
<p>First the data is converted to a Dataframe from a csv file.</p>

```
df = pd.read_csv("StudentsPerformance.csv")
```
<br/>
<p>Then I defined two functions. The first is for the scatter plot. The second is for the barchart.</p>

<h5>Scatter plot function</h5>

```
def scatter_plot():
    math_score = df['math score']
    reading_score = df['reading score']

    y = math_score
    x = reading_score

    plt.scatter(x, y, color='blue')
    xy= range(0, 100)
    plt.plot(xy, xy, color='red')
    plt.show()
```

</br>

<h5>Barchart function</h5>

```
def barchart_ethnicity_scores():
	# GROUPS TO SCORES

	n_groups = 5
	index = np.arange(n_groups)
	bar_width = 0.25
	fig, ax = plt.subplots()

	math = []
	reading = []
	writing = []

	groups = ['group A', 'group B', 'group C', 'group D', 'group E',]

	for group in groups:
		is_g = df['race/ethnicity'] == group
		group_df = df[is_g]
		group_math = group_df['math score'].mean()
		math.append(group_math)
		group_read = group_df['reading score'].mean()
		reading.append(group_read)
		group_write = group_df['writing score'].mean()
		writing.append(group_write)

	math_bar = plt.bar(index, math, bar_width, color='r', label='math')
	reading_bar = plt.bar(index + bar_width, reading, bar_width, color='b', label='reading')
	writing_bar = plt.bar(index + bar_width*2, writing, bar_width, color='g', label='writing')

	plt.xticks(index + bar_width, groups)
	plt.ylim(bottom=60)
	plt.legend()
	plt.tight_layout()

	plt.show()
```
