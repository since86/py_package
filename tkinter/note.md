# 消息队列
- 传递机制
    - 自动发出事件/消息
    - 消息由系统负责发送到队列
    - 由想过组件进行绑定、设置
    - 后端自动选择感兴趣的事件并进行相应反应
- 消息格式
    - <[modifier-]---type-[-detail]>
    - <Button-1>:Button表示按钮事件，1代表鼠标左键，2代表中键
    
# tkinter的绑定
- bind_all:全局绑定，默认的全局快捷键，比如F1帮助文档
- bind_class:接收3个参数，第一个类名，第二个事件，第三个函数：
    - w.bind_class('Entry','<Control-V>',my_paste)
- bind:对某个实例进行绑定
- unbind：解绑，参数：事件

# 菜单
### 普通菜单
- 第一个Menu类定义的是parent
- add_command添加菜单项，如果是顶层菜单，从左向右排列，如果不是，就是下拉菜单
    - label：菜单项名称
    - command：调用函数
    - acceletor： 快捷键
    - underline： 菜单项下面有横线
    - menu：指定使用哪个作为顶级菜单
    
### 级联菜单
- add_cascade: 级联菜单，目的是引出后面的菜单
- add_cascade的menu属性： 指明将菜单级联到哪个菜单上
- label： 名称

### 弹出式菜单
- 也叫上下文菜单
- 实现
    - 建立一个功能完备的菜单
    - 监听鼠标右键
    - 根据位置判断弹出
    - 根据menu的pop方法
- add_separator():分隔符

### canvas画布
- 在画布上绘制对象，通常使用create_xxx,xxx为对象类型
    