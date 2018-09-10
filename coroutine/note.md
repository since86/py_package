# 生成器 generator
- 一边循环一边计算下一个元素的机制/算法
- 需要满足三个条件：
    - 每次调用都生产出for循环需要的下一个元素
    - 如果到达最后一个元素，抛出StopIteration异常
    - 可以被next函数调用
    
- 如何生成一个生成器
    - 直接使用 g = (i for i in range(5))
    - 如果函数中包含yield，那么这个函数就是生成器
    - next调用函数，遇到yield返回

# 协程
- 包：ayncnio
- 协程的实现：c02
    - yield返回
    - send调用
    
- 协程的状态 c03
    协程可以身处四个状态中的一个。当前状态可以使用inspect.getgeneratorstate(...) 函数确定，该函数会返回下述字符串中的一个。
    GEN_CREATED：等待开始执行；    
    GEN_RUNNING：解释器正在执行（只有在多线程应用中才能看到这个状态）；    
    GEN_SUSPENDED：在 yield 表达式处暂停；
    GEN_CLOSED：执行结束；

- 协程终止
    - 协程中未处理的异常会向上冒泡，传给next函数或者send方法的调用方（即触发协程的对象）
    - 终止协程的一个方式：发送某个哨符值，让协程退出，内置的None和Ellipsis等常量经常用作哨兵值
    
- yield from
    - 调用协程为了得到返回值，协程须正常终止
    - 生成器正常终止会发出StopIteration异常，异常对象的value属性保持返回值
    - yield from从内部捕获StopIteration异常 c04
    - 委派生成器 c05
        - 包含yield from的生成器函数
        - 委派生成器在yield from处暂停，调用方可以把数据发给子生成器
        - 子生成器把产生的值发给调用方
        - 子生成器在最后，解释器会抛出StopIteration异常，并将返回值附加到异常对象上
        
#asyncio
- python3.4引入，内置对异步io的支持    
- asyncio本身是个消息循环
- 步骤
    - 创建消息循环
    - 把协程导入
    - 关闭