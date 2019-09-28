https://learnpythonthehardway.org/book/ex44.html

 Inheritance Versus Composition

In the fairy tales about heroes defeating evil villains there's always a dark forest of some kind. It could be a cave, a forest, another planet, just some place that everyone knows the hero shouldn't go. Of course, shortly after the villain is introduced you find out, yes, the hero has to go to that stupid forest to kill the bad guy. It seems the hero just keeps getting into situations that require him to risk his life in this evil forest.

You rarely read fairy tales about the heroes who are smart enough to just avoid the whole situation entirely. You never hear a hero say, "Wait a minute, if I leave to make my fortunes on the high seas leaving Buttercup behind I could die and then she'd have to marry some ugly prince named Humperdink. Humperdink! I think I'll stay here and start a Farm Boy for Rent business." If he did that there'd be no fire swamp, dying, reanimation, sword fights, giants, or any kind of story really. Because of this, the forest in these stories seems to exist like a black hole that drags the hero in no matter what they do.

In object-oriented programming, Inheritance is the evil forest. Experienced programmers know to avoid this evil because they know that deep inside the Dark Forest Inheritance is the Evil Queen Multiple Inheritance. She likes to eat software and programmers with her massive complexity teeth, chewing on the flesh of the fallen. But the forest is so powerful and so tempting that nearly every programmer has to go into it, and try to make it out alive with the Evil Queen's head before they can call themselves real programmers. You just can't resist the Inheritance Forest's pull, so you go in. After the adventure you learn to just stay out of that stupid forest and bring an army if you are ever forced to go in again.

This is basically a funny way to say that I'm going to teach you something you should use carefully called Inheritance. Programmers who are currently in the forest battling the Queen will probably tell you that you have to go in. They say this because they need your help since what they've created is probably too much for them to handle. But you should always remember this:

Most of the uses of inheritance can be simplified or replaced with composition, and multiple inheritance should be avoided at all costs.

What is Inheritance?

Inheritance is used to indicate that one class will get most or all of its features from a parent class. This happens implicitly whenever you write class Foo(Bar), which says "Make a class Foo that inherits from Bar." When you do this, the language makes any action that you do on instances of Foo also work as if they were done to an instance of Bar. Doing this lets you put common functionality in the Bar class, then specialize that functionality in the Foo class as needed.

When you are doing this kind of specialization, there are three ways that the parent and child classes can interact:

Actions on the child imply an action on the parent.
Actions on the child override the action on the parent.
Actions on the child alter the action on the parent.
I will now demonstrate each of these in order and show you code for them.

Implicit Inheritance

First I will show you the implicit actions that happen when you define a function in the parent, but not in the child.

 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
class Parent(object):

    def implicit(self):
        print "PARENT implicit()"

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()
The use of pass under the class Child: is how you tell Python that you want an empty block. This creates a class named Child but says that there's nothing new to define in it. Instead it will inherit all of its behavior from Parent. When you run this code you get the following:

$ python ex44a.py
PARENT implicit()
PARENT implicit()
Notice how even though I'm calling son.implicit() on line 16, and even though Child does not have a implicit function defined, it still works and it calls the one defined in Parent. This shows you that, if you put functions in a base class (i.e., Parent) then all subclasses (i.e., Child) will automatically get those features. Very handy for repetitive code you need in many classes.

Override Explicitly

The problem with having functions called implicitly is sometimes you want the child to behave differently. In this case you want to override the function in the child, effectively replacing the functionality. To do this just define a function with the same name in Child. Here's an example:

 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
class Parent(object):

    def override(self):
        print "PARENT override()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

dad = Parent()
son = Child()

dad.override()
son.override()
In this example I have a function named override in both classes, so let's see what happens when you run it.

$ python ex44b.py
PARENT override()
CHILD override()
As you can see, when line 14 runs, it runs the Parent.override function because that variable (dad) is a Parent. But when line 15 runs it prints out the Child.override messages because son is an instance of Child and Child overrides that function by defining its own version.

Take a break right now and try playing with these two concepts before continuing.

Alter Before or After

The third way to use inheritance is a special case of overriding where you want to alter the behavior before or after the Parent class's version runs. You first override the function just like in the last example, but then you use a Python built-in function named super to get the Parent version to call. Here's the example of doing that so you can make sense of this description:

 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
class Parent(object):

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.altered()
son.altered()
The important lines here are 9-11, where in the Child I do the following when son.altered() is called:

Because I've overridden Parent.altered the Child.altered version runs, and line 9 executes like you'd expect.
In this case I want to do a before and after so after line 9, I want to use super to get the Parent.altered version.
On line 10 I call super(Child, self).altered(), which is aware of inheritance and will get the Parent class for you. You should be able to read this as "call super with arguments Child and self, then call the function altered on whatever it returns."
At this point, the Parent.altered version of the function runs, and that prints out the Parent message.
Finally, this returns from the Parent.altered and the Child.altered function continues to print out the after message.
If you run this, you should see this:

