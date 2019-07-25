import subprocess
from time import sleep
import inspect
import os


#компиляция того  файла, из которого эта функция была вызвана
def compil_this_file():
    result = inspect.getouterframes(inspect.currentframe(), 2)
    input_file = str(result[1][1]).split('/')[-1].split('.')[0]#входной файл
    file_open=open(str(input_file)+".py")
    be_read=file_open.read()
    create_new_file=open(str(input_file)+".pyx","w+")
    create_new_file.write(be_read)

    setup_create=open("setup.py","w+")
    setup_create.write("from  distutils.core import setup\n")
    setup_create.write("from Cython.Build import cythonize\n")
    setup_create.write("setup(ext_modules=cythonize('"+str(input_file)+".pyx'))\n")

    sleep(2)
    command_1=subprocess.call(["python3", "setup.py","build_ext","--inplace"])
    command_2=subprocess.call(["cython","--embed","-o",str(input_file)+".cpp",str(input_file)+".py"])
    command_3=subprocess.call(["gcc","-Os","-I","/usr/include/python3.6m","-o",str(input_file),str(input_file)+".cpp","-lpython3.6m","-lpthread","-lm","-lutil","-ldl"])
    return input_file

#компиляция любого файла, который есть в папке
def compil_any_file():
    input_file = input("Введите имя файла без расширения:")
    file_open = open(str(input_file) + ".py")
    be_read = file_open.read()
    create_new_file = open(str(input_file) + ".pyx", "w+")
    create_new_file.write(be_read)

    setup_create = open("setup.py", "w+")
    setup_create.write("from  distutils.core import setup\n")
    setup_create.write("from Cython.Build import cythonize\n")
    setup_create.write("setup(ext_modules=cythonize('" + str(input_file) + ".pyx'))\n")

    sleep(2)
    command_1 = subprocess.call(["python3", "setup.py", "build_ext", "--inplace"])
    command_2 = subprocess.call(["cython", "--embed", "-o", str(input_file) + ".cpp", str(input_file) + ".py"])
    command_3 = subprocess.call(
        ["gcc", "-Os", "-I", "/usr/include/python3.6m", "-o", str(input_file), str(input_file) + ".cpp", "-lpython3.6m",
         "-lpthread", "-lm", "-lutil", "-ldl"])
    return input_file


#удаление ненужных файлов и оставление только исходника
# данную функцию вызывать не стоит, т.к внизу всё автоматизировано
def delete(input_file):
    try:
        for filename in os.listdir("."):
            os.remove('setup.py')
            os.remove(str(input_file)+'.pyx')
            os.remove(str(input_file)+'.cpp')

    except FileNotFoundError:
        pass
    except TypeError:
        print('Эту функцию вызывать не нужно')

# формирование только исходника для этого файла,т.е для файла, где была вызвана эта функция
def source_this_file():
    delete(compil_this_file())


#формирование только исходника для любого файла
def source_any_file():
    delete(compil_any_file())
