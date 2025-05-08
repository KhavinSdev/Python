#!/usr/bin/env python
# coding: utf-8

# In[27]:


def SortFilesavKeyword(source, destination):
    '''
    source path, destination path both in strings. New folders will be created for organisational purposes?
    for windows, path in this manner for ex: C:\\users\\usernamen\\Diruno\\Dir2\\ ... in windows. For other OS
    refer to os module documentation for correct path formats..
    '''

    import os
    import os.path
    import shutil
    
    os.chdir(source)

    try:
        os.mkdir(destination + '\\' + 'PDF')
        os.mkdir(destination + '\\' + 'videos')
        os.mkdir(destination + '\\' + 'images')
        os.mkdir(destination + '\\' + 'audio')
        os.mkdir(destination + '\\' + 'WordDocs')
        os.mkdir(destination + '\\' + 'Pythonscripts')
    finally:    
        filetype = input("Choose a file type( python, pdf, video, image, audio, docx): ") 
        search = input('Type a search key or phrase(please use lower cased letters) or leave blank for all files: ')
        if search == '':
            search = '.'
        
        filetopath = {
            'pdf' : "PDF",
            'video': "videos",
            'image': "images",
            'audio': "audio",
            'docx': "WordDocs",
            'python' : "PythonScripts"
        }
        
        filetoextension = {
            'pdf' : '.pdf',
            'video' : ['.mp4', '.MPEG-4', '.mov'],
            'image' : ['.jpg', '.jpeg', '.png'],
            'audio': ['.mp3', '.wav'],
            'docx': '.docx',
            'python' : '.py'
        }
        
        #print(filetoextension[filetype])
        
        for i in os.listdir():
            x,y = (os.path.splitext(i))
        
            if y in filetoextension[filetype] and search in i.lower():
                #print(i)
                shutil.copy(i, destination + '\\' + filetopath[filetype])
            else:
                continue
        
        print('Files copied') 

if __name__ == '__main__':

    source = input('Enter the path of your source folder: ')
    destination = input('Enter the path of you destination folder: ')
    SortFilesavKeyword(source, destination)
    


# In[ ]:




