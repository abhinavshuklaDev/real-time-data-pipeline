import traceback


def log_exception(

    logger,

    exception

):

    logger.error(str(exception))

    logger.error(

        traceback.format_exc()

    )