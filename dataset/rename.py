import os
import glob


def rename(alcohol, name):
    root_path = 'C:\\Users\\IBK\\Documents\\kyx\\elice\\aiproject\\crawl\\train'

    for i, f in enumerate(alcohol):
        os.rename(f, os.path.join(
            root_path+'\\{0}'.format(name), '{0}__'.format(name)+'{0:03d}.jpg'.format(i)))
    a = glob.glob((root_path+'\\{}'+'\\*').format(name))
    print('성공')


root_path = 'C:\\Users\\IBK\\Documents\\kyx\\elice\\aiproject\\crawl\\train'

al_list = ['mudshake']
for i in al_list:
    a = glob.glob((root_path+'\\{}'+'\\*').format(i))
    rename(a, i)
