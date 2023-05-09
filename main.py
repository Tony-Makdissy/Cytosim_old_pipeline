# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import cytosim

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# how to run the preconfig!
# python3 preconfig.py dummy_code.cym.tpl

#how to run the simulations
# python3 go_sim.py sim dummy_code*.cym njobs=6

#how to analyze the results
# python3 scan.py 'python3 ../random_analysis_code.py' run00* njobs=6


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

#https://www.geeksforgeeks.org/reading-writing-text-files-python/