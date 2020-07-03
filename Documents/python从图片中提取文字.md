# python从图片中提取文字

笔者环境:Arch Linux

## 1. 系统安装`teseract`和英文中文语言包

arch下安装十分简单，pacman会自动帮我们解决所有依赖

```zsh
sudo pacman -S tesseract tesseract-data-eng tesseract-data-chi_sim
```

## 2. python安装必要的第三方库

```
sudo pip install pillow
sudo pip install pytesseract
```

## 2. 代码展示

分别识别中文，英文，数字

我测试时识别的图片在代码同一目录下的img目录下

```python
import os
import pytesseract
from PIL import Image

BASE_DIR = os.path.dirname(__file__)

zh_img = os.path.join(BASE_DIR, "img/zh_demo.png")
en_img = os.path.join(BASE_DIR, "img/en_demo.png")
num_img = os.path.join(BASE_DIR, "img/num_demo.png")

zh = pytesseract.image_to_string(Image.open(zh_img), lang="chi_sim").replace(" ","")    # 中文识别有时不是特别准确，识别结果中间有空格
en = pytesseract.image_to_string(Image.open(en_img))    # 也只有识别规矩的英文和数字了，可以用来破解低级验证码
num = pytesseract.image_to_string(Image.open(num_img))

print(zh)	# 山重水覆疑无路,柳暗花明又一村
print(en)	# kainhuck
print(num)	# 0771-5785703


```

