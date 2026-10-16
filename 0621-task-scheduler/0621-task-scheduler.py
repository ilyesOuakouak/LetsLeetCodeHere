class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        dic = {}
        remaining = len(tasks)
        result = 0

        for task in tasks:
            count = dic.get(task, [0, 0])[0] + 1
            dic[task] = [count, 0]

        while remaining > 0:

            # job 1: pick the ready task with the highest count
            chosen = None
            for key in dic:
                if dic[key][0] > 0 and dic[key][1] == 0:
                    if chosen is None or dic[key][0] > dic[chosen][0]:
                        chosen = key

            # job 2: tick. Every wait above 0 goes down by 1
            for key in dic:
                if dic[key][1] > 0:
                    dic[key][1] -= 1

            # job 3: set. The chosen task has one less left and must wait n
            if chosen is not None:
                dic[chosen][0] -= 1
                dic[chosen][1] = n
                remaining -= 1

            result += 1      # every slot counts, a task or an idle

        return result