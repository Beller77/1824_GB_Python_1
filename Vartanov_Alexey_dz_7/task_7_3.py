from os.path import exists, join
from os import walk, listdir, path, mkdir
from shutil import copyfile

work_dir = 'my_project'
dir_templates = 'templates'
if not path.exists(join(work_dir, dir_templates)):
    mkdir(join(work_dir, dir_templates))

list_obj_in_folder = []
for root, dirs, files in walk(work_dir):
    search_folder = "templates"
    if search_folder in root and not root.endswith(search_folder)\
            and not join(work_dir, dir_templates) in root:
        list_obj_in_folder = listdir(root)
        folder_name = path.split(path.abspath(root))[1]
        create_folder = join(work_dir, dir_templates, folder_name)
        if not path.exists(create_folder):
            mkdir(create_folder)
        for file in list_obj_in_folder:
            src_full_path = join(path.abspath(root), file)
            copyfile(src_full_path, join(create_folder, file))
