# Input: n = 2, logs = ["0:start:0","1:start:2","1:end:5","0:end:6"]
# Output: [3,4]
# Explanation:
# Function 0 starts at the beginning of time 0, then it executes 2 for units of time and reaches the end of time 1.
# Function 1 starts at the beginning of time 2, executes for 4 units of time, and ends at the end of time 5.
# Function 0 resumes execution at the beginning of time 6 and executes for 1 unit of time.
# So function 0 spends 2 + 1 = 3 units of total time executing, and function 1 spends 4 units of total time executing.
import re
class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = {}
        currentTime = 0
        
        matches = re.findall("[^:]+",logs[0])
        id_ = matches[0]
        status = matches[1]
        currentTime = int(matches[2]) + 1
            
        for i in range(1,len(logs)):
            log = logs[i]
            
            matches = re.findall("[^:]+",log)
            time = matches[2]

            if status == 'end':
                id_ = matches[0]

            print(times)
            if id_ in times:
                times[id_] += int(time) - int(currentTime) + 1
            else:
                times[id_] = int(time) - int(currentTime) + 1
                
            currentTime = time
            id_ = matches[0]
            status = matches[1]
            
        return list(times.values())
            