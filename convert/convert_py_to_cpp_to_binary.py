import subprocess
from time import sleep
input_file=input("Введите имя файла без расширения:")

def create_pyx_and_setup():
    file_open=open(str(input_file)+".py")
    be_read=file_open.read()
    create_new_file=open(str(input_file)+".pyx","w+")
    create_new_file.write(be_read)

    setup_create=open("setup.py","w+")
    setup_create.write("from  distutils.core import setup\n")
    setup_create.write("from Cython.Build import cythonize\n")
    setup_create.write("setup(ext_modules=cythonize('"+str(input_file)+".pyx'))\n")

def terminal():
    sleep(3)
    command_1=subprocess.call(["python3", "setup.py","build_ext","--inplace"])
    command_2=subprocess.call(["cython","--embed","-o",str(input_file)+".cpp",str(input_file)+".py"])
    command_3=subprocess.call(["gcc","-Os","-I","/usr/include/python3.6m","-o",str(input_file),str(input_file)+".cpp","-lpython3.6m","-lpthread","-lm","-lutil","-ldl"])



if __name__=="__main__":
    create_pyx_and_setup()
    terminal()
