
设计文档自动部署配置
^^^^^^^^^^^^^^^^^^^^

成员:baixusata

----

KPI: 200

DDL: 2019/4/19 24:00
--------------------

编写\ ``Jenkinsfile`` 实现\ `shattickite-doc <https://github.com/buaaembeddedse/shattuckite-doc>`_\ 仓库\ ``SDD`` 分支中设计文档的自动编译与部署。

注意请尽快将编写完成的\ ``Jenkinsfile``\ 通过PR提交到\ ``SDD-dev``\ 分支。在文件首次PR前，由于不会执行\ ``SDD-dev``\ 向\ ``SDD``\ 分支的合并，所以配置文件可能无法测试。

设计文档构建脚本编写
^^^^^^^^^^^^^^^^^^^^

成员:wenguang1998

----

KPI: 200

DDL: 2019/4/19 24:00
--------------------

修改\ `shattickite-doc <https://github.com/buaaembeddedse/shattuckite-doc>`_\ 仓库\ ``SDD-dev`` 分支下的 ``conf.py``\ 文件，实现


* 生成符合要求的文档封面
* 从git tags 读取版本信息，并在编译期将版本号插入文档
* 从\ ``Commit`` 历史内读取修订记录，并在编译期将记录插入文档

注意，以上功能均在之前的分支中实现，只需要移植即可。完成移植工作后，请向\ ``SDD-dev``\ 分支提交PR。

前端开发-移动端UI设计-第二期
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

成员:mqlKKK

继续使用 ``Axure`` 进行移动端原型设计

与用例分析联动
~~~~~~~~~~~~~~

修改 `shattuckite-doc <https://github.com/buaaembeddedse/shattuckite-doc>`_ 仓库 ``PRD-dev``\ 分支下记载用例的\ ``case.json``\ 文件，对于每一个用例，添加一个新的字段\ ``mobileGUI``\ ，用于记录与该用例相关的原型界面设计文件。\ ``mobileGUI``\ 字段存储一个\ ``原型页面对象(PageObj)``\ 列表。一个\ ``PageObj``\ 包括以下字段


#. pageName(String): 字符串，表示\ ``Axure``\ 中该页面名称
#. subPage(Union[PageObj[],String]): 原型页面对象列表，存储 **与本用例有关的** ，且为该页面子页面的页面。当子页面不再嵌套其它子页面时，可仅用PageName表述一个子页面。

此外请注意,为了保证最大的兼容性,请将\ ``Axure``\ 页面名称全部改为英文.

一个简单的示例

.. code-block::

   "mobileGUI":[
       { 
           "pageName":"login",
           "subPage":["login_wrongInfo"]
       },
       {
           "pageName":"index",
           "subPage":[
               {
                   pageName:"data",
                   subPage:["historyData","realtimeData"]
               }
           ]
       }
   ]

添加简单的交互功能
~~~~~~~~~~~~~~~~~~

请为原型页面添加易于实现的交互逻辑。

页面间的跳转是一个典型的交互逻辑。例如\ ``主界面``\ 中的\ ``监控数据按钮``\ ，可以添加\ ``onClick``\ 回调，实现在原型输出文件中点击该按钮可以跳转到\ ``监控数据``\ 页面中。

本次任务中请至少为所有的跳转按钮添加页面跳转交互逻辑。其他的交互逻辑请视情况添加。

提升美观性
~~~~~~~~~~

请参考 


#. `Martial Design <https://material.io/design/>`_
#. `Ant Design Guidelines <https://ant.design/docs/spec/introduce>`_ 

等成文的设计规范，\ **尽量** 改善UI的表现力，提高界面美观程度。

《测试文档》编写计划
^^^^^^^^^^^^^^^^^^^^

成员:Dicky35,baixusata

----

KPI: 200

DDL: 2019/3/30 24:00
--------------------

设计测试方案并考虑《测试文档》的编写。在本次任务结束前，请提交《测试文档》的编写大纲。

请 @Dicky35  与 @baixusata 共同完成本任务。请二位自行商议各自负责的部分。

注: 截止2019/03/22本项目后端可能使用的技术栈包括


#. Scala     (\ ``Akka`` + ``Kafka``\ + ``gRPC`` ) : 嵌入式终端与服务器数据交互
#. C/C++  (Linux system call) : 嵌入式终端设备驱动
#. Python  (\ ``Django``\ +\ ``gRPC``\ ) :  数据库管理与提供Web接口

前端使用的主要技术是 ``React.js``

