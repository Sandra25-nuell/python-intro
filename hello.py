try:
    from colorama import Fore, Style, init
    init()  # needed on Windows
    print(Fore.GREEN + 'SUCCESS: colorama is installed!')
    print(Fore.YELLOW + 'WARNING: This is a yellow warning.')
    print(Fore.RED + 'ERROR: This is a red error message.')
    print(Style.RESET_ALL + 'Back to normal text.')
except ImportError:
    print('colorama not installed. Run: pip install colorama')
    print('Without colorama, output shows without color.')

    