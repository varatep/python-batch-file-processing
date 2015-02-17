import os

def renameFiles(path, basefilename, depth=1):
    # hit depth; return; (base case)
    if depth < 0: return
	
    # ensure !(symbolic link);
    if os.path.isdir(path) and not os.path.islink(path):
        ind = 1

        # for every file, create full path;
        for file in os.listdir(path):
            fullpath = path + os.path.sep + file

            # check symbolic link;
            if not os.path.islink(fullpath):

                # check for directory recursion;
                if os.path.isdir(fullpath):
                    renameFiles(fullpath, basefilename, depth - 1)
                else:
                    # Find the extension (if available) and rebuild file name 
                    # using the directory, new base filename, index and the old extension.
                    extension = os.path.splitext(fullpath)[1]
                    os.rename(fullpath, os.path.dirname(fullpath) + os.path.sep + basefilename + "_" + str(ind) + extension)
                    ind += 1
    return

