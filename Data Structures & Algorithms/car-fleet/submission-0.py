class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        st = []
        for p, s in cars:
            time = (target - p) / s
            if not st or time > st[-1]:
                st.append(time)

        return len(st)
                 