其中\ ``Scala``\ 和\ ``Python``\ 自带单元测试框架，\ ``React.js``\ 可以使用\ ``jest``\ 测试框架，\ ``C/C++``\ 可以使用\ ``gTest``\ 测试框架。

此外，移动端可以使用\ ``ADB``\ 进行自动化测试，Web端可以使用\ ``Selenium``\ 进行自动化测试。

前端开发-移动端UI原型设计
^^^^^^^^^^^^^^^^^^^^^^^^^

成员:mqlKKK

----

KPI: 200

DDL: 2019/3/30 24:00
--------------------

根据需求文档的描述，进行移动端用户界面的原型。设计UI时请注意:


#. 使用 ``Axure`` 原型工具进行绘制
#. 最终产品需要严格按照本版原型进行开发，在设计时请考虑可实现性。
#. 尽可能cover用户可见的每一个页面
#. 尽量保证设计的美观
#. 在buaase下新建仓库\ ``shattuckite-gui-mobile``\ ,并将设计稿提交到该仓库。

此外，如果时间允许的话，请为UI原型添加简单的交互逻辑。

注: `Antd library <https://library.ant.design/>`_ 提供\ ``ant-design``\ 及\ ``ant-design-mobile``\ 组件的Axure模型。

非x86 平台测试环境搭建
^^^^^^^^^^^^^^^^^^^^^^

成员:Dicky35

请使用 ``qemu`` 仿真非x86 体系结构的cpu，搭建测试环境。

具体要求

``50KPI`` qemu-docker 环境的搭建
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

继续修改 #7 中的\ ``Dockerfile``\ ，在其内部配置\ ``qemu``\ 环境

``150KPI`` 建立\ ``qemu``\ 虚拟机
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

建立首个 ``qemu``\ 虚拟机，需要满足以下几点要求


#. 基于\ ``Cortex-A9``\ 架构 
#. 指令长度为64位
#. 安装\ ``Debian``\ 系统

注意建立\ ``Qemu``\ 过程中的一切静态文件(包括系统配置文件及虚拟磁盘文件)应当保存在宿主机而非Docker中，Docker容器应该通过VOLUME挂载的方式访问这些静态文件。

该任务计200KPI

该任务应当在 ``2019年3月22日24:00``\ 前完成

《需求文档》绘制用户用例活动图
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

成员:wenguang1998

请为 `shattuckite-doc <https://github.com/buaaembeddedse/shattuckite-doc/>`_ `/requirements/source/userOriented/cont.json <https://github.com/buaaembeddedse/shattuckite-doc/blob/PRD-dev/requirments/source/userOriented/case.json>`_\ 目录下 的每个case绘制 ``UML 活动图``

基本要求


#. 使用\ ``plantuml``\ 进行绘制
#. 在\ ``/source/userOriented``\ 目录下新建一个\ ``uml``\ 文件夹，并将绘制(编写)的UML图置于此处
#. 每一个\ ``case``\ 对应一个\ ``uml``\ 文件，文件名应该是\ ``case``\ 的\ ``name``\ 字段, 文件扩展名是\ ``plantuml``\ 。该文件应当置于\ ``uml``\ 文件夹内。
#. 请注意\ ``uml活动图``\ 的规范, 建议阅读\ `Activity Diagram <https://en.wikipedia.org/wiki/Activity_diagram>`_

该任务计200KPI

该任务应当在\ ``2019年3月22日24:00``\ 前完成

注: 至少完成 #9 提交的 ``case.json`` 版本中用例的建模。

《需求文档》继续细化面向用户的需求建模
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

成员:mqlKKK

文档仓库\ `shattuckite-doc <https://github.com/buaaembeddedse/shattuckite-doc/tree/PRD-dev>`_\ 的\ ``PRD-dev``\ 分支内正在进行需求文档的编写。

请参考\ ``/requirements/source/userOriented/intro.rst``\ 文件内的概述信息，并自行扮演用户的角色，完成面向用户的需求建模。

修改建议
~~~~~~~~


#. ``查看监控数据`` 用例拆分

该用例至少可进一步拆分为 ``查看实时监控数据`` 及 ``查看历史数据``\ 。


#. ``管理传感器`` 用例重新设计

管理传感器实际应为管理 ``设备`` 。 ``设备`` 包括\ ``传感器`` ,\ ``执行器`` , ``摄像头`` 等本系统可能会用到的物理设备。

管理设备请细分为\ ``批量设备管理`` ，\ ``传感器管理``  ``执行器管理``\ 等


#. 添加\ ``操作执行器``\ 的用例

用户可能会直接操作隶属于\ ``执行器``\ 类的设备。\ **操作** 与 **管理** 属于不同的逻辑，应当为操作执行器单独设计用例。


