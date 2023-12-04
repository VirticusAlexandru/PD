import os
import shutil

# Путь к исходному датасету
source_directory = "D:\\UTM\\PD\\PD_git_lab\\lab_2\\dataset"
# Путь к целевой директории
target_directory = "D:\\UTM\\PD\\PD_git_lab\\lab_3\\dataset3"

# Создайте список классов
classes = ["zebra"]

# Функция для создания файла аннотации
def create_annotation_file(class_name, original_filename, target_filename):
    annotation_file = os.path.join(target_directory, f"{class_name}.csv")
    with open(annotation_file, "a") as f:
        f.write(f"{original_filename} {target_filename}\n")

# Пройдем по всем классам
for class_name in classes:
    class_source_directory = os.path.join(source_directory, class_name)
    
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    file_list = os.listdir(class_source_directory)
    for i, filename in enumerate(file_list):
        if filename.endswith(".jpg"):
            original_file_path = os.path.join(class_source_directory, filename)
            new_file_name = f"{class_name}_{i:04d}.jpg"
            target_file_path = os.path.join(target_directory, new_file_name)

            shutil.copy(original_file_path, target_file_path)
            create_annotation_file(class_name, original_file_path, new_file_name)
