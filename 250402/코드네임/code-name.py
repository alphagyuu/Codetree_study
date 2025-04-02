class Agent:
    def __init__(self,c,score):
        self.c=str(c)
        self.score=int(score)

agents=[
    Agent(*input().split())
    for _ in range(5)
]
low = min(agents, key=lambda x: x.score)
print(low.c,low.score)