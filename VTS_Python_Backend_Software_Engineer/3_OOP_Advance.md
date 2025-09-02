# 🔥 Deep OOP Roadmap 

## 1️⃣ Core OOP Pillars 

### 🔹 Encapsulation (তথ্য গোপন রাখা)
মানে হলো ডেটা (variables) আর ফাংশন (methods) একসাথে ক্লাসের ভিতরে রাখা।  
বাইরে থেকে ডিরেক্ট অ্যাক্সেস না দিয়ে getter/setter বা @property এর মাধ্যমে কন্ট্রোল করা।  

**Python-এ:**  
- public → সবার জন্য উন্মুক্ত (`name`)  
- protected → আন্ডারস্কোর `_name` দিয়ে (ক্লাস আর সাবক্লাসে ব্যবহার হয়)  
- private → ডাবল আন্ডারস্কোর `__name` দিয়ে (শুধু সেই ক্লাসের ভেতরে)  

**👉 ব্যবহার:** ডেটা সুরক্ষিত রাখা, বাইরের ইউজারকে ডিরেক্ট পরিবর্তন করতে না দেয়া।  

### 🔹 Inheritance (উত্তরাধিকার)
একটি ক্লাস অন্য একটি ক্লাসের property/method ব্যবহার করতে পারবে।  

**ধরন:**  
- Single → এক ক্লাস থেকে অন্য ক্লাস ইনহেরিট (A → B)  
- Multiple → একাধিক ক্লাস থেকে ইনহেরিট (A, B → C)  
- Multilevel → A → B → C  
- Hybrid → একসাথে একাধিক ধরনের কম্বিনেশন  

**👉 ব্যবহার:** কোড পুনরায় ব্যবহার (Code Reusability)।

### 🔹 Polymorphism (এক নামে অনেক রূপ)
একই জিনিস ভিন্ন ভিন্নভাবে কাজ করবে।  

**দুইভাবে হয়:**  
- Method Overriding → সাবক্লাস প্যারেন্টের ফাংশনকে নিজের মতো করে লিখবে।  
- Operator Overloading → `+`, `-`, `*` ইত্যাদি অপারেটরকে কাস্টমাইজ করা।  

**👉 ব্যবহার:** বিভিন্ন object একই method কে আলাদা কাজে লাগানো।  

### 🔹 Abstraction (অপ্রয়োজনীয় জিনিস লুকানো)
শুধু দরকারি জিনিস দেখানো, অপ্রয়োজনীয় details লুকানো।  

- **Python-এ:** `abc` মডিউল ব্যবহার করে abstract class তৈরি করা যায়।  
- **Java/C++:** Interface আর Abstract Class ব্যবহার হয়।  

**👉 ব্যবহার:** শুধু "কি করতে হবে" সেটি বলা, "কিভাবে করতে হবে" সেটা subclass কে ঠিক করতে দেওয়া।  

## 2️⃣ Advanced OOP Concepts
- **Composition বনাম Inheritance** → অনেক ক্ষেত্রে ইনহেরিটেন্সের বদলে কম্পোজিশন (এক ক্লাসের ভিতরে অন্য ক্লাস ব্যবহার) বেশি ফ্লেক্সিবল।  
- **Mixins (Python Specific)** → ছোট ছোট ফাংশনালিটি আলাদা ক্লাসে রেখে মিশিয়ে ব্যবহার করা (Django-তে খুব কমন)।  
- **Metaclasses** → ক্লাসকে কে তৈরি করে, সেটি কন্ট্রোল করা।  
- **Duck Typing** → "যদি হাঁসের মতো হাঁটে, আর ডাক দেয় হাঁসের মতো, তাহলে সেটি হাঁস।" → Python-এ অবজেক্ট টাইপের চেয়ে অবজেক্টের আচরণ বেশি গুরুত্বপূর্ণ।  
- **SOLID Principles** → সফটওয়্যার ডিজাইনের ৫টি স্বর্ণনীতি (Interview-এ অবশ্যই লাগে)।  
- **Design by Contract** → প্রতিটি মেথডে স্পষ্ট চুক্তি (input/output শর্ত) দেওয়া।  
- **Encapsulation Enforcement** → ডেটাকে সঠিকভাবে সুরক্ষিত রাখা।  

#### 

<h6> 
  
 > Inheritance (উত্তরাধিকার)
  
