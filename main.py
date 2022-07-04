import sys
import subprocess

print(""" Problem Statement : Given the participants' score sheet for your University Sports Day,\nyou are required to find the runner-up score. You are given 'n' scores. \nStore them in a list and find the score of the runner-up.\n""")
print("The first line contains the value of n \nthe second line contains an array A[]\n")
print("""Sample input \n5\n2 3 6 6 5\n""")
print("Sample output \n5\n")




#Driver Code
print("Driver Code")
print("""if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())\n""")




print("Write Your Code Here\n")


lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
text = '\n'.join(lines)



file = open('submission.py', 'w')
file.write("""import sys , io 
old_stdout = sys.stdout
new_stdout = io.StringIO()
sys.stdout = new_stdout\n""")

file.write("\narr=[2,3,4,5,6,7,8,9,1]\n")
file.write(text)

file.write("""\noutput = new_stdout.getvalue()

sys.stdout = old_stdout

print("Output = ",output)

if ( int(output) == 8) :
    print("Congratulations !! , Your answer is correct")
else:
    print("Oopsie Daisy!! , Your answer is incorrect")""")

file.close()

cmd = 'python submission.py'
subprocess.Popen(cmd, shell = True)



