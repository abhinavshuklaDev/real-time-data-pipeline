from src.silver.pipeline import SilverPipeline
from src.common.app import Application


def main():

    pipeline = SilverPipeline()

    Application.run(

        pipeline

    )


if __name__ == "__main__":

    main()