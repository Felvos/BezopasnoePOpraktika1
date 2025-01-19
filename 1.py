import os
import os
import json
import xml.etree.ElementTree as ET
import zipfile

def list_files(directory):
    try:
        print(f"Поиск файлов в директории: {directory}")  
        files = [
            f for f in os.listdir(directory) 
            if os.path.isfile(os.path.join(directory, f)) 
            and not f.endswith('.zip') 
            and f != '.DS_Store'  # исключаем .DS_Store
        ] 
        if not files:
            print("В данной директории нет файлов")
        return files
    except Exception as e:
        print(f"Ошибка доступа {directory}: {e}")
        return []

def write_to_file(file_path, content):
    """Запись содержимого в .txt файл."""
    with open(file_path, 'w') as f:
        f.write(content)
    print(f"Файл успешно создан и данные записаны: {content}")

def read_file(file_path):
    """Чтение содержимого .txt файла."""
    try:
        with open(file_path, 'r') as f:
            content = f.read()
        print(f"Содержимое файла:\n{content}")
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except Exception as e:
        print(f"Ошибка чтения файла: {e}")

def delete_file(file_path):
    """Удаление файла."""
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Файл успешно удалён: {file_path}")
    else:
        print("Файл не существует.")

def create_json(file_path, data):
    """Создание JSON файла с данными."""
    with open(file_path, 'w') as json_file:
        json.dump(data, json_file)
    print(f"JSON файл успешно создан: {file_path}")

def read_json(file_path):
    """Чтение JSON файла."""
    try:
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        print(f"Содержимое JSON файла:\n{data}")
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except json.JSONDecodeError:
        print("Ошибка декодирования JSON.")
    except Exception as e:
        print(f"Ошибка чтения JSON файла: {e}")

def delete_json(file_path):
    """Удаление JSON файла."""
    delete_file(file_path)

def create_xml(file_path, data):
    """Создание XML файла с данными."""
    root = ET.Element("root")
    data_element = ET.SubElement(root, "data")
    data_element.text = data
    tree = ET.ElementTree(root)
    tree.write(file_path)
    print(f"XML файл успешно создан: {file_path}")

def read_xml(file_path):
    """Чтение XML файла."""
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        data = root.find("data").text
        print(f"Содержимое XML файла:\n{data}")
    except FileNotFoundError:
        print(f"Файл не найден: {file_path}")
    except ET.ParseError:
        print("Ошибка парсинга XML.")
    except Exception as e:
        print(f"Ошибка чтения XML файла: {e}")

def delete_xml(file_path):
    """Удаление XML файла."""
    delete_file(file_path)

def create_zip(zip_path, file_paths):
    """Создание zip-архива, содержащего указанные файлы."""
    try:
        with zipfile.ZipFile(zip_path, 'a') as zipf:
            for file_path in file_paths:
                zipf.write(file_path, os.path.basename(file_path))
                print(f"Файл {file_path} успешно добавлен в zip-архив: {zip_path}")
                os.remove(file_path)  # Удалить оригинальные файлы после архивирования
    except Exception as e:
        print(f"Ошибка создания zip-архива: {e}")

def unzip(zip_path, extract_path):
    """Разархивирование zip-файла в указанную директорию."""
    try:
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print(f"Содержимое архива разархивировано: {zip_path}")
        os.remove(zip_path)  # Удалить zip-файл после разархивирования
    except FileNotFoundError:
        print(f"Архив не найден: {zip_path}")
    except zipfile.BadZipFile:
        print("Ошибка: Некорректный zip-файл.")
    except Exception as e:
        print(f"Ошибка разархивирования: {e}")

def main():
    directory = "/Users/User/Desktop/Безопасное ПО"
    
    while True:
        print("\nДействия:")
        print("1) Список файлов")
        print("2) Написать .txt")
        print("3) Прочитать .txt")
        print("4) Удалить .txt")
        print("5) Создать .json")
        print("6) Прочитать .json")
        print("7) Удалить .json")
        print("8) Создать .xml")
        print("9) Прочитать .xml")
        print("10) Удалить .xml")
        print("11) Заархивировать в .zip")
        print("12) Разархивировать")
        print("13) Завершить работу программы")
        
        choice = input("Выберите действие (1-13): ")
        
        if choice == '1':
            print("--------Чтение файлов--------")  
            files = list_files(directory)
            if files:
                print("Найденные файлы:")
                for i, file in enumerate(files, start=1):
                    print(f"{i}. {file}")
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '2':
            print("--------Написание .txt--------") 
            filename = input("Введите название файла: ")
            content = input("Введите содержимое файла: ")
            write_to_file(os.path.join(directory, f"{filename}.txt"), content)
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '3':
            filename = input("Введите название файла (без расширения): ")
            read_file(os.path.join(directory, f"{filename}.txt"))
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '4':
            filename = input("Введите название файла (без расширения): ")
            delete_file(os.path.join(directory, f"{filename}.txt"))
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '5':
            filename = input("Введите название файла (без расширения): ")
            data = {"name": "John Doe", "age": 30, "email": "john.doe@example.com"}
            create_json(os.path.join(directory, f"{filename}.json"), data)
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '6':
            filename = input("Введите название файла (без расширения): ")
            read_json(os.path.join(directory, f"{filename}.json"))
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '7':
            filename = input("Введите название файла (без расширения): ")
            delete_json(os.path.join(directory, f"{filename}.json"))
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '8':
            filename = input("Введите название файла (без расширения): ")
            data = input("Введите содержимое для XML: ")
            create_xml(os.path.join(directory, f"{filename}.xml"), data)
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '9':
            filename = input("Введите название файла (без расширения): ")
            read_xml(os.path.join(directory, f"{filename}.xml"))
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '10':
            filename = input("Введите название файла (без расширения): ")
            delete_xml(os.path.join(directory, f"{filename}.xml"))
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '11':
            zip_filename = input("Введите название zip-файла (без расширения): ")
            print("Выберите файлы для записи в zip (введите номера через пробел):")
            files_to_zip = list_files(directory)
            if not files_to_zip:
                print("Нет доступных файлов для zip.")
                input("Нажмите enter чтобы вернуться в меню...")
                continue
            for i, file in enumerate(files_to_zip, start=1):
                print(f"{i}. {file}")
            selected_files = input("Введите ваш выбор: ")
            selected_indices = map(int, selected_files.split())
            file_paths = [os.path.join(directory, files_to_zip[i-1]) for i in selected_indices if 1 <= i <= len(files_to_zip)]
            create_zip(os.path.join(directory, f"{zip_filename}.zip"), file_paths)
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '12':
            input("--------Разархивирование--------")
            zip_filename = input("Введите название разархивируемого файла: ")
            unzip(os.path.join(directory, f"{zip_filename}.zip"), directory)
            input("--------Нажмите enter для продолжения--------")
            
        elif choice == '13':
            input("--------Завершение работы программы--------")
            break
            
        else:
            print("Выбранного действия не существует.")
            input("--------Нажмите enter для продолжения--------")

if __name__ == "__main__":
    main()
