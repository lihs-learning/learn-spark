# 远程使用指南

要求：PyCharm 专业版

参考官方文档配置 [SSH 远程连接](https://www.jetbrains.com/help/pycharm/configuring-remote-interpreters-via-ssh.html)

注意在选择 python 解释器（interpreter）时，
不要使用 `/usr/bin/python`
而要使用 `/home/hadoop/app/python3.8.7/bin/python3`。

注意最好不要勾选使用 sudo 执行。（不确定影响）

注意在选择同步本地文件到服务器时，不要选在 `/tmp` 下面，容易丢失文件。

另外由于 pyspark 作为了一个单独的包，使用 pip3 安装了，使用的也是远程环境。
所以不必再配置环境变量（PYTHONPATH）。（瞎蒙的，反正不配置环境变量也可用）
