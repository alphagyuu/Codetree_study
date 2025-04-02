class Day:
    def __init__(self,date,day,weather):
        self.date=str(date)
        self.day=str(day)
        self.weather=str(weather)
    def out(self):
        print(f"{self.date} {self.day} {self.weather}")
ln=int(input())
days=[
    Day(*input().split())
    for _ in range(ln)
]
close=min(list(filter(lambda x:x.weather=="Rain",days)),key=lambda x: x.date )
close.out()