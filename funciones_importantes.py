import pandas as pd

def validate_columns(df):
    # Initialize an empty list to store validation results
    validation_results = []

    # Loop through each column in the input DataFrame
    for col in df.columns:
        # Calculate the number of unique values
        num_unique_values = df[col].nunique()

        # Calculate the number of null values
        num_null_values = df[col].isnull().sum()

        # Calculate the percentage of null values
        percent_null_values = (num_null_values / len(df)) * 100

        # Get sample unique values
        sample_unique_values = df[col].dropna().sample(min(num_unique_values, 5)).tolist()

        # Create a dictionary with the validation results for the current column
        validation_results.append({
            'Column': col,
            'Unique_Values': df[col].unique(),
            'Num_Unique_Values': num_unique_values,
            'Num_Null_Values': num_null_values,
            'Sample_Unique_Values': sample_unique_values,
            '%_null' : percent_null_values
        })

    # Convert the list of dictionaries to a DataFrame
    validation_df = pd.DataFrame(validation_results)

    return validation_df

import matplotlib.pyplot as plt 
import seaborn as sns 


def grafico_out_boxplot(df):
    cols = df.select_dtypes(include=['number']).columns

    filas = len(cols)
    columnas = 1

    fig, axes = plt.subplots(filas, columnas, figsize=(6,50 ))

    for i, columna in enumerate(cols):
        sns.boxplot(y=df[columna], ax=axes[i])
        axes[i].set_title(columna)

    plt.tight_layout()
    return (plt.show())

import seaborn as sns
import matplotlib.pyplot as plt

def plot_histograms(dataframe):
    # Obtén la lista de nombres de todas las columnas del DataFrame
    column_names = dataframe.columns

    # Itera a través de los nombres de las columnas y crea un histograma para cada una
    for column_name in column_names:
        plt.figure(figsize=(8, 6))  # Tamaño de la figura
        sns.histplot(dataframe[column_name], kde=True, edgecolor='w')
        plt.title(f'Histograma de {column_name}')
        plt.xlabel(column_name)
        plt.ylabel('Frecuencia')
        plt.show()
