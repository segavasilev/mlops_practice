import pandas as pd

def replace_nan_with_mean(data):
    data['Age'] = data['Age'].fillna(data['Age'].mean())
    return data


def main():
    data = pd.read_csv('../data/titanic_data.csv')
    data = replace_nan_with_mean(data)
    data.to_csv('../data/titanic_data.csv', index=False)


if __name__ == '__main__':
    main()
