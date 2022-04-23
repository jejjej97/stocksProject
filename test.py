# 교집합
from View.bookmark.bookmark import bookmarkdao
from Model.bookmark.bookmarkvo.bookmarkvo import bookmarkVO

stockname = ['삼성']
b = ['삼성', '퍼스텍', '카카오']

if '삼성' not in b:
    print('a')


data = bookmarkdao.selectall('jejjej97@')
for i in range(len(data)):
    a = bookmarkVO.pr(data[i])
    print(a[1])

