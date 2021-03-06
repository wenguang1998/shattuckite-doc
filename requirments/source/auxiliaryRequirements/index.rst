非功能需求
--------------

可测试性
#############

系统应在发布业务代码的同时发布测试程序。测试程序应该能够实现

1. 提供虚拟的测试环境，可以在不接入真实硬件的情况下测试系统功能的完整性
2. 能够自动化验证功能完整性, 例如确保 :ref:`用例` 中描述的业务流程可以正常进行

可扩展性
#############

在设计时应当考虑系统的可扩展性。可扩展性包括但不限于以下几点

数据可扩展性
***********************

当系统处理的数据量上升时，开发者应该能够在不改动，或少量改动代码的前提下，将数据流转逻辑与现有的分布式系统及负载均衡系统相结合，以实现流转及持久化容量的扩展。


健壮性
###############

系统各部分应当具有足够的健壮性。健壮性需求系统的特性包括但不限于

1. 在云端服务器出现故障时, 嵌入式终端应该能够保证系统不会崩溃，且能在下次服务可用时重连。
2. 在嵌入式终端出现故障时，服务器应当能正确处理来自用户的控制命令，提供合理的重询机制及异常反馈机制。
3. 在某个设备出现故障时，嵌入式终端应该能保证继续可用，且能够提供合理的异常反馈机制。

美观性
##############

系统提供的用户接口整体应当简单, 美观, 需要实现

1. 合理使用,布局交互控件
2. 合理选择配色方案
3. 在某些情景下添加合理的交互动画
