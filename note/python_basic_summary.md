# python中的变量类型
变量赋值简单粗暴不需要声明类型，灵活多变，非常好用。  
数字数据类型是不可改变的数据类型，改变数字数据类型会分配新的对象。  
字符串的操作有基本的功能不需要再自己进行并接遍历操作。  
列表用"[]" 类似C中的数组;  
元组用"()" 内部元素用逗号隔开。但是元组不能二次赋值，相当与只读列表。  
字典用"{}" 字典由索引key和它对应的值value组成。  

变量赋值
```python
a = 1
b = "abcd"
```
字符串赋值  
```python
str_ = 'this is a string'
```
列表串赋值  
```python
lists = ['this','is','a','list']
```
元组赋值
```python
tuples = ('this','is','a','tuple')
```
字典赋值  
```python
dicts = {1:'this',2:'is',3:'a',4:'dict'}
```

数据类型分为**数字型**和**非数字型**  
数字型包括整型，长整型，浮点型，复数型;  
非数字型包括字符串，列表，元组，字典;  

非数字型的共同点：  
都可以使用切片、链接(+)、重复( * )、取值（a[]）等相关运算;  
非数字型的不同点：  
列表可以直接赋值，元组不可以赋值，字典按照dict[key]=value方式赋值。  