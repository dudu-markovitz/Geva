import itertools as it, random, sys, collections as coll

class Stat:
    
    stat = {}
    attempts = coll.Counter()
    
    def increase(self, k):
        self.stat[k] = self.stat.get(k, 0) + 1   
        
    def print(self):
        
        print('\nStatistics')
        print('-'*13)
        
        for k, v in sorted(self.stat.items(), key = lambda e: e):
            print(f'{k:20}{v:-5}')
        
        print()
        print('attempts  questions')
        print('--------  ---------')
        for k, v in self.attempts.items():
            print(f'{k:5}{v:-15}')


def get_int_input(prompt_msg, error_msg, default):
    
    while True:
        i = input(prompt_msg)
        if i == '':
            return default
        try:
            int_i = int(i)
        except:
            print(error_msg)
            continue
        return int_i

error_msg = 'Please insert an integer...'

range_1_start = get_int_input('range 1, start (default = 1):', error_msg, 1)
range_1_end = get_int_input('range 1, end (default = 10):', error_msg, 10)
range_2_start = get_int_input('range 2, start (default = 1):', error_msg, 1)
range_2_end = get_int_input('range 2, end (default = 10):', error_msg, 10)

range1 = (range_1_start, range_1_end + 1)
range2 = (range_2_start, range_2_end + 1)

product = list(it.product(range(*range1),range(*range2)))
random.shuffle(product)
           
stat = Stat()

for x, y in product:
    
    stat.increase('01) questions')
    
    attempts = 0
    
    while True:
        
        print(f'{x} x {y} = ?')
        answer = input ()
        
        if answer == 'quit':
            stat.print()
            sys.exit(0)
        
        try:
            answer_int = int(answer)
        except:
            print('\nPlease insert a number\n')
            continue
            
        attempts = attempts + 1
        stat.increase('02) total_answers')
        
        if answer_int == x * y:
            stat.attempts[attempts] += 1
            stat.increase('03) right_answers')
            print('\nGreat!\n')
            break
    
        stat.increase('04) wrong_answers')
        print('\nPlease try again...\n')
            
        
stat.print()        
