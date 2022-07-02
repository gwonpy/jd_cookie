# 获取京东cookie（JDcookie）的脚本-基于pysimplegui的界面和playwright

- 使用方法一
  - pip install -r requirements.txt
  - playwright install 
  - python3 jdScript.py

- 使用方法二
  - 下载后直接打开jdScript文件夹的打包好的jdScript.exe（由于使用的是playwright打包的因此程序会比较大，大概有300M+）

> 使用截图

![image-20220702103858333](.\img\image-20220702103858333.png)

![image-20220702104055141](.\img\image-20220702104055141.png)

- 点击运行后弹出浏览器界面
- 需要手动输入账号密码获取验证码登录（滑动验证那需要多划几次，京东的网页端滑动有点问题）
- 登录后程序将获取cookie到软件输出框并且将浏览器界面关闭

- 点击复制将cookie复制到剪切板
