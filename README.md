# Topsis-Sanyam-101903481
A package to implement Technique for Order Performance by Similarity to Ideal Solution (TOPSIS) for dealing with multi-attribute or multi-criteria decision making (MADM/MCDM) problems in the real world.

### How to install
This package is available through [PyPi](https://pypi.org/) and can be installed via the following command:

` $ pip install Topsis-Sanyam-101903481`

### Usage
To implement TOPSIS, run the following command in the terminal:

`$ topsis <inputFileName> <weights> <impacts> <outputFileName>`

**inputFileName**: CSV input file containing atleast three columns. First column must be the object/variable name and other columns must contain **numeric values only**. 

**weights** : comma separated **numeric values** enclosed between "" or ''. Number of weights must be **equal** to the number of attributes/criteria (2nd to last column)

**impacts** : comma separated **'+'** or **'-'** values enclosed between "" or ''. Number of impacts must be **equal** to the number of attributes/criteria (2nd to last column)

**outputFileName** : CSV output file which will contain all the columns of inputs file and two additional columns having **TOPSIS Score** and **Rank** 

### Example
`$ topsis sample.csv "0.25,0.25,0.25,0.25" "-,+,+,+" result.csv`

##### Input File - sample.csv
---
| Model | Price | Storage | Camera | Looks |
|-------|-------|---------|--------|-------|
| M1    | 250   | 16      | 12     | 5     |
| M2    | 200   | 16      | 8      | 3     |
| M3    | 300   | 32      | 16     | 4     |
| M4    | 275   | 32      | 8      | 4     |
| M5    | 225   | 16      | 16     | 2     |
---
##### Output File - result.csv
---
| Model | Price | Storage | Camera | Looks | TOPSIS Score | Rank |
|-------|-------|---------|--------|-------|--------------|------|
| M1    | 250   | 16      | 12     | 5     | 0.5342768571 | 3    |
| M2    | 200   | 16      | 8      | 3     | 0.3083677687 | 5    |
| M3    | 300   | 32      | 16     | 4     | 0.6916322312 | 1    |
| M4    | 275   | 32      | 8      | 4     | 0.5347365844 | 2    |
| M5    | 225   | 16      | 16     | 2     | 0.4010461215 | 4    |

### License
?? 2022 Sanyam Sharma
