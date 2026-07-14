from src.parser import Parser
from src.validation.validator import Validator
from src.bronze.models import BronzeOutput


class BronzeTransformer:

    @staticmethod
    def transform(df):

        parsed_df = Parser.parse(df)

        validated_df = Validator.validate(parsed_df)

        bronze_df, dlq_df = Validator.split(validated_df)

        return BronzeOutput(
            bronze=bronze_df,
            dlq=dlq_df
        )