#. 关于\ ``prerequisites``\ 字段

该字段主要体现用例的相互依赖关系。例如在\ ``A``\ 用例的\ ``prerequisites``\ 字段中列出\ ``B``\ 用例，则说明\ ``A``\ 用例一定要在用户执行了\ ``B``\ 用例后才会执行。 目前部分用例该字段有些许不妥，请修改。


#. 关于\ ``case.json`` 文件编辑

`9 <https://github.com/buaaembeddedse/shattuckite-META/issues/9>`_  中提交的\ ``case.json``\ 版本存在些许语法错误。建议使用带有\ ``json lint``\ 功能的编辑器对本文件进行编辑。

该任务计\ ``100KPI``

该任务应当在\ ``2019年3月20日24:00``\ 前完成。

《需求文档》面向用户的需求建模编写
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

成员:mqlKKK

文档仓库\ `shattuckite-doc <https://github.com/buaaembeddedse/shattuckite-doc/tree/PRD-dev>`_\ 的\ ``PRD-dev``\ 分支内正在进行需求文档的编写。

请参考\ ``/requirements/source/userOriented/intro.rst``\ 文件内的概述信息，并自行扮演用户的角色，完成面向用户的需求建模。

在编写用例时，应当编辑\ ``/requirements/source/userOriented/case.json``\ 文件。该文件内已经设计了两个用例供参考。

请尽可能多的提出需求并以标准化用例的形式记录。

该任务计\ ``100KPI``

该任务应当在\ ``2019年3月17日24:00``\ 前完成。

《需求文档》编译配置
^^^^^^^^^^^^^^^^^^^^

成员:wenguang1998

修改\ `shattuckite-doc <https://github.com/buaaembeddedse/shattuckite-doc>`_\ 仓库\ ``requirements``\ 分支,\ ``requirements/source``\ 目录下的\ ``conf.py``\ 文件, 实现


#. ``(100kpi)``\ 输出\ ``pdf``\ 的\ ``title page``\ 和项目计划书的相同。
#. ``(100kpi)``\ 自动根据符合特定格式的commit信息修改文档内的修订历史记录

注: 上述\ ``符合格式的commit信息``\ ，格式定义为:  使用\ ``git log``\ 输出提交历史记录后，可被正则表达式

.. code-block::

   ^commit(.*?)$\nAuthor:(.*?)$\nDate:(.*?)$\s+SHADOC-002\sDOC\sUPDATE\s+AUTHOR:(.*?)\s+CENSOR:(.*?)\s+NOTE:(.*?)$

匹配并提取分组的格式。

该任务应当在\ ``2019年3月15日24:00``\ 前完成。

arm交叉编译环境搭建
^^^^^^^^^^^^^^^^^^^

成员:Dicky35

``100kpi``\ 编译环境搭建
~~~~~~~~~~~~~~~~~~~~~~~~~~

编写 ``Dockerfile``\ , 新建一个\ ``docker img``\ 。 在使用该\ ``img``\ 实例化\ ``container``\ 后, 应当实现


#. 内部含有交叉编译各种\ ``arm``\ 架构二进制程序的编译环境
#. ``/root``\ 目录下提供一个shell脚本\ ``armenv.sh``\ , ``source``\ 该脚本后, 系统内和编译有关的环境变量会被自动替换为\ ``arm``\ 交叉编译器版本。

``100kpi`` 测试与提交
~~~~~~~~~~~~~~~~~~~~~~~~~

在完成\ ``Dockerfile`` 的编写后, 使用该环境交叉编译 `grpc <https://github.com/grpc/grpc>`_\ 到\ ``Cortex-A9``\ 架构。

该任务应当在\ ``2019年3月15日24:00``\ 前完成。

《需求文档》自动化发布
^^^^^^^^^^^^^^^^^^^^^^

成员:baixusata

----

KPI: 200

DDL: 2019/03/15 24:00:00
------------------------

``150kpi`` 自动发布逻辑编写
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

修改文档仓库\ `(shattuckite-doc) <https://github.com/buaaembeddedse/shattuckite-doc>`_\ 项目文件夹内的\ ``Jenkinsfile``\ , 在Jenkins流程被触发后


#. 自动编译更新后的《需求文档》，生成\ ``pdf``\ 文件。
#. 将生成的\ ``pdf``\ 重新命名为 ``需求文档-$version`` 的格式。\ ``$version``\ 为使用\ ``git describe``\ 生成的版本号。
#. 将生成的文档自动push到\ `Team105 <https://github.com/sebuaa2019/Team105>`_\ 仓库

