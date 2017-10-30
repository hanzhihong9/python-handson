
'''
with open(SOME_LARGE_FILE) as fh:
    count = # your code here
    count = sum(character.isupper() for line in fh for character in line)
'''

count = 0

for line in fh:
    for character in line:
        count += (1 if character.isupper() else 0)
        
        
def print_directory_contents(sPath):
    import os                                       
    for sChild in os.listdir(sPath):                
        sChildPath = os.path.join(sPath,sChild)
        if os.path.isdir(sChildPath):
            print_directory_contents(sChildPath)
        else:
            print(sChildPath        
        
daily_balances = [107.92, 108.67, 109.86, 110.15]
print 'daily_balances[-2 :0: -1]' + str(daily_balances[-2 : 0:-1]) ##[109.86,108.67]
print 'daily_balances[-2 : 0]' + str(daily_balances[-2 : 0]) ##[] from 2 to 0, so empty

def show_balances(daily_balances):
    num_days =  len(daily_balances)
    # do not include -1 because that slice will only have 1 balance, 
    #yesterday
    for day in range(num_days-3, num_days-1):
        print day
        balance_slice = daily_balances[day : day + 2]

        # use positive number for printing
        print("slice starting %d days ago: %s" % (abs(day),balance_slice))

show_balances(daily_balances)        



'''
class
'''
class Pet(object):
    num_pets = 0

    def __init__(self, name):
        self.name = name
        self.num_pets += 1 ## should be Pet.num_pets +=1

    def speak(self):
        print("My name's %s and the number of pets is %d" % (self.name, self.num_pets))

rover = Pet("rover")
spot = Pet("spot")       
rover.speak()   #
spot.speak()    #



question_template = {
    "title": "default title",
    "question": "default question",
    "answer": "default answer",
    "hints": []
}

def make_new_question(title, question, answer, hints=None):
    from copy import deepcopy

    new_q = deepcopy(question_template)

    # always require title, question, answer
    new_q["title"] = title
    new_q["question"] = question
    new_q["answer"] = answer

    # sometimes there aren't hints, that's fine. Otherwise, add them:
    if hints is not None:
        new_q["hints"].extend(hints)

    return new_q
    
question_1 = make_new_question("title1", "question1", "answer1", ["q1 hint1", "q1 hint2"])
question_2 = make_new_question("title2", "question2", "answer2")
question_3 = make_new_question("title3", "question3", "answer3", ["q3 hint1"])   
