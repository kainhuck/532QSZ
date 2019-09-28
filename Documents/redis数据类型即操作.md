## redis数据类型即操作

### 1. 字符串

- **set**

  设置字符串

  格式: set key value

  例子: set name kainhuck

- **get**

  获取字符串的值

  格式: get key

  例子: get name

- **incr**

  对值做加一操作

  要求: 该字符串为数字字符串

  格式: incr key

  例子: incr age

- **inrcby**

  对值加指定值

  要求: 该字符串为数字字符串

  格式: incrby key num

  例子: incrby age 50

### 2.hash

类似Python中的字典

- **hset**

  设置哈希的一组key和value

  格式: hset hashname key value

  例子: hset user:01 name kainhuck

  例子: hset user:01 age 18

- **hget**

  获取哈希一组key对应的value

  格式: hget hashname key

  例子: hget user:01 name

- **hmset**

  设置哈希的多组key和value

  格式: hset hashname key1 value1 key2 value2 ....

  例子: hset user:01 name kainhuck age 18

- **hmget**

  获取哈希多组key对应的value

  格式: hmget hashname key1 key2 ...

  例子: hmget user:01 name age

- **hgetall**

  获取哈希所有key对应的value

  格式: hgetall hashname

  例子: hgetall user:01

### 3.链表

- **lpush**

  从左边向链表添加元素

  格式: lpush listname value

  例子: lpush namelist kainhuck

- **lrange**

  获取链表中的数据

  格式: lrange listname start end

  格式: lrange namelist 0 -1

- **rpush**

  从右边向链表添加元素

  格式: rpush listname value

  例子: rpush namelist kainhuck

- **ltrim**

  截取链表,删除其他

  格式: ltrim listname start end

  例子: ltrim namelist 0 1
  
- **lpop**

  从左边将链表元素弹出

  格式: lpop listname

  例子: lpop namelist

- **llen**

  获取链表长度

  格式: llen listname

  例子: llen namelist

### 4.集合

- **sadd**

  向集合中添加元素

  格式: sadd setname value

  例子: sadd idset 1

- **smembers**

  获取集合元素

  格式: smembers setname 

  例子: smembers idset

- **sdiff**

  获取集合差集(集合1中存在,集合2中不存在)

  格式: sdiff setname1 setname2

  例子: sdiff set1 set2

- **sinter**

  获取交集

  格式: sdiff setname1 setname2

  例子: sdiff set1 set2

- **sunion**

  获取并集

  格式: sunion setname1 setname2

  例子: sunion set1 set2

- **scard**

  获取集合中的元素个数

  格式: scard setname

  例子: scard set1

### 5.有序集合

元素由两部分组成: 序号和值

取出有序集合里面的元素时,要根据序号排序,取出

- **zadd**

  向有序集合中添加元素,默认是升序排列

  格式: zadd zsetname number value

  例子: zadd zset 10 kainhuck

  例子: zadd zset 12 hahaha

- **zrange**

  按序号升序获取有序集合内容

  格式: zrange zsetname start end

  例子: zrange zset 0 -1

- **zrevrange**

  按序号降序获取有序集合内容

  格式: zrevrange zsetname start end

  例子: zrevrange zset 0 -1

- **zcard**

  获取有序集合长度

  格式: zcard zsetname

  例子: zcard zset