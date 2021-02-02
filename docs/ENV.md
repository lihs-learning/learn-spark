# 大数据与算法环境搭建

centOS7

## system

``` bash
groupadd bigdata
useradd -g bigdata --no-user-group --create-home hadoop
passwd hadoop
```

`vim /etc/hosts`

<!-- 如果将安装过程脚本自动化，需要考虑怎么将 hadoop000 作为变量 -->

```
127.0.0.1 hadoop000
```

``` bash
su - hadoop
mkdir ~/downloads
mkdir ~/app
ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
chmod 0600 ~/.ssh/authorized_keys
```

## java

``` bash
cd downloads
wget --no-cookies --no-check-certificate --header "Cookie: oraclelicense=accept-securebackup-cookie" https://javadl.oracle.com/webapps/download/GetFile/1.8.0_271-b09/61ae65e088624f5aaa0b1d2d801acb16/linux-i586/jdk-8u271-linux-x64.tar.gz
tar -zxvf jdk-8u271-linux-x64.tar.gz -C ~/app
echo 'export JAVA_HOME=/home/hadoop/app/jdk1.8.0_271' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
```

## hdfs

``` bash
cd ~/downloads
wget https://mirrors.tuna.tsinghua.edu.cn/apache/hadoop/common/hadoop-3.2.1/hadoop-3.2.1.tar.gz
tar -zxvf hadoop-3.2.1.tar.gz -C ~/app
echo 'export HADOOP_HOME=/home/hadoop/app/hadoop-3.2.1' >> ~/.bashrc
echo 'export PATH=$HADOOP_HOME/bin:$PATH' >> ~/.bashrc
sed -i "s/# export JAVA_HOME=/export JAVA_HOME=\/home\/hadoop\/app\/jdk1.8.0_271/g" $HADOOP_HOME/etc/hadoop/hadoop-env.sh
```

`vim $HADOOP_HOME/etc/hadoop/core-site.xml`

<!-- 如果将安装过程脚本自动化，需要考虑怎么将 hadoop000 作为变量 -->

```
<configuration>
    <property>
        <name>fs.defaultFS</name>
        <value>hdfs://hadoop000:8082</value>
    </property>
</configuration>
```

`vim $HADOOP_HOME/etc/hadoop/hdfs-site.xml`

<!-- 如果将安装过程脚本自动化，需要考虑怎么将 hadoop000 作为变量 -->

```
<configuration>
    <property>
        <name>dfs.replication</name>
        <value>1</value>
    </property>
    <property>
        <name>dfs.namenode.name.dir</name>
        <value>/home/hadoop/app/tmp/dfs/name</value>
    </property>
    <property>
        <name>dfs.datanode.name.dir</name>
        <value>/home/hadoop/app/tmp/dfs/data</value>
    </property>
</configuration>
```

`vim $HADOOP_HOME/etc/hadoop/workers`

<!-- 如果将安装过程脚本自动化，需要考虑怎么将 hadoop000 作为变量 -->

```
hadoop000
```

### ~~单独启动~~

``` bash
$HADOOP_HOME/bin/hdfs namenode -format
```

正常的话会有输出：  
Storage directory /home/hadoop/app/tmp/dfs/name has been successfully formatted.

``` bash
$HADOOP_HOME/sbin/hadoop-daemons.sh start namenode
$HADOOP_HOME/sbin/hadoop-daemons.sh start datanode
```

如果正常启动可以使用 `jps` 命令看到 `NameNode` 和 `DataNode`

如果有权限问题，检查是否漏掉了 [系统配置](#system) 最后为 hadoop 用户生成 ssh 公私钥的步骤

### 启动

``` bash
$HADOOP_HOME/sbin/start-dfs.sh
```

## yarn

`vim $HADOOP_HOME/etc/hadoop/mapred-site.xml`

``` xml
<configuration>
    <property>
        <name>mapreduce.framework.name</name>
        <value>yarn</value>
    </property>
</configuration>
```

`vim $HADOOP_HOME/etc/hadoop/yarn-site.xml`

``` xml
<configuration>
    <property>
        <name>yarn.nodemanager.aux-services</name>
        <value>mapreduce_shuffle</value>
    </property>
    <property>
        <name>yarn.nodemanager.env-whitelist</name>
        <value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_MAPRED_HOME</value>
    </property>
</configuration>
```

```
# 3.x required
sudo ln -s $JAVA_HOME/bin/java /bin/java
```

```
$HADOOP_HOME/sbin/start-yarn.sh
```

### 测试

test-1

```
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapredce-examples-3.2.1.jar pi 2 3
```

test-2

`vim wc.data`

```
hello   hello   hello
world   world
welcome
```

```
hadoop jar $HADOOP_HOME/share/hadoop/mapreduce/hadoop-mapredce-examples-3.2.1.jar wc
```

## python

```
sudo yum -y install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
cd downloads
wget https://www.python.org/ftp/python/3.8.7/Python-3.8.7.tgz
tar -zvxf Python-3.8.7.tgz
cd Python-3.8.7
./configure --prefix=/home/hadoop/app/python3.8.7
make && make install
echo 'export PYTHON3_HOME=/home/hadoop/app/python3.8.7' >> ~/.bashrc
echo 'export PATH=$JAVA_HOME/bin:$PATH' >> ~/.bashrc
```

## spark

注意：下述为非源码编译安装，源码编译安装参考 [Building Spark](https://spark.apache.org/docs/latest/building-spark.html) 一文

```
# URL 可能因版本升级失效
wget https://mirrors.tuna.tsinghua.edu.cn/apache/spark/spark-3.0.1/spark-3.0.1-bin-hadoop3.2.tgz
mkdir -r ~/app/spark-3.0.1
tar -zvxf spark-3.0.1-bin-hadoop3.2.tgz -C ~/app
echo 'export SPARK_HOME=/home/hadoop/app/spark-3.0.1-bin-hadoop3.2' >> ~/.bashrc
echo 'export PATH=$SPARK_HOME/bin:$PATH' >> ~/.bashrc
echo 'export PYSPARK_PYTHON=python3' >> ~/.bashrc
pip3 install pyspark
# 如果出错找不到 _ctype，那么在安装 python 时漏掉了 libffi-devel
# 安装这个包后重新编译安装 python
```

### submit

[Submitting Applications](https://spark.apache.org/docs/latest/submitting-applications.html)


