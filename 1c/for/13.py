# Çàäà÷à ¹345. Íóëè
# Âõîäíûå äàííûå
# Ââîäèòñÿ ÷èñëî N, à çàòåì N ÷èñåë.

# Âûõîäíûå äàííûå
# Ïîäñ÷èòàéòå è âûâåäèòå, ñêîëüêî ñðåäè äàííûõ N ÷èñåë íóëåé.


n = int(input())
cnt = sum(1 for i in range(n) if int(input()) == 0)
print(cnt)