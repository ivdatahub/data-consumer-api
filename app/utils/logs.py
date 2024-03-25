import logging

# Configurar o logger
logging.basicConfig(
    level=logging.CRITICAL,  # Defina o nível globalmente como CRITICAL
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'  # Formato da data e hora
)

# Criar um logger para cada nível desejado
logger_error = logging.getLogger('error_logger')
logger_warn = logging.getLogger('warn_logger')
logger_info = logging.getLogger('info_logger')

# Configurar os níveis desejados para cada logger
logger_error.setLevel(logging.ERROR)
logger_warn.setLevel(logging.WARNING)
logger_info.setLevel(logging.INFO)


def ConsoleInfo(msg):
    return logger_info.info(msg)

def ConsoleError(msg):
    return logger_error.error(msg)

def ConsoleWarning(msg):
    return logger_warn.warning(msg)

