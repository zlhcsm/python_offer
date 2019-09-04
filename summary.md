
[TOC]

### 行输入
```python
x = input()
```
---
### k行输入，输入一位数组

```python
k = 5
list1 = []
while k > 0:
    x = input()
    list1.extend(x.strip().split(" "))
list
```
---
### 数组操作
#### 访问列表中的值
```python
list1 = [1, 2, 3, 4, 5, 6]
list2 = ['a', 'b', 'c']
list2[0] # a
list1[1:5] #[2, 3, 4, 5]
```
#### 更新
```python
list = []
list.append('Google')
list.append('Runoob')
list
# ['Google', Runboon]

```
----
### extend和append的区别
```python
li = ['a', 'b', 'c']
zl = ['d', 'e', 'f']
li.extend(zl)
# ['a', 'b', 'c', 'd', 'e', 'f']

li.append(zl)
# ['a', 'b', 'c', ['d', 'e', 'f']]

```
---
### 同时迭代两个list
```python
li = ['a', 'b', 'c']
zl = ['d', 'e', 'f']
for (x, y) in zip(li, zl):
    print(x, y)
#a d
#b e
#c f
```