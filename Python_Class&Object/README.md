

OOP (Object-Oriented Programming):
It is a programming paradigm that revolves around the concept of "objects" that can contain data (known as attributes) and functions (known as methods) that operate on that data. The main aim of OOP is to model real-world entities in the form of objects in order to make code easier to develop and maintain

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Juan", 30)
persona1.saludar()
-------

"First-class everything":
This is a principle in Python that means that everything in Python, including functions and classes, are treated as first-class objects. This means that they can be passed as arguments to functions, assigned to variables, and stored in data structures.


Class:
A class is a "mold" or "blueprint" for creating objects. It defines the properties and behaviors that objects of that class will have.
class Coche:
    pass  #se utiliza solamente para que el editor entienda que esta ssintacticamente correcta

    --------------

Object and Instance:
An object is an instance of a class. When you create an object using a class, you are instantiating that class and creating a specific entity based on that class.

coche1 = Coche()  # Creando una instancia de la clase Coche

--------------
variables == atributos
funciones == metodos
------------
Attribute:
An attribute is a variable that is associated with a class or object and stores data about the object.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

-------------------
Public, Protected, and Private Attributes:
In Python, all attributes are public by default. However, a naming convention can be used to indicate that an attribute should be treated as protected (by using a single leading underscore) or private (by using two leading underscores).
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo público
        self._edad = edad     # Atributo protegido
        self.__dni = dni      # Atributo privado

-----------
self:
In Python, self is a convention that is used to refer to the current instance of a class within the methods of that class.

class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

    def saludar(self):
        print(f"Hola, soy {self.nombre}.")

--------------
Method:
A method is a function that is associated with a class and can operate on the attributes of that class.
class Coche:
    def conducir(self):
        print("El coche está en movimiento.")

class Coche:
    def conducir(self):
        print("El coche está en movimiento.")


Special Method init:
The init method is a special method in Python that is used to initialize the attributes of an instance when an object is created.
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
-------
Data Abstraction, Data Encapsulation, and Information Hiding:
These are principles of OOP that refer to the idea of hiding the internal details of an object and only exposing a public interface to interact with it.


Property:
A property is an attribute that has an associated getter and setter, which allows for controlling the access and modification of that attribute.
class Persona:
    def __init__(self, nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        self._nombre = nuevo_nombre
