class Solution(object):
    def dailyTemperatures(self, temperatures):

        answers = [0] * len(temperatures)
        waiting_days = []


        for i in range(len(temperatures)):

            while waiting_days and temperatures[i] > temperatures[waiting_days[-1]]:
                last_day_index = waiting_days.pop()
                answers[last_day_index] = i - last_day_index
            
            waiting_days.append(i)
        
        return answers
