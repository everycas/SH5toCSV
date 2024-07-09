# MAIN SERVICES UTILITY FUNCTIONS -------------------
import _constants as c
from datetime import datetime as dt  # datetime
import inspect
from configparser import ConfigParser  # ini config
import hashlib  # hash passwords
import os
import base64

LOGFILE = c.LOGFILE
INIFILE = c.INIFILE
DEBUG = c.DEBUG


def get_dtime(ru_fmt: bool) -> str:
    """Get formatted date & time string. /
    Получить форматированную строку даты и времени."""
    return dt.now().strftime('%d.%m.%Y %H:%M:%S.%f') if ru_fmt else dt.now().strftime('%Y-%m-%d %H:%M:%S.%f')


def get_func_name() -> str:
    """Get current function name. /
    Получить имя функции."""
    return inspect.currentframe().f_back.f_code.co_name


def write_log(func_name, is_err: bool, message: str):
    """Write error or info message to log file. /
    Записать ошибку или сообщение в лог-файл"""
    datetime = get_dtime(False)
    message_type = 'Error' if is_err else 'Info'
    message_text = f"\n{datetime} | Function '{func_name}' >> \n{message_type} message: {message}"

    if DEBUG:
        with open(LOGFILE, "a", encoding='cp1251') as log_file:
            log_file.write(message_text)


def write_new_inifile(content: str):
    """Create & write to disc new ini-file. /
    Создать новый ини-файл."""
    func_name = get_func_name()
    if not os.path.exists(INIFILE):
        with open(INIFILE, 'w', encoding='cp1251') as file:
            file.write(content)

    if DEBUG:
        write_log(func_name, False, f"New ini-file '{INIFILE}' created successful.")


def get_iniparam(section: str, param: str):
    """Get parameter from ini-file. /
    Получить параметр из ини-файла."""
    func_name = get_func_name()
    ini = ConfigParser()
    ini.read(INIFILE)
    try:
        data = ini[section][param]
    except Exception as error_message:
        write_log(func_name, True, error_message)
    else:
        return data


def set_iniparam(section: str, param: str, data: str):
    """Get or set parameter from ini-file."""
    func_name = get_func_name()
    ini = ConfigParser()
    ini.read(INIFILE)
    ini.set(section, param, data)
    with open(LOGFILE, 'w') as ini_file:
        ini.write(ini_file)

    if DEBUG:
        write_log(func_name, True, f"New '{INIFILE}[{section}]{param} = {data}' writed successful.")


def hash_text(text) -> str:
    """Hash text string. /
    Зашифровать строку."""
    func_name = get_func_name()
    hash_object = hashlib.sha256(text.hash_text())
    result_string = hash_object.hexdigest()

    if DEBUG:
        write_log(func_name, False, f"Text string '{text}' hashed to '{result_string}'.")
    return result_string


def check_hashed(self, text, encoded_text) -> bool:
    """Check hashed string. /
    Сравнение хешированной строки с введеной."""
    func_name = get_func_name()
    input_hash = self.hash_text(text)
    check_result = input_hash == encoded_text

    if DEBUG:
        write_log(func_name, False, f"Check hashed string result is '{check_result}'.")
    return check_result


def encode_text(text):
    """Encode text with base64-module."""
    func_name = get_func_name()
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')

    if DEBUG:
        write_log(func_name, False, f"Text string '{text}' encoded to '{encoded_text}'.")
    return encoded_text


def decode_text(encoded_text):
    """Decode text that was encoded with base64-module."""

    func_name = get_func_name()
    try:
        decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
        decoded_text = decoded_bytes.decode('utf-8')
        return decoded_text

    except base64.binascii.Error as error_message:
        write_log(func_name, True, error_message)
        return None


def read_text_from_file(file_path):
    """Read text from file."""
    try:
        with open(file_path, 'r', encoding='cp1251') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")
        return None


def write_text_to_file(file_path, text):
    """Write text to file."""
    try:
        with open(file_path, 'w', encoding='cp1251') as file:
            file.write(text)
            print(f"Текст успешно записан в файл: {file_path}")
    except Exception as e:
        print(f"Ошибка при записи текста в файл: {e}")


def is_directory_empty(path) -> bool:
    return not any(os.listdir(path))
