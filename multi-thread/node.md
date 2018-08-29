# 多线程 vs 多进程
- 程序：一堆代码以文本形式存入一个文档
- 进程： 程序运行的一个状态
    - 包括地址空间、内存、数据栈等
    - 每个进程有自己完全独立的运行环境，多进程共享数据是一个问题
    
- 线程
    - 一个进程的独立运行片段，一个进程可能有多个线程
    - 轻量化的进程
    - 一个进程的多个线程间共享数据和上下文运行环境
    - 共享互斥问题
    
- 全局解释器锁（GIL）
    - python代码的执行由python的虚拟机控制
    - 在主循环中只能有一个控制线程在执行
   
- python包
    - thread：有问题，不好用
    - threading： 通用的包
    
- 案例01 （t01）
- 案例02：使用多线程完成t01（t02）
- 案例03：多线程传参

- threading使用(t04)
    - 直接使用threading.Thread生成Thread实例
        1. t = threading.Thread(target=xx, args=(xxx,))
        2. t.start()
        3. t.join() 等待多线程执行完成
        - 守护线程daemon （t05非守护 t06守护）
            - 如果在程序中将子线程设置成守护线程，则子线程在主线程结束后自动退出
            - 一般认为，子线程不重要或者不允许离开主线程独立运行
            - 守护线程是否有效果跟环境相关
    
    - 直接继承threading.Thread （t08）
        - 直接继承Thread
        - 重写run函数
        - 类实例可以直接运行
        - t09工业风
        
- 共享变量
    - 案例t10
    - 解决方案
        - 锁（Lock）t11
            - 是一个标准，表示一个线程在占用一些资源
            - 使用方法
                - 上锁
                - 使用共享资源
                - 取消锁
                
        - 线程安全问题
            - 如果一个资源|变量，对于多线程来讲，如果不加锁也不会有任何问题，称为线程安全
            - 线程不安全变量： list、set、dict
            - 线程安全： queue
         
    - 消费者与生产者 t12
    
    - 车站售票 t13
                
    - 死锁问题 lock.acquire(timeout = 3)//最多等待3秒
    
    - semaphore t14
        - 允许一个资源最多被多少个线程使用
        
    - threading.Timer
        - Timer是利用多线程，在指定时间后启动一个功能
        
    - 可重入锁 t15
        - 一个锁，可以被一个线程多次申请
        - 主要解决递归调用的时候，需要申请锁的状况
    
    
     