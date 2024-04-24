# 定義條件不等式
def f(x, y):
	if (x**2 + y**2 - 1)**3 > x**2 * y**3:
		return 1
	else:
		return 0

# 設定顏色
cc = [(255, 0, 0), (255, 255, 255)]		# 紅色 白色

# 開一張畫紙
from PIL import Image
m = 10000
n = 10000
pic = Image.new("RGB", (m, n))

# 定義著色方法
for i in range(m):
	x = 4 * i / m - 2		# x的範圍為 [-2, 2]
	for j in range(n):
		y = -(4 * j / n - 2)
		pic.putpixel((i, j), cc[f(x, y) % len(cc)])		# x的範圍為 [-2, 2]

# 儲存圖片
pic.save("heart.png")
print("ok")
