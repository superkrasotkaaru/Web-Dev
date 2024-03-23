# Çàäà÷à ¹335. Êâàäðàòû
# Âûõîäíûå äàííûå
# Âûâåäèòå âñå ÷èñëà íà îòðåçêå îò a äî b, ÿâëÿþùèåñÿ ïîëíûìè êâàäðàòàìè. Åñëè òàêèõ ÷èñåë íåò, òî íè÷åãî âûâîäèòü íå íóæíî.

from math import floor, sqrt
a, b = int(input()), int(input())
for x in [i * i for i in range(floor(sqrt(a)), b + 1)]:
    if a <= x <= b:
        print(x, end=' ')