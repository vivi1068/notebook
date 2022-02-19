### int(11)是什么意思?  
从编程语言的角度去看一个`int`类型对象, 一个`int`占用`4`个字节,    
`Signed int`(默认)它的最小存储数字是`-2147483648`, 它最大存储的数字是`2147483647`,    
`UnSigned int`它的最小存储数字是`0`, 它最大存储的数字是`4294967295`.   

> 最大值最小值是怎么计算出来的?  
- Signed Int   
  `signed_min_int = 2 ** (4 * 8) / 2 * -1 == -2147483648`  
  `signed_max_int = 2 ** (4 * 8) / 2 - 1  == 2147483647`  
  
- UnSigned Int  
  `unsigned_min_int = 0`   
  `unsigned_max_int = 2 ** (4 * 8) - 1    == 4294967295`

> 以 `UnSinged int`为例, 观察二进制形式的规律.     

|字节(byte)|位(bit)|二进制(binary)|最大值|python表达式|
|:---:|:---:|:---:|:---:|:---:|
|1|8|11111111|255|int('0b11111111', 2)|  
|2|16|`11111111` `11111111`|65535|int('0b1111111111111111', 2)|  
|3|24|`11111111` `11111111` `11111111`|16777215|int('0b111111111111111111111111', 2)|  
|4|32|`11111111` `11111111` `11111111` `11111111`|4294967295|int('0b11111111111111111111111111111111', 2)|  

了解了`int`背后相关的知识之后, 再回来看数据库中的`int(11)`的问题,   
`MySQL`在存储时并不关注建表时定义的限定值, 比如说建表时定义了 `int(1)`,    
实际存储`10`, `100`, `1000` 都是可以存储的, 只要不超过`2147483647`,    
也就是说, 这个限定值对于`MySQL`来说是没有意义的.    

它的作用是, 让像`Django ORM`这种客户端程序来约束程序的规范.  