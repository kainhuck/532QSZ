# 前言

[参考文章](<https://www.jianshu.com/p/4ba20afacce2>)

-------------

利用Python加密先确保待加密数据为字节类型

利用`encode()`将数据转化为字节类型,Python字节类型的字符串以***b***开头,

如`b'abcdefg'`

举个例子:

```python
In [1]: "kainhuck".encode()                                                     
Out[1]: b'kainhuck'

In [2]: "你好".encode()                                                         
Out[2]: b'\xe4\xbd\xa0\xe5\xa5\xbd'
```

注意中文转换成字节时的显示,

#### 引用`binascii`模块

```Python
In [3]: import binascii                                                         

In [4]: binascii.b2a_hex("你好".encode())                                       
Out[4]: b'e4bda0e5a5bd'
```

对比和上面的输出结果

***注意,binascii方法的操作对象是字节.***

# URL编码

URL编码出现在URL中,为了避免***特殊字符***的出现,

特点:格式为`%`后面跟上两个十六进制数

使用`urllib`模块的`parse`进行URL编码

```Python
In [6]: from urllib import parse                                                

In [7]: parse.quote("你好")                                                     
Out[7]: '%E4%BD%A0%E5%A5%BD'

In [8]: parse.quote("hello9")                                                   
Out[8]: 'hello9'

In [9]: parse.quote("#$%^&*(")                                                  
Out[9]: '%23%24%25%5E%26%2A%28'
```

***注意只对特殊字符编码***

# Base64编码

- Base64是一种用64个字符来表示任意二进制数据的方法。

- Base64编码可以称为密码学的基石。可以将任意的二进制数据进行Base64编码。所有的数据都能被编码为并只用65个字符就能表示的文本文件。（ 65字符：A~Z a~z 0~9 + / = ）编码后的数据~=编码前数据的4/3，会大1/3左右。

#### 原理

1. 将所有字符转化为ASCII码。
2. 将ASCII码转化为8位二进制 。
3. 将二进制3个归成一组(不足3个在后边补0)共24位，再拆分成4组，每组6位。
4. 统一在6位二进制前补两个0凑足8位。
5. 将补0后的二进制转为十进制。
6. 从Base64编码表获取十进制对应的Base64编码。

#### 例子

使用`base64`进行base64加密

```python 
In [14]: import base64                                                          

In [15]: base64.b64encode(b"hello")                                             
Out[15]: b'aGVsbG8='

In [16]: base64.b64decode(b'aGVsbG8=')                                          
Out[16]: b'hello'

In [17]: base64.b64encode("你好".encode())                                      
Out[17]: b'5L2g5aW9'

In [18]: base64.b64decode( b'5L2g5aW9')                                         
Out[18]: b'\xe4\xbd\xa0\xe5\xa5\xbd'

In [19]: b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode()                                   
Out[19]: '你好'
```

# MD5

md5（信息-摘要算法），其实就是一种算法。可以将一个字符串，或文件，或压缩包，执行md5后，就可以生成一个固定长度为128bit的串。这个串，基本上是唯一的。

#### 特点

1. 压缩性：任意长度的数据，算出的MD5值长度都是固定的。

2. 容易计算：从原数据计算出MD5值很容易。

3. 抗修改性：对原数据进行任何改动，哪怕只修改1个字节，所得到的MD5值都有很大区别。

4. 强抗碰撞：已知原数据和其MD5值，想找到一个具有相同MD5值的数据（即伪造数据）是非常困难的。

5. 不可逆性：每个人都有不同的指纹，看到这个人，可以得出他的指纹等信息，并且唯一对应，但你只看一个指纹，是不可能看到或读到这个人的长相或身份等信息。

#### 例子

Python3中使用`hashlib`进行MD5加密

```Python
import hashlib

# 待加密数据
# string = b"hello"
string = "你好"

# 创建MD5对象
hl = hashlib.md5()

# 参数为字节
hl.update(string.encode())

print('MD5加密前为 ：', string)
print('MD5加密后为 ：', hl.hexdigest())

# 输出
# MD5加密前为 ： 你好
# MD5加密后为 ： 7eca689f0d3389d9dea66ae112e5cfd7
```

#### 注意

md5的长度，默认为128bit，也就是128个0和1的二进制串。这样表达是很不友好的。所以将二进制转成了16进制，每4个bit表示一个16进制，所以128/4 = 32 换成16进制表示后，为32位了。

# Python加密库PyCryptodome

这是一个第三方库,使用前请安装

# DES

- DES算法为密码体制中的对称密码体制，又被称为美国数据加密标准。
- DES是一个分组加密算法，典型的DES以64位为分组对数据加密，加密和解密用的是同一个算法。
- DES算法的入口参数有三个：Key、Data、Mode。其中Key为7个字节共56位，是DES算法的工作密钥；Data为8个字节64位，是要被加密或被解密的数据；Mode为DES的工作方式,有两种:加密或解密。
- 密钥长64位，密钥事实上是56位参与DES运算（第8、16、24、32、40、48、56、64位是校验位，使得每个密钥都有奇数个1），分组后的明文组和56位的密钥按位替代或交换的方法形成密文组。

#### 例子

```Python
from Crypto.Cipher import DES
import binascii

# 这是密钥
key = b'abcdefgh'
# 需要去生成一个DES对象
des = DES.new(key, DES.MODE_ECB)

# 需要加密的数据
text = '你好世界, hello world'

# 长度必须被8整除,一个汉字长度为3,为方便字节对字节进行计算
text = text.encode()
text = text + (8 - (len(text) % 8)) * b'='

# 加密的过程
encrypto_text = des.encrypt(text)
encrypto_text = binascii.b2a_hex(encrypto_text)
print(encrypto_text)
```

# 3DES

3DES（或称为Triple DES）是三重数据加密算法（TDEA，Triple Data Encryption Algorithm）块密码的通称。它相当于是对每个数据块应用三次DES加密算法。

由于计算机运算能力的增强，原版DES密码的密钥长度变得容易被暴力破解。3DES即是设计用来提供一种相对简单的方法，即通过增加DES的密钥长度来避免类似的攻击，而不是设计一种全新的块密码算法。

3DES（即Triple DES）是DES向AES过渡的加密算法（1999年，NIST将3-DES指定为过渡的加密标准），加密算法，其具体实现如下：设Ek()和Dk()代表DES算法的加密和解密过程，K代表DES算法使用的密钥，M代表明文，C代表密文，这样：

3DES加密过程为：C=Ek3(Dk2(Ek1(M)))

3DES解密过程为：M=Dk1(EK2(Dk3(C)))

# AES

**高级加密标准**（英语：**Advanced Encryption Standard**，缩写：**AES**），在密码学中又称**Rijndael加密法**，是美国联邦政府采用的一种区块加密标准。这个标准用来替代原先的DES，已经被多方分析且广为全世界所使用。经过五年的甄选流程，高级加密标准由美国国家标准与技术研究院（NIST）于2001年11月26日发布于FIPS PUB 197，并在2002年5月26日成为有效的标准。2006年，高级加密标准已然成为对称密钥加密中最流行的算法之一。

AES为分组密码，分组密码也就是把明文分成一组一组的，每组长度相等，每次加密一组数据，直到加密完整个明文。在AES标准规范中，分组长度只能是128位，也就是说，每个分组为16个字节（每个字节8位）。密钥的长度可以使用128位、192位或256位。密钥的长度不同，推荐加密轮数也不同。

**一般常用的是128位**

#### 例子

```Python
#!/usr/bin/python3
# -*- coding: utf-8 -*-
from Crypto.Cipher import AES
from Crypto import Random
from binascii import b2a_hex

# 要加密的密文
data = "你好世界,hello world"

# 密钥key 长度必须为16（AES-128）、24（AES-192）、或32（AES-256）Bytes 长度.
# 目前AES-128足够用
key = b'this is a 16 key'
# 生成长度等于AES块大小的不可重复的密钥向量
iv = Random.new().read(AES.block_size)

# 使用key和iv初始化AES对象, 使用MODE_CFB模式
mycipher = AES.new(key, AES.MODE_CFB, iv)
# 加密的明文长度必须为16的倍数，如果长度不为16的倍数，则需要补足为16的倍数
# 将iv（密钥向量）加到加密的密文开头，一起传输
ciphertext = iv + mycipher.encrypt(data.encode())

# 解密的话要用key和iv生成新的AES对象
mydecrypt = AES.new(key, AES.MODE_CFB, ciphertext[:16])
# 使用新生成的AES对象，将加密的密文解密
decrypttext = mydecrypt.decrypt(ciphertext[16:])


print('密钥k为：', key)
print('iv为：', b2a_hex(ciphertext)[:16])
print('加密后数据为：', b2a_hex(ciphertext)[16:])
print('解密后数据为：', decrypttext.decode())
```

输出:

```
密钥k为： b'this is a 16 key'
iv为： b'e2652a5a58d75f44'
加密后数据为： b'54fa109a41963878e3424fe10d5848db94ad9d170e655eec72cd105a7e81f105'
解密后数据为： 你好世界,hello world
```



# RSA

**RSA加密算法**是一种`非对称加密算法`。在公开密钥加密和电子商业中RSA被广泛使用。

该算法基于一个十分简单的数论事实：将两个大素数相乘十分容易，但那时想要对其乘积进行因式分解却极其困难，因此可以将乘积公开作为加密密钥，即公钥，而两个大素数组合成私钥。公钥是可发布的供任何人使用，私钥则为自己所有，供解密之用。

#### 非对称加密

典型的如RSA等，常见方法，使用openssl ,keytools等工具生成一对公私钥对，使用被公钥加密的数据可以使用私钥来解密，反之亦然（被私钥加密的数据也可以被公钥解密) 。

