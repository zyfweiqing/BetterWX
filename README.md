# BetterWX
<img width="400" src="https://github.com/user-attachments/assets/4bdfb590-d913-4543-b54c-347f6b1d14e7" />

微信 PC 4.0 防撤回/多开补丁工具

支持平台：Windows x64<br>
验证版本：**WeChat 4.0.3.34**

## 使用方法
0. 首先你要有比较新的 [Python](https://www.python.org/downloads/)，并且关掉了微信和烦人的安全管家。
1. 把仓库克隆下来。
2. 运行下列补丁代码，填入对应的文件路径（不填=自动查找），保存修改前会自动备份原文件。<br>

   - `revoke.py`：**防撤回无提示**<br>将所有的 revokemsg 撤回操作消息改为未知消息，不能成功撤回也没有撤回提示。

   - `unmutex.py`：**多开**<br>移除 4.0.3+ Mutex 检测，可以多次启动同一个微信程序。**不推荐用于登录多个账号，容易闪退。**

   - `coexist.py`：**共存版制作器**<br>选择编号 ζ=0~9，创建一个共存版 Weixinζ.exe（最多十个），隔离设置和自动登录端口。<br>共存版的所有消息记录和原版共用，可以随意换着登录。

   - `sound_extract.py`：**提取提示音**<br>提取提示音到当前目录，文件名为 `Sound_编号_十六进制大小.wav`。

   - `sound_replace.py`：**修改提示音**<br>替换提示音，新的音频必须为 WAV 格式，大小不能超过原版（超过会截断）。<br>
     - Sound 0 000110D0：锁定
     - Sound 1 0001678C：新消息通知
     - Sound 2 00022E2C：通话接通/挂断
     - Sound 3 000857AE：通话来电铃声
     - Sound 4 000126E0：解锁

## 问题解答

- 无权修改文件？<br>
  以管理员权限运行试试？还不行的话请反馈。

- 运行代码报错了？补丁失效了？<br>
  在 [**议题**](https://github.com/zetaloop/BetterWX/issues) 中反馈。

- 微信 3.9.x 能用吗？<br>
  猜你想找 [huiyadanli/RevokeMsgPatcher](https://github.com/huiyadanli/RevokeMsgPatcher)。

- Linux、macOS 能用吗？<br>
  目前不行，送我台 mac 电脑我就去学。

- 共存、防撤回这几个特性我可以挑选几个 or 全都要吗？<br>
  可以的，只需执行你要的补丁即可。但是共存必须启用多开。<br>共存版拥有单独的 `Weixin.dll`，你甚至可以让不同的共存版有不同的提示音。

- 本项目的许可证？<br>
  Unlicense，完全放弃任何权利。包括那个图标。

- 特征怎么来的？<br>
  我家猫找的。

- 作者可爱吗？<br>
  很可爱的 OwO，要不要[来看看我做的其他东西](https://github.com/zetaloop)？
