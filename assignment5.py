#assignment 5
#problem 1

School_marksheet = {'Rohit' : 45, 'Suresh' : 50, 'Mukesh' : 49, 'Srushti':48, 'Sayli':46, 'Vasundara':50 }

while True:
    print("NOTE:- Capaitalize your name.")
    name = input("Enter your name:- ")
    name = str(name)

    try:
        print("welcome", name , "your grades are here")
        print( name,"'s grade:- ", School_marksheet[name])

    except:
        print('your name is not in the list')
        break

#problem 2

list = [1,2,3,4,5,6,7,8,9,10]
extractor = []

for i in range(5):

    z = i
    extractor.append(list[z])

print(extractor)
 
z = 4
reverser = []
for i in range(5):
    i = i + z
    z = z - 2
    reverser.append(extractor[i])
print(reverser)