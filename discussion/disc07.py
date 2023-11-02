class Email:
    """
    Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    >>> email = Email('hello', 'Alice', 'Bob')
    >>> email.msg
    'hello'
    >>> email.sender_name
    'Alice'
    >>> email.recipient_name
    'Bob'
    """
    def __init__(self, msg, sender_name, recipient_name):
        "*** YOUR CODE HERE ***"
        self.msg = msg
        self.sender_name = sender_name
        self.recipient_name = recipient_name

class Server:
    """
    Each Server has one instance attribute: clients (which
    is a dictionary that associates client names with
    client objects).
    """
    def __init__(self):
        self.clients = {}

    def send(self, email):
        """
        Take an email and put it in the inbox of the client
        it is addressed to.
        """
        "*** YOUR CODE HERE ***"
        self.client[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """
        Takes a client object and client_name and adds them
        to the clients instance attribute.
        """
        "*** YOUR CODE HERE ***"
        self.clients[client_name] = client

class Client:
    """
    Every Client has three instance attributes: name (which is
    used for addressing emails to the client), server
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).

    >>> s = Server()
    >>> a = Client(s, 'Alice')
    >>> b = Client(s, 'Bob')
    >>> a.compose('Hello, World!', 'Bob')
    >>> b.inbox[0].msg
    'Hello, World!'
    >>> a.compose('CS 61A Rocks!', 'Bob')
    >>> len(b.inbox)
    2
    >>> b.inbox[1].msg
    'CS 61A Rocks!'
    """
    def __init__(self, server, name):
        self.inbox = []
        "*** YOUR CODE HERE ***"
        self.name = name
        self.server = server
        self.server.register_client(self, self.name)

    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the given recipient client."""
        "*** YOUR CODE HERE ***"
        self.server.clients[recipient_name].receive(Email(msg, self.name, recipient_name))


    def receive(self, email):
        """Take an email and add it to the inbox of this client."""
        "*** YOUR CODE HERE ***"
        self.inbox += [email]

# Q3

class Button:
    def __init__(self, pos, key):
        self.pos = pos
        self.key = key
        self.times_pressed = 0

class Keyboard:
    """A Keyboard stores an arbitrary number of Buttons in a dictionary. 
    Each dictionary key is a Button's position, and each dictionary
    value is the corresponding Button.
    >>> b1, b2 = Button(5, "H"), Button(7, "I")
    >>> k = Keyboard(b1, b2)
    >>> k.buttons[5].key
    'H'
    >>> k.press(7)
    'I'
    >>> k.press(0) # No button at this position
    ''
    >>> k.typing([5, 7])
    'HI'
    >>> k.typing([7, 5])
    'IH'
    >>> b1.times_pressed
    2
    >>> b2.times_pressed
    3
    """
    def __init__(self, *args):
        self.buttons = {}
        for button in args:
            self.buttons[button.pos] = button

    def press(self, pos):
        """Takes in a position of the button pressed, and
        returns that button's output."""
        if self.buttons.get(pos):
            self.buttons.get(pos).times_pressed += 1
            return self.buttons.get(pos).key
        return ''
    
    def typing(self, typing_input):
        """Takes in a list of positions of buttons pressed, and
        returns the total output."""
        word = ''
        for position in typing_input:
            word += self.press(position)
        return word

# Q4

class Butterfly():
    def __init__(self, wings=2):
        self.wings = wings

class Monarch(Butterfly):
    def __init__(self):
        super().__init__()
        self.colors = ['orange', 'black', 'white']

class MimicButterfly(Butterfly):
    def __init__(self, mimic_animal):
        super().__init__()
        self.mimic_animal = mimic_animal

# Q5

class Pet():

    def __init__(self, name, owner):
        self.is_alive = True    # It's alive!!!
        self.name = name
        self.owner = owner

    def eat(self, thing):
        print(self.name + " ate a " + str(thing) + "!")

    def talk(self):
        print(self.name)

class Cat(Pet):

    def __init__(self, name, owner, lives=9):
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner)
        self.lives = lives

    def __repr__(self):
        "*** YOUR CODE HERE ***"
        return f'{self.name}, {self.lives} lives' # f is needed for that
    
    def __str__(self):
        "*** YOUR CODE HERE ***"
        return self.name

    def talk(self):
        """Print out a cat's greeting.
        >>> Cat('Thomas', 'Tammy').talk()
        Thomas says meow!
        """
        "*** YOUR CODE HERE ***"
        print(self.name + ' says meow!')

    def lose_life(self):
        """Decrements a cat's life by 1. When lives reaches zero,
        is_alive becomes False. If this is called after lives has
        reached zero, print 'This cat has no more lives to lose.'
        """
        "*** YOUR CODE HERE ***"
        if self.lives == 0:
            self.is_alive = False
            print('This cat has no more lives to lose.')
        else:
            self.lives -= 1

    def revive(self):
        """Revives a cat from the dead. The cat should now have 
        9 lives and is_alive should be true. Can only be called
        on a cat that is dead. If the cat isn't dead, print 
        'This cat still has lives to lose.'
        """
        if not self.is_alive:
            self.lives = 9
            self.is_alive = True
        else:
            print('This cat still has lives to lose.')

# Q6

class NoisyCat(Cat): # Fill me in!
    """A Cat that repeats things twice."""

    def __init__(self, name, owner, lives=9):
        # Is this method necessary? Why or why not?
        # Not because no need to override __init__ method since there are no new attributes, or rather no new parameters 
        # because you could always just write it in the class itself if it's constant
        "*** YOUR CODE HERE ***"
        super().__init__(name, owner, lives)

    def talk(self):
        """Talks twice as much as a regular cat.
        >>> NoisyCat('Magic', 'James').talk()
        Magic says meow!
        Magic says meow!
        """
        "*** YOUR CODE HERE ***"
        print(self.name + ' says meow!')
        print(self.name + ' says meow!')

# Q7

# (The rest of the Cat class is omitted here, but assume all methods from the Cat class above are implemented)
   

