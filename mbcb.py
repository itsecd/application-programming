import argparse
import re


def get_smt_from_cmd() -> str:
    """ 
    получает из командной строки: название файла и имя для подсчета
    """
    parser = argparse.ArgumentParser() 
    parser.add_argument('filename', type=str, help='file that needs to open')
    parser.add_argument('humanname', type=str, help='name for find how many people same have it')
    return parser.parse_args()


def read(filename: str) -> str:
    """
     считывает файл
     :param filename: имя исх. файла
    :return: строку со всеми данными из считываемого файла
    """
    try:
        with open(filename, "r", encoding="utf-8") as file:
            text = file.read()
        return text
    except FileNotFoundError as erorrreading:
        raise FileNotFoundError(f"Ошибка: файл с именем '{filename}'  не найден : {erorrreading}")


def define_count(text: str, humanname:str) -> None:
    print(text.count(humanname))
    

def main():
    """
    """
    try:
        arguments = get_smt_from_cmd()
        txt = read(arguments.filename)
        define_count(txt, arguments.humanname)
    except Exception as erorr:
        print(f"Произошла ошибка: {erorr}")

if __name__ == "__main__":
    main()