
# 目录结构初始化

#### 新建python项目 *python-mall*
在pytho-mall下新建python 文件 *set_up.py*
    
    import setuptools
    
    setuptools.setup(setup_requires=['pbr'], pbr=True)

最后的目录结构如图所示

![项目最终目录结构图](/etc/mall/category.PNG "目录结构")

*cmd*目录用于管理整个项目的启动，开启api服务或者运行更新数据库脚本文件  
*common*包下用于存放辅助功能文件  
*db*包下存放整个项目与数据库的访问文件，包括各个数据库的连接引擎，models，数据库更新脚本文件
，访问数据库的dao层  
> *engines* 包下存放各个数据库的连接  
> *migrate* 包下存放数据库更新脚本  
> *models* 包下存放对数据库的crud操作

*router*包下存放前端发送后端的接口处理
