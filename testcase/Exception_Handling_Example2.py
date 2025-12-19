

print("start of code")
print("code is started")

try:
    print(10/0)

except ZeroDivisionError:
    print("exception @ZeroDivisionError is handled")
except SyntaxError:
    print("exception @SyntaxError is handled")

else: #else not execute if there is exception
   print("no exception occured in @else block")

finally: #finally keyword is added at last to execute coding. exception occur or not finally block will execute
    print("Close the browser @finally block")