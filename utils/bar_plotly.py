import plotly.express as px
import pandas as pd

df = px.data.tips()
fig = px.bar(df, x="sex", y="total_bill", color='time')
#fig.show()
a = {'person': 0.13149921004694962,
 'car': 0.6116563950391843,
 'truck': 0.025372486360442374,
 'bicycle': 0.06175508322479871,
 'traffic light': 0.08158223344119661,
 'motorcycle': 0.06339317283635663,
 'bus': 0.016143686417730754,
 'train': 0.005697508403041655,
 'airplane': 0.0019155802014939735,
 'boat': 0.0009846440288053134}
df = pd.DataFrame.from_dict(a)
#fig = px.bar(df, x="sex", y="total_bill", color='time')

#I actually dont want a histogram: I am not counting occurences I
#just want to compare percentages