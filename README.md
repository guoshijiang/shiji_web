### 1.项目概述

市集商城这个项目，一共有三个工程代码，一个是 web 网站，也就是本仓库的代码，有一个是 go 语言写的后端服务，，还有一个是 uniapp 写的移动端的应用，请查看关联项目。


### 2.项目部署

在部署代码前，你需要安装 python 3.8 以上版本，Mysql 数据库和 Redis

第一步，克隆代码：
```buildoutcfg
git clone git@github.com:guoshijiang/shiji_web.git
```

第二步，搭建一个 virtualenv：
```buildoutcfg
cd chaineye
virtualenv .env
source .env/bin/activate
```

第三步，安装依赖：
```buildoutcfg
pip3 install -r requirements.txt -i https://mirrors.aliyun.com/pypi/simple/
```

第四步，数据库migrate：
```buildoutcfg
 python3 manage.py migrate
```
如果你改变数据库结构，请先运行 `python3 manage.py makemigrations`, 然后再运行 `python3 manage.py migrate`

第五步，运行服务：
```buildoutcfg
 python3 manage.py runserver
```

如果你在线上部署，建议使用，supervisor 管理进程，Ng 转发，把静态文件使用 `python3 manage.py collectstatic` 收集到相应的目录。


### 3.关联项目

后端代码： https://github.com/guoshijiang/ganji




