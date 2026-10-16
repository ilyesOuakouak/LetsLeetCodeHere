class TimeMap:

    def __init__(self):
        self.data = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.data:
            self.data[key] = []
        self.data[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.data:
            return ""

        my_list = self.data[key]

        left = 0
        right = len(my_list) - 1
        saved = 0

        while left <= right:
            mid = (left + right) // 2
            if my_list[mid][1] <= timestamp:
                saved = my_list[mid][0]
                left = mid + 1
            
            else:
                right = mid - 1

        return saved if saved else ""



            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)