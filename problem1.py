"""
Drake Watson
Trimble Data Science Assessment
"""

import pandas as pd


def check_for_e(string):
    """
    Checks if a string has an e and capitilizes if it does,
    converts to lowercase if it does not
    """

    if 'e' in string:
        string = string.upper()
    else:
        string = string.lower()

    return string


def problem1b(df):
    """
    Convert names in the 'Name' column containing an e to uppercase,
    otherwise converting to lowercase
    """

    df['Name'] = df['Name'].apply(check_for_e)

    return df


def check_for_caps(string):
    """
    Checks if a string is all-caps or lowercase and renames accordingly
    """

    if string.isupper():
        string = 'uppercase'
    else:
        string = 'lowercase'

    return string


def problem1c(name_df, mark_df):
    """
    Create new dataframe summarizing average scores of uppercase
    and lowercase names
    """

    # Join the data frames for joint analysis
    merged_df = name_df.merge(mark_df, left_on='StudentID',
                              right_on='StudentID', how='left')

    # Rename 'Names' classifying by upper/lower case
    merged_df['Name'] = merged_df['Name'].apply(check_for_caps)

    # Find average score of the upper/lower case names
    result = merged_df.groupby('Name')['Total_marks'].mean()

    return result


def main():
    mark_table = pd.read_csv('data/mark_table.csv')
    name_table = pd.read_csv('data/name_table.csv')
    new_name_table = problem1b(name_table)
    problem1c(new_name_table, mark_table)


if __name__ == '__main__':
    main()