$ python ex44c.py
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()
All Three Combined

To demonstrate all of these, I have a final version that shows each kind of interaction from inheritance in one file:

 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
class Parent(object):

    def override(self):
        print "PARENT override()"

    def implicit(self):
        print "PARENT implicit()"

    def altered(self):
        print "PARENT altered()"

class Child(Parent):

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
Go through each line of this code, and write a comment explaining what that line does and whether it's an override or not. Then run it and confirm you get what you expected:

$ python ex44d.py
PARENT implicit()
PARENT implicit()
PARENT override()
CHILD override()
PARENT altered()
CHILD, BEFORE PARENT altered()
PARENT altered()
CHILD, AFTER PARENT altered()
The Reason for super()

This should seem like common sense, but then we get into trouble with a thing called multiple inheritance. Multiple inheritance is when you define a class that inherits from one or more classes, like this:

class SuperFun(Child, BadStuff):
    pass
This is like saying, "Make a class named SuperFun that inherits from the classes Child and BadStuff at the same time."

In this case, whenever you have implicit actions on any SuperFun instance, Python has to look-up the possible function in the class hierarchy for both Child and BadStuff, but it needs to do this in a consistent order. To do this Python uses "method resolution order" (MRO) and an algorithm called C3 to get it straight.

Because the MRO is complex and a well-defined algorithm is used, Python can't leave it to you to get the MRO right. Instead, Python gives you the super() function, which handles all of this for you in the places that you need the altering type of actions as I did in Child.altered. With super() you don't have to worry about getting this right, and Python will find the right function for you.

Using super() with __init__

The most common use of super() is actually in __init__ functions in base classes. This is usually the only place where you need to do some things in a child, then complete the initialization in the parent. Here's a quick example of doing that in the Child:

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        super(Child, self).__init__()
This is pretty much the same as the Child.altered example above, except I'm setting some variables in the __init__ before having the Parent initialize with its Parent.__init__.

Composition

Inheritance is useful, but another way to do the exact same thing is just to use other classes and modules, rather than rely on implicit inheritance. If you look at the three ways to exploit inheritance, two of the three involve writing new code to replace or alter functionality. This can easily be replicated by just calling functions in a module. Here's an example of doing this:

 1
 2
 3
 4
 5
 6
 7
 8
 9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"

son = Child()

son.implicit()
son.override()
son.altered()
In this code I'm not using the name Parent, since there is not a parent-child is-a relationship. This is a has-a relationship, where Child has-a Other that it uses to get its work done. When I run this I get the following output:

$ python ex44e.py
OTHER implicit()
CHILD override()
CHILD, BEFORE OTHER altered()
OTHER altered()
CHILD, AFTER OTHER altered()
You can see that most of the code in Child and Other is the same to accomplish the same thing. The only difference is that I had to define a Child.implicit function to do that one action. I could then ask myself if I need this Other to be a class, and could I just make it into a module named other.py?

When to Use Inheritance or Composition

The question of "inheritance versus composition" comes down to an attempt to solve the problem of reusable code. You don't want to have duplicated code all over your software, since that's not clean and efficient. Inheritance solves this problem by creating a mechanism for you to have implied features in base classes. Composition solves this by giving you modules and the ability to call functions in other classes.

If both solutions solve the problem of reuse, then which one is appropriate in which situations? The answer is incredibly subjective, but I'll give you my three guidelines for when to do which:

Avoid multiple inheritance at all costs, as it's too complex to be reliable. If you're stuck with it, then be prepared to know the class hierarchy and spend time finding where everything is coming from.
Use composition to package code into modules that are used in many different unrelated places and situations.
Use inheritance only when there are clearly related reusable pieces of code that fit under a single common concept or if you have to because of something you're using.
Do not be a slave to these rules. The thing to remember about object-oriented programming is that it is entirely a social convention programmers have created to package and share code. Because it's a social convention, but one that's codified in Python, you may be forced to avoid these rules because of the people you work with. In that case, find out how they use things and then just adapt to the situation.

Study Drills

There is only one Study Drill for this exercise because it is a big exercise. Go and read http://www.python.org/dev/peps/pep-0008/ and start trying to use it in your code. You'll notice that some of it is different from what you've been learning in this book, but now you should be able to understand their recommendations and use them in your own code. The rest of the code in this book may or may not follow these guidelines depending on if it makes the code more confusing. I suggest you also do this, as comprehension is more important than impressing everyone with you knowledge of esoteric style rules.