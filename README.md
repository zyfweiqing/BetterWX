# BetterWX
<img width="400" src="https://github.com/user-attachments/assets/4bdfb590-d913-4543-b54c-347f6b1d14e7" />

微信 PC 4.0 防撤回/多开补丁工具

支持平台：Windows x64<br>
验证版本：WeChat Beta 4.0.1.20

## 使用方法
0. 首先你要有比较新的 Python，并且关掉了微信和烦人的安全管家。
1. 把仓库克隆下来。
2. 运行下列代码，然后输入对应的文件路径（或者把文件拖到终端窗口里）。<br>
   在修改之前，原文件会备份到 Weixin.dll.bak。
   
   `revoke.py`：防撤回无提示<br>【所有 revokemsg 消息变为未知消息，不响应撤回操作】

   `unlock.py`：多开<br>【移除 lock.ini 锁文件检测】

   `coexist.py`：共存版制作器<br>【选择数字 ζ=0~9，生成一个 Weixinζ.exe 和 Weixin.dlζ，其设置数据保存在 global_confζg、自动登录端口数据保存在 host-redirect.xmζ】<br>【共存版的所有消息记录和原版共用，随便登录哪个应该都不会丢消息】

## 问题解答

- 运行代码报错了？补丁失效了？<br>
  在 [**议题**](https://github.com/zetaloop/BetterWX/issues) 中反馈。

- 微信 3.9.x 能用吗？<br>
  猜你想找 [huiyadanli/RevokeMsgPatcher](https://github.com/huiyadanli/RevokeMsgPatcher)。

- Linux、macOS 能用吗？<br>
  不能。我猜应该相似吧，但我不会做。

- 共存、多开、防撤回这几个特性我可以挑选几个 or 全都要吗？<br>
  除了多开是作为共存的前置条件，别的可以自己选。

- 本项目的许可证？<br>
  Unlicense，完全放弃任何权利。包括那个图标。

- 特征怎么来的？<br>
  跟我没有关系，你信我噢 (ˉ▽ˉ；)...

- 作者可爱吗？<br>
  很可爱的 OwO，要不要[来看看我做的其他东西](https://github.com/zetaloop)？
