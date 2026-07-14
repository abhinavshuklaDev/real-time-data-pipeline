from src.bronze.pipeline import BronzePipeline
from src.common.app import Application


def main():

    pipeline = BronzePipeline()

    Application.run(

        pipeline

    )


if __name__ == "__main__":

    main()