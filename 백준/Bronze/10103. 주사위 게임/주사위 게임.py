round = int(input())

cy_score = 100
sd_score = 100

for n in range(round):
    cy_dice, sd_dice = map(int, input().split())
    if cy_dice < sd_dice:
        cy_score = cy_score - sd_dice
    elif cy_dice > sd_dice:
        sd_score = sd_score - cy_dice

print(cy_score)
print(sd_score)