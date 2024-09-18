#!/usr/bin/env python
# coding: utf-8

# In[4]:


def SortFilessaKeyword(source, destination):

    import os
    import os.path
    import shutil
    # import time

    os.chdir(source)


    # filetype = input("Choose a file type( pyfile, pdf, video, image, audio, worddoc): ") 
    # search = input('Type a search key or phrase(please use lower cased letters) or leave blank for all files: ')
    # if search == '':
    #     search = '.'


    filetopath = {
        'pdf' : "PDF",
        'video': "videos",
        'image': "images",
        'audio': "audi",
        'worddoc': "WordDocz",
        'pyfile' : "Pythonscript"
    }

    filetoextension = {
        'pdf' : '.pdf',
        'video' : ['.mp4', '.MPEG-4', '.mov'],
        'image' : ['.jpg', '.jpeg', '.png'],
        'audio': ['.mp3', '.wav'],
        'worddoc': '.docx',
        'pyfile' : '.py'
    }

    try:
        os.mkdir(destination + '\\' + 'PDF')
        os.mkdir(destination + '\\' + 'videos')
        os.mkdir(destination + '\\' + 'images')
        os.mkdir(destination + '\\' + 'audi')
        os.mkdir(destination + '\\' + 'WordDocz')
        os.mkdir(destination + '\\' + 'Pythonscript')
    finally:


        #print(filetoextension[filetype])

        lidr = os.listdir()

        for filetype in ['pyfile', 'pdf', 'video', 'image', 'audio', 'worddoc']:


            for i in lidr:
                x,y = (os.path.splitext(i))

                if y in filetoextension[filetype] and y != '':
                    #print(i)
                    shutil.copy(i, destination + '\\' + filetopath[filetype])
                    # time.sleep(4)

                else:
                    pass


        print('Files copied') 
                    

if __name__ == '__main__':
    SortFilessaKeyword('C:\\Users\\senth\\Downloads', 'C:\\Users\\senth\\Documents\\SortedDownloads')


# In[ ]:




