from datetime import date
import webbrowser, time, sys
today = str(date.today())
def foodtracker():
    

    with open('date.txt') as f:
        todaysdate = f.read()
        
        
        if str(today) != todaysdate:

            with open('date.txt','w') as f:
                f.write(str(today))
            with open('counts.txt','w') as f:
                f.write('0 0')


    with open('foodlibrary.txt') as f:
        foodlib = f.readlines()
    calcount = 0
    proteincount = 0

    while True:

    #ask for userinput
        userinput = input('what did you eat fatty?: ')
        amount = input('how many fatass: ')
        thingy = True
        for i in foodlib:
            if userinput in i:
                tempthing = i.split()
                calcount +=  int(tempthing[1])*int(amount)
                proteincount += int(tempthing[2])*int(amount)
                thingy = False
        if thingy == True:
            calinput = input('how many calories are in this?: ')
            proteininput = input('how much protein is in this?: ')
            with open('foodlibrary.txt','a') as f:
                f.write(f'{userinput} {calinput} {proteininput} \n')
            calcount += int(calinput)*int(amount)
            proteincount += int(proteininput)*int(amount)
        askagain = input('Anything else? y/n: ')
        if askagain == 'n':
            break
        else:
            continue
    with open('counts.txt','r') as f:
        oldcounts = f.read()
        mylist = oldcounts.split()


    with open('counts.txt','w') as f:
        f.write(f'{calcount+int(mylist[0])} {proteincount+int(mylist[1])}')
        
    counts()
    
    finalthing = input('hit any key to exit: ')
            



def meditation():
    
    
    med_start = input("Press Enter to start, or x to leave: ")
    if med_start == 'x':
        return
    else:
        start_time = time.time()

        input("Press Enter to stop")
        end_time = time.time()

        time_lapsed = end_time - start_time
        medtime = time_convert(time_lapsed)
        with open('meditationlog.txt','a') as f:
            f.write(f'{today} {medtime} \n')
            

def time_convert(sec):
    mins = sec // 60
    sec = sec % 60
    hours = mins // 60
    mins = mins % 60
    time_lapsed = "Time Lapsed = {0}:{1}:{2}".format(int(hours), int(mins), int(sec))
    return time_lapsed

        
def counts():
    with open('counts.txt') as f:
        mycounts = f.read().split()
        print(f'{mycounts[0]} calorie(s) and {mycounts[1]} grams of protein')
def medlog():
    with open('meditationlog.txt') as f:
        print(f.read())
boo = True
while boo:
    userwelcome = input('welcome prizm, what would you like to do today?: ')
    if userwelcome == 'food':
        foodtracker()
    elif userwelcome == 'meditation':
        meditation()
    elif userwelcome == 'counts':
        counts()
    elif userwelcome == 'exit':
        sys.exit()
    elif userwelcome == 'medlogs' or userwelcome == 'meditation logs':
        medlog()
    else:
        print('unknown command, try again')
        continue