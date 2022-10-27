import pandas
from collections import Counter
a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
b = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd', 'e', 'e', 'e', ]
letter_counts = Counter(a)
letter_counts1 = Counter(b)
df = pandas.DataFrame.from_dict(letter_counts, orient='index')
df1 = pandas.DataFrame.from_dict(letter_counts1, orient='index')
x = df.plot(kind='bar')
y = df1.plot(kind='bar')
#.get_figure().savefig('pandas_hist.png')
y.get_figure().savefig('pandas_hist.png')

#test = pd.DataFrame([[random.gauss(3,1) for _ in range(400)], 
#                     [random.gauss(4,2) for _ in range(400)]])
#plt.hist(test.values.T)
#plt.show()

"""
#More consise
a = ['a', 'a', 'a', 'a', 'b', 'b', 'c', 'c', 'c', 'd', 'e', 'e', 'e', 'e', 'e']
pd.Series(a).value_counts(sort=False).plot(kind='bar')
"""