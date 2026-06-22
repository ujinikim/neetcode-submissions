class TimeMap:

    def __init__(self):
        self.dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[(key, timestamp)] = value

    def get(self, key: str, timestamp: int) -> str:
        i = timestamp
        res = ""
        while i > 0:
            if (key, i) in self.dict:
                res = self.dict[(key, i)]
                return res
            else:
                i -= 1
        return res
