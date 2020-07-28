import os

############
def createLoggerFile(config):
    #filename from config file
    filename = config.get('filenameLogger','folderPATH')+config.get('filenameLogger','filename')

    # create indented filename
    i = 0
    while os.path.exists(filename+"%s.txt" % format(i, '02d')):
        i += 1
    filename=filename+"%s.txt" % format(i, '02d')

    #create repository if not exist
    if not os.path.exists(os.path.dirname(filename)):
        try:
            os.makedirs(os.path.dirname(filename))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    #create recording file
    print("Logger file name: "+config.get('filenameLogger','filename')+"%s.txt" % format(i, '02d'))
    fh = open(filename, "w")
    fh.write(config.get('filenameLogger','firstLine'))
    
    return fh
