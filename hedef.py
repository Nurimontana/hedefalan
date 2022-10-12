import math

def uzunluk(n1,n2):
	return math.sqrt(math.pow(n2[0]-n1[0],2)+math.pow(n2[1]-n1[1],2))

def alan(a,b,c):
	U = (a+b+c)/2
	return math.sqrt(U*(U-a)*(U-b)*(U-c))


n1 = (3,5)
n2 = (5,9)
n3 = (6,18)
n4 = (3,6)
noktalar = (n1,n2,n3,n4)
u1 = []
for tekrar in range(3):
	u1.append(uzunluk(noktalar[tekrar], noktalar[(tekrar+1)%3]))
#print(u1)
hedefalan = alan(*u1)
#print(hedefalan)
u2 = []
noktalar = (n1,n2,n4)
for tekrar in range(3):
	u2.append(uzunluk(noktalar[tekrar], noktalar[(tekrar+1)%3]))
ucgen2alan = alan(*u2)

u3 = []
noktalar = (n1,n3,n4)
for tekrar in range(3):
	u3.append(uzunluk(noktalar[tekrar], noktalar[(tekrar+1)%3]))
ucgen3alan = alan(*u3)

u4 = []
noktalar = (n2,n3,n4)
for tekrar in range(3):
	u4.append(uzunluk(noktalar[tekrar], noktalar[(tekrar+1)%3]))
ucgen4alan = alan(*u4)
toplamalan = ucgen2alan+ucgen3alan+ucgen4alan
print(hedefalan,ucgen2alan,ucgen3alan,ucgen4alan,toplamalan)

if toplamalan-0.00000001>hedefalan:
	print("Karavana")
else:
	print("Vuruldun")



