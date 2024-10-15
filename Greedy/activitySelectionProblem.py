'''
    Given N number of activities with their start
    and end times. We need to select the max
    number of activities that can be performed
    by a single person, assuming that a person
    can only work on a single activity at a time.
'''

activities = [["A1",0,6],
              ["A2",3,4],
              ["A3",1,2],
              ["A4",5,8],
              ["A5",5,7],
              ["A6",8,9]]

def printMaxActivities(activities):
    activities.sort(key = lambda x:x[2])
    i = 0
    firstA = activities[i][0]
    print(firstA)
    for j in range(len(activities)):
        if activities[i][2] < activities[j][1]:
            print(activities[j][0])
            i = j

printMaxActivities(activities)