注意


#. 文档仓库内可能同时存在多个分支。在编译及重命名文档时，可能需要通过检查当前分支的名称，来选择不同的编译/发布逻辑。
#. 没有开放文档仓库的写权限，请自行fork一个仓库进行调试。

``50kpi`` Jenkins项目配置
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

请配置\ ``Jenkins``\ 项目，使其响应除\ ``master分支``\ 和\ ``*-dev``\ 分支外的所有分支的更新。(可以通过项目配置页面里的正则表达式过滤器实现)

该任务应当在\ ``2019年3月15日24:00``\ 前完成。

React+Redux 前端: UI框架 前端路由与scss样式
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

成员:mqlKKK

1. 使用 ``antd`` 提供的组件 对 #4  与 #1  中的用户交互组件进行美化。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

(主要是替换按钮/输入框/列表等组件)

2. 使用 ``scss`` 为组件提供简单的样式。
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

注意，可能需要改变Webpack配置文件。如果是用\ ``create-react-app``\ 生成的项目需要\ ``eject``\ 操作。

3. 使用 ``React-Router``\ 编写前端路由，实现
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

a. 设计一个主界面，主界面上有连接到TickTocToe 和 TodoList的按钮
b. 在\ ``TickTocToe``\ 和\ ``TodoList``\ 的页面上分别加上返回主界面的按钮
c. 请使用\ ``Hash-Router``

此外，关于一些代码组织上的建议


#. 组件源代码主要存储在\ ``src/container`` 和\ ``src/presentation``\ 下; ``Reducer.ts(Root)``\ , ``index.tsx``\ 等存放在\ ``src/`` 下
#. 每个组件拥有自己的独立文件夹
#. 所有组件的主类均在文件夹内的\ ``index.tsx``\ 文件实现与导出
#. 对于容器组件，文件夹内，除了\ ``index.tsx``\ 外，通常情况下还会拥有\ ``action.ts``\ 和\ ``reducers.ts``
#. 如果需要添加样式的话，可以在组件所属的文件夹内添加\ ``index.scss``

React+Redux前端 - TikTacToe 编写
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

成员:mqlKKK

``TikTakToe`` 是 ``React``\ 官方文档中的例子 请参照官方文档中的实现，使用\ ``Typescript`` 和 ``Webpack`` 完成该示例程序。

测试与持续集成-基础
^^^^^^^^^^^^^^^^^^^

成员:Dicky35,baixusata

https://github.com/buaaembeddedse/group-training/commit/2a72c991a8e5f940e23a6acd8766e87bb6f99368 上传了两个文件，分别用c++和python实现了最简单的a+b功能，需要分别使用 ``gTest`` 和 ``unittest`` 为这两个函数添加单元测试。

该任务计100KPI

应当在 ``2019年3月8日24:00`` 前完成本任务

文档撰写和UML建模 -PlantUML的使用
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

成员:wenguang1998

https://github.com/buaaembeddedse/group-training/commit/6783b777dfd1fcc55897a52e3b3fcf21065b8d9c 上传了一个简单的基于场景的需求用例。


#. 请使用UML活动图对该用例进行建模
#. 使用reStructuredText语法将上述活动图添加到文档中

请注意


#. 不要使用GUI工具进行UML图绘制，理由是GUI工具绘制的UML图一致性差且难于维护。推荐使用\ ``plantUML``\ 或\ ``GraphViz``\ 进行绘制。
#. rst文档中图片的引用文法，请确保github能够识别并且能在网页预览页面上渲染图片。
   ### React+Redux前端 - TodoList编写

成员:mqlKKK

``TodoList`` 是\ ``Redux``\ 官方教程中的例子。


#. 使用\ ``create-react-app``\ 脚手架创建项目
#. 使用\ ``redux``\ 进行状态管理
#. 编码时将\ ``Container  Component``\ , ``Presentation Component``\ 分开处理, 并在注释中标明。
#. 使用\ ``Redux``\ 时，注意结合\ ``TS``\ 的模板编程技术进行\ ``Type Hint``\ 。\ ``Action``\ ，\ ``Root Reducers`` 都应该是强类型的，而不是\ ``any``

开发的基本模式是\ ``Container Component``\ 使用\ ``connect``\ 作为一个高阶组件的输入，并作为其他若干\ ``Presentation Component``\ 的父组件。仅有\ ``Container Component``\ 会与\ ``Redux``\ 维护的状态树产生交互。

该任务计100KPI

该任务应当在 ``2019年3月8日24:00`` 前完成
