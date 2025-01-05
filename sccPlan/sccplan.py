#!/usr/bin/python3
import sys
import os
def parser():
    try:
        if sys.argv[1] == '--new' or sys.argv[1] == '-n':
            makePlan()
        elif sys.argv[1] == '--list' or sys.argv[1] == '-l':
            listPlan()
        elif sys.argv[1] == '--remove' or sys.argv[1] == '-r':
            killPlan()
        elif sys.argv[1] == '--help' or sys.argv[1] == '-h':
            helpText = open('help', 'r')
            print(helpText.read())
        else:
            print('Error: Invalid command')
    except IndexError:
        print('Error: Malformed argument')
def makePlan():
    while True:
        try: 
            planFile = sys.argv[2]
            open(planFile, 'x')
            print(f'Created plan with file name {planFile}!')
            while True:
                addPlan = input('Plan name(type "end to finish"): ')
                with open(planFile, 'a') as file:
                    file.write('- ' + addPlan + '\n')
                if addPlan == 'end':
                    os.system('sed -i "$ d" {0}'.format(planFile))
                    listPlanFile = open(planFile, 'r')
                    print(listPlanFile.read())
                    exit(1)
        except KeyboardInterrupt:
            print('\nGoodbye!')	
            break
        except FileNotFoundError:
            print('You need a file name!')
            continue
        except FileExistsError:
            print(f'File name {addPlan} exists!')
        except UnboundLocalError:
            print('')
            continue
def listPlan():
    try:
        askName = sys.argv[2]
        listPlanVar = open(askName, 'r')
        print(listPlanVar.read())
    except FileNotFoundError:
        print('File name not found!') # Ok so the reason this is not a f-string is cuz i kept getting an "UnboundLocal" error :P
def killPlan():
    if os.path.exists(sys.argv[2]):
        os.remove(sys.argv[2])
        print(f'Removed plan {sys.argv[2]}.')
    else:
        print(f'The plan {sys.argv[2]} does not exist!')
parser()


