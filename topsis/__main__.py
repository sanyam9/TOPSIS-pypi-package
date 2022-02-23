def main():
    import pandas as pd
    import sys

    if len(sys.argv) != 5:
        sys.exit("Error: Incorrect Number of arguments\nDesired Syntax: topsis <inputDataFile> <weights> <impacts> <outputFileName>")
    try:
        df = pd.read_csv(sys.argv[1])
    except:
        sys.exit("Error: File not Found! Make sure the file is saved in the current working directory.")

    if len(df.columns) < 3:
        sys.exit("Error: Input file must contain three or more columns")

    if df.shape[1] != df.select_dtypes(include=["float", 'int']).shape[1]+1:
        sys.exit("Error: From 2nd to last columns must contain numeric values only")

    if df.isnull().sum().sum() != 0:
        sys.exit("Error: Input file contains NULL values!")

    try:
        weights = list(map(float, sys.argv[2].split(',')))
    except ValueError:
        sys.exit("Error: Weights must be numeric only")

    if len(weights) != len(df.columns)-1:
        sys.exit(
            f"Error: Incorrect number of weights! Pass only {len(df.columns)-1} weights\nMake sure weights are separated by ',' (comma)")

    impacts = sys.argv[3].split(',')

    if len(impacts) != len(df.columns)-1:
        sys.exit(
            f"Error: Incorrect number of impacts! Pass only {len(df.columns)-1} impacts\nMake sure impacts are separated by ',' (comma)")

    if any(i not in ['+', '-'] for i in impacts):
        sys.exit("Error: Impacts must be either '+' or '-'")

    impacts = list(map(lambda x: 1 if x == '+' else -1, impacts))

    if sys.argv[4][-4:] != '.csv':
        sys.exit("Error: Output file must contain .csv extension")

    sumOfSquares = df.iloc[:, 1:].apply(lambda x: x*x).sum().apply(lambda x: x**0.5)
    sumOfSquares = sumOfSquares.to_frame().transpose()

    normalized_df = df.iloc[:, 1:].divide(sumOfSquares.values)

    weighted_df = normalized_df.multiply(weights)

    ideal_best = weighted_df.multiply(impacts).max().apply(lambda x: abs(x)).to_frame().transpose()
    ideal_worst = weighted_df.multiply(impacts).min().apply(lambda x: abs(x)).to_frame().transpose()

    dist_best = weighted_df.subtract(ideal_best.values).apply(
        lambda x: x**2).sum(axis=1).apply(lambda x: x**0.5)

    dist_worst = weighted_df.subtract(ideal_worst.values).apply(
        lambda x: x**2).sum(axis=1).apply(lambda x: x**0.5)

    Pi = dist_worst/(dist_best+dist_worst)
    df['TOPSIS Score'] = Pi
    df['Rank'] = Pi.rank(ascending=False).astype(int)

    df.to_csv(sys.argv[4], index=False)


if __name__ == '__main__':
    main()
