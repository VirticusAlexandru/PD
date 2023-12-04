import os
import random

def get_next_instance(class_label, dataset_path):
    class_files = [f for f in os.listdir(dataset_path) if f.startswith(class_label)]
    if class_files:
        random.shuffle(class_files)
        return os.path.join(dataset_path, class_files.pop())
    else:
        return None


# Пример использования функции
next_instance = get_next_instance('zebra', "D:\\UTM\\PD\\PD_git_lab\\lab_3\\dataset3")
print(f'Следующий экземпляр класса zebra: {next_instance}')
