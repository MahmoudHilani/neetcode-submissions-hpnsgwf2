class TimeMap:

    def __init__(self):
        self.dict = defaultdict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = {timestamp: value}
        else:
            self.dict[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        if timestamp in self.dict[key]:
            return self.dict[key][timestamp]
        elif timestamp < min(self.dict[key]):
            return ""
        else:
            while timestamp not in self.dict[key]:
                timestamp -= 1
            return self.dict[key][timestamp]