সংজ্ঞা: Inheritance মানে হলো একটি ক্লাস (child/subclass) অন্য একটি ক্লাসের (parent/superclass) প্রপার্টি এবং মেথড ব্যবহার করতে পারা। <br>
এক কথায়, child ক্লাস parent ক্লাস থেকে “উত্তরাধিকার” পায়।
  
 > Composition (সংযোগ/সমন্বয়)

 
সংজ্ঞা: Composition মানে হলো একটি ক্লাসের ভিতরে অন্য ক্লাসকে ব্যবহার করা। <br>
এক কথায়, “এক ক্লাসের object অন্য ক্লাসের object কে use করে”।  <br>
Inheritance-এর পরিবর্তে বেশি flexible, কারণ classes আলাদা থাকে এবং চাইলে replace করা যায়। 
  
</h6>

## 3️⃣ OOP Design Principles
- **DRY (Don’t Repeat Yourself)** → একই কোড বারবার না লিখে পুনর্ব্যবহার করা।  
- **KISS (Keep It Simple, Stupid)** → কোড জটিল না করা, সহজ রাখা।  
- **YAGNI (You Aren’t Gonna Need It)** → অপ্রয়োজনীয় ফিচার আগে থেকে না বানানো।  
- **Cohesion vs Coupling**  
  - Cohesion → ক্লাস/মডিউল কতটা ফোকাসড।  
  - Coupling → ক্লাস/মডিউলের মধ্যে নির্ভরশীলতা কম রাখা।  
- **Dependency Inversion Principle (DIP)** → হাই লেভেল মডিউল লো লেভেল মডিউলের উপর নির্ভর করবে না, বরং abstraction-এর উপর নির্ভর করবে।  
- **Law of Demeter** → "Don’t talk to strangers" → এক ক্লাস অন্য ক্লাসের ভিতরের ডিটেইলসে ঢুকবে না।  

## 4️⃣ Design Patterns (খুব গুরুত্বপূর্ণ 🚀)
**Creational**  
- Singleton → একটাই অবজেক্ট বানানো।  
- Factory → অবজেক্ট তৈরি করার দায়িত্ব অন্য ক্লাসকে দেওয়া।  
- Builder → জটিল অবজেক্ট ধাপে ধাপে তৈরি করা।  
- Prototype → কপি করে অবজেক্ট বানানো।  

**Structural**  
- Adapter → এক সিস্টেমকে আরেক সিস্টেমের সাথে মানিয়ে দেওয়া।  
- Decorator → বিদ্যমান অবজেক্টে নতুন ফিচার যোগ করা।  
- Proxy → আসল অবজেক্টে যাওয়ার আগে মধ্যবর্তী অবজেক্ট ব্যবহার।  
- Composite → ট্রি-স্ট্রাকচারের মতো অবজেক্ট ম্যানেজ করা।  

**Behavioral**  
- Observer → একটি ইভেন্ট ঘটলে অন্যদের নোটিফাই করা।  
- Strategy → রানটাইমে অ্যালগরিদম বদলানো।  
- Command → অ্যাকশনকে অবজেক্ট আকারে রাখা।  
- State → অবজেক্টের অবস্থা বদলালে আচরণ বদলানো।  
- Visitor → অবজেক্টে নতুন অপারেশন যোগ করা।  

**👉 ব্যবহার:** এগুলো শিখলে Django, Spring, React ফ্রেমওয়ার্কের ভিতরের ডিজাইন বুঝতে পারবে।  

## 5️⃣ Practical Applications
- Django Model = ক্লাস  
- Django Class-Based Views = Inheritance + Mixins  
- DRF = Polymorphism + Abstract classes  
- Spring/Hibernate = Design Patterns  
- C++ STL = Templates + OOP concepts  

## 6️⃣ Next Level
- **UML Diagrams** → ক্লাস, সিকোয়েন্স, ইউজ-কেস ভিজ্যুয়ালাইজ করা।  
- **Design Patterns** → Python, Java, C++ এ তুলনা করা।  
- **Testing OOP** → Unit testing, Mocking, TDD.

---
<br>
<br>


# Example


## 1️⃣ Encapsulation (ডেটা গোপন রাখা)
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner       # public
        self.__balance = balance # private

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance
 
# ব্যবহার
acc = BankAccount("Alice", 1000)
acc.deposit(500)
print(acc.get_balance())  # 1500
# print(acc.__balance)  # Error: private
```

👉 এখানে __balance private রাখা হয়েছে। বাইরের কোড direct modify করতে পারবে না।

## 2️⃣ Inheritance (উত্তরাধিকার)
```python
class Animal:
    def speak(self):
        print("Some sound")

