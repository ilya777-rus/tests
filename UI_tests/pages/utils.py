import logging


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Установите уровень логирования

# Формат сообщений
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

# Обработчик для вывода в консоль
console_handler = logging.StreamHandler()
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.INFO)  # Установите уровень для консольного вывода

# Обработчик для записи в файл
file_handler = logging.FileHandler('app.log', encoding='utf-8')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)  # Установите уровень для записи в файл

# Добавляем обработчики к логгеру
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def log_message(message, level = 'info'):
    levels = {
        'debug': logger.debug,
        'info': logger.info,
        'warning': logger.warning,
        'error': logger.error,
        'critical': logger.critical
    }
    log_func = levels.get(level, logger.info)
    log_func(message)