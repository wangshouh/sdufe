# 山东财经大学疫情打卡自动化——基于Python requests库
### 百度智慧云API获取
请自行参见[该网站](https://cloud.baidu.com/doc/OCR/s/dk3iqnq51)
> 百度智慧云登录可选择使用冗余百度系APP扫码
> 
> 百度智慧云的通用文字识别（标准版），一天可免费调用50,000次

### basicinfo获取
1. 打开任一浏览器（以下以firefox为例）
2. 打开山东财经大学区块链打卡系统的官网，并打开打卡页面 ![gXaU8x.png](https://z3.ax1x.com/2021/05/23/gXaU8x.png)
3. 如实填入相关信息后，并输入错误验证码 
<p align="center">
  <img src="https://z3.ax1x.com/2021/05/23/gXajMT.png" />
</p>
4. 点击F12后，打开 `Network` 选项卡 
<a href="https://imgtu.com/i/gXd2TJ"><img src="https://z3.ax1x.com/2021/05/23/gXd2TJ.png" alt="gXd2TJ.png" border="0" /></a>
5. 点击 `handle_ext_do` file,在左侧的弹出窗口选择 `Request` ,再点击 `Raw` ，复制字符串
<a href="https://imgtu.com/i/gXwi7Q"><img src="https://z3.ax1x.com/2021/05/23/gXwi7Q.png" alt="gXwi7Q.png" border="0" /></a>
6. 删除`verify=1111`,剩余部分输入 `main.py` 中的指定位置

```python
#打卡基础信息，请自行查阅JS代码填写
basicinfo = 

```

免责声明：
本人不对此程序所造成的一切后果担责。
