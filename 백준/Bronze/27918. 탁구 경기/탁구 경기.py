round = int(input())

dal_score = 0
pnx_score = 0

for n in range(round):
    winner = input()
    if winner == 'D':
        dal_score += 1
    elif winner == 'P':
        pnx_score += 1
    
    if abs(dal_score - pnx_score) >= 2:
        break

print(f'{dal_score}:{pnx_score}')