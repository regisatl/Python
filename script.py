class Hello():
      def __init__(self, name):
                  self.name = name
                  self.hello()
      def hello(self):
                  print("Hello", self.name, "!")
ted = Hello("Ted")