# Enter name as variable and use title, lower, and upper methods

name = "thomas Abraham"

print("Hello, " + name + " this is a test in Python.")

print(name.title())
print(name.upper())
print(name.lower())
# create a variable famousQuote print it with quotation marks displaying
famousQuote = 'Nelson Mandela once said, "The greatest glory in living lies not in never falling,' \
              ' but in rising every time we fall."'

print(famousQuote)
# Create a variable for both famous person and famous quote print with quotation marks
famousPerson = "Nelson Mandela"
message = '"The greatest glory in living lies not in never falling,' \
          ' but in rising every time we fall."'

print(famousPerson + " once said, " + message)
# Display strip functionality
stripName = ' \tSteve \n\tBallmer'
print(stripName.rstrip())
print(stripName.lstrip())
print(stripName.strip())
