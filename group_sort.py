import json

people = []

with open('studydubs.json', 'r') as id:
    people = json.load(id)

gpaSum = 0
for person in people:
    gpaSum += person['gpa']

gpaAvg = gpaSum/len(people)

print(gpaAvg)

'''
for person in people:
    for compare in people:
        groups = []
        if (abs(person['auditory'] - compare['auditory']) < 2):
            if (person['auditory'] >= 4 or compare['auditory'] >= 4):
                audio = (person['id'], compare['id'], "audio")
                groups.append(audio)
            else:
                audio = (person['id'], compare['id'], "")
                groups.append(audio)
        if (abs(person['visual'] - compare['visual']) < 2):
            if (person['visual'] >= 4 or compare['visual'] >= 4):
                visual = (person['id'], compare['id'], "visual")
                groups.append(visual)
            else:
                visual = (person['id'], compare['id'], "")
                groups.append(visual)  
        if (abs(person['kinect'] - compare['kinect']) < 2):
            kinect = (person['id'], compare['id'], "")
            groups.append(kinect)  
        
        matches = groups
        mat = []
        #print(matches)
        filt = list(filter(lambda x: x[2] != "", matches))
        for set in filt:
            if (set[0] != set[1]):
               if (len(set) == 3):
                   m = set
                   print(m)
                   mat.append(m);
                   #matches.remove(set);
        '''
'''
        maat = []
        for match in matches:
            if (match[0][0] == match[0][1]):
                match.remove(            
        '''

def Sort_Tuple(tup): 
    return(sorted(tup, key = lambda x:x[1], reverse=True)) 

for person in people:
    matches = []
    for compare in people:
        points = abs(person['gpa']-compare['gpa'])
        if (person == compare): 
            points = 0
        else:
           if (compare['auditory'] > 0):
               if (compare['auditory'] == 1 or person['auditory'] == 1):
                   points += 0
               elif  (compare['auditory'] == 2 or person['auditory'] == 2):
                   points += 1 
               elif  (compare['auditory'] == 3 or person['auditory'] == 3):
                   points += 2
               elif  (compare['auditory'] == 4 or person['auditory'] == 4):
                   points += 3  
               else:
                   points += 4
           if (compare['visual'] > 0):
               if (compare['visual'] == 1 or person['visual'] == 1):
                   points += 0
               elif  (compare['visual'] == 2 or person['visual'] == 2):
                   points += 1 
               elif  (compare['visual'] == 3 or person['visual'] == 3):
                   points += 2
               elif  (compare['visual'] == 4 or person['visual'] == 4):
                   points += 3  
               else:
                   points += 4
           if (compare['kinect'] > 0):
               if (compare['kinect'] == 1 or person['kinect'] == 1):
                   points += 0
               elif  (compare['kinect'] == 2 or person['kinect'] == 2):
                   points += 1 
               elif  (compare['kinect'] == 3 or person['kinect'] == 3):
                   points += 2
               elif  (compare['kinect'] == 4 or person['kinect'] == 4):
                   points += 3  
               else:
                   points += 4
        scores = (person['id'], points)  
        matches.append(scores)
        sorts = Sort_Tuple(matches)
    print(sorts)              
    print(person['names'] + " is paired with " + str(sorts[0][0]))               