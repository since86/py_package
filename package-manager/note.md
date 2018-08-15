# 1.模块
- 一个模块就是一个包括python文件的代码，后缀名是.py就可以，模块就是个python文件
- 为什么用模块
    - 方便文件的维护
    - 增加代码重复利用的放松
    - 当做命名空间使用，避免命名冲突
 
 - 如何定义模块
    - 模块就是一个普通python文件
    - 根据模块的规范，最好在模块中编写如下内容
        - 函数（单一功能）
        - 类（相似功能的组合，或者类似业务模块）
        - 测试代码
        
 - 如何使用模块
    - 直接模块导入
        - 加入模块名称直接以数字开头，importlab.import
    
    - 语法
        import module_name
        module_name.function_name
        module_name.class_name
        
    - import module_name as 别名
        - 案例p03
        
    - from module_name import func_name, class_name
    
    - from module_name import *
        - 导入所有内容
        - 使用时不需要前缀
        - 容易造成命名污染