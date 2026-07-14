from src.gold.pipeline import GoldPipeline
from src.common.app import Application


def main():

    pipeline = GoldPipeline()

    Application.run(

        pipeline

    )


if __name__ == "__main__":

    main()