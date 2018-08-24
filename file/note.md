# 文件
- 长久保存信息的一种数据信息集合
- 常用操作：
    - 打开关闭
    - 读写
    - 查找
    
#   open函数（f01）
- open函数负责打开文件，带有很多参数
- 第一个参数：必须有，文件的路径和名称
- mod： 表示文件以什么方式打开
    - r： 以只读方式
    - w： 写方式打开，会覆盖以前的内容
    - x： 创建方式打开，如文件已存在，则报错
    - a： append方式，追加的方式对文件内容进行写入
    - b： binary方式，二进制方式打开
    - t： 文本方式打开
    - +： 可读写
    
# with语句
- 使用上下文管理协议的技术（ContextManagementProtocal)
- 自动判断文件的作用域

# read函数（f01)
- read是按照字符读取文件内容

# seek(offset,from)
- 移动文件的读取位置（读取指针）
- from的位置
    - 0：从文件头开始偏移
    - 1：从文件当前位置开始偏移
    - 2：从文件末尾开始偏移
- offset单位是字节（byte）

# tell函数 用来显示读写指针的当前位置
- tell返回的单位是字节（byte）

# 文件的写操作（write）f03
- write(str) str只能是字符串
- writeline(str) str可以是字符串，也可以是字符串序列

# 序列化与反序列化 f04
- 序列化：把程序运行中的信息保存在磁盘上
- 反序列化

- pickle:python提供的序列化模块
- pickle.dump: 序列化
- pickle.load: 反序列化

# shelve-持久化 f05
- 持久化工具
- 类似字典，用kv保存数据，存储方式也相似
- open close
- 不支持并行写入
    - 为了解决这个问题，open的时候可以使用flag=r
- 写回问题

# logging模块的处理流程
- 四大组件
    - 日志器（Logger）：产生日志的一个接口
    - 处理器（Handler）： 把产生的日志发送到相应的目的地
    - 过滤器（Filter）： 更精细的控制日志输出
    - 格式器（Formatter）： 对输出信息进行格式化

-Logger
    
    - 操作
        Logger.setLevel()
        Logger.addHandler()与Logger.removerHandler()
        Logger.addFilter()与Logger.removerFilter()
        Logger.debug:产生一条debug级别的日志
        Logger.exception(): 创建类似于Logger.error的日志消息
        Logger.log(): 获取一个明确的日志level参数创建一个日志记录
        
    - 如何得到一个logger对象
        - 实例化
        - logging.getLogger()
        
- Handler
    - 把log发送到特定位置
    - 方法
        - setLevel
        - setFormat
        - addFilter, removeFilter
        
    - 不需要直接使用，Handler是基类
    
- Format类
    - 直接实例化
    - 可以继承Format类添加特殊内容
    - 三个参数
        - fmt 指定消息格式化字符串，如果不指定该参数则默认使用message的原始值
        - datefmt 指定日期格式字符串，如果不指定该参数则默认使用'%Y-%m-%d %H-%M-%S'
        - style: 可取值为'%','{'和'$',如果不指定该参数则默认使用'%'
    
- Filter类
    - 可以被Handler和Logger使用
    - 控制传递过来的信息的具体内容
    