import sys
import operator

d = {"a":"a", "d":"d", "f":"f", "c":"c", "b":"b"}

sort_asc_d = sorted(d.items(), key=operator.itemgetter(1))
print("Dictionary in ascending order by value :", sort_asc_d)

sort_dsc_d = sorted(d.items(), key=operator.itemgetter(1), reverse=True)
print("Dictionary in descending order by value :", sort_dsc_d)


print("system path:", sys.path.insert(0, "."))
