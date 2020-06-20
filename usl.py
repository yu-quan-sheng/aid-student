"""
    用户user 显示show 层layer
"""
from bll import StudentController
from model import StudentModel


class StudentView:
    """
        # 学生视图:负责处理界面逻辑(输入/输出/界面跳转)
    """

    def __init__(self):
        self.__controller = StudentController()

    def __display_menu(self):
        print("1) 添加学生信息")
        print("2) 显示所有学生信息")
        print("3) 删除学生信息")

    def __select_menu(self):
        item = input("请输入选项:")
        if item == "1":
            self.__input_student()
        elif item == "2":
            # 先写方法调用,通过快捷键生成方法.
            # alt + 回车 + 回车
            self.__display_students()
        elif item == "3":
            self.__delete_student()

    def __input_student(self):
        stu = StudentModel()
        stu.name = input("请输入姓名:")
        stu.age = self.get_int("请输入年龄:")
        stu.sex = input("请输入性别:")
        stu.score = self.get_int("请输入成绩:")
        self.__controller.add_student(stu)

    def get_int(self,message):
        while True:
            try:
                data = int(input(message))
                return data
            except:
                print("重新输入")

    def main(self):
        while True:
            self.__display_menu()
            self.__select_menu()

    def __display_students(self):
        # list_students
        for stu in self.__controller.list_students:
            # print("我是xx,今年xx,性别xx,成绩xx,学号xx.")
            print(f"我是{stu.name},今年{stu.age},性别{stu.sex},成绩{stu.score},学号{stu.sid}.")

    def __delete_student(self):
        # sid = int(input("请输入学生编号:"))
        sid = self.get_int("请输入学生编号:")
        if self.__controller.remove_student(sid):
            print("删除成功")
        else:
            print("删除失败")

