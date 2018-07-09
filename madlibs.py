def MadLibs():
  print("Welcome to MadLibs!")
  name = input("Please enter a name: ")
  noun = input("Please enter a noun: ")

  story = "{0} went for a walk in the park. {0} found a {1}. {0} decided 
to take it home".format(name, noun)

  return story

print(MadLibs())