在实际使用中私钥一般保存在发布者手中，是私有的不对外公开的，只将公钥对外公布，就能实现只有私钥的持有者才能将数据解密的方法。   这种加密方式安全系数很高，因为它不用将解密的密钥进行传递，从而没有密钥在传递过程中被截获的风险，而破解密文几乎又是不可能的。

但是算法的效率低，所以常用于很重要数据的加密，常和对称配合使用，使用非对称加密的密钥去加密对称加密的密钥。

例子

使用前先安装`rsa`

```Python
import rsa
import binascii

# 使用网页中获得的n和e值，将明文加密
def rsa_encrypt(rsa_n, rsa_e, message):
    # 用n值和e值生成公钥
    key = rsa.PublicKey(rsa_n, rsa_e)
    # 用公钥把明文加密
    message = rsa.encrypt(message.encode(), key)
    # 转化成常用的可读性高的十六进制
    message = binascii.b2a_hex(message)
    # 将加密结果转化回字符串并返回
    return message.decode()

# RSA的公钥有两个值n和e，我们在网站中获得的公钥一般就是这样的两个值。
# n常常为长度为256的十六进制字符串
# e常常为十六进制‘10001’
pubkey_n = '8d7e6949d411ce14d7d233d7160f5b2cc753930caba4d5ad24f923a505253b9c39b09a059732250e56c594d735077cfcb0c3508e9f544f101bdf7e97fe1b0d97f273468264b8b24caaa2a90cd9708a417c51cf8ba35444d37c514a0490441a773ccb121034f29748763c6c4f76eb0303559c57071fd89234d140c8bb965f9725'
pubkey_e = '10001'
# 需要将十六进制转换成十进制
rsa_n = int(pubkey_n, 16)
rsa_e = int(pubkey_e, 16)
# 要加密的明文
message = '你好世界'

print("公钥n值长度：", len(pubkey_n))
print(rsa_encrypt(rsa_n, rsa_e, message)
```

输出

```
公钥n值长度： 256
5b5f9396c609a1356c5dce4ef2674774ff2c1944ab8b002b86f7c623f81700272a19634bf77fdcc86150867552d3bc9204508e98dd15e20e12100452bb74e439bf21862160513758a4f71fde924e955e1731cabae99536f3b6c58827076a1e4a755bb8cb5728cb7f548e381224f9112c84ed54b43bf87b568599d1060c57383f
```

