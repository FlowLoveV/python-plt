RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RESET = '\033[0m'


def printErrors(msg: str):
    print(RED + msg + RED)
    print(RESET + RESET)


def printSuccess(msg: str):
    print(GREEN + msg + GREEN)
    print(RESET + RESET)


def printWarnning(msg: str):
    print(YELLOW + msg + YELLOW)
    print(RESET + RESET)
