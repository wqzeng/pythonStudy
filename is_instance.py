from collections.abc import Iterator
print(isinstance('adb',Iterator))
print(isinstance([],Iterator))
print(isinstance({1,2,3},Iterator))
print(isinstance(iter('adb'),Iterator))