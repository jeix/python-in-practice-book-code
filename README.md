# python-in-practice-book-code

![Python in Practice](https://image.aladin.co.kr/product/4551/98/cover200/8998139650_1.jpg)

# Python in Practice

## 1. Creational Design Patterns

### 1.1 Abstract Factory Pattern
#### 1.1.1 A Classic Abstract Factory
  - @see diagram1.py
#### 1.1.2 A More Pythonic Abstract Factory
  - @see diagram2.py

### 1.2 Builder Pattern
  - @see formbuilder.py

### 1.3 Factory Method Pattern
  - @see gameboard1.py
  - @see gameboard2.py
  - @see gameboard3.py
  - @see gameboard4.py

### 1.4 Prototype Pattern

  - ```python
    class Point:
    	
  	__slots__ = ("x", "y")
    	
    	def __init__(self, x, y):
    		self.x = x
    		self.y = y
    ```
    ```python
    def make_object(Class, *args, **kwargs):
    	return Class(*args, **kwargs)
    
    point1 = Point(1, 2)
    point2 = eval("{}({}, {})".format("Point", 2, 4)) # Risky
    point3 = getattr(sys.modules[__name__], "Point")(3, 6)
    point4 = globals()["Point"](4, 8)
    point5 = make_object(Point, 5, 10)
    point6 = copy.deepcopy(point5)
    point6.x = 6
    point6.y = 12
    point7 = point1.__class__(7, 14) # Could have used any of point1 to point6
    ```

### 1.5 Singleton Pattern
  - @see Rates.py


## 2. Structural Design Patterns

### 2.1 Adapter Pattern
  - @see render1.py
  - @see render2.py

### 2.2 Bridge Pattern
  - @see barchart1.py
  - @see barchart2.py
  - @see barchart3.py

  - ```python
    # Qtrac.has_methods
    def has_methods(*methods):
    	def decorator(Base):
    		def __subclasshook__(Class, Subclass):
    			if ClassisBase:
    				attributes = collections.ChainMap(*(Superclass.__dict__
    						for Superclass in Subclass.__mro__))
    				if all(method in attributes for method in methods):
    					return True
    			return NotImplemented
    		Base.__subclasshook__ = classmethod(__subclasshook__)
    		return Base
    	return decorator
    ```

  - ```python
    class BarRenderer(Qtrac.Requirer):
    	required_methods = {"initialize", "draw_caption", "draw_bar", "finalize"}
    ```

### 2.3 Composite Pattern
#### 2.3.1 A Classic Composite/Noncomposite Hierarchy
  - @see stationery1.py
#### 2.3.2 A Single Class for (Non)Composites
  - @see stationery2.py

### 2.4 Decorator Pattern
#### 2.4.1 Function and Method Decorators

  - ```python
    @float_args_and_return
    def mean(first, second, *rest):
    	numbers = (first, second) + rest
    	return sum(numbers) / len(numbers)
    ```
    ```python
    def mean(first, second, *rest):
    	numbers = (first, second) + rest
    	return sum(numbers) / len(numbers)
    mean = float_args_and_return(mean)
    ```
    ```python
    def float_args_and_return(function):
    	def wrapper(*args, **kwargs):
    		args = [float(arg) for arg in args]
    		return float(function(*args, **kwargs))
    	return wrapper
    ```
    ```python
    def float_args_and_return(function):
    	@functools.wraps(function)
    	def wrapper(*args, **kwargs):
    		args = [float(arg) for arg in args]
    		return float(function(*args, **kwargs))
    	return wrapper
    ```

  - ```python
    @statically_typed(str, str, return_type=str)
    def make_tagged(text, tag):
    	return "<{0}>{1}</{0}>".format(tag, escape(text))
    
    @statically_typed(str, int, str) # Will accept any return type
    def repeat(what, count, separator):
    	return ((what + separator) * count)[:-len(separator)]
    ```
    ```python
    def statically_typed(*types, return_type=None):
    	def decorator(function):
    		@functools.wraps(function)
    		def wrapper(*args, **kwargs):
    			if len(args) > len(types):
    				raise ValueError("too many arguments")
    			elif len(args) < len(types):
    				raise ValueError("too few arguments")
    			for i, (arg, type_) in enumerate(zip(args, types)):
    				if not isinstance(arg, type_):
    					raise ValueError("argument {} must be of type {}"
    							.format(i, type_.__name__))
    			result = function(*args, **kwargs)
    			if (return_type is not None and
    				not isinstance(result, return_type)):
    				raise ValueError("return value must be of type {}".format(
    						return_type.__name__))
    			return result
    		return wrapper
    	return decorator
    ```

  - ```python
    @application.post("/mailinglists/add")
    @Web.ensure_logged_in
    def person_add_submit(username):
    	name = bottle.request.forms.get("name")
    	try:
    		id = Data.MailingLists.add(name)
    		bottle.redirect("/mailinglists/view")
    	except Data.Sql.Error as err:
    		return bottle.mako_template("error", url="/mailinglists/add",
    				text="Add Mailinglist", message=str(err))
    ```
    ```python
    def ensure_logged_in(function):
    	@functools.wraps(function)
    	def wrapper(*args, **kwargs):
    		username = bottle.request.get_cookie(COOKIE,
    				secret=secret(bottle.request))
    		if username is not None:
    			kwargs["username"] = username
    			return function(*args, **kwargs)
    		bottle.redirect("/login")
    	return wrapper
    ```

#### 2.4.2 Class Decorators
  - @see validate1.py
##### 2.4.2.1 Using a Class Decorator to Add Properties
  - @see validate2.py
##### 2.4.2.2. Using a Class Decorator Instead of Subclassing

  - ```python
    class Mediated:
    
    	def __init__(self):
    			self.mediator = None
    
    	def on_change(self):
    		if self.mediator is not None:
    			self.mediator.on_change(self)
    ```
    ```python
    def mediated(Class):
    	setattr(Class, "mediator", None)
    	def on_change(self):
    		if self.mediatoris not None:
    			self.mediator.on_change(self)
    	setattr(Class,"on_change", on_change)
    	return Class
    ```

  - @see mediator1d.py
  - @see mediator2d.py

### 2.5 Façade Pattern
  - @see Unpack.py

### 2.6 Flyweight Pattern
  - @see pointstore1.py
  - @see pointstore2.py

### 2.7 Proxy Pattern
  - @see imageproxy1.py
  - @see imageproxy2.py


## 3. Behavioral Design Patterns

### 3.1 Chain of Responsibility Pattern
#### 3.1.1 A Conventional Chain
  - @see eventhandler1.py
#### 3.1.2 A Coroutine-based Chain

  - ```python
    def coroutine(function):
    	@functools.wraps(function)
    	def wrapper(*args, **kwargs):
    		generator = function(*args, **kwargs)
    		next(generator)
    		return generator
    	return wrapper
    ```

  - @see eventhandler2.py

### 3.2 Command Pattern
  - @see 2_7-Proxy/imageproxy1.py
  - @see 2_7-Proxy/imageproxy2.py
  - @see grid.py

### 3.3 Interpreter Pattern

  - ```python
    try:
    	count = int(userCount)
    	when = datetime.datetime.strptime(userDate, "%Y/%m/%d").date()
    except ValueError as err:
    	print(err)
    ```

  - PLY (Python Lex-Yacc) @ http://www.dabeaz.com/ply/
  - pyparsing @ http://pyparsing.wikispaces.com/

#### 3.3.1 Expression Evaluation with eval()

  - ```sh
    $ ./calculator.py
    Enter an expression (Ctrl+D to quit): 65
    A=65
    ANS=65
    Enter an expression (Ctrl+D to quit): 72
    A=65, B=72
    ANS=72
    Enter an expression (Ctrl+D to quit): hypotenuse(A, B)
    name 'hypotenuse' is not defined
    Enter an expression (Ctrl+D to quit): hypot(A, B)
    A=65, B=72, C=97.0
    ANS=97.0
    Enter an expression (Ctrl+D to quit): ^D
    ```
    ```python
    def main():
    	quit = "Ctrl+Z,Enter" if sys.platform.startswith("win") else "Ctrl+D"
    	prompt = "Enter an expression ({} to quit): ".format(quit)
    	#current = ["A"]
    	#current = type("_", (), dict(letter="A"))()
    	current = types.SimpleNamespace(letter="A")
    	globalContext = global_context()
    	localContext = collections.OrderedDict()
    	while True:
    		try:
    			expression = input(prompt)
    			if expression:
    				calculate(expression, globalContext, localContext, current)
    		except EOFError:
    			print()
    			break
    ```
    ```python
    import math
    def global_context():
    	globalContext = globals().copy()
    	for name in dir(math):
    		if not name.startswith("_"):
    			globalContext[name] = getattr(math, name)
    	return globalContext
    ```
    ```python
    def calculate(expression, globalContext, localContext, current):
    	try:
    		result = eval(expression, globalContext, localContext)
    		update(localContext, result, current)
    		print(", ".join(["{}={}".format(variable, value)
    				for variable, value in localContext.items()]))
    		print("ANS={}".format(result))
    	except Exception as err:
    		print(err)
    ```
    ```python
    def update(localContext, result, current):
    	localContext[current.letter] = result
    	current.letter =chr(ord(current.letter) +1)
    	if current.letter >"Z": # We only support 26 variables
    		current.letter = "A"
    ```

#### 3.3.2 Code Evaluation with exec()
  - @see genome1.py
#### 3.3.3 Code Evaluation using a Subprocess
  - @see genome2.py
  - @see genome3.py

### 3.4 Iterator Pattern
#### 3.4.1 Sequence Protocol Iterators

  - ```python
    for letter in AtoZ():
    	print(letter, end="")
    print()
    
    for letter in iter(AtoZ()):
    	print(letter, end="")
    print()
    ```
    ```python
    class AtoZ:
    	def __getitem__(self, index):
    		if 0 <= index < 26:
    			return chr(index + ord("A"))
    		raise IndexError()
    ```

#### 3.4.2 Two-argument iter() Function Iterators

  - ```python
    # stop if the callable raises a StopIteration exception
    for president in iter(Presidents("George Bush"), None):
    	print(president, end=" * ")
    print()
    
    # stop if it returns the sentinel value
    for president in iter(Presidents("George Bush"), "George W. Bush"):
    	print(president, end=" * ")
    print()
    ```
    ```python
    class Presidents:
    
    	__names = ("George Washington", "John Adams", "Thomas Jefferson",
    				...
    				"Bill Clinton", "George W. Bush", "Barack Obama")
    
    	def __init__(self, first=None):
    		self.index = (-1 if first is None else
    						Presidents.__names.index(first) - 1)
    
    	def __call__(self):
    		self.index += 1
    		if self.index < len(Presidents.__names):
    			return Presidents.__names[self.index]
    		raise StopIteration()
    ```

#### 3.4.3 Iterator Protocol Iterators
  - @see Bag1.py
  - @see Bag2.py
  - @see Bag3.py
  - @use collections.Counter

### 3.5 Mediator Pattern
#### 3.5.1 A Conventional Mediator
  - @see mediator1.py
#### 3.5.2 A Coroutine-based Mediator
  - @see mediator2.py

### 3.6 Memento Pattern
  - @use pickle
  - @use json

### 3.7 Observer Pattern
  - @see observer.py

### 3.8 State Pattern
#### 3.8.1 Using State-Sensitive Methods
  - @see multiplexer1.py
#### 3.8.2 Using State-Specific Methods
  - @see multiplexer2.py

### 3.9 Strategy Pattern
  - @see tabulator1.py
  - @see tabulator2.py
  - @see tabulator3.py
  - @see tabulator4.py

### 3.10 Template Method Pattern
  - @see wordcount1.py
  - @see wordcount2.py

### 3.11 Visitor Pattern

  - ```python
    newList = map(function, oldSequence)
    ```
    ```python
    newList = [function(item) for item in oldSequence]
    ```
    ```python
    for item in collection:
    	function(item)
    ```

### 3.12 Case Study: An Image Package
#### 3.12.1. The Generic Image Module

  - ```python
    _Modules = []
    for name in os.listdir(os.path.dirname(__file__)):
    	if not name.startswith("_") and name.endswith(".py"):
    		name = "." + os.path.splitext(name)[0]
    		try:
    			module = importlib.import_module(name, "Image")
    			_Modules.append(module)
    		except ImportError as err:
    			warnings.warn("failed to load Image module: {}".format(err))
    del name, module
    ```

  - @ https://docs.python.org/dev/library/zipimport.html

  - @use pkgutil.walk_packages()

#### 3.12.2. An Overview of the Xpm Module
#### 3.12.3. The PNG Wrapper Module


## 4. High-Level Concurrency

### 4.1 CPU-bound Concurrency
#### 4.1.1 Using Queues and Multiprocessing
#### 4.1.2 Using Futures and Multiprocessing

### 4.2 I/O-bound Concurrency
#### 4.2.1 Using Queues and Threading
#### 4.2.2 Using Futures and Threading

### 4.3 Case Study: A Concurrent GUI Application

## 5. Extending Python

### 5.1 Accessing C Libraries with ctypes

### 5.2 Using Cython
#### 5.2.1 Accessing c Libraries with Cython
#### 5.2.2 Writing Cython Modules for Greater Speed

### 5.3 Case Study: An Accelerated Image Package

## 6. High-Level Networking

### 6.1 Writing XML-RPC Applications
#### 6.1.1 A Data Wrapper
#### 6.1.2 Writing XML-RPC Servers
#### 6.1.3 Writing XML-RPC Clients

### 6.2 Writing RPyC Applications
#### 6.2.1 A Thread-Safe Data Wrapper
#### 6.2.2 Writing RPyC Servers
#### 6.2.3 Writing RPyC Clients

## 7. Graphical User Interfaces with Tkinter

### 7.1 Introduction to Tkinter

### 7.2 Creating Dialogs with Tkinter
#### 7.2.1 Creating a Dialog-style Application
#### 7.2.2 Creating Application Dialogs

### 7.3 Creating Main Window Applications with Tkinter
#### 7.3.1 Creating a Main Window
#### 7.3.2 Creating Menus
#### 7.3.3 Creating a Status Bar with Indicators

## 8. OpenGL 3D Graphics

### 8.1 A Perspective Scene
#### 8.1.1 Creating a Cylinder with PyOpenGL
#### 8.1.2 Creating a Cylinder with pyglet

### 8.2 An Orthographic Game
#### 8.2.1 Drawing the Board Scene
#### 8.2.2 Handling Scene Object Selection
#### 8.2.3 Handling User Interaction

## A. Epilogue
## B. Selected Bibliograpy

:wq