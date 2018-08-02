def hanoi_rec (n, A, B, C):
	global step_num
	if n == 1 :
		step_num = step_num + 1
		print("Step", step_num, ": move disk", n, "from", A, "to", C)
	else : 
		hanoi_rec(n-1, A, C, B)
		step_num = step_num + 1
		print("Step", step_num, ": move disk", n, "from", A, "to", C)
		hanoi_rec(n-1, B, A, C)

class Stack:
    def __init__(self, n=0):
        self.stack = []
        self.stack.extend(range(1,n+1))

    def pop(self):
        return self.stack.pop() if not self.empty() else 0
    
    def push(self, disk):
        self.stack.append(disk)

    def empty(self):
        return len(self.stack)==0

    def top(self):
        return self.stack[-1] if not self.empty() else 0


class hanoi():
    def __init__(self, src=1, dst=3):
        self.dst = dst
        #make index from 1
        self.hanoi = [None]
        #[1 to n]
        self.hanoi.append(Stack(n))
        #[]
        self.hanoi.append(Stack(0))
        #[]
        self.hanoi.append(Stack(0))

        
    def realmove(self, src, dst):
        disk = self.hanoi[src].pop()
        self.hanoi[dst].push(disk)
        if src == 1 :
        	s = 'A'
        elif src == 2 :
            s = 'B'
        else: s = 'C'
        if dst == 1 :
        	d = 'A'
        elif dst == 2 :
            d = 'B'
        else: d = 'C'
        print("move disk", n-disk+1, "from", s, "to", d)
        

    def move(self, one, two):
        top1 = self.hanoi[one].top()
        top2 = self.hanoi[two].top()
        # num bigger, disk smaller 
        if top1 > top2:
            self.realmove(one, two)
        else:
            self.realmove(two, one)


global step_num
step_num = 0
n = input("Please input disk number : ")
n = int(n)
#using recursion
hanoi_rec(n, 'A', 'B', 'C')
print("Moving", n, "disk hanoi tower with recursion needs", step_num, "steps\n")
#without using recursion
step_num = 0
if n % 2 ==1: #if num of disk is odd A=1, B=2, C=3
	flow = ((1, 3), (1, 2), (2, 3))
else:
	flow = ((1, 2), (1, 3), (2, 3))
s = hanoi(n)
for i in range(1, 2**n):
	step_num = step_num + 1
	print("Step", step_num, ": ", end = "")
	s.move(*flow[(step_num-1) % 3])
print("Moving", n, "disk hanoi tower without recursion needs", step_num, "steps\n")
