import os

dir = os.getcwd()
print(dir)

#os.chdir('g:/python-project/pythonLearn/package-manager/pkg01')
dir = os.getcwd()
print(dir)

ld = os.listdir()
print(ld)

print(os.curdir)
print(os.pardir,os.sep,os.name)

if not os.path.exists('g:/python-project/pythonLearn/package-manager/danan'):

    pst = os.mkdir('danan')

rst = os.getenv('PATH')
print(rst)
