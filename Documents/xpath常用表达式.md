# xpath常用表达式

| 表达式   | 说明                         |
| -------- | ---------------------------- |
| nodename | 选取nodename节点的所有子节点 |
| /        | 从当前节点获取直接子节点     |
| //       | 从当前节点获取所有子孙节点   |
| .        | 选取当前节点                 |
| ..       | 选取当前节点的父节点         |
| @        | 选取属性                     |

# xpath谓语常用表达式

| 表达式                        | 说明                                     |
| ----------------------------- | ---------------------------------------- |
| /html/body/div[1]             | 选取body子节点的第一个div节点            |
| /html/body/div[last()]        | 选取body子节点的最后一个div节点          |
| /html/body/div[last()-1]      | 选取body子节点的倒数第二个div节点        |
| /html/body/div[position()<3]  | 选取body子节点的前两个div节点            |
| /html/body/div[@id]           | 选取body子节点带有id属性的div节点        |
| /html/body/div[@id="content"] | 选取body子节点id属性值为content的div节点 |
| /html/body/div[xx>10.00]      | 选取body子节点的xx元素值大于10的节点     |



# xpath常用功能函数

| 功能函数   | 示例                                               | 说明                           |
| ---------- | -------------------------------------------------- | ------------------------------ |
| start-with | //div[start-with(@id, "co")]                       | 选取id值以co开头的div节点      |
| contains   | //div[contains(@id, "co")]                         | 选取id值包含co的div节点        |
| and        | //div[contains(@id, "co") and contains(@id, "en")] | 选取id值包含co和en的div节点    |
| text       | //li[contains(text(), "first")]                    | 选取节点文本包含first的div节点 |

