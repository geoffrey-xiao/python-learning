class Person():
    # 要想实例化类 必须返回object.__new__(cls)
    # 如果不return 则默认返回None,实例化失败
    def __new__(cls, *args, **kwargs):
        print('触发了构造方法')
        print(*args)
        return object.__new__(cls)

    def __call__(self, *args, **kwargs):
        print('对象被当成方法调用了')

    def __init__(self, name, age, sex):
        print('触发了初始化方法')
        self.name = name
        self.age = age
        self.sex = sex

    def __del__(self):
        print('触发了析构方法')


summer = Person('SUMMER', 2, 'female')
summer()