class Dog(Animal):  # Animal থেকে উত্তরাধিকার
    def speak(self):
        print("Woof!")

class Cat(Animal):
    def speak(self):
        print("Meow!")

dog = Dog()
cat = Cat()
dog.speak()  # Woof!
cat.speak()  # Meow!
```

👉 Dog এবং Cat Animal থেকে মেথড পায়, কিন্তু নিজের মতো করে override করে।

## 3️⃣ Polymorphism (এক নামে অনেক রূপ)
```python
animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.speak()


Output:

Woof!
Meow!
Some sound
```

👉 একই মেথড speak() ভিন্ন অবজেক্টে ভিন্নভাবে কাজ করছে।

## 4️⃣ Abstraction (অপ্রয়োজনীয় লুকানো)
```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

rect = Rectangle(5, 10)
print(rect.area())  # 50

```
👉 Shape class abstract → area কিভাবে calculate হবে তা subclasses define করবে।

## 5️⃣ Advanced Use Case (Encapsulation + Inheritance + Polymorphism + Abstraction)
```python
from abc import ABC, abstractmethod

# Abstract Base Class
class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary  # Encapsulation

    @abstractmethod
    def calculate_bonus(self):
        pass

    def get_salary(self):
        return self.__salary

# Inheritance + Polymorphism
class Developer(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.2

class Manager(Employee):
    def calculate_bonus(self):
        return self.get_salary() * 0.3

# ব্যবহার
employees = [Developer("Alice", 5000), Manager("Bob", 8000)]
for emp in employees:
    print(f"{emp.name} bonus: {emp.calculate_bonus()}")

```

Output:
- Alice bonus: 1000.0
- Bob bonus: 2400.0


✅ এখানে সবকিছু একসাথে ব্যবহার করা হয়েছে:

- `__salary` → Encapsulation
- `Employee` → Abstraction
- `Developer ও Manager` → Inheritance
- `calculate_bonus()` → Polymorphism



<br>
<br>
<br>
<br>


## 1️⃣ Composition vs Inheritance
```py
# Composition
class Engine:
    def start(self):
        print("Engine starting...")

class CarInheritance(Engine):  # Car inherits Engine
    def drive(self):
        print("Car is driving")

car1 = CarInheritance()
car1.start()  # Engine starting...
car1.drive()  # Car is driving

# Composition (Flexible)
class CarComposition:
    def __init__(self, engine):
        self.engine = engine  # Engine as a component

    def drive(self):
        self.engine.start()
        print("Car is driving")

engine = Engine()
car2 = CarComposition(engine)
car2.drive()
```

👉 Composition বেশি flexible, কারণ CarComposition engine কে সহজে replace করতে পারে।

<br>
<br>
<br>

## 2️⃣ Mixins (Python Specific)
```python
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class Person(JSONMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.to_json())  # {"name": "Alice", "age": 25}
```
--
```python
class Notifier:
    def send(self, msg: str):
        print(f"[BASE] {msg}")

class EmailMixin(Notifier):
    def send(self, msg: str):
        print(f"Email → {msg}")
        super().send(msg)

class SmsMixin(Notifier):
    def send(self, msg: str):
        print(f"SMS → {msg}")
        super().send(msg)

class AlertService(EmailMixin, SmsMixin):
    pass

service = AlertService()
service.send("Server down!")
# Order: Email → SMS → BASE (follows MRO)
# Check: AlertService.mro()
```

#### usecase of explanaiton `__dict__`
--
```python
class Person:
    species = "Human"  # class variable
    def __init__(self, name, age):
        self.name = name
        self.age = age

p = Person("Alice", 25)
print(p.__dict__)        # {'name': 'Alice', 'age': 25}
print(Person.__dict__)   # shows 'species' among other class info

```

```python
class Person:
    def __init__(self, name, age):
        self.__name = name   # private
        self.age = age

p = Person("Alice", 25)
print(p.__dict__)  # {'_Person__name': 'Alice', 'age': 25}
# 👉 Private variable access:
print(p._Person__name)  # Alice

```

👉 ছোট ফাংশনালিটি আলাদা ক্লাসে রেখে মিশিয়ে ব্যবহার করা হয়। Django CBV তে Mixins খুব common।

<br>
<br>
<br>

## 3️⃣ Metaclasses
```python
# Metaclass defines how classes are created
class UppercaseAttributesMeta(type):
    def __new__(cls, name, bases, dct):
        uppercase_attrs = {k.upper(): v for k, v in dct.items()}
        return super().__new__(cls, name, bases, uppercase_attrs)

class Person(metaclass=UppercaseAttributesMeta):
    name = "Alice"
    age = 25

print(hasattr(Person, "NAME"))  # True
print(hasattr(Person, "name"))  # False
```

👉 Metaclasses দিয়ে আমরা class-এর structure কে কাস্টমাইজ করতে পারি।


### Metaclass কী?

Python-এ class নিজেই একটি object।

#### কোন class কে কে তৈরি করবে এবং তার behavior কেমন হবে, সেটা Metaclass দ্বারা নিয়ন্ত্রণ করা যায়।

type হলো Python-এর built-in metaclass।
সাধারণভাবে:
```
object → instance of class  
class → instance of metaclass  
```
### UppercaseAttributesMeta - এটি হলো একটি custom metaclass।  

#### Step by step:
- এটা `type` কে inherit করেছে → অর্থাৎ class কিভাবে তৈরি হবে সেটা কাস্টমাইজ করতে পারি।  
- **`__new__` method**  
- class তৈরি হওয়ার আগে call হয়।  
- **Parameters:**  
  - `cls` → metaclass নিজেই  
  - `name` → নতুন class এর নাম (যেমন "Person")  
  - `bases` → parent classes (যদি inheritance থাকে)  
  - `dct` → class attributes dictionary `{attribute_name: value}`

<br>
<br>
<br>

## 4️⃣ Duck Typing
```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I can quack like a duck!")

def make_it_quack(thing):
    thing.quack()  # কোন টাইপ চেক করা হয় না, behavior দেখেই কাজ

duck = Duck()
person = Person()
make_it_quack(duck)    # Quack!
make_it_quack(person)  # I can quack like a duck!
```

👉 Python এ টাইপের চেয়ে behavior বেশি গুরুত্বপূর্ণ।

<br>
<br>
<br>

## 5️⃣ Design by Contract & Encapsulation Enforcement

```python
class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, amount):
        assert amount > 0, "Amount must be positive"  # Design by Contract
        self.__balance += amount

    def withdraw(self, amount):
        assert 0 < amount <= self.__balance, "Invalid withdrawal amount"
        self.__balance -= amount

    def get_balance(self):
        return self.__balance

