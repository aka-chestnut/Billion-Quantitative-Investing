import os
if __name__ == '__main__':
    os.system('chcp 65001')
    from PyInstaller.__main__ import run
    opts=[r'C:\Users\Administrator\PycharmProjects\untitled\a.py','-w',r'--icon=C:\Users\Administrator\PycharmProjects\untitled\mainicon.ico']
    run(opts)
