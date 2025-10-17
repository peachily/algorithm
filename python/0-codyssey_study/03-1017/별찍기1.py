def star_2():
  N = int(input())
  answer = ''
  for i in range(1, N+1):
    spaces = ' ' *(N-i)
    stars = '*' *i
    answer += spaces +stars +'\n'
  return answer

print (star_2())