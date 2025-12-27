# 이차원 배열 순회 연습입니다.

def main():
    cy, cx = 2, 2   # 현재 위치
    rows, cols = 4, 5  # 격자 크기
    moves = [(-1,0), (1,0), (0,-1), (0,1)]  # 상, 하, 좌, 우

    # 1️. (cx, cy)에서 갈 수 있는 상하좌우 좌표를 모두 구해
    #    grid 안에 있는 경우만 valid 리스트에 담아라.
    valid = []
    for dy, dx in moves:
        ny, nx = ________, ________   # 새 좌표
        if 0 <= ny < rows and 0 <= nx < cols:
            valid.append((ny, nx))
            pass

    print("valid moves:", valid)

if __name__ == "__main__":
    main()