acc = BankAccount(1000)
acc.deposit(500)
# acc.withdraw(2000)  # AssertionError: Invalid withdrawal amount
print(acc.get_balance())
```

👉 Assertions enforce contract; private __balance ensures encapsulation.

<br>
<br>
<br>

## 6️⃣ Advanced Use Case: Online Shop System
```python
from abc import ABC, abstractmethod

# Metaclass Example
class UppercaseAttrsMeta(type):
    def __new__(cls, name, bases, dct):
        dct = {k.upper(): v for k, v in dct.items()}
        return super().__new__(cls, name, bases, dct)

# Abstraction
class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Composition
class Wallet:
    def __init__(self, balance):
        self.__balance = balance

    def deduct(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            return True
        return False

    def get_balance(self):
        return self.__balance

# Mixins
class ReceiptMixin:
    def receipt(self):
        print(f"Receipt: {self.__dict__}")

# Duck Typing & Polymorphism
class User(Payment, ReceiptMixin, metaclass=UppercaseAttrsMeta):
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def pay(self, amount):
        if self.wallet.deduct(amount):
            print(f"{self.name} paid {amount}")
        else:
            print(f"{self.name} has insufficient funds")

wallet1 = Wallet(500)
user1 = User("Alice", wallet1)
user2 = User("Bob", Wallet(300))

users = [user1, user2]
for u in users:
    u.pay(200)  # Polymorphic behavior
    u.receipt()

```

✅ এই use case-এ সব advanced concept আছে:

<h6>
  
Composition → Wallet inside User <br>
Mixins → ReceiptMixin <br>
Metaclass → uppercase attributes <br>
Duck Typing & Polymorphism → same pay() method বিভিন্ন objects এ ভিন্নভাবে কাজ করছে <br>
Encapsulation Enforcement → __balance private <br>
Design by Contract → deduct logic ensures correct payment <br>

</h6>
