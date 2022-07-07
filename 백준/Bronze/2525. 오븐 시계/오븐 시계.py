h, m = input().split()
h = int(h)
m = int(m)
m_oven = int(input())

extra_h = 0
if (m+m_oven)//60 == 0:
    print(h, m+m_oven)
else:
    print((h+(m+m_oven)//60)%24, (m+m_oven)%60)