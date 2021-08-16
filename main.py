import subprocess


def tt():
    print('tt')


def run(*args):

    return subprocess.check_call(['git'] + list(args))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    run("add", "--all",)
    run("commit", "-m", 'ttt commit')
    run("push", "-u", "origin", "master")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
