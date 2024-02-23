# Enter your code here. Read input from STDIN. Print output to STDOUT

x = input()

enq = []
deq = []

for i in range(int(x)):
    q = input()
    func = int(q[0])

    if func == 1:
        val = int(q[2:])
        enq.append(val)
    elif func == 2:
        if not deq:
            for i in range(len(enq)):
                deq.append(enq.pop())
        deq.pop()
    else:
        if deq:
            print(deq[-1])
        elif enq:
            print(enq[0])
