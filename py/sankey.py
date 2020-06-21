import plotly.graph_objects as go
import data as d
import numpy as np

purchases = d.selectAllPurchases() #return list of dictionary

costs = list(map(lambda m: float(m.get('Cost')), purchases))
category = list(map(lambda m: m.get('CategoryName')[0:10], purchases))

targets = np.ones(len(category))
sourceIndex = list(range(0,len(category)))

print([costs,costs])
fig = go.Figure(data=[go.Sankey(
	node = dict(
		pad = 15,
		thickness = 20,
		line = dict(color = "black", width = 0.5),
		label = category,
		color = "blue"
	),
	link = dict(
		source = sourceIndex,
		target = targets,
		value = costs
	)
)])

fig.update_layout(title_text="Basic Sankey Diagram", font_size=10)
fig.show()