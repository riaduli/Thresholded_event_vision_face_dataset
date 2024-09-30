import os

def create_txt_file(folder_path, file_name):
    with open(os.path.join(folder_path, file_name), 'w') as file:
        for root, dirs, files in os.walk(folder_path):
            for filename in files:
                if filename.endswith('.png'):
                    relative_path = os.path.relpath(os.path.join(root, filename), folder_path)
                    file.write(os.path.join(folder_path, relative_path) + '\n')

def main():
    base_path = os.getcwd()  # Get the current working directory
    threshold_folders = ['threshold_4','threshold_8','threshold_12','threshold_16']
    data_folders = ['train','valid','test']
    
    for threshold_folder in threshold_folders:
        for data_folder in data_folders:
            folder_path = os.path.join(base_path, threshold_folder, data_folder)
            txt_file_name = f'{data_folder}.txt'
            create_txt_file(folder_path, txt_file_name)
            print(f'{txt_file_name} created for {folder_path}')

if __name__ == "__main__":
    main()
