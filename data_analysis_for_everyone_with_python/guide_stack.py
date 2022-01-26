from typing import TypeVar, Generic, Union
import logging

T = TypeVar("T")
myLog = logging.getLogger("my")
myLog.setLevel(logging.INFO)

# https://stackoverflow.com/questions/57706180/generict-base-class-how-to-get-type-of-t-from-within-instance/60984681#60984681
# 임시 클래스 Stack
class Stack(Generic[T]):
    def __init__(self):
        ## 데이터를 담는 class 멤버 변수 1개를 선언한다.
        self.stack: list[T] = []

    def push(self, item: T) -> None:
        # stack의 맨 위에 데이터 하나를 집어넣는다.
        if not isinstance(item, self.__orig_class__.__args__[0]):
            myLog.error("Wrong Data Type or Data")
            myLog.info(self.__orig_class__.__args__[0])  # 이거 왜 출력 안돼냐
            return None

        self.stack.append(item)

    def pop(self) -> Union[T, bool]:
        # stack이 비어있지 않다면, stack의 맨 위 원소 하나를 꺼내어 반환한다.
        # 기존의 stack은 비어있는 상태에서 pop을 하면 런타임 에러를 일으키기도 합니다.
        if self.is_empty():
            return False
        else:
            return self.stack.pop()

    def is_empty(self) -> bool:
        # stack이 비어있는지 확인하고 비어있으면 True를, 비어있지 않다면 False를 반환한다.
        if self.stack.__len__() == 0:
            return True
        else:
            return False

    def top(self) -> Union[T, bool]:
        # stack이 비어있지 않다면 stack의 가장 위 원소를 반환한다. 단, pop을 사용하지는 않는다.
        # 기존의 stack은 비어있는 상태에서 top을 하면 런타임 에러를 일으키기도 합니다.
        if self.is_empty():
            return False
        else:
            return self.stack[-1]


### TEST ###

myClass: Stack[int] = Stack[int]()

myClass.push("1")
myClass.push(1)
myClass.push(2)
myClass.push(3)
myClass.push(4)

while not myClass.is_empty():
    print(myClass.stack.pop())
