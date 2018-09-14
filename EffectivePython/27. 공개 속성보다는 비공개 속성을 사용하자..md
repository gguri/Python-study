# PEP 8 스타일 가이드 : 명명(naming)
- 보호(protected) 인스턴스 속성은 _leading_underscrore 형식을 따른다.
- 비공개(private) 인스턴스 속성은 __double_leading_underscroe 형식을 따른다.

<br/> 
 
### 보호(protected) / 비공개(private)

정보 은닉(Information Hiding)을 위한 **접근 제한자(Access Modifier)**  
객체지향 언어에서 클래스, 메소드, 변수에 대한 접근성을 지정하는 키워드
  1. public : 모든 접근을 허용
  2. protected : 같은 패키지(폴더)에 있는 객체와 상속관계의 객체들만 허용
  3. private : 현재 객체 내에서만 허용

<br/>

### BETTER WAY 27. 공개 속성보다는 비공개 속성을 사용하자
파이썬에는 클래스 속성의 가시성(visibility)이 공개(public)와 비공개(private) 두 유형 밖에 없다.  
즉, 다른 OOP와 다르게 **파이썬은 별도의 제한자** 를 지원하지 않으며 모든 속성, 메소드는 기본적으로 public


```python
class MyObject(object):
    def __init__(self):
        self.public_field = 5
        self.__private_field = 10

    def get_private_field(self):
        return self.__private_field
```

공개 속성은 어디서든 객체에 점 연산자(.)를 사용하여 접근이 가능


```python
foo = MyObject()
assert foo.public_field == 5
```

-추가-  
assert < condition >  
해당 조건이 True가 아닐 경우 Error를 발생시킴


```python
assert foo.__private_field == 10

>>> AttributeError: 'MyObject' object has no attribute '__private_field'
```

하지만 클래스 외부에서 비공개 필드에 접근하면 예외가 발생


```python
class MyOtherObject(object):
    def __init__(self):
        self.__private_field = 71

    @classmethod
    def get_private_field_of_instance(cls, instance):
        return instance.__private_field
```

-추가-
정적메소드 @classmethod 공부 필요  
첫번째 인자가 클래스지만 생략하고 접근


```python
bar = MyOtherObject()
assert MyOtherObject.get_private_field_of_instance(bar) == 71
```


```python
class MyParentObject(object):
    def __init__(self):
        self.__private_field = 71

class MyChildObject(MyParentObject):
    def get_private_field(self):
        return self.__private_field

baz = MyChildObject()
baz.get_private_field()


>>> AttributeError: 'MyChildObject' object has no attribute '_MyChildObject__private_field'
```

get_private_field 함수는 __private_field를 반환하지만 이는 부모 클래스의 비공개 필드이므로 접근할 수 없다.

비공개 속성의 동작은 속성 이름을 변환하는 방식으로 구현된다.  
파이썬 컴파일러는 서브클래스에서 비공개 속성에 접근하는 코드(MyChileObject.get_private_field)를 발견하면   
서브클래스의 __private_field를 _MyChildObject.get_private_field에 접근하는 코드로 변환한다.  


위 예제에서는 \__private_field가 MyParentObject.\__init__에만 정의되어 있으므로   
비공개 속성의 실제 이름은 **_MyParentObject__private_field**가 된다.  
즉, 자식 클래스에서 부모의 비공개 속성에 접근하는 동작은 단순히 변환된 속성 이름이 일치하지 않아서 실패한다.


```python
MyChildObject.__dict__

>>> mappingproxy({'__module__': '__main__',
                  'get_private_field': <function __main__.MyChildObject.get_private_field(self)>,
                  '__doc__': None})

assert baz._MyParentObject__private_field == 71
```

파이썬에서 문법적으로 엄격하게 강제하지 않는 이유는 '우리 모두 성인이라는 사실에 동의합니다' 라는 철학적 좌우명에 있다.   
파이썬 프로그래머들은 개방으로 얻는 장점이 폐쇄로 얻는 단점보다 크다고 믿는다.

파이썬에서는 다양한 메소드를 활용하여 언제든지 객체의 내부를 조작할 수 있다.   
무분별한 객체의 내부에 접근하는 위험을 최소화 하기위해 PEP 8에 정의된 명명 관례를 따른다.  
_protected_field처럼 앞에 밑줄 한 개를 붙인 필드는 보호 필드로 취급해서 클래스의 외부 사용자들이 신중하게 다뤄야함을 명시적으로 의미한다.-

