class File:
    def __init__(self, name, size, tab):
        self.name = name
        self.size = size
        self.tab = tab

    def __repr__(self):
        if self.size < 100000:
            return "  "*self.tab + "- {} (file, size={})\n".format(self.name, self.size)
        return "  "*self.tab + "- {} (file)\n".format(self.name)

    def get_size(self):
        return self.size


class Folder:
    def __init__(self, name, parent, tab):
        self.name = name
        self.dirs = {}
        self.files = {}
        self.parent = parent
        self.tab = tab
        self.size = None

    def __repr__(self):
        if self.get_size() < 100000:
            self_repr = "  "*self.tab + "- {} (dir, size={}) <==\n".format(self.name, self.get_size())
        else:
            self_repr = "  "*self.tab + "- {} (dir)\n".format(self.name)

        folder_repr = "".join(str(k) for k in self.dirs.values())
        file_repr = "".join(str(k) for k in self.files.values())
        return self_repr + folder_repr + file_repr

    def add_file(self, filename, file_obj):
        self.files[filename] = file_obj

    def add_dir(self, dirname, dir_obj):
        self.dirs[dirname] = dir_obj

    def dir_in(self, dirname):
        return dirname in self.dirs.values()

    def file_in(self, filename):
        return filename in self.files.values()
    
    def get_parent(self):
        return self.parent

    def get_dir(self, dirname):
        return self.dirs[dirname]

    def get_size(self, force=False):
        if self.size is None or force: # compute only if has not been computed yet
            self.size = sum([k.get_size() for k in self.files.values()] + [k.get_size() for k in self.dirs.values()])
        return self.size


all_folders = []
root = Folder("/", None, 0)
current_dir = None

all_folders.append(root)

with open("input7.txt") as file:
    lines = file.readlines()

for line in lines:
    line = line.replace("\n", "")
    tokens = line.split()
    if tokens[0] == "$":
        if tokens[1] == "cd":
            if tokens[2] == "/":
                current_dir = root # go to root dir
            elif tokens[2] == "..":
                current_dir = current_dir.get_parent() # go back once
            else:
                current_dir = current_dir.get_dir(tokens[2]) # go to the specified dir
                all_folders.append(current_dir) # update the all_folder dict
        # ls does nothing

    if tokens[0] == "dir":
        dir_name = tokens[1]
        if not current_dir.dir_in(dir_name):
            current_tab = current_dir.tab
            new_dir = Folder(dir_name, current_dir, current_tab+1)
            current_dir.add_dir(dir_name, new_dir)
    if tokens[0].isdigit():
        file_name = tokens[1]
        file_size = int(tokens[0])
        if not current_dir.file_in(file_name):
            current_tab = current_dir.tab
            new_file = File(file_name, file_size, current_tab+1)
            current_dir.add_file(file_name, new_file)
            

occupied_space = root.get_size() # recursively counts each folder size
remaining_space = 70000000 - occupied_space

list_potential_sizes = []
for folder in all_folders:
    folder_size = folder.get_size()
    if remaining_space + folder_size > 30000000:
        list_potential_sizes.append(folder_size)

print(min(list_potential_sizes))
