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
        
    - if __name__ == '__main__'
        - 建议作为所有模块导入的程序入口
        
# 2. 模块的搜索路径和存储
- 什么是模块的搜索路径
    - 加载模块的时候，系统会在何处搜索模块
    
- 系统默认的搜索路径
    - import sys
    - sys.path 属性可以获取路径列表 案例p06
    
- 添加搜索路径
    - sys.path.append(dir)
    
- 搜索路径顺序
    1. 上搜索内存加载好的模块
    2. python的内置模块
    3. 搜索sys.path路径
    
# 3. 包
- 包是一种管理组织代码的方式，包里面存储的就是模块
- 自定义包的格式

- 包的导入操作
    - import package_name
        - 直接导入包，可以使用__init__.py的内容
        - 使用方式：
            package_name.func_name
            package_name.class_name.func_name
            
        - 对__init__.py内容的导入，不包括包里面的内容
        
    - import package.module
        - 导入包里面其中一个模块
        
  
        
        
   - from package import module
        - 此方法不执行'__init__.py'里面的内容
        
   - from package import *
        - 导入当前包'__init__.py'里面包含的所有函数和类
        - 使用方法
            - func_name()
            - class_name_func_name()
            - class_name.var
        
   - from package.module import *
        - 导入包中指定模块的所有内容
        
            - func_name()
            - class_name.func_name()
            
   - '__all__'的用法
        - 使用 from package import * 时可以使用的内容
        - 如果'__init__.py'里面的内容为空，或者没有'__all__'，那么只可以吧'__init__.py'里面的内容导入