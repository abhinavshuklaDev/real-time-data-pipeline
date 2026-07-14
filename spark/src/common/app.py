from src.common.exception_handler import log_exception


class Application:

    @staticmethod
    def run(pipeline):

        try:

            pipeline.execute()

        except Exception as e:

            log_exception(
                pipeline.logger,
                e
            )

            raise