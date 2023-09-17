from sys import stdin

N = int(stdin.readline())

# stack = list(stdin.readline() for _ in range(N))
st = []
result = []
start = 1

for n in range(N):
    num = int(stdin.readline())
    # for i in range(1,num+1):
    while start <= num:     # 조건이 만족할때까지 반복, 조건에 부합하지않으면 pass
        st.append(start)
        result.append("+")
        start += 1
    
    if st[-1] == num:  # num = 4, 
        st.pop()      
        result.append("-")
    else:               
        print("NO")
        result.clear()       
        flag = 1           
        break   

if result is not None: print("\n".join(oper for oper in result))