# Assign functions to variables
def greet(name):
    return "hello "+name


greet_someone = greet
print(greet_someone("John"))
# Outputs: hello John

# define functions inside other functions


def greet(name):
    def get_message():
        return "Hello "

    result = get_message()+name
    return result


print(greet("John"))
# Outputs: Hello John


# Functions can be passed as parameters to other functions
def greet(name):
    return "Hello " + name


def call_func(func):
    other_name = "John"
    return func(other_name)


print(call_func(greet))
# Outputs: Hello John


# Functions can return other functions
def compose_greet_func():
    def get_message():
        return "Hello there!"

    return get_message


greet = compose_greet_func()
print(greet())
# Outputs: Hello there!


# Inner functions have access to the enclosing scope
# More commonly known as a closure. A very powerful pattern that we will come across while building decorators. Another thing to note, Python only allows read access to the outer scope and not assignment. Notice how we modified the example above to read a "name" argument from the enclosing scope of the inner function and return the new function.

def compose_greet_func(name):
    def get_message():
        return "Hello there "+name+"!"

    return get_message


greet = compose_greet_func("John")
print(greet())
# Outputs: Hello there John!

# Composition of Decorators
# Function decorators are simply wrappers to existing functions. Putting the ideas mentioned above together,
# we can build a decorator. In this example let's consider a function that wraps the string output of another function by p tags.

# base func returns a string but no p tags to format it


def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)
# p_decorate takes a function as an argument and wraps the return of get_text in p tags


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


# function gets called
# Another thing to notice is that our decorated function takes a name argument.
my_get_text = p_decorate(get_text)
# All we had to do in the decorator is to let the wrapper of get_text pass that argument.
print(my_get_text("John"))
# <p>Outputs lorem ipsum, John dolor sit amet</p>


# Python makes creating and using decorators a bit cleaner and nicer for the programmer through some syntactic sugar
# To decorate get_text we don't have to get_text = p_decorator(get_text) There is a neat shortcut for that, which is
# to mention the name of the decorating function before the function to be decorated. The name of the decorator
# should be perpended with an @ symbol.
def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


print(get_text("John"))
# Outputs <p>lorem ipsum, John dolor sit amet</p>

# Now let's consider we wanted to decorate our get_text function by 2 other functions to wrap a div and strong tag
# around the string output.


def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper


def strong_decorate(func):
    def func_wrapper(name):
        return "<strong>{0}</strong>".format(func(name))
    return func_wrapper


def div_decorate(func):
    def func_wrapper(name):
        return "<div>{0}</div>".format(func(name))
    return func_wrapper

# With the basic approach, decorating get_text would be along the lines of
# get_text = div_decorate(p_decorate(strong_decorate(get_text)))
# With Python's decorator syntax, same thing can be achieved with much more expressive power.


@div_decorate
@p_decorate
@strong_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)


print(get_text("John"))
# Outputs <div><p><strong>lorem ipsum, John dolor sit amet</strong></p></div>


# In Python, methods are functions that expect their first parameter to be a reference to the current object.
# We can build decorators for methods the same way, while taking self into consideration in the wrapper function.

def p_decorate(func):
    def func_wrapper(self):
        return "<p>{0}</p>".format(func(self))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family


my_person = Person()
print(my_person.get_fullname())


# A much better approach would be to make our decorator useful for functions and methods alike.
# This can be done by putting args and *kwargs as parameters for the wrapper, then it can accept
# any arbitrary number of arguments and keyword arguments.
def p_decorate(func):
    def func_wrapper(*args, **kwargs):
        return "<p>{0}</p>".format(func(*args, **kwargs))
    return func_wrapper


class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family


my_person = Person()
print(my_person.get_fullname())
