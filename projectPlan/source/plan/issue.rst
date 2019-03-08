
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
