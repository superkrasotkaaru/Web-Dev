# Çàäà÷à ¹341. Êîëè÷åñòâî äåëèòåëåé
# Âõîäíûå äàííûå
# Ââîäèòñÿ íàòóðàëüíîå ÷èñëî x.

# Âûõîäíûå äàííûå
# Âûâåäèòå åäèíñòâåííîå ÷èñëî - êîëè÷åñòâî äåëèòåëåé ÷èñëà x.
import math

a = int(input())
divisors = set()

for i in range(1, int(math.sqrt(a)) + 1):
    if a % i == 0:
        divisors.add(i)
        divisors.add(a // i)

print(len(divisors))