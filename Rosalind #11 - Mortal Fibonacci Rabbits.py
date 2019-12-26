"""
Problem

Figure 4. A figure illustrating the propagation of Fibonacci's rabbits if they die after three months.
Recall the definition of the Fibonacci numbers from “Rabbits and Recurrence Relations”, which followed the recurrence relation Fn=Fn−1+Fn−2 and assumed that each pair of rabbits reaches maturity in one month and produces a single pair of offspring (one male, one female) each subsequent month.

Our aim is to somehow modify this recurrence relation to achieve a dynamic programming solution in the case that all rabbits die out after a fixed number of months. See Figure 4 for a depiction of a rabbit tree in which rabbits live for three months (meaning that they reproduce only twice before dying).

Given: Positive integers n≤100 and m≤20.

Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

        > (n, m) 태어나서부터 m달 동안만 사는 토끼쌍에 대해서 n개월이 지난 후 토끼쌍의 갯수

Sample Dataset
6 3
Sample Output
4
"""

# 추축 = 토끼를 a, A, B, C 로 나눈다
    # a는 새끼 토끼쌍 / A, B, C 는 성체 토끼쌍
        # C 는 다음달에는 죽어서 안 나타남

# sample >> (6_th month, live for 3_month)
"""
replace "a' -> "A"
replace "A" -> "B", "a"
replace "B" -> "C", "a"
replace "C" -> ""
"""
# 여러곳에 적용 시키려면
"""
1 -> 2 (1 이면 +1 반환)
2 -> 1, 3 (2 이상이면 1, r+1 반환)
.
.
m-1 -> 1, m
m -> X (m 이면 정지)
"""

"""def mortal_fibo_rabbit(m):
    rabbit = [1]
    for i in rabbit:
            if i == 1:
                del rabbit[i]
                rabbit.append(2)
            elif i == m:
                del(rabbit[i])
            else:
                rabbit[i] += 1
                rabbit.append(1)

print(mortal_fibo_rabbit(3))"""
# Failed

# retry
def mortal_fibo_rabbit(n, m):
	gen = [0]*m
	gen[0], gen[1] = 0,1
	for x in range(2, n):
		temp = list(gen)
		gen[0] = sum(gen[1:])
		for i in range(1, m):
			gen[i] = temp[i-1]
	return sum(gen)

print(mortal_fibo_rabbit(82, 20))

print("")
# or

def fib(n, m):
  ages = [1] + [0]*(m-1)
  for i in range(n-1):
    ages = [sum(ages[1:])] + ages[:-1]
  return sum(ages)

print(fib(82, 20))