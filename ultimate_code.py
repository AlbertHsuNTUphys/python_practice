# The argument 'agent' can be changed.
# you sould make use of the agent.hit(x) function.
# Don't try to return agent.ans, this is useless for judge.
class UltimateAgent():
    def __init__(self):
        self.ans = 1234 #you can tune the answer here
    def hit(self,x):
        if(x>self.ans):
            return "smaller"
        elif(x<self.ans):
            return "bigger"
        else:
            return "you get it"
 
def ultimate_code(agent):
    mi = 1
    ma = 100000000 
    g = mi + (ma-mi)//2
    respond = agent.hit(g)
    while (respond != "you get it") :
        if respond == 'smaller':
            ma = g
            g = mi + (ma-mi)//2
            respond = agent.hit(g)
        if respond == 'bigger':
            mi = g
            g = mi + (ma-mi)//2
            respond = agent.hit(g)
 
    return g
 
## When you want to test your function, please follow the following code.
if __name__ == '__main__':
    example_agent = UltimateAgent()
    print(ultimate_code(example_agent)) 
