'''
import sys -> any exception basically getting control sys library will automatically have that information.
in this contain custom exception for our entire project
'''
import sys
from MlProjects.src.logger import logging


def error_message_detail(error, error_details: sys):

    # exc_tb include what is the line error that occur which file, which line like that
    _, _, exc_tb = error_details.exc_info()

    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occur in python script name [{0}] line number [{1}] error message [{2}]".format(
        file_name, exc_tb.tb_lineno, str(error)
    )
    return error_message


class CustomException(Exception):
    def __init__(self, error_message, error_details: sys) -> None:
        super().__init__(error_message)
        self.error_message = error_message_detail(
            error_message, error_details=error_details)

    def __str__(self) -> str:
        return self.error_message


if __name__ == "__main__":

    try:
        a = 1/0
    except Exception as e:
        logging.info("Logging has started")
        raise CustomException(e, sys)from e
