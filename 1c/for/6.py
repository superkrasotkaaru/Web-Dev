# Çàäà÷à ¹338. Ïåðåâåðíè ÷èñëî
# Âõîäíûå äàííûå
# Ââîäèòñÿ íàòóðàëüíîå ÷èñëî x

# Âûõîäíûå äàííûå
# Âûâåäèòå ÷èñëî, ñîñòîÿùåå èç öèôð äàííîãî ÷èñëà x â îáðàòíîì ïîðÿäêå. Âåäóùèå íóëè âûâîäèòü íå íóæíî.

a, res = input(), 0
n = int(a)
for i in range(len(a)):
    d = n % 10
    n //= 10
    res *= 10
    res += d
print(res)

# a = input()
# print(int(a[::-1]))