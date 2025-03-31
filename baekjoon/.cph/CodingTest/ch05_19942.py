# 19942
# 재귀(백트래킹)
# 틀렸음 다시 풀어보기 - 조건 확인

def recursion(idx, Protein, Fat, Carbo, Vitamin, Price):
    global answer
    global used
    global used_idx
    
    
    if protein <= Protein and fat <= Fat and carbo <= Carbo and vitamin <= Vitamin:
        if answer > Price:
            answer = min(answer, Price)
            used_idx = []
            for i in used:
                used_idx.append(i)
    
    if idx == n:
        return
        
    # 재료가 선택 되었다면
    used.append(idx+1)
    recursion(idx+1, ingredient[idx][0]+Protein,
        ingredient[idx][1]+Fat, ingredient[idx][2]+Carbo,
        ingredient[idx][3]+Vitamin, ingredient[idx][4]+Price)
        
    
    # 재료가 선택되지 않았다면
    used.pop()
    recursion(idx+1, Protein, Fat, Carbo, Vitamin, Price)
        
    



n = int(input())
used = []
used_idx = []

protein, fat, carbo, vitamin = list(map(int, input().split()))

ingredient = [list(map(int, input().split())) for _ in range(n)]

answer = 999999999
recursion(0, 0, 0, 0, 0, 0)

print(answer)
print(*used_idx)