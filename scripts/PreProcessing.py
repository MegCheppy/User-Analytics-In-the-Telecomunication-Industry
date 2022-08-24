import numpy as np
import pandas as pd
import sys
import os
sys.path.append(os.path.abspath(os.path.join('../')))
# from logger import Logger


class PreProcess:
    def __init__(self, db: pd.DataFrame):
        """Initialize the PreProcess class.
        Args:
            db (pd.DataFrame): dataframe to be preprocessed
        """
        try:
            self.db = db
            # self.logger = Logger("preprocessing.log").get_app_logger()
            # self.logger.info(
            # 'Successfully Instantiated Outlier Class Object')
        except Exception:
            # self.logger.exception(
            # 'Failed to Instantiate Preprocessing Class Object')
            sys.exit(1)

    def convert_to_datetime(self, db, column: str):
        """Convert a column to a datetime.
        Args:
            db (pd.DataFrame): dataframe to be preprocessed
            column (str): dataframe column to be converted
        """
        db[column] = pd.to_datetime(
            db[column], errors='coerce')
        # self.logger.info(
        # 'Converted datetime columns to datetime')
        return db

    def convert_to_float(self, db, column: str):
        """Convert column to float.
        Args:
            db (pd.DataFrame): dataframe to be preprocessed
            column (str): Column to be converted to string
        """
        self.db[column] = db[column].astype(float)
        # self.logger.info(
        # 'Successfully converted to float columns')
        return self.db

    def drop_variables(self, db):
        """Drop variables based on a percentage.
        Args:
            db (pd.DataFrame): dataframe to be preprocessed
            percentage(int): Percentage of variables to be dropped
        """
        db_before_filling = db.copy()
        db = db[db.columns[db.isnull().mean() < 0.3]]
        missing_cols = db.columns[db.isnull().mean() > 0]
        print(missing_cols)
        # self.logger.info(
        #     'Missing columns are: ', missing_cols)
        return db, db_before_filling, missing_cols

    def clean_feature_name(self, db):
        """Clean labels of the dataframe.
        Args:
            db (pd.DataFrame): dataframe to be preprocessed
        """
        db.columns = [column.replace(' ', '_').lower()
                      for column in db.columns]
        # self.logger.info(
        #     'Cleaned feature names')
        return db

    def rename_columns(self, db: pd.DataFrame, column: str, new_column: str):
        """Rename a column.
        Args:
            db (pd.DataFrame): dataframe to be preprocessed
            column (str): column to be renamed
            new_column (str): New column name
        """
        db[column] = db[column].rename(new_column)
        dbRenamed = db.rename({column: new_column}, axis=1)
        return dbRenamed

    def fill_numerical_variables(self, db):
        """Fill numerical variables.
        Args:
            db (pd.DataFrame): dataframe to be preprocessed
        """
        db_single = db
        cols = db_single.columns
        num_cols = db_single.select_dtypes(include=np.number).columns
        db_single.loc[:, num_cols] = db_single.loc[:, num_cols].fillna(
            db_single.loc[:, num_cols].median())
        print(num_cols)
        print(db_single.loc[:, num_cols].median())
        # self.logger.info(
        #     'Filled missing numerical variables')
        return cols, db_single, num_cols

    def fill_categorical_variables(self, db, cols, num_cols, db_single):
        """Fill categorical variables.
        Args:
            db (pd.DataFrame): dataframe to be preprocessed
            cols(list): List of columns
            num_cols(list): List of numerical columns
            db_single(pd.DataFrame): Dataframe with filled numerical variables
        """
        cat_cols = list(set(cols) - set(num_cols))
        db_single.loc[:, cat_cols] = db_single.loc[:, cat_cols].fillna(
            db.loc[:, cat_cols].mode().iloc[0])
        db_cols = db_single.columns
        print(cat_cols)
        print(db_single.loc[:, cat_cols].mode().iloc[0])
        # self.logger.info(
        #     'Filled missing categorical variables with mode')
        return db_cols, db_single, cat_cols

    def drop_duplicates(self, db):
        """Drop duplicates.
        Args:
            db (pd.DataFrame): A dataframe to be preprocessed
        """
        db = db.drop_duplicates()

        return db

    def convert_bytes_to_megabytes(self, db, col):
        """Convert byte data to megabyte.
        Args:
            db (pd.DataFrame): A dataframe to be preprocessed
        """
        megabyte = 1*10e+5
        megabyte_col = db[col] / megabyte
        # self.logger.info(
        #     'Converted bytes to megabytes')
        return megabyte_col
