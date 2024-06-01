import matplotlib

def standard_setup():
    matplotlib.rc('figure', figsize=(14, 6))
    matplotlib.rc('font', size = 16)
    matplotlib.rcParams['axes.spines.right'] = False
    matplotlib.rcParams['axes.spines.top'] = False
    return

# if __name__ == '__main__':
#     print('aapjes')