하지만 파이썬을 처음 접하는 많은 프로그래머가 서브클래스나 외부에서 접근하면 안 되는 내부 API를 비공개 필드로 나타낸다.  


```python
class MyClass(object):
    def __init__(self, value):
        self.__value = value

    def get_value(self):
        return str(self.__value)

foo = MyClass(5)
assert foo.get_value() == "5"
```

이러한 접근 방식은 잘못된 방식이다.  
클래스에 새 동작을 추가하거나 기존 메서드의 결함을 해결하기 위해 서브클래스를 만든다.  
비공개 속성을 선택하면 서브클래스의 오버라이드와 확장을 다루기 어렵고 불안정하게 만든다.  
나중에 만들 서브클래스에서 꼭 필요하면 여전히 비공개 필드에 접근할 수도 있다.


```python
class MyIntegerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)

foo = MyIntegerSubclass(5)
assert foo.get_value() == 5
```

하지만 나중에 클래스의 계층이 변경되면 MyIntegerSubclass 같은 클래스는 비공개 참조가 더는 유효하지 않게 된다.  
MyIntegerSubclass의 직계 부모인  MyClass에 MyBaseCalss라는 또 다른 부모 클래스가 추가된다고 생각해보자.


```python
class MyBaseClass(object):
    def __init__(self, value):
        self.__value = value

class MyClass(object):        
    def get_value(self):
        return str(self.__value)


class MyIntergerSubclass(MyClass):
    def get_value(self):
        return int(self._MyClass__value)
```


```python
foo = MyIntergerSubclass(5)
foo.get_value()
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-51-3a414d566c82> in <module>()
    ----> 1 foo = MyIntergerSubclass(5)
          2 foo.get_value()


    TypeError: object() takes no parameters


일반적으로 보호 속성을 사용해서 서브클래스가 더 많은 일을 할 수 있게 하는 편이 낫다.  
각각의 보호 필드를 문서화해서 서브클래스에서 내부 API 중 어느 것을 쓸 수 있고 어느 것을 그대로 둬야 하는 지 설명하자.  
자신이 작성한 코드를 미래에 안전하게 확장하는 지침이 되는 것처럼 다른 프로그래머에게도 조언이 된다.


```python
class MyClass(object):
    def __init__(self, value):
        # 사용자가 객체에 전달한 값을 저장한다.
        # 문자열로 강제할 수 있는 값이어야 하며,
        # 객체에 할당하고 나면 불변으로 취급해야 한다.
        self._value = value
```

비공개 속성을 사용할지 진지하게 고민할 시점은 서브클래스와 이름이 충돌할 염려가 있을 때 뿐이다.  
이 문제는 자식 클래스가 부모 클래스에서 이미 정의한 속성을 정의할 떄 일어난다.


```python
class ApiClass(object):
    def __init__(self):
        self._value = 5
    def get(self):
        return self._value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'
```


```python
a = Child()
print(a.get(), 'and', a._value, 'should be different')    

>>> hello and hello should be different
```

이러한 위험을 줄이려면 부모 클래스에서 비공개 속성을 사용해서 자식 클래스와 속성 이름이 겹치지 않게 하면 된다.


```python
class ApiClass(object):
    def __init__(self):
        self.__value = 5
    def get(self):
        return self.__value

class Child(ApiClass):
    def __init__(self):
        super().__init__()
        self._value = 'hello'
```


```python
a = Child()
print(a.get(), 'and', a._value, 'should be different')  

>>> 5 and hello should be different
```


### 핵심 정리  
- 파이썬 컴파일러는 비공개 속성을 엄격하게 강요하지 않는다.
- 서브클래스가 내부 API와 속성에 접근하지 못하게 막기보다는 처음부터 내부 API와 속성으로 더 많은 일을 할 수 있게 설계하자.
- 비공개 속성에 대한 접근을 강제로 제어하지 말고 보호 필드를 문서화해서 서브클래스에 필요한 지침을 제공하자.
- 직접 제어할 수 없는 서브클래스와 이름이 충돌하지 않게 할 때만 비공개 속성을 사용하는 방안을 고려하자
