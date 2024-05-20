# Awesome Project: ETL Process for Currency Quotes Data


![Project Status](https://img.shields.io/badge/status-in%20development-yellow) ![License](https://img.shields.io/badge/license-MIT-blue) ![GitHub release (latest by date)](https://img.shields.io/github/v/release/IvanildoBarauna/ETL-awesome-api) ![Python Version](https://img.shields.io/badge/python-3.9-blue) ![GitHub Workflow Status](https://github.com/IvanildoBarauna/ETL-awesome-api/actions/workflows/CI-CD.yaml/badge.svg)

## Project Description
This project, called "Awesome Project: ETL Process for Currency Quotes Data", is a solution dedicated to extracting, transforming, and loading (ETL) currency quote data. It makes a single request to a specific endpoint to obtain quotes for multiple currencies.

The request response is then processed, where each currency quote is separated and stored in individual files in Parquet format. This makes it easier to organize data and efficiently retrieve it for future analysis.

Additionally, the project includes a Jupyter Notebook for data exploration. This notebook is responsible for consolidating all individual Parquet files into a single dataset. From there, the data can be explored and analyzed to gain valuable insights into currency quotes.

In summary, this project provides a complete solution for collecting, processing, and analyzing currency quote data.

## Project Structure

- [`data/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/data): Stores raw data in Parquet format.
  - ETH-EUR-1713658884.parquet: Example: Raw data for ETH-EUR quotes. file-name = symbol + unix timestamp of extraction
- [`notebooks/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/notebooks): Contains the `data_explorer.ipynb` notebook for data exploration.
- [`etl/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl): Holds the project source code.
  - [`main.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/main.py): The entry point for the ETL Module.
  - [`models/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/jobs): ETL Modules.
    - [`ExtractApiData/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/jobs/ExtractApiData): Module for data extraction from API.
      - [`ApiToParquetFile.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/jobs/ExtractApiData/ApiToParquetFile.py): Extract API data to Parquet File and store in /data.
  - [`utils/`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/etl/utils)
    - [`logs.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/utils/logs.py): Package for managing logs.
    - [`common.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/utils/common.py): Package for common tasks in the code.
    - [`constants.py`](https://github.com/IvanildoBarauna/ETL-awesome-api/blob/main/etl/utils/constants.py): Constants used in the code.

## How to run this project and verify execution time:

<details>
  <summary>Click here:</summary>
  
  ## Step by Step
  1. Clone the repository:
     ```sh
     $ git clone https://github.com/IvanildoBarauna/ETL-awesome-api.git
     ```

  2. Create a virtual environment and install dependencies:
   Ensure you have Python 3.9 installed on your system.
     ```sh
     $ cd ETL-awesome-api
     $ python -m venv .venv
     $ source .venv/bin/activate  # On Windows use `venv\Scripts\activate`
     $ .venv/bin/python -m pip install --upgrade pip 
     $ echo "SERVER_URL=https://economia.awesomeapi.com.br" > .env # Create enviroment variable for server URL`
     $ pip install -e .
     $ python etl/main.py
     ```

     Learn more about [venv module in python](https://docs.python.org/pt-br/3/library/venv.html)

  3. Alternatively, you can run the project using [`Dockerfile`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/Dockerfile) or [`docker-compose`](https://github.com/IvanildoBarauna/ETL-awesome-api/tree/main/docker-compose.yml). To build and run the Docker image, use the following command:
     ```sh
     $ docker build -t etl-awesome-api . && docker run etl-awesome-api
     ```
     To run the project with Docker Compose, use the following command:
     ```sh
     $ docker-compose up --build
     ```
     Learn more about [docker](https://docs.docker.com/)

  4. Or you can install and run the project using the dependency manager [`poetry`](https://python-poetry.org/):
     ```sh
     $ poetry install && poetry run python etl/main.py
     ```
</details>

## ETL and Data Analysis Results:
You can see the complete data analysis, see: 

---
lang: en
title: data\_explorer
viewport: 'width=device-width, initial-scale=1.0'
---

::: {role="main"}
::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
1. Consolidated files in the unique DataFrame and show the total files extracted[¶](#1.-Consolidated-files-in-the-unique-DataFrame-and-show-the-total-files-extracted){.anchor-link} {#1.-Consolidated-files-in-the-unique-DataFrame-and-show-the-total-files-extracted}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[2\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    import os
    import sys
    import pandas as pd
    from etl.common.utils.common import DefaultOutputFolder as dir

    notebook_path = os.path.dirname(os.path.abspath("data_explorer.ipynb"))
    sys.path.append(os.path.dirname(notebook_path))

    ## Files from Default Folder
    files = os.listdir(dir())
    dfs = []


    if not files: print("No files found in the output folder.")

    for file in files:
        if file.endswith(".parquet"):
            df = pd.read_parquet(dir() + file)
            dfs.append(df)
        
    allFiles = pd.concat(dfs, ignore_index=True)

    # Ordering DataFrame by column name
    allFiles = allFiles.sort_values(by=['extracted_at'], ascending=False)

    # count the rows in the all dataframe
    allFiles.shape[0]
:::
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
1.1 Data set sample, list 5 files[¶](#1.1-Data-set-sample,-list-5-files){.anchor-link} {#1.1-Data-set-sample,-list-5-files}
--------------------------------------------------------------------------------------
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[4\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    allFiles.head(3)
:::
:::
:::
:::
:::

::: {.jp-Cell-outputWrapper}
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::: {.jp-OutputArea .jp-Cell-outputArea}
::: {.jp-OutputArea-child .jp-OutputArea-executeResult}
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
Out\[4\]:
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output .jp-OutputArea-executeResult mime-type="text/html" tabindex="0"}
<div>

        code   codein   name                                  high     low      varBid   pctChange   bid       ask       timestamp    create\_date          symbol    extracted\_at
  ----- ------ -------- ------------------------------------- -------- -------- -------- ----------- --------- --------- ------------ --------------------- --------- ---------------------
  89    EUR    TTD      Euro/Dólar de Trinidad                7.289    7.288    0.001    0.01        7.139     7.439     1714135022   2024-04-26 09:37:02   EUR-TTD   2024-04-26 12:37:16
  114   EUR    TWD      Euro/Dólar Taiuanês                   35.022   34.889   0.003    0.01        34.944    34.945    1714135022   2024-04-26 09:37:02   EUR-TWD   2024-04-26 12:37:16
  67    USD    BIF      Dólar Americano/Franco Burundinense   2874     2865.3   -8.7     -0.3        2839.22   2891.39   1714134877   2024-04-26 09:34:37   USD-BIF   2024-04-26 12:35:02

</div>
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
2. Change DataTypes and Reorder columns[¶](#2.-Change-DataTypes-and-Reorder-columns){.anchor-link} {#2.-Change-DataTypes-and-Reorder-columns}
--------------------------------------------------------------------------------------------------
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[5\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    # Change data types
    df = allFiles.astype({'ask': float, 'bid': float, 'varBid': float, 'pctChange': float})

    # Show the dataframe
    df.head(3)
:::
:::
:::
:::
:::

::: {.jp-Cell-outputWrapper}
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::: {.jp-OutputArea .jp-Cell-outputArea}
::: {.jp-OutputArea-child .jp-OutputArea-executeResult}
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
Out\[5\]:
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output .jp-OutputArea-executeResult mime-type="text/html" tabindex="0"}
<div>

        code   codein   name                                  high     low      varBid   pctChange   bid        ask        timestamp    create\_date          symbol    extracted\_at
  ----- ------ -------- ------------------------------------- -------- -------- -------- ----------- ---------- ---------- ------------ --------------------- --------- ---------------------
  89    EUR    TTD      Euro/Dólar de Trinidad                7.289    7.288    0.001    0.01        7.139      7.439      1714135022   2024-04-26 09:37:02   EUR-TTD   2024-04-26 12:37:16
  114   EUR    TWD      Euro/Dólar Taiuanês                   35.022   34.889   0.003    0.01        34.944     34.945     1714135022   2024-04-26 09:37:02   EUR-TWD   2024-04-26 12:37:16
  67    USD    BIF      Dólar Americano/Franco Burundinense   2874     2865.3   -8.700   -0.30       2839.220   2891.390   1714134877   2024-04-26 09:34:37   USD-BIF   2024-04-26 12:35:02

</div>
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
3. Using SQL for Data Exploration[¶](#3.-Using-SQL-for-Data-Exploration){.anchor-link} {#3.-Using-SQL-for-Data-Exploration}
--------------------------------------------------------------------------------------

    3.1 What is the currency with the highest ask value?
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[6\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    from pandasql import sqldf

    query = """
        SELECT symbol, name, max(ask) max_ask FROM df 
        where code = 'BRL' 
        group by symbol, name
        order by 3 desc limit 1
    """

    newDf = sqldf(query, locals())

    newDf
:::
:::
:::
:::
:::

::: {.jp-Cell-outputWrapper}
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::: {.jp-OutputArea .jp-Cell-outputArea}
::: {.jp-OutputArea-child .jp-OutputArea-executeResult}
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
Out\[6\]:
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output .jp-OutputArea-executeResult mime-type="text/html" tabindex="0"}
<div>

      symbol    name                             max\_ask
  --- --------- -------------------------------- ----------
  0   BRL-LBP   Real Brasileiro/Libra Libanesa   17206.94

</div>
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
    3.1 Disponible Data
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[7\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    from pandasql import sqldf

    query = """
        SELECT code, codein, name FROM df 
        group by 1,2,3
    """

    newDf = sqldf(query, locals())

    newDf
:::
:::
:::
:::
:::

::: {.jp-Cell-outputWrapper}
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::: {.jp-OutputArea .jp-Cell-outputArea}
::: {.jp-OutputArea-child .jp-OutputArea-executeResult}
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
Out\[7\]:
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedHTML .jp-OutputArea-output .jp-OutputArea-executeResult mime-type="text/html" tabindex="0"}
<div>

         code   codein   name
  ------ ------ -------- ----------------------------------------
  0      AED    BRL      Dirham dos Emirados/Real Brasileiro
  1      AED    EUR      Dirham dos Emirados/Euro
  2      AFN    USD      Afghani do Afeganistão/Dólar Americano
  3      ARS    EUR      Peso Argentino/Euro
  4      AUD    EUR      Dólar Australiano/Euro
  \...   \...   \...     \...
  297    XAGG   USD      Prata/Dólar Americano
  298    XBR    USD      Brent Spot/Dólar Americano
  299    XRP    EUR      XRP/Euro
  300    ZAR    EUR      Rand Sul-Africano/Euro
  301    ZAR    USD      Rand Sul-Africano/Dólar Americano

302 rows × 3 columns

</div>
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
4. Using SQL + Matplotlib for Data Viz[¶](#4.-Using-SQL-+-Matplotlib-for-Data-Viz){.anchor-link} {#4.-Using-SQL-+-Matplotlib-for-Data-Viz}
------------------------------------------------------------------------------------------------

    4.1 What is the TOP 10 Most Value Currency considering BRL?
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[8\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    import matplotlib.pyplot as plt

    query = """
        SELECT 
            name
            ,round(avg(ask),2) AvgAsk
        FROM df 
        where codein = 'BRL'
        and not code in ('BTC', 'ETH', 'LTC', 'DOGE')
        group by name
        order by avg(ask) desc limit 10
    """

    newDf = sqldf(query, locals())
    newDf.sort_values(by='AvgAsk', ascending=True, inplace=True)

    AvgAskByCurrency = newDf.plot(
        kind='barh', x='name', y='AvgAsk', 
        figsize=(15, 10), 
        legend=False, 
        color='blue', title='Top 10 Most Valuable Currencies by Ask Price', xlabel='Ask Price', ylabel='Symbol')


    # Adicionando rótulos aos dados
    for index, value in enumerate(newDf['AvgAsk']):
        plt.text(value, index, str(value))

    # Exibir o gráfico
    plt.show()
:::
:::
:::
:::
:::

::: {.jp-Cell-outputWrapper}
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::: {.jp-OutputArea .jp-Cell-outputArea}
::: {.jp-OutputArea-child}
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedImage .jp-OutputArea-output tabindex="0"}
![No description has been provided for this
image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABbkAAANXCAYAAAAYXFJxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAACC80lEQVR4nOzdd5gW5dk34GvpS1l6D4IiXbBgRwUVxYZiVCxEQEFsiCViR8CKxoYaiLEAISgoimAD0YBRbCAWVGwIYkeRjrRlvj/8eF6XXWBBFCee53HMcbzPzD0z18wzS3x/e+81WUmSJAEAAAAAAClUZFsXAAAAAAAAW0rIDQAAAABAagm5AQAAAABILSE3AAAAAACpJeQGAAAAACC1hNwAAAAAAKSWkBsAAAAAgNQScgMAAAAAkFpCbgAAAAAAUkvIDQAA/G7169cvsrKyftVzDB06NLKysmLatGmbHNumTZto06bNr1rPH03Xrl2jXr16v+k569WrF0cdddRves5fas6cOZGVlRW33HLLNjn/5MmTIysrKyZPnrxNzg8AGyPkBgAgFbKysgq1/BYBzODBg+OEE06I7bbbLrKysqJr164bHLtw4cLo0aNHVK1aNcqUKRMHHnhgTJ8+vVDnadOmTWRlZUWDBg0K3D5x4sTMdY8ePXpLLmWTnn766ejXr98mx82bNy+KFSsWf/nLXzY4ZsmSJZGdnR1//vOft2KF/xsmT54cf/7zn6NGjRpRokSJqFatWrRv3z4ee+yxbV0aW8HMmTMjKysrSpUqFQsXLtwmNfz838kiRYpErVq14tBDDxVaA/A/odi2LgAAAApj+PDheT7/61//iokTJ+Zb36RJk1+9lptuuimWLFkSe+65Z3z99dcbHLd27do48sgj4+23347evXtHlSpVYtCgQdGmTZt44403Nhhe/1ypUqXik08+iddffz323HPPPNtGjBgRpUqVihUrVvzia9qQp59+Ov7+979vMuiuVq1aHHLIITF27NhYvnx5lC5dOt+Yxx57LFasWLHRIPyPqG/fvnHNNddEgwYN4swzz4y6devG/Pnz4+mnn47jjjsuRowYEaeccsq2LvNXc++998batWu3dRm/qn//+99Ro0aNWLBgQYwePTq6d+++Teo45JBDonPnzpEkScyePTsGDRoUBx10UDz11FNx+OGHb3TfAw44IH788ccoUaLEb1QtABSekBsAgFRYPxh99dVXY+LEidskMH3hhRcys7jLli27wXGjR4+Ol19+OR555JE4/vjjIyKiY8eO0bBhw+jbt288+OCDmzxX/fr1Y82aNfHQQw/lCblXrFgRY8aMiSOPPDIeffTRX35RW0GnTp1i/PjxMW7cuDjppJPybX/wwQejfPnyceSRR26D6n6fRo8eHddcc00cf/zx8eCDD0bx4sUz23r37h0TJkyI1atXb5VzbeiXD2vWrIm1a9dus/Dy59f8vyhJknjwwQfjlFNOidmzZ8eIESO2WcjdsGHDPP9mHnvssdGiRYu44447Nhhyr1ixIkqUKBFFihSJUqVK/ValAsBm0a4EAID/GcuWLYu//vWvUadOnShZsmQ0atQobrnllkiSJM+4rKys6NmzZ4wYMSIaNWoUpUqVipYtW8Z///vfQp2nbt26heoTPXr06KhevXqe9hxVq1aNjh07xtixY2PlypWFOt/JJ58co0aNyjPb9Yknnojly5dHx44dC9znzTffjMMPPzxycnKibNmycfDBB8err76aZ8zq1aujf//+0aBBgyhVqlRUrlw59ttvv5g4cWJE/NQr+e9//3tE5G11sCHHHntslClTpsDwft68efH888/H8ccfHyVLlowXX3wx0/KlZMmSUadOnbjwwgvjxx9/3Oi9WNeXeOjQofm2ZWVl5Zlx/tlnn8U555wTjRo1iuzs7KhcuXKccMIJMWfOnAKPvXz58jjzzDOjcuXKkZOTE507d44FCxZstJ6IiJUrV0bfvn1jxx13zFzLJZdcUqjvt0+fPlGpUqV44IEHCgx727Vrl+kdva53+Pr1F9QruU2bNrHTTjvFG2+8EQcccECULl06rrjiijx9ne+4446oX79+lCxZMt5///2IiPjggw/i+OOPj0qVKkWpUqVi9913j3HjxuU537o6pkyZEhdddFGmFc+xxx4b3333Xb5reOaZZ6J169ZRrly5yMnJiT322CPPM1JQT+61a9fGHXfcEc2aNYtSpUpF9erV48wzz8z3fUybNi3atWsXVapUiezs7Nh+++3j9NNP3+R9X+fZZ5+NXXbZJUqVKhVNmzbN0x7m008/jaysrLj99tvz7ffyyy9HVlZWPPTQQ5s8x5QpU2LOnDlx0kknxUknnRT//e9/44svvsg3bkuuJUmS6NGjR5QoUWKLWts0b948qlSpErNnz46I/3uWRo4cGVdddVXUrl07SpcuHYsXL95gT+7XXnstjjjiiKhYsWKUKVMmWrRoEQMHDswzpjDPFQD8EmZyAwDwPyFJkjj66KNj0qRJ0a1bt9hll11iwoQJ0bt37/jyyy/zBVUvvPBCjBo1Knr16hUlS5aMQYMGxWGHHRavv/567LTTTlulpjfffDN22223KFIk79ySPffcM/75z3/GRx99FM2bN9/kcU455ZTo169fTJ48OQ466KCI+GlW9MEHHxzVqlXLN/69996L/fffP3JycuKSSy6J4sWLxz333BNt2rSJF154Ifbaa6+I+OmljjfeeGN079499txzz1i8eHFMmzYtpk+fHoccckiceeaZ8dVXXxXYFqYgZcqUiWOOOSZGjx4dP/zwQ1SqVCmzbdSoUZGbmxudOnWKiIhHHnkkli9fHmeffXZUrlw5Xn/99bjrrrviiy++iEceeWST5yqMqVOnxssvvxwnnXRS/OlPf4o5c+bE4MGDo02bNvH+++/nm9Xcs2fPqFChQvTr1y8+/PDDGDx4cHz22WeZcK8ga9eujaOPPjpeeuml6NGjRzRp0iRmzJgRt99+e3z00Ufx+OOPb7C+jz/+OD744IM4/fTTo1y5clvlmn9u/vz5cfjhh8dJJ50Uf/nLX6J69eqZbUOGDIkVK1ZEjx49omTJklGpUqV47733olWrVlG7du247LLLokyZMvHwww9Hhw4d4tFHH41jjz02z/HPO++8qFixYvTt2zfmzJkTd9xxR/Ts2TNGjRqVGTN06NA4/fTTo1mzZnH55ZdHhQoV4s0334zx48dvtAXLmWeeGUOHDo3TTjstevXqFbNnz46777473nzzzZgyZUoUL1485s2bF4ceemhUrVo1LrvssqhQoULMmTOn0GHvxx9/HCeeeGKcddZZ0aVLlxgyZEiccMIJMX78+DjkkENihx12iFatWsWIESPiwgsvzLPviBEjoly5cnHMMcds8jwjRoyI+vXrxx577BE77bRTlC5dOh566KHo3bt3ZsyWXEtubm6cfvrpMWrUqMxfdWyuBQsWxIIFC2LHHXfMs/7aa6+NEiVKxMUXXxwrV67c4Cz/iRMnxlFHHRU1a9aM888/P2rUqBEzZ86MJ598Ms4///yIiM1+rgBgiyQAAJBC5557bvLz/5x9/PHHk4hIrrvuujzjjj/++CQrKyv55JNPMusiIomIZNq0aZl1n332WVKqVKnk2GOP3aw6ypQpk3Tp0mWD204//fR865966qkkIpLx48dv9NitW7dOmjVrliRJkuy+++5Jt27dkiRJkgULFiQlSpRIhg0blkyaNCmJiOSRRx7J7NehQ4ekRIkSyaxZszLrvvrqq6RcuXLJAQcckFm38847J0ceeeRGa1j/Pm/Kumu755578qzfe++9k9q1aye5ublJkiTJ8uXL8+174403JllZWclnn32WWde3b9885589e3YSEcmQIUPy7R8RSd++fTOfCzrHK6+8kkRE8q9//SuzbsiQIUlEJC1btkxWrVqVWX/zzTcnEZGMHTs2s65169ZJ69atM5+HDx+eFClSJHnxxRfznOcf//hHEhHJlClT8tWwztixY5OISG6//fYNjvm5dXXOnj07z/p1z8CkSZPy1BkRyT/+8Y88Y9fdv5ycnGTevHl5th188MFJ8+bNkxUrVmTWrV27Ntl3332TBg0a5Kujbdu2ydq1azPrL7zwwqRo0aLJwoULkyRJkoULFyblypVL9tprr+THH3/Mc66f79elS5ekbt26mc8vvvhiEhHJiBEj8uwzfvz4POvHjBmTREQyderUDd2yDapbt24SEcmjjz6aWbdo0aKkZs2aya677ppZd8899yQRkcycOTOzbtWqVUmVKlU2+HP/c6tWrUoqV66cXHnllZl1p5xySrLzzjvnGVeYa1n33f3tb39LVq9enZx44olJdnZ2MmHChEJc8U8/H926dUu+++67ZN68eclrr72WHHzwwUlEJLfeemuSJP/3LO2www75fn7Wf87WrFmTbL/99kndunWTBQsW5Bn78++3sM8VAPwS2pUAAPA/4emnn46iRYtGr1698qz/61//GkmSxDPPPJNn/T777BMtW7bMfN5uu+3imGOOiQkTJkRubu5WqenHH3+MkiVL5lu/rq/tplpz/Nwpp5wSjz32WKxatSpGjx4dRYsWLXAGZG5ubjz77LPRoUOH2GGHHTLra9asGaecckq89NJLsXjx4oiIqFChQrz33nvx8ccfb+6lbdC62ag/b0cxe/bsePXVV+Pkk0/OzGrPzs7ObF+2bFl8//33se+++0aSJPHmm29ulVp+fo7Vq1fH/PnzY8cdd4wKFSrE9OnT843v0aNHnpYhZ599dhQrViyefvrpDZ7jkUceiSZNmkTjxo3j+++/zyzrZtxPmjRpg/uu+x5+jVncERElS5aM0047rcBtxx13XFStWjXz+Ycffoj//Oc/0bFjx1iyZEnmOubPnx/t2rWLjz/+OL788ss8x+jRo0eeGe77779/5ObmxmeffRYRP83yXbJkSVx22WX5ejlvrO3NI488EuXLl49DDjkkzz1t2bJllC1bNnNPK1SoEBERTz755Bb1La9Vq1aen6F1LWrefPPN+OabbyLipx76pUqVihEjRmTGTZgwIb7//vtCvQ/gmWeeifnz58fJJ5+cWXfyySfH22+/He+9915m3eZcy6pVq+KEE06IJ598Mp5++uk49NBDC3W9ERH3339/VK1aNapVqxZ77bVXpuXMBRdckGdcly5d8vz8FOTNN9+M2bNnxwUXXJCpf5113++WPFcAsCWE3AAA/E/47LPPolatWvkCwyZNmmS2/1yDBg3yHaNhw4axfPnyAvsKb4ns7OwC+zKvWLEis72wTjrppFi0aFE888wzMWLEiDjqqKMKDEe/++67WL58eTRq1CjftiZNmsTatWvj888/j4iIa665JhYuXBgNGzaM5s2bR+/eveOdd94pdE0FKVasWJx44onx4osvZsKrdYH3ulYlERFz586Nrl27RqVKlaJs2bJRtWrVaN26dURELFq06BfVsM6PP/4YV199daZHe5UqVaJq1aqxcOHCAs+x/jNRtmzZqFmz5gZ7eEf81PLivffei6pVq+ZZGjZsGBE/taHYkJycnIiIWLJkyRZc3abVrl17g20mtt9++zyfP/nkk0iSJPr06ZPvWvr27RsR+a9lu+22y/O5YsWKERGZvtmzZs2KiNjs9j8ff/xxLFq0KKpVq5avlqVLl2bqaN26dRx33HHRv3//qFKlShxzzDExZMiQQve633HHHfOF7eu+t3XfeYUKFaJ9+/Z5fmkzYsSIqF27duYXGRvz73//O7bffvsoWbJkfPLJJ/HJJ59E/fr1o3Tp0nmC8825lhtvvDEef/zxGD16dLRp06ZQ17rOMcccExMnToznnnsuXnvttfj+++/j1ltvzddSaf3noyCF+X635LkCgC2hJzcAAPxKatasGV9//XW+9evW1apVa7OO1aZNm7j11ltjypQp8eijj/7i+g444ICYNWtWjB07Np599tm477774vbbb49//OMf0b179y0+7l/+8pe4++6746GHHoqLL744HnrooWjatGnssssuEfHTbPNDDjkkfvjhh7j00kujcePGUaZMmfjyyy+ja9eueV6wub4NzQAuaPb9eeedF0OGDIkLLrgg9tlnnyhfvnxkZWXFSSedtNFzbI61a9dG8+bN47bbbitwe506dTa4b+PGjSMiYsaMGYU61+Zce8TGf4my/rZ19+Piiy+Odu3aFbjP+n2bixYtWuC4ZL0XvW6utWvXRrVq1fKEwD+3bgZ6VlZWjB49Ol599dV44oknYsKECXH66afHrbfeGq+++mqULVv2F9WxTufOneORRx6Jl19+OZo3bx7jxo2Lc845J18wvL7FixfHE088EStWrCjwl2oPPvhgXH/99ZkXuhb2Wtq1axfjx4+Pm2++Odq0aZNvlvzG/OlPf4q2bdtuctzm/AJuY7bkuQKALSHkBgDgf0LdunXjueeeiyVLluSZ4fzBBx9ktv9cQS06PvrooyhdunSeNg6/xC677BIvvvhirF27Nk8g9tprr0Xp0qUzs0YL65RTTonu3btHhQoV4ogjjihwTNWqVaN06dLx4Ycf5tv2wQcfRJEiRfIEr5UqVYrTTjstTjvttFi6dGkccMAB0a9fv0zIvbG2Ehuy1157Rf369ePBBx+MQw45JN577724/vrrM9tnzJgRH330UQwbNiw6d+6cWT9x4sRNHnvdbOGFCxfmWb/+TP2IiNGjR0eXLl3i1ltvzaxbsWJFvn3X+fjjj+PAAw/MfF66dGl8/fXXG7zXERH169ePt99+Ow4++ODNvlcNGzaMRo0axdixY2PgwIGbDGU359o317rWNsWLFy9UCFoY9evXj4iId999d7OCzPr168dzzz0XrVq1KlTYuvfee8fee+8d119/fTz44IPRqVOnGDly5CZ/UbNulvHPv7ePPvooIiLq1auXWXfYYYdF1apVY8SIEbHXXnvF8uXL49RTT91kXY899lisWLEiBg8eHFWqVMmz7cMPP4yrrroqpkyZEvvtt99mXcvee+8dZ511Vhx11FFxwgknxJgxY6JYsd/+/7X/+fe7oWfm13iuAKAg2pUAAPA/4Ygjjojc3Ny4++6786y//fbbIysrKw4//PA861955ZU8fZk///zzGDt2bBx66KEbnKG6uY4//vj49ttv47HHHsus+/777+ORRx6J9u3bF9ive1PH69u3bwwaNGiDbSiKFi0ahx56aIwdOzZPm41vv/02Hnzwwdhvv/0ybTLmz5+fZ9+yZcvGjjvumKdFQpkyZSIif7C6KZ06dYo333wz+vbtG1lZWXHKKafkqTEi74zfJEli4MCBmzxuTk5OVKlSJf773//mWT9o0KB8Y4sWLZpvVvFdd921wZnP//znP/P0Qx48eHCsWbMm37Pzcx07dowvv/wy7r333nzbfvzxx1i2bNlGr6d///4xf/786N69e6xZsybf9meffTaefPLJiPi/UPHn156bmxv//Oc/N3qOwqhWrVq0adMm7rnnngL/+mBLWvgceuihUa5cubjxxhszLXrW2dhs744dO0Zubm5ce+21+batWbMm8ywuWLAg33HW/bVAYVqWfPXVVzFmzJjM58WLF8e//vWv2GWXXaJGjRqZ9cWKFYuTTz45Hn744Rg6dGg0b948WrRoscnj//vf/44ddtghzjrrrDj++OPzLBdffHGULVs2M1t9c6+lbdu2MXLkyBg/fnyceuqpW+0vEzbHbrvtFttvv33ccccd+f59WHctv8ZzBQAFMZMbAID/Ce3bt48DDzwwrrzyypgzZ07svPPO8eyzz8bYsWPjggsuyASE6+y0007Rrl276NWrV5QsWTITkvbv33+T53riiSfi7bffjoifXmj4zjvvxHXXXRcREUcffXQmADv++ONj7733jtNOOy3ef//9qFKlSgwaNChyc3MLdZ71lS9fPvr167fJcdddd11MnDgx9ttvvzjnnHOiWLFicc8998TKlSvj5ptvzoxr2rRptGnTJlq2bBmVKlWKadOmxejRo6Nnz56ZMeteztmrV69o165dFC1aNE466aRN1vCXv/wlrrnmmhg7dmy0atUqz8zYxo0bR/369ePiiy+OL7/8MnJycuLRRx/N9HLelO7du8eAAQOie/fusfvuu8d///vfzAzcnzvqqKNi+PDhUb58+WjatGm88sor8dxzz0XlypULPO6qVavi4IMPjo4dO8aHH34YgwYNiv322y+OPvroDdZy6qmnxsMPPxxnnXVWTJo0KVq1ahW5ubnxwQcfxMMPPxwTJkyI3XfffYP7n3jiiTFjxoy4/vrr480334yTTz456tatG/Pnz4/x48fH888/n+kH3axZs9h7773j8ssvjx9++CEqVaoUI0eOLDAc3xJ///vfY7/99ovmzZvHGWecETvssEN8++238corr8QXX3yReeYLKycnJ26//fbo3r177LHHHnHKKadExYoV4+23347ly5fHsGHDCtyvdevWceaZZ8aNN94Yb731Vhx66KFRvHjx+Pjjj+ORRx6JgQMHxvHHHx/Dhg2LQYMGxbHHHhv169ePJUuWxL333hs5OTkbnX2/TsOGDaNbt24xderUqF69ejzwwAPx7bffxpAhQ/KN7dy5c9x5550xadKkuOmmmzZ57K+++iomTZqU70W465QsWTLatWsXjzzySNx5551bdC0dOnSIIUOGROfOnSMnJyfuueeeTda1NRUpUiQGDx4c7du3j1122SVOO+20qFmzZnzwwQfx3nvvxYQJEyJi6z9XAFCgBAAAUujcc89N1v/P2SVLliQXXnhhUqtWraR48eJJgwYNkr/97W/J2rVr84yLiOTcc89N/v3vfycNGjRISpYsmey6667JpEmTCnXuLl26JBFR4DJkyJA8Y3/44YekW7duSeXKlZPSpUsnrVu3TqZOnVqo87Ru3Tpp1qzZRsdMmjQpiYjkkUceybN++vTpSbt27ZKyZcsmpUuXTg488MDk5ZdfzjPmuuuuS/bcc8+kQoUKSXZ2dtK4cePk+uuvT1atWpUZs2bNmuS8885LqlatmmRlZeW75xuzxx57JBGRDBo0KN+2999/P2nbtm1StmzZpEqVKskZZ5yRvP322/nuYd++ffOdc/ny5Um3bt2S8uXLJ+XKlUs6duyYzJs3L4mIpG/fvplxCxYsSE477bSkSpUqSdmyZZN27dolH3zwQVK3bt2kS5cumXFDhgxJIiJ54YUXkh49eiQVK1ZMypYtm3Tq1CmZP39+nnO3bt06ad26dZ51q1atSm666aakWbNmScmSJZOKFSsmLVu2TPr3758sWrSoUPfq+eefT4455pikWrVqSbFixZKqVasm7du3T8aOHZtn3KxZs5K2bdsmJUuWTKpXr55cccUVycSJE5OIyPP8bujZmT17dhIRyd/+9rcC65g1a1bSuXPnpEaNGknx4sWT2rVrJ0cddVQyevTofPdr/ed43bO4/s/RuHHjkn333TfJzs5OcnJykj333DN56KGHMtu7dOmS1K1bN18t//znP5OWLVsm2dnZSbly5ZLmzZsnl1xySfLVV18lSfLTM37y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/1iyZEmh9r/00kujVq1a0bZt21+50l/HHzrk7tq1a6YRe/HixaN69epxyCGHxAMPPBBr164tcJ/zzjsvOnToEF27dv1ti42Ihx56KIoWLRrnnnvub37u9Q0cODCGDh26rcso0GeffRbZ2dmxdOnSPE33ixYtGnXq1IkePXrEDz/88JvWtC5oXreUKFEidtxxx7juuusiSZJf9dx16tSJr7/+OnbaaactPsbUqVOjR48eW7EqAAAAALaWww8/PE444YRo0aJFtGvXLp5++ulYuHBhPPzww5vcd8CAATFy5MgYM2ZMlCpV6jeoduv7w/fkPuyww2LIkCGRm5sb3377bYwfPz7OP//8GD16dIwbNy6KFct7i+69995frZbVq1dH8eLFN7j9/vvvj0suuSTuueeeuPXWW7fJQ5ebmxtZWVlRvnz53/zchTV27Ng48MADo2zZshHxU9P95557LnJzc2PmzJlx+umnx6JFi2LUqFG/eW3PPfdcNGvWLFauXBkvvfRSdO/ePWrWrBndunUrcPyqVauiRIkSv+icRYsWLXQ/pg2pWrXqRrdv6tkFAAAA4LdToUKFaNiwYXzyyScbHXfLLbfEgAED4rnnnosWLVr8RtVtfX/omdwRESVLlowaNWpE7dq1Y7fddosrrrgixo4dG88880yemcpz586NY445JsqWLRs5OTnRsWPH+Pbbbzd43KlTp8YhhxwSVapUifLly0fr1q1j+vTpecZkZWXF4MGD4+ijj44yZcrE9ddfv8HjzZ49O15++eW47LLLomHDhvHYY4/l2T506NCoUKFCPPnkk9GoUaMoXbp0HH/88bF8+fIYNmxY1KtXLypWrBi9evWK3NzczH4rV66Miy++OGrXrh1lypSJvfbaKyZPnpzvuOPGjYumTZtGyZIlY+7cufnalaxduzZuvvnm2HHHHaNkyZKx3Xbb5bmeSy+9NBo2bBilS5eOHXbYIfr06ROrV6/ObF/X7mP48OFRr169KF++fJx00kl5/qRi5cqV0atXr6hWrVqUKlUq9ttvv5g6dWq+ezV27Ng4+uijM5/XNd2vXbt2tG3bNk444YSYOHFinn3uu+++aNKkSZQqVSoaN24cgwYNyrN9U/UXVuXKlaNGjRpRt27d6NSpU7Rq1SrPc7Huvl5//fVRq1ataNSoUUREDB8+PHbfffcoV65c1KhRI0455ZSYN29eZr8FCxZEp06domrVqpGdnR0NGjSIIUOGRET+diUFeemll2L//feP7OzsqFOnTvTq1SuWLVuW2b5+u5INPbuDBw+O+vXrR4kSJaJRo0YxfPjwzb5HAAAAAPwyS5cujVmzZkXNmjU3OObmm2+Oa6+9NsaPHx+77777b1jd1veHD7kLctBBB8XOO++cCZLXrl0bxxxzTPzwww/xwgsvxMSJE+PTTz+NE088cYPHWLJkSXTp0iVeeumlePXVV6NBgwZxxBFH5OuD069fvzj22GNjxowZcfrpp2/weEOGDIkjjzwyypcvH3/5y1/i/vvvzzdm+fLlceedd8bIkSNj/PjxMXny5Dj22GPj6aefjqeffjqGDx8e99xzT4wePTqzT8+ePeOVV16JkSNHxjvvvBMnnHBCHHbYYfHxxx/nOe5NN90U9913X7z33ntRrVq1fOe+/PLLY8CAAdGnT594//3348EHH4zq1atntpcrVy6GDh0a77//fgwcODDuvffeuP322/McY9asWfH444/Hk08+GU8++WS88MILMWDAgMz2Sy65JB599NEYNmxYTJ8+PXbcccdo165dntYjCxcujJdeeilPyP1zc+bMiQkTJuSZHT1ixIi4+uqr4/rrr4+ZM2fGDTfcEH369Ilhw4ZtVv2ba9q0afHGG2/EXnvtlWf9888/Hx9++GFMnDgxnnzyyYj4aab0tddeG2+//XY8/vjjMWfOnDwtc9bd92eeeSZmzpwZgwcPjipVqhSqjlmzZsVhhx0Wxx13XLzzzjsxatSoeOmll6Jnz54b3W/9Z3fMmDFx/vnnx1//+td4991348wzz4zTTjstJk2atMFjrFy5MhYvXpxnAQAAAGDzXHzxxfHCCy/EnDlz4uWXX45jjz02ihYtGieffHJERHTu3Dkuv/zyzPibbrop+vTpEw888EDUq1cvvvnmm/jmm29i6dKl2+oSfpnkD6xLly7JMcccU+C2E088MWnSpEmSJEny7LPPJkWLFk3mzp2b2f7ee+8lEZG8/vrrSZIkSd++fZOdd955g+fKzc1NypUrlzzxxBOZdRGRXHDBBZusMzc3N6lTp07y+OOPJ0mSJN99911SokSJ5NNPP82MGTJkSBIRySeffJJZd+aZZyalS5dOlixZklnXrl275Mwzz0ySJEk+++yzpGjRosmXX36Z53wHH3xwcvnll+c57ltvvZVnzM/v3eLFi5OSJUsm99577yavZZ2//e1vScuWLTOf+/btm5QuXTpZvHhxZl3v3r2TvfbaK0mSJFm6dGlSvHjxZMSIEZntq1atSmrVqpXcfPPNmXUjRoxIdt999zzHLVKkSFKmTJmkVKlSSUQkEZHcdtttmTH169dPHnzwwTz1XXvttck+++yzWfVv7PufPXt2EhFJdnZ2UqZMmaR48eJJRCQ9evTIM65Lly5J9erVk5UrV27wWEmSJFOnTk0iIvPdtm/fPjnttNM2eu4333wzSZIkmTRpUhIRyYIFC5IkSZJu3brlq+PFF19MihQpkvz4449JkiRJ3bp1k9tvvz2zvaBnd999903OOOOMPOtOOOGE5IgjjtjgdfTt2zfzneRdFiURicVisVgsFovFYrFYLBaLZRNLkvyUZdasWTMpUaJEUrt27eTEE0/MkxO2bt066dKlS+Zz3bp1k4Iymb59+24wx/mtLVq0KImIZNGiRZsc+4fvyb0hSZJEVlZWRETMnDkz6tSpE3Xq1Mlsb9q0aVSoUCFmzpwZe+yxR779v/3227jqqqti8uTJMW/evMjNzY3ly5fH3Llz84wrzJ8CTJw4MZYtWxZHHHFERERUqVIl84LMa6+9NjOudOnSUb9+/czn6tWrR7169TK9qdetW9fmYsaMGZGbmxsNGzbMc76VK1dG5cqVM59LlCix0Z48M2fOjJUrV8bBBx+8wTGjRo2KO++8M2bNmhVLly6NNWvWRE5OTp4x9erVi3LlymU+16xZM1PrrFmzYvXq1dGqVavM9uLFi8eee+4ZM2fOzKxbv1VJRESjRo1i3LhxsWLFivj3v/8db731Vpx33nkREbFs2bKYNWtWdOvWLc4444zMPmvWrMnTd7ww9RfGqFGjokmTJrF69ep4991347zzzouKFSvmmbHevHnzfH2433jjjejXr1+8/fbbsWDBgsyLUefOnRtNmzaNs88+O4477riYPn16HHroodGhQ4fYd999C1XT22+/He+8806MGDEisy5Jkli7dm3Mnj07mjRpUuB+6z+7M2fOzPdyylatWsXAgQM3eO7LL788LrroosznxYsX5/k5AwAAAGDTRo4cudHtP29PHPFTt4P/JULuDZg5c2Zsv/32W7x/ly5dYv78+TFw4MCoW7dulCxZMvbZZ59YtWpVnnFlypTZ5LHuv//++OGHHyI7Ozuzbu3atfHOO+9E//79o0iRn7rOrP/iv6ysrALXrQtIly5dGkWLFo033ngjihYtmmfcz4Px7OzsTOBfkJ/XVZBXXnklOnXqFP3794927dpF+fLlY+TIkXHrrbfmGbexWgtj1apVMX78+LjiiivyrC9RokTsuOOOEfHT22KPPPLI6N+/f1x77bWZP8G4995787UNWXdPClt/YdSpUydTS5MmTWLWrFnRp0+f6NevX+ZFous/E8uWLYt27dpFu3btYsSIEVG1atWYO3dutGvXLvM8HX744fHZZ5/F008/HRMnToyDDz44zj333Ljllls2WdPSpUvjzDPPjF69euXbtt12221wv8I8u5tSsmTJKFmy5C8+DgAAAAB/XELuAvznP/+JGTNmxIUXXhgRP4WRn3/+eXz++eeZWabvv/9+LFy4MJo2bVrgMaZMmRKDBg3KzL7+/PPP4/vvv9/sWubPnx9jx46NkSNHRrNmzTLrc3NzY7/99otnn302DjvssM0+bkTErrvuGrm5uTFv3rzYf//9t+gYERENGjSI7OzseP7556N79+75tr/88stRt27duPLKKzPrPvvss806x7qXGU6ZMiXq1q0bET/1qZ46dWpccMEFEfHTb6QqVqwYO++880aPddVVV8VBBx0UZ599dtSqVStq1aoVn376aXTq1KnA8Vuj/g0pWrRorFmzJlatWpUJudf3wQcfxPz582PAgAGZ52/atGn5xlWtWjW6dOkSXbp0if333z969+5dqJB7t912i/fffz8Tvm+pJk2axJQpU6JLly6ZdVOmTNngzwgAAAAAbA1/+JB75cqV8c0330Rubm58++23MX78+LjxxhvjqKOOis6dO0dERNu2baN58+bRqVOnuOOOO2LNmjVxzjnnROvWrTfYbqRBgwYxfPjw2H333WPx4sXRu3fvTc54Lsjw4cOjcuXK0bFjx3yzqY844oi4//77tzjkbtiwYXTq1Ck6d+4ct956a+y6667x3XffxfPPPx8tWrSII488slDHKVWqVFx66aVxySWXRIkSJaJVq1bx3XffxXvvvRfdunWLBg0axNy5c2PkyJGxxx57xFNPPRVjxozZrFrLlCkTZ599dvTu3TsqVaoU2223Xdx8882xfPny6NatW0REjBs3boMvnPy5ffbZJ1q0aBE33HBD3H333dG/f//o1atXlC9fPg477LBYuXJlTJs2LRYsWBAXXXTRVql/nfnz58c333wTa9asiRkzZsTAgQPjwAMP3Gjrk+222y5KlCgRd911V5x11lnx7rvv5mlTExFx9dVXR8uWLaNZs2axcuXKePLJJzfYZmR9l156aey9997Rs2fP6N69e5QpUybef//9mDhxYtx9992FvrbevXtHx44dY9ddd422bdvGE088EY899lg899xzhT4GAAAAAGyuItu6gG1t/PjxUbNmzahXr14cdthhMWnSpLjzzjtj7NixmXYVWVlZMXbs2KhYsWIccMAB0bZt29hhhx1i1KhRGzzu/fffHwsWLIjddtstTj311OjVq1dUq1Zts+t74IEH4thjjy2wXchxxx0X48aN26IZ4usMGTIkOnfuHH/961+jUaNG0aFDh5g6depG21QUpE+fPvHXv/41rr766mjSpEmceOKJmX7aRx99dFx44YXRs2fP2GWXXeLll1+OPn36bHatAwYMiOOOOy5OPfXU2G233eKTTz6JCRMmRMWKFSOi8CF3RMSFF14Y9913X3z++efRvXv3uO+++2LIkCHRvHnzaN26dQwdOjTTrmZr1R/x0y9M1j1vPXr0iCOOOGKjz1HETzO0hw4dGo888kg0bdo0BgwYkG+GdokSJeLyyy+PFi1axAEHHBBFixbdZC+mdVq0aBEvvPBCfPTRR7H//vvHrrvuGldffXXUqlVrs66tQ4cOMXDgwLjllluiWbNmcc8998SQIUOiTZs2m3UcAAAAANgcWUmSJNu6CPilpk+fHgcddFB89913+Xp7kx6LFy/+/y/8XBQRm/9iTwAAAIA/mv/VdHddTrRo0aKNdkGIMJOb/xFr1qyJu+66S8ANAAAAAH8wZnIDvxtmcgMAAABsnv/VdNdMbgAAAAAA/hCE3AAAAAAApJaQGwAAAACA1BJyAwAAAACQWkJuAAAAAABSS8gNAAAAAEBqCbkBAAAAAEgtITcAAAAAAKkl5AYAAAAAILWE3AAAAAAApJaQGwAAAACA1BJyAwAAAACQWkJuAAAAAABSS8gNAAAAAEBqCbkBAAAAAEgtITcAAAAAAKkl5AYAAAAAILWE3AAAAAAApJaQGwAAAACA1BJyAwAAAACQWkJuAAAAAABSS8gNAAAAAEBqCbkBAAAAAEgtITcA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hTtgVlZ8+umnv6go4I9p8eLFUb58+YhYFBE527ocAACALVK4pAWAjVmXEy1atChycjaeExV6Jvfs2bN/cWEAAAAAALA1/eKe3EmSRCEngwMAAAAAwFa1xSH3v/71r2jevHlkZ2dHdnZ2tGjRIoYPH741awMAAAAAgI0qdLuSn7vtttuiT58+0bNnz2jVqlVERLz00ktx1llnxffffx8XXnjhVi0SAAAAAAAKUugXT/7c9ttvH/3794/OnTvnWT9s2LDo16+f/t3AFvHiSQAA4H+Brq4Av9zmvHhyi9qVfP3117HvvvvmW7/vvvvG119/vSWHBAAAAACAzbZFIfeOO+4YDz/8cL71o0aNigYNGvziogAAAAAAoDC2qCd3//7948QTT4z//ve/mZ7cU6ZMieeff77A8BsAAAAAAH4NWzST+7jjjovXXnstqlSpEo8//ng8/vjjUaVKlXj99dfj2GOP3do1AgAAAABAgbboxZMAvwYvngQAAP4XSFoAfrnNefHkFrUriYjIzc2NMWPGxMyZMyMiomnTpnHMMcdEsWJbfEgAAAAAANgsW9Su5L333ouGDRtGly5dYsyYMTFmzJjo0qVLNGjQIN59992tXSMAAABAqgwePDhatGgROTk5kZOTE/vss08888wzG93njjvuiEaNGkV2dnbUqVMnLrzwwlixYkWeMV9++WX85S9/icqVK0d2dnY0b948pk2b9mteCsDv3hZNu+7evXs0a9Yspk2bFhUrVoyIiAULFkTXrl2jR48e8fLLL2/VIgEAAADS5E9/+lMMGDAgGjRoEEmSxLBhw+KYY46JN998M5o1a5Zv/IMPPhiXXXZZPPDAA7HvvvvGRx99FF27do2srKy47bbbIuKn7KVVq1Zx4IEHxjPPPBNVq1aNjz/+OJPNAPxRbVFP7uzs7Jg2bVq+f5Tffffd2GOPPeLHH3/cagUCfxx6cgMAAP8LNpS0VKpUKf72t79Ft27d8m3r2bNnzJw5M55//vnMur/+9a/x2muvxUsvvRQREZdddllMmTIlXnzxxV+lboDfk83pyb1F7UoaNmwY3377bb718+bNix133HFLDgkAAADwPyk3NzdGjhwZy5Yti3322afAMfvuu2+88cYb8frrr0dExKeffhpPP/10HHHEEZkx48aNi9133z1OOOGEqFatWuy6665x7733/ibXAPB7VuiQe/HixZnlxhtvjF69esXo0aPjiy++iC+++CJGjx4dF1xwQdx0002/Zr1b7JNPPokbbrjBLHMAAADgNzFjxowoW7ZslCxZMs4666wYM2ZMNG3atMCxp5xySlxzzTWx3377RfHixaN+/frRpk2buOKKKzJjPv300xg8eHA0aNAgJkyYEGeffXb06tUrhg0b9ltdEsDvUqFD7goVKkTFihWjYsWK0b59+3j//fejY8eOUbdu3ahbt2507Ngx3n333Wjfvv2vWe8WWbFiRRx//PFRq1atyM7Ozqzv169f7LLLLr9ZHfXq1Ys77rjjVz/P0KFDo0KFCr/6efg/v/WztDnmzJkTWVlZ8dZbb0VExOTJkyMrKysWLlxY6GP8Vs8uAADA/5JGjRrFW2+9Fa+99lqcffbZ0aVLl3j//fcLHDt58uS44YYbYtCgQTF9+vR47LHH4qmnnoprr702M2bt2rWx2267xQ033BC77rpr9OjRI84444z4xz/+8VtdEsDvUqFfPDlp0qRfs45C69q1a+Y3lMWKFYtKlSpFixYt4uSTT46uXbtGkSL5c/vzzjsvOnToEF27dv2Nq/11TJo0Kf72t7/Fa6+9Fj/++GPUq1cvDj/88Ljooouidu3aceKJJ+b5c6Y/ms8++ywaN24c3333Xdxyyy3Rv3//iIgoUqRI1KpVKw4//PAYMGBAVKpU6Terac6cObH99ttnPhcvXjy222676Nq1a1x55ZWRlZX1q527Tp068fXXX0eVKlW2+BhTp06NMmXKbMWqAAAA/veVKFEi09a1ZcuWMXXq1Bg4cGDcc889+cb26dMnTj311OjevXtERDRv3jyWLVsWPXr0iCuvvDKKFCkSNWvWzDcTvEmTJvHoo4/++hcD8DtW6JC7devWv2Ydm+Wwww6LIUOGRG5ubnz77bcxfvz4OP/882P06NExbty4KFYs72X9mv2pVq9eHcWLF//Vjr++e+65J84555zo0qVLPProo1GvXr2YO3du/Otf/4pbb701brvttsjOzs4zYz3tVq1aFSVKlCj0+LFjx8aBBx4YZcuWjYiIZs2axXPPPRe5ubkxc+bMOP3002PRokUxatSoX6vkDXruueeiWbNmsXLlynjppZeie/fuUbNmzQJfOhKx+ddekKJFi0aNGjV+0TGqVq260e2/9c8BAABAGq1duzZWrlxZ4Lbly5fnm7hXtGjRiIhI/v+bLFu1ahUffvhhnjEfffRR1K1b91eoFiA9tujFkxE/tQB5/fXX48knn4xx48blWX5tJUuWjBo1akTt2rVjt912iyuuuCLGjh0bzzzzTAwdOjQzbu7cuXHMMcdE2bJlIycnJzp27FjgCzPXmTp1ahxyyCFRpUqVKF++fLRu3TqmT5+eZ0xWVlYMHjw4jj766ChTpkxcf/31BR5r3rx50b59+8jOzo7tt98+RowYkW/MwoULo3v37lG1atXIycmJgw46KN5+++0N1vfFF19Er169olevXvHAAw9EmzZtol69enHAAQfEfffdF1dffXVE5G9Xsq6VxvDhw6NevXpRvnz5OOmkk2LJkiWZMUuWLIlOnTpFmTJlombNmnH77bdHmzZt4oILLsiMGT58eOy+++5Rrly5qFGjRpxyyikxb968zPZ1bTCeeuqpaNGiRZQqVSr23nvvePfdd/PV8nN33HFH1KtXL/O5a9eu0aFDh7j++uujVq1a0ahRo0Kdf52xY8fG0UcfnflcrFixzPPStm3bOOGEE2LixIl59rnvvvuiSZMmUapUqWjcuHEMGjQoz/ZLL700GjZsGKVLl44ddtgh+vTpE6tXr97AN7VhlStXjho1akTdunWjU6dO0apVqzzP2JZe+4IFC6JTp05RtWrVyM7OjgYNGsSQIUMiIn+7koK89NJLsf/++0d2dnbUqVMnevXqFcuWLctsX79dyYZ+DgYPHhz169ePEiVKRKNGjWL48OGbfY8AAAD+F1x++eXx3//+N+bMmRMzZsyIyy+/PCZPnhydOnWKiIjOnTvH5Zdfnhnfvn37GDx4cIwcOTJmz54dEydOjD59+kT79u0zYfeFF14Yr776atxwww3xySefxIMPPhj//Oc/49xzz90m1wjwe1Homdw/N378+OjcuXN8//33+bZlZWVFbm7uLy5scx100EGx8847x2OPPRbdu3ePtWvXZgLuF154IdasWRPnnntunHjiiTF58uQCj7FkyZLo0qVL3HXXXZEkSdx6661xxBFHxMcffxzlypXLjOvXr18MGDAg7rjjjnyzxtfp2rVrfPXVVzFp0qQoXrx49OrVK18ge8IJJ0R2dnY888wzUb58+bjnnnvi4IMPjo8++qjAVhqPPPJIrFq1Ki655JICz7mxPtyzZs2Kxx9/PJ588slYsGBBdOzYMQYMGJAJJy+66KKYMmVKjBs3LqpXrx5XX311TJ8+PU8gvXr16rj22mujUaNGMW/evLjooouia9eu8fTTT+c5V+/evWPgwIFRo0aNuOKKK6J9+/bx0UcfbdZM3+effz5ycnLyhNGFOf/ChQvjpZde2mC4OmfOnJgwYUKe2dEjRoyIq6++Ou6+++7Ydddd480334wzzjgjypQpE126dImIiHLlysXQoUOjVq1aMWPGjDjjjDOiXLlyG/wuCmPatGnxxhtvROfOnX/xtffp0yfef//9eOaZZ6JKlSrxySefFPolq7NmzYrDDjssrrvuunjggQfiu+++i549e0bPnj0zQXlB1v85GDNmTJx//vlxxx13RNu2bePJJ5+M0047Lf70pz/FgQceWOAxVq5cmWcWw+LFiwtVMwAAwO/dvHnzonPnzvH1119H+fLlo0WLFjFhwoQ45JBDIuKniXk/n7l91VVXRVZWVlx11VXx5ZdfRtWqVaN9+/Z5JtftscceMWbMmLj88svjmmuuie233z7uuOOOTHAO8IeVbIEdd9wxOeecc5JvvvlmS3b/Rbp06ZIcc8wxBW478cQTkyZNmiRJkiTPPvtsUrRo0WTu3LmZ7e+9914SEcnrr7+eJEmS9O3bN9l55503eK7c3NykXLlyyRNPPJFZFxHJBRdcsNEaP/zwwzznSZIkmTlzZhIRye23354kSZK8+OKLSU5OTrJixYo8+9avXz+55557Cjzu2WefneTk5Gz03EmSJEOGDEnKly+f+dy3b9+kdOnSyeLFizPrevfuney1115JkiTJ4sWLk+LFiyePPPJIZvvChQuT0qVLJ+eff/4GzzN16tQkIpIlS5YkSZIkkyZNSiIiGTlyZGbM/Pnzk+zs7GTUqFGZWta/57fffntSt27dzOcuXbok1atXT1auXLnR61z//EmSJCNGjEh23333PNdepEiRpEyZMkmpUqWSiEgiIrntttsyY+rXr588+OCDeY597bXXJvvss88Gz/23v/0tadmyZZ7zbOxZmj17dhIRSXZ2dlKmTJmkePHiSUQkPXr0yDNuS6+9ffv2yWmnnbbRc7/55ptJkvzf97RgwYIkSZKkW7du+ep48cUXkyJFiiQ//vhjkiRJUrdu3cyzmyQF/xzsu+++yRlnnJFn3QknnJAcccQRG7yOvn37Zr6TvMuiJCKxWCwWi8VisVgsllQuAPxyixYtSiIiWbRo0SbHblG7km+//TYuuuiiqF69+i+I17e+JEkyL/CbOXNm1KlTJ+rUqZPZ3rRp06hQoULMnDmzwP2//fbbOOOMM6JBgwZRvnz5yMnJiaVLl8bcuXPzjNt99903WsfMmTOjWLFi0bJly8y6xo0b55lp/fbbb8fSpUujcuXKUbZs2cwye/bsmDVr1iavb3PVq1cvz2z0mjVrZmaWf/rpp7F69erYc889M9vLly+faZWxzhtvvBHt27eP7bbbLsqVK5fp077+/dlnn30y/3elSpWiUaNGG7znG9K8efN8vagLc/71W5VE/N/brKdOnRqXXnpptGvXLs4777yIiFi2bFnMmjUrunXrlud7uO666/J8D6NGjYpWrVpFjRo1omzZsnHVVVflu+7CGDVqVLz11lvx9ttvx8MPPxxjx46Nyy677Bdf+9lnnx0jR46MXXbZJS655JJ4+eWXC13T22+/HUOHDs1z/e3atYu1a9fG7NmzN7jf+j8HM2fOjFatWuVZ16pVq41+95dffnksWrQos3z++eeFrhsAAAAAIrawXcnxxx8fkydPjvr162/ten6RmTNnxvbbb7/F+3fp0iXmz58fAwcOjLp160bJkiVjn332iVWrVuUZV6ZMmV9aaixdujRq1qxZYOuUDbUdadiwYSxatCi+/vrrqFmz5madb/1WIVlZWbF27dpC779s2bJo165dtGvXLkaMGBFVq1aNuXPnRrt27fLdn40pUqRIJEmSZ11Bva3Xv8eFOf+qVati/PjxccUVV+TZ9+dvsx4wYEAceeSR0b9//7j22mtj6dKlEfHTy0n32muvPPut63n2yiuvRKdOnaJ///7Rrl27KF++fIwcOTJuvfXWQl/3OnXq1MnU0qRJk5g1a1b06dMn+vXrF6VKldriaz/88MPjs88+i6effjomTpwYBx98cJx77rlxyy23bLKmpUuXxplnnhm9evXKt2277bbb4H5b4+egZMmSUbJkyV98HAAAAAD+uLYo5L777rvjhBNOiBdffDGaN2+eL0AtKCz7tf3nP/+JGTNmxIUXXhgRPwWIn3/+eXz++eeZ2dzvv/9+LFy4MJo2bVrgMaZMmRKDBg2KI444IiIiPv/88wL7jm9K48aNY82aNfHGG2/EHnvsERERH374YSxcuDAzZrfddotvvvkmihUrluelixtz/PHHx2WXXRY333xz3H777fm2L1y4cKN9uTdkhx12iOLFi8fUqVMzoeaiRYvio48+igMOOCAiIj744IOYP39+DBgwIHM/p02bVuDxXn311cxxFixYEB999FE0adIkIiKqVq0a33zzTZ5Z6Rt7IeI6hTn/5MmTo2LFirHzzjtv9FhXXXVVHHTQQXH22WdHrVq1olatWvHpp59usIfZyy+/HHXr1o0rr7wys+6zzz7bZM2FUbRo0VizZk2sWrUqE3Kvr7D3vmrVqtGlS5fo0qVL7L///tG7d+9Chdy77bZbvP/++5nwfUs1adIkpkyZkuljHvHTz9SGft4AAAAAYGvYopD7oYceimeffTZKlSoVkydPztNCIysr61cPuVeuXBnffPNN5Obmxrfffhvjx4+PG2+8MY466qjMS/zatm0bzZs3j06dOsUdd9wRa9asiXPOOSdat269wXYjDRo0iOHDh8fuu+8eixcvjt69e0d2dvZm19eoUaM47LDD4swzz4zBgwdHsWLF4oILLshzrLZt28Y+++wTHTp0iJtvvjkaNmwYX331VTz11FNx7LHHFlhjnTp14vbbb4+ePXvG4sWLo3PnzlGvXr344osv4l//+leULVt2i2YXlytXLrp06RK9e/eOSpUqRbVq1aJv375RpEiRzHe73XbbRYkSJeKuu+6Ks846K95999249tprCzzeNddcE5UrV47q1avHlVdeGVWqVIkOHTpERESbNm3iu+++i5tvvjmOP/74GD9+fDzzzDORk5Oz0RoLc/5x48bla1VSkH322SdatGgRN9xwQ9x9993Rv3//6NWrV5QvXz4OO+ywWLlyZUybNi0WLFgQF110UTRo0CDmzp0bI0eOjD322COeeuqpGDNmTCHubH7z58+Pb775JtasWRMzZsyIgQMHxoEHHrjR6y/MtV999dXRsmXLaNasWaxcuTKefPLJzC8WNuXSSy+NvffeO3r27Bndu3ePMmXKxPvvvx8TJ06Mu+++u9DX1rt37+jYsWPsuuuu0bZt23jiiSfisccei+eee67QxwAAAACAzbVFPbmvvPLK6N+/fyxatCjmzJkTs2fPziyffvrp1q4xn/Hjx0fNmjWjXr16cdhhh8WkSZPizjvvjLFjx2ZaTGRlZcXYsWOjYsWKccABB0Tbtm1jhx12iFGjRm3wuPfff38sWLAgdttttzj11FOjV69eUa1atS2qcciQIVGrVq1o3bp1/PnPf44ePXrkOVZWVlY8/fTTccABB8Rpp50WDRs2jJNOOik+++yzjfY6P+ecc+LZZ5+NL7/8Mo499tho3LhxdO/ePXJycuLiiy/eolojIm677bbYZ5994qijjoq2bdtGq1atokmTJpnZxVWrVo2hQ4fGI488Ek2bNo0BAwZscJbwgAED4vzzz4+WLVvGN998E0888USmx3STJk1i0KBB8fe//z123nnneP311wtVd2HOX9iQOyLiwgsvjPvuuy8+//zz6N69e9x3330xZMiQaN68ebRu3TqGDh2aaX1z9NFHx4UXXhg9e/aMXXbZJV5++eXo06dPoc6zvrZt22ae3R49esQRRxyx0WeysNdeokSJuPzyy6NFixZxwAEHRNGiRWPkyJGFqqlFixbxwgsvxEcffRT7779/7LrrrnH11VdHrVq1NuvaOnToEAMHDoxbbrklmjVrFvfcc08MGTIk2rRps1nHAQAAAIDNkZWs3yC5ECpVqhRTp0793fXkZutZtmxZ1K5dO2699dbo1q1bofaZPHlyHHjggbFgwYItapvyS0yfPj0OOuig+O677/K1zyE9Fi9eHOXLl4+IRRGx8dn9AAAAv1ebn7QAsL51OdGiRYs22QVii2Zyd+nSZZOzT0mXN998Mx566KGYNWtWTJ8+PdOf+phjjtnGlRXOmjVr4q677hJwAwAAAMAfzBb15M7NzY2bb745JkyYEC1atMgXLN52221bpTh+W7fcckt8+OGHUaJEiWjZsmW8+OKLUaVKlW1dVqHsueeeseeee27rMgAAAACA39gWtSs58MADN3zArKz4z3/+84uKAv6YtCsBAAD+F2hXAvDLbU67ki2ayT1p0qQtKgwAAAAAALamLerJPWTIkPjxxx+3di0AAAAAALBZtijkvuyyy6J69erRrVu3ePnll7d2TQAAAAAAUChbFHJ/+eWXMWzYsPj++++jTZs20bhx47jpppvim2++2dr1AQAAAADABm1RyF2sWLE49thjY+zYsfH555/HGWecESNGjIjtttsujj766Bg7dmysXbt2a9cKAAAAAAB5bFHI/XPVq1eP/fbbL/bZZ58oUqRIzJgxI7p06RL169ePyZMnb4USAQAAAACgYFsccn/7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+vXrF9ttt12ULFkyatWqFb169droObOysqJGjRp5lurVq2e2t2nTJs4777y44IILomLFilG9evW49957Y9myZXHaaadFuXLlYscdd4xnnnkm3z1Z165kXeuLcePGRdOmTaNkyZIxd+7cmDp1ahxyyCFRpUqVKF++fLRu3TqmT5+ep76PP/44DjjggChVqlQ0bdo0Jk6cmO8aZsyYEQcddFBkZ2dH5cqVo0ePHrF06dI89ey5555RpkyZqFChQrRq1So+++yzzPYVK1bEs88+myfkLl26dNSoUSPq1q0bp512WrRo0SLPuVeuXBkXX3xx1K5dO8qUKRN77bVXTJ48ObN9/vz5cfLJJ0ft2rWjdOnS0bx583jooYc2+l1s6vtp0KBBXHfddVGkSJF45513MmPq1asX1157bXTu3DlycnKiR48eERFx6aWXRsOGDaN06dKxww47RJ8+ffI822+//XYceOCBUa5cucjJyYmWLVvGtGnTIqJwrXLuu+++aNKkSZQqVSoaN24cgwYNymxbv13JumfimWeeiZYtW0bJkiXjpZdeipUrV0avXr2iWrVqUapUqdhvv/1i6tSpGzznypUrY/HixXkWgLRaunRpvPXWW5l/K2fPnh1vvfVWzJ07NyIiLr/88ujcuXNERBQpUiR22mmnPMu6fzt32mmnKFOmTET81KLk3//+dzz44INRrly5+Oabb+Kbb76JH3/8cZtcIwAAwO/RNg+5C3LQQQfFzjvvvMk2Dpdddlmcf/75MXPmzGjXrl1EREyaNClmzZoVkyZNimHDhsXQoUPzhOWrV6+Oa6+9Nt5+++14/PHHY86cOdG1a9d8x+7Xr1/cfffd8fLLL8fnn38eHTt2jDvuuCMefPDBeOqpp+LZZ5+Nu+66a4O1vfbaa9GtW7fo2bNnvPXWW3HggQfGddddl2fMmDFj4vzzz4+//vWv8e6778aZZ54Zp512WkyaNCkiIh599NG4/fbb45577omPP/44Hn/88WjevHkh7+KGDRs2LKpUqRKvv/56nHfeeXH22WfHCSecEPvuu29Mnz49Dj300Dj11FM3GuIvX748brrpprjvvvvivffei2rVqsWSJUuiS5cu8dJLL8Wrr74aDRo0iCOOOCKWLFkSET+9MOvPf/5zlChRIl577bX4xz/+EZdeemme4y5btizatWsXFStWjKlTp8YjjzwSzz33XPTs2TMiItasWRMdOnSI1q1bxzvvvBOvvPJK9OjRI89s9eeffz5q164djRs3zld3kiTx4osvxgcffJBndnTPnj3jlVdeiZEjR8Y777wTJ5xwQhx22GHx8ccfR8RPwXnLli3jqaeeinfffTd69OgRp556arz++utb/D3k5ubGsGHDIiJit912y7PtlltuiZ133jnefPPN6NOnT0RElCtXLoYOHRrvv/9+DBw4MO699964/fbbM/t06tQp/vSnP8XUqVPjjTfeiMsuuyyKFy9eqFpGjBgRV199dVx//fUxc+bMuOGGG6JPnz6Z+jbksssuiwEDBsTMmTOjRYsWcckll8Sj/6+9ew+2qrzvB/w5HAWRy1EMImfkokHAGwiiiCZKlQSVoLTehqKQRK0xeEHUto5GMKYRo2bAkjpqCDQxBmkUrxEEo9goVsBi1aJGaoJJEBUpeNCAHNbvD3+ceuSqwW5W+jwza4b9rne967vX3kvls1/fdffd+ed//uc8++yz6dKlSwYOHJh33nlnk8dfd911qampadg6dOiwTfUC7Ijmz5+fXr16pVevXkmS0aNHp1evXrn66quTfLj02obAe1vdcsstWblyZfr375/27ds3bHfdddd2rx8AAKC0igoaMWJEcfLJJ29y3xlnnFHsv//+Da+TFNOnTy+Koihee+21Ikkxfvz4jcbr1KlTsW7duoa20047rTjjjDM2W8O8efOKJMW7775bFEVRPPbYY0WSYvbs2Q19rrvuuiJJsXjx4oa28847rxg4cOBmxx06dGhx4oknbvSeampqGl4feeSRxbnnntuoz2mnndZw3E033VR07dq1WLt27WbP81GTJ08ukhQtWrRotB1//PENfY455pjiC1/4QsPrdevWFS1atCjOOuushralS5cWSYq5c+cWRfE/12TFihWNzrNw4cIt1lNfX1+0atWqeOCBB4qiKIqZM2cWO+20U/H73/++oc/DDz/c6LO97bbbit13372oq6tr6PPQQw8VTZo0Kd54441i+fLlRZLi8ccf3+x5zz333OKyyy5r9J533nnnokWLFsXOO+9cJCl22WWX4sknnyyKoih++9vfFtXV1Y3qKoqiOO6444orrrhis+cZNGhQcemllzY6z8UXX7zZ/h//fJo0aVI0a9asmDx5cqN+nTp1KoYMGbLZcTa44YYbikMPPbThdatWrYopU6Zs9twf/e6NGTOm6NmzZ8Prz3/+88Wdd97Z6Jhrr7226NevX1EU/3PP/fu//3tRFP/znbj33nsb+tfV1RU777xz8dOf/rShbe3atUVtbW3xve99b5N1/fGPfyxWrlzZsL3++utFkiJZWSSFzWazlWIDAABg+1u5cmWRpFi5cuVW++6wC+gWRbHVtaT79OmzUduBBx6Y6urqhtft27dvtOblggULMnbs2Dz33HNZsWJFwwMulyxZkgMOOKChX48ePRr+3K5du4YlIj7atqVZvIsWLcpf/uVfNmrr169fZsyY0ajPhqUoNjjqqKMyYcKEJMlpp52W8ePHZ999983xxx+fE088MYMHD97iusetWrXaaImQj6/F/NH3Vl1dnT322KPRDPENy5t8dBmXj2vatGmjcZJk2bJlueqqq/L444/nzTffTH19fd57772GWWuLFi1Khw4dUltb2+iafNSiRYvSs2fPhv9Ne8M1Wb9+fV5++eUcffTR+epXv5qBAwfmS1/6UgYMGJDTTz897du3T/Lh9+aBBx7ItGnTGo07bNiwXHnllVmxYkXGjBmTI488MkceeWSSD5dHqa+vT9euXRsds2bNmuyxxx5JPpx1/d3vfjfTpk3L73//+6xduzZr1qzJrrvuutlrtCkf/Xzee++9zJ49O9/4xjeyxx57ZPDgwQ39NvXdvuuuu3LzzTdn8eLFqaury7p169K6deuG/aNHj84555yTn/zkJxkwYEBOO+20fP7zn99qTatXr87ixYtz9tln59xzz21oX7du3VYfNvrROhcvXpwPPvggRx11VEPbzjvvnMMPPzyLFi3a5PHNmjVLs2bNtlojAAAAAGzODhtyL1q0aKsPV/poELrBx5dnqKqqagiyNyyFMXDgwPz0pz9N27Zts2TJkgwcODBr167d7DhVVVVbHPez0qFDh7z88suZPXt2Zs2alW9+85u54YYbMmfOnM0uQ9GkSZN06dJli+Nu6r18/P0m2eL7a968+UY/QowYMSLLly/PhAkT0qlTpzRr1iz9+vXb6Nr+qSZPnpyLLrooM2bMyF133ZWrrroqs2bNyhFHHJFnnnkm69atawiwN6ipqWm4LtOmTUuXLl1yxBFHZMCAAamrq0t1dXUWLFjQ6AeSJGnZsmWS5IYbbsiECRMyfvz4HHzwwWnRokVGjRr1id/bxz+fHj165JFHHsn111/fKOT++Hd77ty5GTZsWK655poMHDgwNTU1mTp1am666aaGPmPHjs1f//Vf56GHHsrDDz+cMWPGZOrUqRv92PJxG9Y7v/3229O3b99G+z5+PT5uU/cgAAAAAPxv2iHX5P7lL3+Z559/Pqeccsp2Hfell17K8uXLM27cuHzxi19M9+7dtzhb+U+x//7759/+7d8atT399NMb9XnyyScbtT355JONZpQ3b948gwcPzs0335zHH388c+fObTQzfUfy5JNP5qKLLsqJJ56YAw88MM2aNcvbb7/dsH///ffP66+/nqVLlza0beqaPPfcc1m9enWjcZs0aZJu3bo1tPXq1StXXHFFnnrqqRx00EG58847kyT33XdfBg0atMVwtmXLlrn44otz2WWXpSiK9OrVK/X19XnzzTfTpUuXRttee+3VUMPJJ5+cM888Mz179sy+++6bV1555U+7YP9fdXX1Vh8g9tRTT6VTp0658sor06dPn+y3336NHra5QdeuXXPJJZfkkUceyV/91V9l8uTJWz1/u3btUltbm//6r//a6P1v7Yemj9rwANWPfqc/+OCDzJs3r9F3GgAAAAC2p4rP5F6zZk3eeOON1NfXZ9myZZkxY0auu+66fOUrX8nw4cO367k6duyYpk2b5h//8R/zjW98Iy+88EKuvfba7XqODS666KIcddRRufHGG3PyySdn5syZjZYqSZLLL788p59+enr16pUBAwbkgQceyD333JPZs2cnSaZMmZL6+vr07ds3u+66a+644440b948nTp12ux5i6LIG2+8sVH7nnvumSZNPtvfNPbbb7/85Cc/SZ8+fbJq1apcfvnljZZKGTBgQLp27ZoRI0bkhhtuyKpVq3LllVc2GmPYsGEZM2ZMRowYkbFjx+att97KhRdemLPOOivt2rXLa6+9lttuuy0nnXRSamtr8/LLL+fXv/51w3fl/vvvz7e//e2t1nreeefl2muvzd13351TTz01w4YNy/Dhw3PTTTelV69eeeutt/Loo4+mR48eGTRoUPbbb7/8/Oc/z1NPPZXdd9893//+97Ns2bJPHN5+9PN5//33M2vWrMycObPhoWRburZLlizJ1KlTc9hhh+Whhx7K9OnTG/a///77ufzyy3Pqqadmn332ye9+97vMmzdvm38ouuaaa3LRRRelpqYmxx9/fNasWZP58+dnxYoVGT169DaN0aJFi5x//vm5/PLL06ZNm3Ts2DHf+9738t577+Xss8/epjEAAAAA4JOq+EzuGTNmpH379uncuXOOP/74PPbYY7n55ptz3333bXWphE+qbdu2mTJlSv7lX/4lBxxwQMaNG5cbb7xxu55jgyOOOCK33357JkyYkJ49e+aRRx7JVVdd1ajPkCFDMmHChNx444058MADc+utt2by5Mnp379/kmS33XbL7bffnqOOOio9evTI7Nmz88ADDzSsE70pq1atSvv27TfaPqsZ6x81adKkrFixIr17985ZZ52Viy66KHvuuWfD/iZNmmT69Ol5//33c/jhh+ecc87JP/zDPzQaY9ddd83MmTPzzjvv5LDDDsupp56a4447LhMnTmzY/9JLL+WUU05J165d8zd/8zcZOXJkzjvvvCxevDivvvpqBg4cuNVa27Rpk+HDh2fs2LFZv359Jk+enOHDh+fSSy9Nt27dMmTIkMybNy8dO3ZMklx11VXp3bt3Bg4cmP79+2evvfbKkCFDPvE1+ujns//+++emm27Kt7/97Y3C/o876aSTcskll+SCCy7IIYcckqeeeirf+ta3GvZXV1dn+fLlGT58eLp27ZrTTz89J5xwQq655pptquucc87JD3/4w0yePDkHH3xwjjnmmEyZMuUTzeROknHjxuWUU07JWWedld69e+fVV1/NzJkzs/vuu3+icQAAAABgW1UVRVFUugjYHr7//e9n9uzZ+cUvflHpUviUVq1a9f8fdrkySeutdQfYIfgvKQAAgO1vQ060cuXKtG695Zyo4jO5YXvZe++9c8UVV1S6DAAAAADgf1HF1+SG7eX000+vdAkAAAAAwP8yM7kBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAA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TJ48eZNj1dfX5+tf/3q6d++eJUuWbPacO+20U/baa6/svffeOeOMMzJs2LDcf//9ST6c6X3IIYfkhz/8YfbZZ5/ssssuSTZermTNmjX5u7/7u3To0CHNmjVLly5dMmnSpIb9L7zwQk444YS0bNky7dq1y1lnnZW33377U14lAIDKEXIDAABswbRp09K9e/d069YtZ555Zn70ox+lKIqG/d/61rfyn//5n3n44YezaNGi3HLLLfnc5z630Thr1qzJaaedloULF+Zf//Vf07Fjx22uoXnz5g0ztpPk1Vdfzd1335177rlns+t9Dx8+PD/72c9y8803Z9GiRbn11lvTsmXLJMl///d/59hjj02vXr0yf/78zJgxI8uWLcvpp5++zTUBAOwodqp0AQAAADuySZMm5cwzz0ySHH/88Vm5cmXmzJmT/v37J0mWLFmSXr16pU+fPkmSzp07bzRGXV1dBg0alDVr1uSxxx5LTU3NNp9/wYIFufPOO3Psscc2tK1duzY//vGP07Zt200e88orr2TatGmZNWtWBgwYkCTZd999G/ZPnDgxvXr1yne/+92Gth/96Efp0KFDXnnllXTt2nWb6wMAqDQzuQEAADbj5ZdfzjPPPJOhQ4cm+XAZkTPOOKPRsh/nn39+pk6dmkMOOSR/+7d/m6eeemqjcYYOHZrVq1fnkUce2aaA+/nnn0/Lli3TvHnzHH744enXr18mTpzYsL9Tp06bDbiTZOHChamurs4xxxyzyf3PPfdcHnvssbRs2bJh6969e5Jk8eLFW60PAGBHYiY3AADAZkyaNCnr1q1LbW1tQ1tRFGnWrFkmTpyYmpqanHDCCfntb3+bX/ziF5k1a1aOO+64jBw5MjfeeGPDMSeeeGLuuOOOzJ07t9GM7M3p1q1b7r///uy0006pra1N06ZNG+1v0aLFFo9v3rz5FvfX1dVl8ODBuf766zfa1759+63WBwCwIzGTGwAAYBPWrVuXH//4x7npppuycOHChu25555LbW1tfvaznzX0bdu2bUaMGJE77rgj48ePz2233dZorPPPPz/jxo3LSSedlDlz5mz13E2bNk2XLl3SuXPnjQLubXHwwQdn/fr1mz1X79698+KLL6Zz587p0qVLo21rAToAwI5GyA0AALAJDz74YFasWJGzzz47Bx10UKPtlFNOaViy5Oqrr859992XV199NS+++GIefPDB7L///huNd+GFF+Y73/lOvvKVr+RXv/rVZ1p7586dM2LEiHz961/Pvffem9deey2PP/54pk2bliQZOXJk3nnnnQwdOjTz5s3L4sWLM3PmzHzta19LfX39Z1obAMD2JuQGAADYhEmTJmXAgAGbXEP7lFNOyfz58/Mf//Efadq0aa644or06NEjRx99dKqrqzN16tRNjjlq1Khcc801OfHEEze5dvf2dMstt+TUU0/NN7/5zXTv3j3nnntuVq9enSSpra3Nk08+mfr6+nz5y1/OwQcfnFGjRmW33XZLkyb+mggAlEtVURRFpYsAAAAAAIBPw0/0AAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBa/w9AOTIYxo0+3wAAAABJRU5ErkJggg==)
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
4.2 What is the TOP 10 locations BRL has + value?
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[9\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    import matplotlib.pyplot as plt

    query = """
        SELECT 
            name
            ,round(avg(ask),2) AvgAsk
        FROM df 
        where codein = 'BRL'
        and not code in ('BTC', 'ETH', 'LTC')
        group by name
        order by avg(ask) limit 10
    """

    newDf = sqldf(query, locals())
    newDf.sort_values(by='AvgAsk', ascending=False, inplace=True)

    AvgAskByCurrency = newDf.plot(
        kind='barh', x='name', y='AvgAsk', 
        figsize=(15, 10), 
        legend=False, 
        color='blue', title='Top 10 Most Valuable Currencies by Ask Price', xlabel='Ask Price', ylabel='Symbol')


    # Adicionando rótulos aos dados
    for index, value in enumerate(newDf['AvgAsk']):
        plt.text(value, index, str(value))

    # Exibir o gráfico
    plt.show()
:::
:::
:::
:::
:::

::: {.jp-Cell-outputWrapper}
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::: {.jp-OutputArea .jp-Cell-outputArea}
::: {.jp-OutputArea-child}
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedImage .jp-OutputArea-output tabindex="0"}
![No description has been provided for this
image](data:image/png;base64,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XLlymjRpksOYtDxXAAD8HczkBgAAwL+CMUbNmjXT+vXr1bVrV1WoUEGrVq3S4MGD9euvvyYLqjZu3Ki5c+cqIiJCbm5umjx5sho1aqStW7eqbNmyD6SmXbt2qVKlSnJycpxbUq1aNX388cc6fPiwgoKC7nueDh06aPjw4dqwYYOeeOIJSX/Niq5fv75y586dbPz+/fv1+OOPy8fHRy+//LKyZMmiqVOnKiQkRBs3blT16tUl/fVSxzFjxqhbt26qVq2a4uPjtX37du3cuVMNGjRQz5499dtvv6XYFiYlXl5eat68uebPn68///xTOXLksO+bO3euEhIS1LFjR0nSvHnzdPXqVfXq1Us5c+bU1q1b9f777+uXX37RvHnz7nuttNi2bZu2bNmiZ555Ro899piOHz+uKVOmKCQkRAcOHEg2q7lv377Kli2bhg8frkOHDmnKlCk6ceKEPdxLSWJiopo1a6Zvv/1WPXr0UGBgoPbu3asJEybo8OHDWrRoUar1HTlyRAcPHtTzzz8vb2/vB3LPdzp//ryefPJJPfPMM3r22WeVJ08e+76oqChdv35dPXr0kJubm3LkyKH9+/erdu3aKlCggIYMGSIvLy99+eWXatGihb766iu1bNnS4fz9+vVT9uzZFRkZqePHj2vixInq27ev5s6dax8zY8YMPf/88ypTpoyGDh2qbNmyadeuXVq5cuU9W7D07NlTM2bMUJcuXRQREaFjx47pgw8+0K5du7R582ZlyZJF586dU8OGDeXn56chQ4YoW7ZsOn78eJrD3iNHjqhdu3Z64YUXFB4erqioKLVp00YrV65UgwYNVLRoUdWuXVvR0dF68cUXHY6Njo6Wt7e3mjdvft/rREdHq1ixYqpatarKli0rT09PffHFFxo8eLB9TEbuJSEhQc8//7zmzp1r/1sd6XXhwgVduHBBxYsXd9g+atQoubq6atCgQbpx40aqs/zXrFmjJk2aKF++fOrfv7/y5s2r2NhYLV26VP3795ekdD9XAABkiAEAAAAsqE+fPubO/5xdtGiRkWTeeOMNh3GtW7c2NpvN/PTTT/Ztkowks337dvu2EydOGHd3d9OyZct01eHl5WXCw8NT3ff8888n275s2TIjyaxcufKe5w4ODjZlypQxxhhTpUoV07VrV2OMMRcuXDCurq5m5syZZv369UaSmTdvnv24Fi1aGFdXV3P06FH7tt9++814e3ubunXr2reVL1/ePPXUU/es4e7P+X6S7m3q1KkO22vUqGEKFChgEhISjDHGXL16NdmxY8aMMTabzZw4ccK+LTIy0uH6x44dM5JMVFRUsuMlmcjISPt6Stf47rvvjCTz2Wef2bdFRUUZSaZy5crm5s2b9u1vv/22kWRiYmLs24KDg01wcLB9fdasWcbJycls2rTJ4TofffSRkWQ2b96crIYkMTExRpKZMGFCqmPulFTnsWPHHLYnPQPr1693qFOS+eijjxzGJn1+Pj4+5ty5cw776tevb4KCgsz169ft2xITE02tWrVMQEBAsjpCQ0NNYmKiffuLL75onJ2dzcWLF40xxly8eNF4e3ub6tWrm2vXrjlc687jwsPDjb+/v31906ZNRpKJjo52OGblypUO2xcuXGgkmW3btqX2kaXK39/fSDJfffWVfVtcXJzJly+fqVixon3b1KlTjSQTGxtr33bz5k2TK1euVH/u73Tz5k2TM2dO8+qrr9q3dejQwZQvX95hXFruJem7e+edd8ytW7dMu3btjIeHh1m1alUa7vivn4+uXbua33//3Zw7d8788MMPpn79+kaSGT9+vDHm/56lokWLJvv5ufs5u337tilSpIjx9/c3Fy5ccBh75/eb1ucKAIC/g3YlAAAA+FdYvny5nJ2dFRER4bD9pZdekjFGK1ascNhes2ZNVa5c2b5eqFAhNW/eXKtWrVJCQsIDqenatWtyc3NLtj2pr+39WnPcqUOHDlqwYIFu3ryp+fPny9nZOcUZkAkJCVq9erVatGihokWL2rfny5dPHTp00Lfffqv4+HhJUrZs2bR//34dOXIkvbeWqqTZqHe2ozh27Ji+//57tW/f3j6r3cPDw77/ypUr+uOPP1SrVi0ZY7Rr164HUsud17h165bOnz+v4sWLK1u2bNq5c2ey8T169HBoGdKrVy+5uLho+fLlqV5j3rx5CgwMVKlSpfTHH3/Yl6QZ9+vXr0/12KTv4WHM4pYkNzc3denSJcV9rVq1kp+fn339zz//1Ndff622bdvq0qVL9vs4f/68wsLCdOTIEf36668O5+jRo4fDDPfHH39cCQkJOnHihKS/ZvleunRJQ4YMSdbL+V5tb+bNmydfX181aNDA4TOtXLmysmbNav9Ms2XLJklaunRphvqW58+f3+Fn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QrLzJP1tgbS0LPntt9+0cOFC+3p8fLw+++wzVahQQXnz5rVvd3FxUfv27fXll19qxowZCgoKUrly5e57/s8//1xFixbVCy+8oNatWzssgwYNUtasWe2z1dN7L6GhoZozZ45Wrlyp55577oH9zYT0qFSpkooUKaKJEycm+/Mh6V4exnMFAEBKmMkNAACAf4WmTZuqXr16evXVV3X8+HGVL19eq1evVkxMjAYMGGAPCJOULVtWYWFhioiIkJubmz0kHTFixH2vtWTJEu3Zs0fSXy80/PHHH/XGG29Ikpo1a2YPwFq3bq0aNWqoS5cuOnDggHLlyqXJkycrISEhTde5m6+vr4YPH37fcW+88YbWrFmjOnXqqHfv3nJxcdHUqVN148YNvf322/ZxpUuXVkhIiCpXrqwcOXJo+/btmj9/vvr27Wsfk/RyzoiICIWFhcnZ2VnPPPPMfWt49tlnNXLkSMXExKh27doOM2NLlSqlYsWKadCgQfr111/l4+Ojr776yt7L+X66deumsWPHqlu3bqpSpYq++eYb+wzcOzVp0kSzZs2Sr6+vSpcure+++05r165Vzpw5UzzvzZs3Vb9+fbVt21aHDh3S5MmTVadOHTVr1izVWp577jl9+eWXeuGFF7R+/XrVrl1bCQkJOnjwoL788kutWrVKVapUSfX4du3aae/evRo9erR27dql9u3by9/fX+fPn9fKlSu1bt06ez/oMmXKqEaNGho6dKj+/PNP5ciRQ3PmzEkxHM+IDz/8UHXq1FFQUJC6d++uokWL6uzZs/ruu+/0yy+/2J/5tPLx8dGECRPUrVs3Va1aVR06dFD27Nm1Z88eXb16VTNnzkzxuODgYPXs2VNjxozR7t271bBhQ2XJkkVHjhzRvHnzNGnSJLVu3VozZ87U5MmT1bJlSxUrVkyXLl3StGnT5OPjc8/Z90lKlCihrl27atu2bcqTJ4+mT5+us2fPKioqKtnYTp066b333tP69ev11ltv3ffcv/32m9avX5/sRbhJ3NzcFBYWpnnz5um9997L0L20aNFCUVFR6tSpk3x8fDR16tT71vUgOTk5acqUKWratKkqVKigLl26KF++fDp48KD279+vVatWSXrwzxUAACkyAAAAgAX16dPH3P2fs5cuXTIvvviiyZ8/v8mSJYsJCAgw77zzjklMTHQYJ8n06dPHfP755yYgIMC4ubmZihUrmvXr16fp2uHh4UZSiktUVJTD2D///NN07drV5MyZ03h6eprg4GCzbdu2NF0nODjYlClT5p5j1q9fbySZefPmOWzfuXOnCQsLM1mzZjWenp6mXr16ZsuWLQ5j3njjDVOtWjWTLVs24+HhYUqVKmVGjx5tbt68aR9z+/Zt069fP+Pn52dsNluyz/xeqlataiSZyZMnJ9t34MABExoaarJmzWpy5cplunfvbvbs2ZPsM4yMjEx2zatXr5quXbsaX19f4+3tbdq2bWvOnTtnJJnIyEj7uAsXLpguXbqYXLlymaxZs5qwsDBz8OBB4+/vb8LDw+3joqKijCSzceNG06NHD5M9e3aTNWtW07FjR3P+/HmHawcHB5vg4GCHbTdv3jRvvfWWKVOmjHFzczPZs2c3lStXNiNGjDBxcXFp+qzWrVtnmjdvbnLnzm1cXFyMn5+fadq0qYmJiXEYd/ToURMaGmrc3NxMnjx5zCuvvGLWrFljJDk8v6k9O8eOHTOSzDvvvJNiHUePHjWdOnUyefPmNVmyZDEFChQwTZo0MfPnz0/2ed39HCc9i3f/HC1evNjUqlXLeHh4GB8fH1OtWjXzxRdf2PeHh4cbf3//ZLV8/PHHpnLlysbDw8N4e3uboKAg8/LLL5vffvvNGPPXM96+fXtTqFAh4+bmZnLnzm2aNGlitm/fnuK93cnf39889dRTZtWqVaZcuXLGzc3NlCpVKtnP0Z3KlCljnJyczC+//HLf848fP95IMuvWrUt1zIwZM4wkExMTk6Z7Se27mzx5spFkBg0adM+akv7cu5fU/jy5c9/d3++3335rGjRoYLy9vY2Xl5cpV66cef/99x3GpOW5AgDg77AZ8zffCgIAAABYjM1mU58+fZK1NgGA1FSsWFE5cuTQunXrMrsUAABwF3pyAwAAAABwD9u3b9fu3bsdXpQKAAAeHfTkBgAAAAAgBfv27dOOHTs0fvx45cuXT+3atcvskgAAQAqYyQ0AAAAAQArmz5+vLl266NatW/riiy/k7u6e2SUBAIAU0JMbAAAAAAAAAGBZzOQGAAAAAAAAAFgWITcAAAAAAAAAwLJ48SSAR0ZiYqJ+++03eXt7y2azZXY5AAAAAAAAyCTGGF26dEn58+eXk9O952oTcgN4ZPz2228qWLBgZpcBAAAAAACAR8SpU6f02GOP3XMMITeAR4a3t7ekv/7w8vHxyeRqAAAAAAAAkFni4+NVsGBBe150L4TcAB4ZSS1KfHx8CLkBAAAAAACQppa2vHgSAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJblktkFAMDdfH0zuwLg7zMmsysAAAAAAOC/gZncAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwDwEH344YcqXLiw3N3dVb16dW3duvWe4ydOnKiSJUvKw8NDBQsW1Isvvqjr16+nOHbs2LGy2WwaMGDAQ6gcAAAAAABrIOQGAOAhmTt3rgYOHKjIyEjt3LlT5cuXV1hYmM6dO5fi+NmzZ2vIkCGKjIxUbGysPv30U82dO1evvPJKsrHbtm3T1KlTVa5cuYd9GwAAAAAAPNIIuQEAeEjeffddde/eXV26dFHp0qX10UcfydPTU9OnT09x/JYtW1S7dm116NBBhQsXVsOGDdW+fftks78vX76sjh07atq0acqePfs/cSsAAAAAADyyCLkBAHgIbt68qR07dig0NNS+zcnJSaGhofruu+9SPKZWrVrasWOHPdT++eeftXz5cjVu3NhhXJ8+ffTUU085nBsAAAAAgP8qQm48smw2mxYtWpTZZaRJ586d1aJFi8wuI0UbNmyQzWbTxYsXJUkzZsxQtmzZ0nUOK30XwKPijz/+UEJCgvLkyeOwPU+ePDpz5kyKx3To0EEjR45UnTp1lCVLFhUrVkwhISEO7UrmzJmjnTt3asyYMQ+1fgAAAAAArIKQ+1+ic+fOstlsstlsypIli/LkyaMGDRpo+vTpSkxMzOzyMuT06dN68skn033cxo0bVbBgQUnJP5ciRYro5ZdfTvUlbg9LUtCctHh4eKhMmTL6+OOPH/q1a9WqpdOnT8vX1zfD58jodwEgfTZs2KA333xTkydP1s6dO7VgwQItW7ZMo0aNkiSdOnVK/fv3V3R0tNzd3TO5WgAAAAAAHg0umV0AHpxGjRopKipKCQkJOnv2rFauXKn+/ftr/vz5Wrx4sVxcrPV1582bN0PHxcTEqGnTpvb1pM/l1q1b2rFjh8LDw2Wz2fTWW289qFLT7NChQ/Lx8dG1a9e0ZMkS9erVS8WKFVP9+vVTHH/z5k25urr+rWu6urpm+LNMcr/jb926pSxZsvytawD/Nrly5ZKzs7POnj3rsP3s2bOp/kwNGzZMzz33nLp16yZJCgoK0pUrV9SjRw+9+uqr2rFjh86dO6dKlSrZj0lISNA333yjDz74QDdu3JCzs/PDuykAAAAAAB5BzOT+F3Fzc1PevHlVoEABVapUSa+88opiYmK0YsUKzZgxwz7u5MmTat68ubJmzSofHx+1bds2WQjzxhtvKHfu3PL29la3bt00ZMgQVahQwWHMJ598osDAQLm7u6tUqVKaPHmyw/5ffvlF7du3V44cOeTl5aUqVarohx9+sO+fMmWKihUrJldXV5UsWVKzZs1yOP7OFhnHjx+XzWbTggULVK9ePXl6eqp8+fIp9rVdvHixmjVrluxzKViwoFq0aKHQ0FCtWbPGvj8xMVFjxoxRkSJF5OHhofLly2v+/Pn2/QkJCeratat9f8mSJTVp0qR7fxmpyJ07t/LmzasiRYooIiJCRYoU0c6dO+37Q0JC1LdvXw0YMEC5cuVSWFiYpL9eXhcUFCQvLy8VLFhQvXv31uXLl+3HnThxQk2bNlX27Nnl5eWlMmXKaPny5ZKStytJSUxMjCpVqiR3d3cVLVpUI0aM0O3bt+37U/ou5s6dq+DgYLm7uys6OlqJiYkaOXKkHnvsMbm5ualChQpauXJlhj4n4N/A1dVVlStX1rp16+zbEhMTtW7dOtWsWTPFY65evSonJ8d/NSeF1sYY1a9fX3v37tXu3bvtS5UqVdSxY0ft3r2bgBsAAAAA8J9kram9SLcnnnhC5cuX14IFC9StWzclJibaA+6NGzfq9u3b6tOnj9q1a6cNGzZIkqKjozV69GhNnjxZtWvX1pw5czR+/HgVKVLEft7o6Gi9/vrr+uCDD1SxYkXt2rVL3bt3l5eXl8LDw3X58mUFBwerQIECWrx4sfLmzaudO3faW6csXLhQ/fv318SJExUaGqqlS5eqS5cueuyxx1SvXr1U7+fVV1/VuHHjFBAQoFdffVXt27fXTz/9ZJ+lvn//fp07d05PPPFEisfv27dPW7Zskb+/v33bmDFj9Pnnn+ujjz5SQECAvvnmGz377LPy8/NTcHCwEhMT9dhjj2nevHnKmTOntmzZoh49eihfvnxq27Zthr4XY4xWrVqlkydPqnr16g77Zs6cqV69emnz5s32bU5OTnrvvfdUpEgR/fzzz+rdu7defvll+y8W+vTpo5s3b+qbb76Rl5eXDhw4oKxZs6aplk2bNqlTp05677339Pjjj+vo0aPq0aOHJCkyMjLV44YMGaLx48erYsWKcnd316RJkzR+/HhNnTpVFStW1PTp09WsWTPt379fAQEBKZ7jxo0bunHjhn09Pj4+TTUDVjFw4ECFh4erSpUqqlatmiZOnKgrV66oS5cukqROnTqpQIEC9v7aTZs21bvvvquKFSuqevXq+umnnzRs2DA1bdpUzs7O8vb2VtmyZR2u4eXlpZw5cybbDgAAAADAf4bBv0J4eLhp3rx5ivvatWtnAgMDjTHGrF692jg7O5uTJ0/a9+/fv99IMlu3bjXGGFO9enXTp08fh3PUrl3blC9f3r5erFgxM3v2bIcxo0aNMjVr1jTGGDN16lTj7e1tzp8/n2JNtWrVMt27d3fY1qZNG9O4cWP7uiSzcOFCY4wxx44dM5LMJ598kqzu2NhY+7bRo0eb1q1bO3wuzs7OxsvLy7i5uRlJxsnJycyfP98YY8z169eNp6en2bJli0MtXbt2Ne3bt0+xdmOM6dOnj2nVqpXDdVL7/I0xZv369UaS8fLyMl5eXsbFxcU4OTmZN954w2FccHCwqVixYqrnSTJv3jyTM2dO+3pQUJAZPnz4Pa994cIFY4wxUVFRxtfX176/fv365s0333Q4ZtasWSZfvnz29ZS+i4kTJzockz9/fjN69GiHbVWrVjW9e/dO9T4iIyONpBSWOCMZFhZLL0nef/99U6hQIePq6mqqVatmvv/+e/u+4OBgEx4ebl+/deuWGT58uClWrJhxd3c3BQsWNL1797b//KYkODjY9O/fP9X9AAAAAABYUVxcnJFk4uLi7juWmdz/AcYY2Ww2SVJsbKwKFixofzGjJJUuXVrZsmVTbGysqlatqkOHDql3794O56hWrZq+/vprSdKVK1d09OhRde3aVd27d7ePuX37tv3lhrt371bFihWVI0eOFGuKjY21zxZOUrt27fu2ASlXrpz9n/PlyydJOnfunEqVKiXpr7Ybffv2dTimXr16mjJliq5cuaIJEybIxcVFrVq1kiT99NNPunr1qho0aOBwzM2bN1WxYkX7+ocffqjp06fr5MmTunbtmm7evJmsfUtabNq0Sd7e3rpx44a2bt2qvn37KkeOHOrVq5d9TOXKlZMdt3btWo0ZM0YHDx5UfHy8bt++revXr+vq1avy9PRURESEevXqpdWrVys0NFStWrVy+KzuZc+ePdq8ebNGjx5t35aQkOBw/pRUqVLF/s/x8fH67bffVLt2bYcxtWvX1p49e1K99tChQzVw4ECH89z5bAL/Bn379k3251KSpL9Bk8TFxUWRkZH3/FsU9zsHAAAAAAD/NYTc/wGxsbEOrUb+rqRe0NOmTUvWaiOpH6yHh8cDu96d7ny5YVJwn9QC5fTp09q1a5eeeuoph2O8vLxUvHhxSdL06dNVvnx5ffrpp+ratav9XpYtW6YCBQo4HOfm5iZJmjNnjgYNGqTx48erZs2a8vb21jvvvOPQXzytihQpomzZskmSypQpox9++EGjR492CLm9vLwcjjl+/LiaNGmiXr16afTo0cqRI4e+/fZbde3aVTdv3pSnp6e6deumsLAwLVu2TKtXr9aYMWM0fvx49evX7741Xb58WSNGjNDTTz+dbJ+7u3uqx91dZ0a4ubnZP2cAAAAAAAAgI3jx5L/c119/rb1799pnLgcGBurUqVM6deqUfcyBAwd08eJFlS5dWpJUsmRJbdu2zeE8d67nyZNH+fPn188//6zixYs7LElherly5bR79279+eefKdYVGBjo0HNakjZv3myvISOWLFmiWrVqpTp7XPqrt/Urr7yi1157TdeuXVPp0qXl5uamkydPJruXpBnFmzdvVq1atdS7d29VrFhRxYsX19GjRzNc552cnZ117dq1e47ZsWOHEhMTNX78eNWoUUMlSpTQb7/9lmxcwYIF9cILL2jBggV66aWXNG3atDTVUKlSJR06dCjZ/RcvXjzZC/BS4+Pjo/z58z/w7xQAAAAAAAC4H2Zy/4vcuHFDZ86cUUJCgs6ePauVK1dqzJgxatKkiTp16iRJCg0NVVBQkDp27KiJEyfq9u3b6t27t4KDg+3tJ/r166fu3burSpUqqlWrlubOnasff/xRRYsWtV9rxIgRioiIkK+vrxo1aqQbN25o+/btunDhggYOHKj27dvrzTffVIsWLTRmzBjly5dPu3btUv78+VWzZk0NHjxYbdu2VcWKFRUaGqolS5ZowYIFWrt2bYbvf/HixWrWrNl9x7Vp00aDBw/Whx9+qEGDBmnQoEF68cUXlZiYqDp16iguLk6bN2+Wj4+PwsPDFRAQoM8++0yrVq1SkSJFNGvWLG3bti1Ds+PPnTun69ev29uVzJo1S61bt77nMcWLF9etW7f0/vvvq2nTptq8ebM++ugjhzEDBgzQk08+qRIlSujChQtav369AgMD01TT66+/riZNmqhQoUJq3bq1nJyctGfPHu3bt09vvPFGmu9t8ODBioyMVLFixVShQgVFRUVp9+7dio6OTvM5AAAAAAAAgPRiJve/yMqVK5UvXz4VLlxYjRo10vr16/Xee+8pJibG3kbEZrMpJiZG2bNnV926dRUaGqqiRYtq7ty59vN07NhRQ4cO1aBBg1SpUiUdO3ZMnTt3dmhd0a1bN33yySeKiopSUFCQgoODNWPGDHvw6+rqqtWrVyt37txq3LixgoKCNHbsWHsdLVq00KRJkzRu3DiVKVNGU6dOVVRUlEJCQjJ071euXNG6devSFHK7uLiob9++evvtt3XlyhWNGjVKw4YN05gxYxQYGKhGjRpp2bJl9nvp2bOnnn76abVr107Vq1fX+fPnk/UsT6uSJUsqX758Kl68uP73v/+pZ8+eev/99+95TPny5fXuu+/qrbfeUtmyZRUdHa0xY8Y4jElISFCfPn3s9ZcoUUKTJ09OU01hYWFaunSpVq9erapVq6pGjRqaMGGC/P3903VvERERGjhwoF566SUFBQVp5cqVWrx4sQICAtJ1HgAAAAAAACA9bMYYk9lF4NHXoEED5c2bV7NmzcrsUlK0YMECvfbaazpw4EBml4K/IT4+/v+/vDROkk9mlwP8LfzbFQAAAACAjEvKieLi4uTjc++ciHYlSObq1av66KOPFBYWJmdnZ33xxRdau3at1qxZk9mlpSpr1qx66623MrsMAAAAAAAAAP8wQm4kY7PZtHz5co0ePVrXr19XyZIl9dVXXyk0NDSzS0tVw4YNM7sEAAAAAAAAAJmAkBvJeHh4/K0XQAIAAAAAAADAP4UXTwIAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJblktkFAMDd4uIkH5/MrgIAAAAAAABWwExuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAluWS2QUAwN18fTO7AgBIO2MyuwIAAAAA+G9jJjcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAPwDfffKOmTZsqf/78stlsWrRoUZqP3bx5s1xcXFShQgWH7WPGjFHVqlXl7e2t3Llzq0WLFjp06NCDLRwAAAAALI6QGwAA4AG4cuWKypcvrw8//DBdx128eFGdOnVS/fr1k+3buHGj+vTpo++//15r1qzRrVu31LBhQ125cuVBlQ0AAAAAlmczxpjMLgIAJCk+Pl6+vr6S4iT5ZHY5AJAmKf2XlM1m08KFC9WiRYv7Hv/MM88oICBAzs7OWrRokXbv3p3q2N9//125c+fWxo0bVbdu3YwXDQAAAACPuKScKC4uTj4+986JmMkNAACQSaKiovTzzz8rMjIyTePj4uIkSTly5HiYZQEAAACApbhkdgEAAAD/RUeOHNGQIUO0adMmubjc/z/JEhMTNWDAANWuXVtly5b9ByoEAAAAAGuwzEzutLzAqXPnzmn6a8GZZcaMGcqWLVtml5FuGzZskM1m08WLFx/K+dP7cq5HVUhIiAYMGJDZZaTo7mdv+PDhyV5udi/Hjx+XzWa751+hBwCkXUJCgjp06KARI0aoRIkSaTqmT58+2rdvn+bMmfOQqwMAAAAAa8nUkLtz586y2Wyy2WzKkiWL8uTJowYNGmj69OlKTEx0GHv69Gk9+eSTmVSpNcyYMcP+ed65uLu7/63z1qpVS6dPn/7/vZKtYebMmapTp46kv8LnOz+LEiVKaMyYMfqn29Hf/f1kzZpVlStX1oIFCx76tdu1a6fDhw9n+PiCBQvq9OnTzBwEgAfk0qVL2r59u/r27SsXFxe5uLho5MiR2rNnj1xcXPT11187jO/bt6+WLl2q9evX67HHHsukqgEAAADg0ZTp7UoaNWqkqKgoJSQk6OzZs1q5cqX69++v+fPna/Hixfa/vps3b957nufWrVv/RLmPPB8fHx06dMhhm81m+1vndHV1vefnn5CQIJvNJienR+cvBsTExKhZs2b29e7du2vkyJG6ceOGvv76a/Xo0UPZsmVTr169/tG67vx+Ll26pKioKLVt21b79+9XyZIlUzzm5s2bcnV1/VvX9fDwkIeHR4aPd3Z2vuczYIxRQkJCmv66PQDgr38f7N2712Hb5MmT9fXXX2v+/PkqUqSIpL/+fO3Xr58WLlyoDRs22LcDAAAAAP5PpqeSbm5uyps3rwoUKKBKlSrplVdeUUxMjFasWKEZM2bYx93Z0iKpdcLcuXMVHBwsd3d3RUdH28eOGzdO+fLlU86cOdWnTx+HAHzWrFmqUqWKvL29lTdvXnXo0EHnzp2z709qzbFq1SpVrFhRHh4eeuKJJ3Tu3DmtWLFCgYGB8vHxUYcOHXT16tV73tuMGTNUqFAheXp6qmXLljp//nyyMVOmTFGxYsXk6uqqkiVLatasWfZ9xhgNHz5chQoVkpubm/Lnz6+IiIh7XtNmsylv3rwOS548eez7Q0JC1K9fPw0YMEDZs2dXnjx5NG3aNF25ckVdunSRt7e3ihcvrhUrViT7TJLalSS1vli8eLFKly4tNzc3nTx5Utu2bVODBg2UK1cu+fr6Kjg4WDt37nSo78iRI6pbt67c3d1VunRprVmzJtk97N27V0888YQ8PDyUM2dO9ejRQ5cvX3aop1q1avLy8lK2bNlUu3ZtnThxwr7/+vXrWr16tUPI7enpqbx588rf319dunRRuXLlHK5948YNDRo0SAUKFJCXl5eqV6+uDRs22PefP39e7du3V4ECBeTp6amgoCB98cUX9/wu7vf9BAQE6I033pCTk5N+/PFH+5jChQtr1KhR6tSpk3x8fNSjRw9J0v/+9z+VKFFCnp6eKlq0qIYNG+bwbO/Zs0f16tWTt7e3fHx8VLlyZW3fvl1S2lrlfPLJJwoMDJS7u7tKlSqlyZMn2/fd3a4k6ZlYsWKFKleuLDc3N3377be6ceOGIiIilDt3brm7u6tOnTratm1bqte8ceOG4uPjHRYAsKrLly9r9+7d9j8rjx07pt27d+vkyZOSpKFDh6pTp06SJCcnJ5UtW9ZhSfqzs2zZsvLy8pL0V4uSzz//XLNnz5a3t7fOnDmjM2fO6Nq1a5lyjwAAAADwKMr0kDslTzzxhMqXL3/fNg5DhgxR//79FRsbq7CwMEnS+vXrdfToUa1fv14zZ87UjBkzHMLyW7duadSoUdqzZ48WLVqk48ePq3PnzsnOPXz4cH3wwQfasmWLTp06pbZt22rixImaPXu2li1bptWrV+v9999PtbYffvhBXbt2Vd++fbV7927Vq1dPb7zxhsOYhQsXqn///nrppZe0b98+9ezZU126dNH69eslSV999ZUmTJigqVOn6siRI1q0aJGCgoLS+CmmbubMmcqVK5e2bt2qfv36qVevXmrTpo1q1aqlnTt3qmHDhnruuefuGeJfvXpVb731lj755BPt379fuXPn1qVLlxQeHq5vv/1W33//vQICAtS4cWNdunRJ0l8vzHr66afl6uqqH374QR999JH+97//OZz3ypUrCgsLU/bs2bVt2zbNmzdPa9euVd++fSVJt2/fVosWLRQcHKwff/xR3333nXr06OEwW33dunUqUKCASpUqlaxuY4w2bdqkgwcPOsyO7tu3r7777jvNmTNHP/74o9q0aaNGjRrpyJEjkv4KzitXrqxly5Zp37596tGjh5577jlt3bo1w99DQkKCZs6cKUmqVKmSw75x48apfPny2rVrl4YNGyZJ8vb21owZM3TgwAFNmjRJ06ZN04QJE+zHdOzYUY899pi2bdumHTt2aMiQIcqSJUuaaomOjtbrr7+u0aNHKzY2Vm+++aaGDRtmry81Q4YM0dixYxUbG6ty5crp5Zdf1ldffaWZM2dq586dKl68uMLCwvTnn3+mePyYMWPk6+trXwoWLJimegHgUbR9+3ZVrFhRFStWlCQNHDhQFStW1Ouvvy7pr9ZrSYF3Wk2ZMkVxcXEKCQlRvnz57MvcuXMfeP0AAAAAYFkmE4WHh5vmzZunuK9du3YmMDDQvi7JLFy40BhjzLFjx4wkM3HixGTn8/f3N7dv37Zva9OmjWnXrl2qNWzbts1IMpcuXTLGGLN+/Xojyaxdu9Y+ZsyYMUaSOXr0qH1bz549TVhYWKrnbd++vWncuHGye/L19bWv16pVy3Tv3t1hTJs2bezHjR8/3pQoUcLcvHkz1evcKSoqykgyXl5eDkujRo3sY4KDg02dOnXs67dv3zZeXl7mueees287ffq0kWS+++47Y8z/fSYXLlxwuM7u3bvvWU9CQoLx9vY2S5YsMcYYs2rVKuPi4mJ+/fVX+5gVK1Y4fLcff/yxyZ49u7l8+bJ9zLJly4yTk5M5c+aMOX/+vJFkNmzYkOp1u3fvbgYNGuRwz1myZDFeXl4mS5YsRpJxd3c3mzdvNsYYc+LECePs7OxQlzHG1K9f3wwdOjTV6zz11FPmpZdecrhO//79Ux1/9/fj5ORk3NzcTFRUlMM4f39/06JFi1TPk+Sdd94xlStXtq97e3ubGTNmpHrtO5+9yMhIU758eft6sWLFzOzZsx2OGTVqlKlZs6Yx5v9+5nbt2mWM+b9nYtGiRfbxly9fNlmyZDHR0dH2bTdv3jT58+c3b7/9dop1Xb9+3cTFxdmXU6dOGUlGijOSYWFhYbHEAgAAAAB48OLi4owkExcXd9+xj2wDXWPMfXtJV6lSJdm2MmXKyNnZ2b6eL18+h56XO3bs0PDhw7Vnzx5duHDB/oLLkydPqnTp0vZx5cqVs/9znjx57C0i7tx2r1m8sbGxatmypcO2mjVrauXKlQ5jklpRJKldu7YmTZokSWrTpo0mTpyookWLqlGjRmrcuLGaNm16z77H3t7eyVqE3N2L+c57c3Z2Vs6cOR1miCe1N7mzjcvdXF1dHc4jSWfPntVrr72mDRs26Ny5c0pISNDVq1fts9ZiY2NVsGBB5c+f3+EzuVNsbKzKly9v/2vaSZ9JYmKiDh06pLp166pz584KCwtTgwYNFBoaqrZt2ypfvnyS/npulixZoi+//NLhvB07dtSrr76qCxcuKDIyUrVq1VKtWrUk/dUeJSEhQSVKlHA45saNG8qZM6ekv2Zdv/nmm/ryyy/166+/6ubNm7px44Y8PT1T/YxScuf3c/XqVa1du1YvvPCCcubMqaZNm9rHpfRsz507V++9956OHj2qy5cv6/bt2/Lx8bHvHzhwoLp166ZZs2YpNDRUbdq0UbFixe5b05UrV3T06FF17dpV3bt3t2+/ffv2fV82emedR48e1a1bt1S7dm37tixZsqhatWqKjY1N8Xg3Nze5ubndt0YAAAAAAAAgNY9syB0bG3vflyvdGYQmubs9g81mswfZSa0wwsLCFB0dLT8/P508eVJhYWG6efNmquex2Wz3PO/DUrBgQR06dEhr167VmjVr1Lt3b73zzjvauHFjqm0onJycVLx48XueN6V7uft+Jd3z/jw8PJL9EiI8PFznz5/XpEmT5O/vLzc3N9WsWTPZZ/t3RUVFKSIiQitXrtTcuXP12muvac2aNapRo4a2bt2q27dv2wPsJL6+vvbP5csvv1Tx4sVVo0YNhYaG6vLly3J2dtaOHTscfkEiSVmzZpUkvfPOO5o0aZImTpyooKAgeXl5acCAAem+t7u/n3Llymn16tV66623HELuu5/t7777Th07dtSIESMUFhYmX19fzZkzR+PHj7ePGT58uDp06KBly5ZpxYoVioyM1Jw5c5L9suVuSf3Op02bpurVqzvsu/vzuFtKP4MAAAAAAADAP+mR7Mn99ddfa+/evWrVqtUDPe/Bgwd1/vx5jR07Vo8//rhKlSp1z9nKf0dgYKB++OEHh23ff/99sjGbN2922LZ582aHGeUeHh5q2rSp3nvvPW3YsEHfffedw8z0R8nmzZsVERGhxo0bq0yZMnJzc9Mff/xh3x8YGKhTp07p9OnT9m0pfSZ79uzRlStXHM7r5OSkkiVL2rdVrFhRQ4cO1ZYtW1S2bFnNnj1bkhQTE6OnnnrqnuFs1qxZ1b9/fw0aNEjGGFWsWFEJCQk6d+6cihcv7rDkzZvXXkPz5s317LPPqnz58ipatKgOHz789z6w/8/Z2fm+LxDbsmWL/P399eqrr6pKlSoKCAhweNlmkhIlSujFF1/U6tWr9fTTTysqKuq+18+TJ4/y58+vn3/+Odn93+8XTXdKeoHqnc/0rVu3tG3bNodnGgAAAAAAAHiQMn0m940bN3TmzBklJCTo7NmzWrlypcaMGaMmTZqoU6dOD/RahQoVkqurq95//3298MIL2rdvn0aNGvVAr5EkIiJCtWvX1rhx49S8eXOtWrXKoVWJJA0ePFht27ZVxYoVFRoaqiVLlmjBggVau3atJGnGjBlKSEhQ9erV5enpqc8//1weHh7y9/dP9brGGJ05cybZ9ty5c8vJ6eH+TiMgIECzZs1SlSpVFB8fr8GDBzu0SgkNDVWJEiUUHh6ud955R/Hx8Xr11VcdztGxY0dFRkYqPDxcw4cP1++//65+/frpueeeU548eXTs2DF9/PHHatasmfLnz69Dhw7pyJEj9mdl8eLFGjly5H1r7dmzp0aNGqWvvvpKrVu3VseOHdWpUyeNHz9eFStW1O+//65169apXLlyeuqppxQQEKD58+dry5Ytyp49u959912dPXs23eHtnd/PtWvXtGbNGq1atcr+UrJ7fbYnT57UnDlzVLVqVS1btkwLFy6077927ZoGDx6s1q1bq0iRIvrll1+0bdu2NP+iaMSIEYqIiJCvr68aNWqkGzduaPv27bpw4YIGDhyYpnN4eXmpV69eGjx4sHLkyKFChQrp7bff1tWrV9W1a9c0nQMAAAAAAABIr0yfyb1y5Urly5dPhQsXVqNGjbR+/Xq99957iomJuW+rhPTy8/PTjBkzNG/ePJUuXVpjx47VuHHjHug1ktSoUUPTpk3TpEmTVL58ea1evVqvvfaaw5gWLVpo0qRJGjdunMqUKaOpU6cqKipKISEhkqRs2bJp2rRpql27tsqVK6e1a9dqyZIl9j7RKYmPj1e+fPmSLQ9rxvqdPv30U124cEGVKlXSc889p4iICOXOndu+38nJSQsXLtS1a9dUrVo1devWTaNHj3Y4h6enp1atWqU///xTVatWVevWrVW/fn198MEH9v0HDx5Uq1atVKJECfXo0UN9+vRRz549dfToUf30008KCwu7b605cuRQp06dNHz4cCUmJioqKkqdOnXSSy+9pJIlS6pFixbatm2bChUqJEl67bXXVKlSJYWFhSkkJER58+ZVixYt0v0Z3fn9BAYGavz48Ro5cmSysP9uzZo104svvqi+ffuqQoUK2rJli4YNG2bf7+zsrPPnz6tTp04qUaKE2rZtqyeffFIjRoxIU13dunXTJ598oqioKAUFBSk4OFgzZsxI10xuSRo7dqxatWql5557TpUqVdJPP/2kVatWKXv27Ok6DwAAAAAAAJBWNmOMyewigAfh3Xff1dq1a7V8+fLMLgUZFB8f//9fdhknyed+wwHgkcB/SQEAAADAg5eUE8XFxcnH5945UabP5AYelMcee0xDhw7N7DIAAAAAAAAA/IMyvSc38KC0bds2s0sAAAAAAAAA8A9jJjcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMtyyewCAOBucXGSj09mVwEAAAAAAAArYCY3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYlktaB7733ntpPmlERESGigEAAAAAAAAAID1sxhiTloFFihRJ2wltNv38889/qygA/03x8fHy9fVVXFycfHx8MrscAAAAAAAAZJL05ERpnsl97Nixv10YAAAAAAAAAAAP0t/uyW2MURongwMAAAAAAAAA8EBlOOT+7LPPFBQUJA8PD3l4eKhcuXKaNWvWg6wNAAAAAAAAAIB7SnO7kju9++67GjZsmPr27avatWtLkr799lu98MIL+uOPP/Tiiy8+0CIBAAAAAAAAAEhJml88eaciRYpoxIgR6tSpk8P2mTNnavjw4fTvBpAhvHgSAAAAAAAAUvpyogy1Kzl9+rRq1aqVbHutWrV0+vTpjJwSAAAAAAAAAIB0y1DIXbx4cX355ZfJts+dO1cBAQF/uygAAAAAAAAAANIiQz25R4wYoXbt2umbb76x9+TevHmz1q1bl2L4DQAAAAAAAADAw5ChmdytWrXSDz/8oFy5cmnRokVatGiRcuXKpa1bt6ply5YPukYAAAAAAAAAAFKUoRdPAsDDwIsnAQAAAAAAIKUvJ8pQuxJJSkhI0MKFCxUbGytJKl26tJo3by4XlwyfEgAAAAAAAACAdMlQIr1//341a9ZMZ86cUcmSJSVJb731lvz8/LRkyRKVLVv2gRYJAAAAAAAAAEBKMtSTu1u3bipTpox++eUX7dy5Uzt37tSpU6dUrlw59ejR40HXCAAAAAAAAABAijI0k3v37t3avn27smfPbt+WPXt2jR49WlWrVn1gxQEAAAAAAAAAcC8ZmsldokQJnT17Ntn2c+fOqXjx4n+7KAAAAAAAAAAA0iLNIXd8fLx9GTNmjCIiIjR//nz98ssv+uWXXzR//nwNGDBAb7311sOsFwAAAAAAAAAAO5sxxqRloJOTk2w2m3096bCkbXeuJyQkPOg6AfwHxMfHy9fXV3FxcfLx8cnscgAAAAAAAJBJ0pMTpbkn9/r16/92YQAAAAAAAAAAPEhpDrmDg4MfZh0AAAAAAAAAAKRbmkPuu12/fl0//vijzp07p8TERId9zZo1+9uFAQAAAAAAAABwPxkKuVeuXKlOnTrpjz/+SLaPntwAAAAAAAAAgH+KU0YO6tevn9q0aaPTp08rMTHRYSHgBgAAAAAAAAD8UzIUcp89e1YDBw5Unjx5HnQ9AAAAAAAAAACkWYZC7tatW2vDhg0PuBQAAAAAAAAAANLHZowx6T3o6tWratOmjfz8/BQUFKQsWbI47I+IiHhgBQL474iPj5evr6/i4uLk4+OT2eUAAAAAAAAgk6QnJ8rQiye/+OILrV69Wu7u7tqwYYNsNpt9n81mI+QGAAAAAAAAAPwjMhRyv/rqqxoxYoSGDBkiJ6cMdTwBAAAAAAAAAOBvy1BCffPmTbVr146AGwAAAAAAAACQqTKUUoeHh2vu3LkPuhYAAAAAAAAAANIlQ+1KEhIS9Pbbb2vVqlUqV65cshdPvvvuuw+kOAAAAAAAAAAA7iVDIffevXtVsWJFSdK+ffsc9t35EkoAAAAAAAAAAB6mDIXc69evf9B1AAAAAAAAAACQbhnqyR0VFaVr16496FoAAAAAAAAAAEiXDIXcQ4YMUZ48edS1a1dt2bLlQdcEAAAAAAAAAECaZCjk/vXXXzVz5kz98ccfCgkJUalSpfTWW2/pzJkzD7o+AAAAAAAAAABSlaGQ28XFRS1btlRMTIxOnTql7t27Kzo6WoUKFVKzZs0UExOjxMTEB10rAAAAAAAAAAAOMhRy3ylPnjyqU6eOatasKScnJ+3du1fh4eEqVqyYNmzY8ABKBAAAAAAAAAAgZRkOuc+ePatx48apTJkyCgkJUXx8vJYuXapjx47p119/Vdu2bRUeHv4gawUAAAAAAAAAwIHNGGPSe1DTpk21atUqlShRQt26dVOnTp2UI0cOhzHnzp1T3rx5aVsCIM3i4+Pl6+uruLg4+fj4ZHY5AAAAAAAAyCTpyYlcMnKB3Llza+PGjapZs2aqY/z8/HTs2LGMnB4AAAAAAAAAgDRJV7uS7777TkuXLtWnn35qD7g/++wzFSlSRLlz51aPHj1048YNSZLNZpO/v/+DrxgAAAAAAAAAgP8vXSH3yJEjtX//fvv63r171bVrV4WGhmrIkCFasmSJxowZ88CLBAAAAAAAAAAgJekKuXfv3q369evb1+fMmaPq1atr2rRpGjhwoN577z19+eWXD7xIAAAAAAAAAABSkq6Q+8KFC8qTJ499fePGjXryySft61WrVtWpU6ceXHUAAAAAAAAAANxDukLuPHny2F8mefPmTe3cuVM1atSw77906ZKyZMnyYCsEAAAAAAAAACAV6Qq5GzdurCFDhmjTpk0aOnSoPD099fjjj9v3//jjjypWrNgDLxIAAAAAAAAAgJS4pGfwqFGj9PTTTys4OFhZs2bVzJkz5erqat8/ffp0NWzY8IEXCQAAAAAAAABASmzGGJPeg+Li4pQ1a1Y5Ozs7bP/zzz+VNWtWh+AbANIqPj5evr6+iouLk4+PT2aXAwAAAAAAgEySnpwoXTO5k/j6+qa4PUeOHBk5HQAAAAAAAAAAGZKuntwAAAAAAAAAADxKCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBluWR2AQBwN1/fzK4AAAAAADLOmMyuAAD+W5jJDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAwAM2ZcoUlStXTj4+PvLx8VHNmjW1YsWKex4zceJElSxZUh4eHipYsKBefPFFXb9+3WHMr7/+qmeffVY5c+aUh4eHgoKCtH379od5KwDwyHPJ7AIAAAAAAAD+bR577DGNHTtWAQEBMsZo5syZat68uXbt2qUyZcokGz979mwNGTJE06dPV61atXT48GF17txZNptN7777riTpwoULql27turVq6cVK1bIz89PR44cUfbs2f/p2wOAR4rNGGMyuwgAkKT4+Hj5+vpKipPkk9nlAAAAAECGpJa05MiRQ++88466du2abF/fvn0VGxurdevW2be99NJL+uGHH/Ttt99KkoYMGaLNmzdr06ZND6VuAHiUJOVEcXFx8vG5d070n2lX8tNPP+nNN9/UtWvXMrsUAAAAAADwH5KQkKA5c+boypUrqlmzZopjatWqpR07dmjr1q2SpJ9//lnLly9X48aN7WMWL16sKlWqqE2bNsqdO7cqVqyoadOm/SP3AACPsv9EyH39+nW1bt1a+fPnl4eHh3378OHDVaFChX+sjsKFC2vixIkP/TozZsxQtmzZHvp18H/+6WcpPY4fPy6bzabdu3dLkjZs2CCbzaaLFy+m+Rz/1LMLAAAAAP8me/fuVdasWeXm5qYXXnhBCxcuVOnSpVMc26FDB40cOVJ16tRRlixZVKxYMYWEhOiVV16xj/n55581ZcoUBQQEaNWqVerVq5ciIiI0c+bMf+qWAOCRZLmQO6kflc1mU5YsWZQnTx41aNBA06dPV2JiYorH9OvXTy1atFDnzp3/2WIfkvXr16tx48bKmTOnPD09Vbp0ab300kv69ddfJUnt2rXT4cOHM7nKzHPixAl5eHjo8uXLGj58uP15cXZ2VsGCBdWjRw/9+eef/2hNSUFz0uLq6qrixYvrjTfe0MPuGFSwYEGdPn1aZcuWzfA5tm3bph49ejzAqgAAAADg369kyZLavXu3fvjhB/Xq1Uvh4eE6cOBAimM3bNigN998U5MnT9bOnTu1YMECLVu2TKNGjbKPSUxMVKVKlfTmm2+qYsWK6tGjh7p3766PPvron7olAHgkWS7klqRGjRrp9OnTOn78uFasWKF69eqpf//+atKkiW7fvp1s/LRp0zR8+PCHUsutW7ceynlTM3XqVIWGhipv3rz66quvdODAAX300UeKi4vT+PHjJUkeHh7KnTv3P1rXw3Tz5s10jY+JiVG9evWUNWtWSVKZMmV0+vRpnTx5UlFRUVq5cqV69er1MEq9r7Vr1+r06dM6cuSIRowYodGjR2v69Ompjk/vvafE2dlZefPmlYtLxt8z6+fnJ09Pz1T3/9M/BwAAAABgBUkTnCpXrqwxY8aofPnymjRpUopjhw0bpueee07dunVTUFCQWrZsqTfffFNjxoyxT+rLly9fspnggYGBOnny5EO/FwB4lFky5HZzc1PevHlVoEABVapUSa+88opiYmK0YsUKzZgxwz7u5MmTat68ubJmzSofHx+1bdtWZ8+eTfW827ZtU4MGDZQrVy75+voqODhYO3fudBhjs9k0ZcoUNWvWTF5eXho9enSK5zp37pyaNm0qDw8PFSlSRNHR0cnGXLx4Ud26dZOfn598fHz0xBNPaM+ePanW98svvygiIkIRERGaPn26QkJCVLhwYdWtW1effPKJXn/9dUnJ25UktdKYNWuWChcuLF9fXz3zzDO6dOmSfcylS5fUsWNHeXl5KV++fJowYYJCQkI0YMAA+5hZs2apSpUq8vb2Vt68edWhQwedO3fOvj+pDcayZctUrlw5ubu7q0aNGtq3b1+yWu40ceJEFS5c2L7euXNntWjRQqNHj1b+/PlVsmTJNF0/SUxMjJo1a2Zfd3FxsT8voaGhatOmjdasWeNwzCeffKLAwEC5u7urVKlSmjx5ssP+//3vfypRooQ8PT1VtGhRDRs2LEPBbs6cOZU3b175+/urY8eOql27tsMzltF7v3Dhgjp27Cg/Pz95eHgoICBAUVFRkpK3K0nJt99+q8cff1weHh4qWLCgIiIidOXKFfv+u9uVpPZzMGXKFBUrVkyurq4qWbKkZs2ale7PCAAAAAD+rRITE3Xjxo0U9129elVOTo4xjbOzsyTZ/wZw7dq1dejQIYcxhw8flr+//0OoFgCsw5Ihd0qeeOIJlS9fXgsWLJD01784mjdvrj///FMbN27UmjVr9PPPP6tdu3apnuPSpUsKDw/Xt99+q++//14BAQFq3LixQxgs/RXUtmzZUnv37tXzzz+f4rk6d+6sU6dOaf369Zo/f74mT56cLJBt06aNzp07pxUrVmjHjh2qVKmS6tevn2orjXnz5unmzZt6+eWXU9x/rz7cR48e1aJFi7R06VItXbpUGzdu1NixY+37Bw4cqM2bN2vx4sVas2aNNm3alCzgv3XrlkaNGqU9e/Zo0aJFOn78eIotYAYPHqzx48dr27Zt8vPzU9OmTdMdCK9bt06HDh3SmjVrtHTp0jRf/+LFi/r2228dQu47HT9+XKtWrZKrq6t9W3R0tF5//XWNHj1asbGxevPNNzVs2DCHnmbe3t6aMWOGDhw4oEmTJmnatGmaMGFCuu7pbtu3b9eOHTtUvXr1v33vw4YN04EDB7RixQrFxsZqypQpypUrV5rqOHr0qBo1aqRWrVrpxx9/1Ny5c/Xtt9+qb9++9zzu7p+DhQsXqn///nrppZe0b98+9ezZU126dNH69etTPceNGzcUHx/vsAAAAADAv8HQoUP1zTff6Pjx49q7d6+GDh2qDRs2qGPHjpKkTp06aejQofbxTZs21ZQpUzRnzhwdO3ZMa9as0bBhw9S0aVN72P3iiy/q+++/15tvvqmffvpJs2fP1scff6w+ffpkyj0CwCPDWEx4eLhp3rx5ivvatWtnAgMDjTHGrF692jg7O5uTJ0/a9+/fv99IMlu3bjXGGBMZGWnKly+f6rUSEhKMt7e3WbJkiX2bJDNgwIB71njo0CGH6xhjTGxsrJFkJkyYYIwxZtOmTcbHx8dcv37d4dhixYqZqVOnpnjeXr16GR8fn3te2xhjoqKijK+vr309MjLSeHp6mvj4ePu2wYMHm+rVqxtjjImPjzdZsmQx8+bNs++/ePGi8fT0NP3790/1Otu2bTOSzKVLl4wxxqxfv95IMnPmzLGPOX/+vPHw8DBz586113L3Zz5hwgTj7+9vXw8PDzd58uQxN27cuOd93n19Y4yJjo42VapUcbh3Jycn4+XlZdzd3Y0kI8m8++679jHFihUzs2fPdjj3qFGjTM2aNVO99jvvvGMqV67scJ17PUvHjh0zkoyHh4fx8vIyWbJkMZJMjx49HMZl9N6bNm1qunTpcs9r79q1yxjzf9/ThQsXjDHGdO3aNVkdmzZtMk5OTubatWvGGGP8/f3tz64xKf8c1KpVy3Tv3t1hW5s2bUzjxo1TvY/IyEj7d+K4xBnJsLCwsLCwsLCwsLCwWHIxxpjnn3/e+Pv7G1dXV+Pn52fq169vVq9ebf//oeDgYBMeHm5fv3Xrlhk+fLgpVqyYcXd3NwULFjS9e/e2/79bkiVLlpiyZcsaNzc3U6pUKfPxxx+n+v9cAGBlcXFxRpKJi4u779iMN+l9BBljZLPZJEmxsbEqWLCgChYsaN9funRpZcuWTbGxsapatWqy48+ePavXXntNGzZs0Llz55SQkKCrV68m621VpUqVe9YRGxsrFxcXVa5c2b6tVKlSDjOt9+zZo8uXLytnzpwOx167dk1Hjx697/2lV+HCheXt7W1fz5cvn31m+c8//6xbt26pWrVq9v2+vr72VhlJduzYoeHDh2vPnj26cOGCvSfYyZMnHXqC1axZ0/7POXLkUMmSJRUbG5uueoOCghxmW6f1+ne3KpH+etHH4sWLdf36dX3++efavXu3+vXrJ0m6cuWKjh49qq5du6p79+72Y27fvi1fX1/7+ty5c/Xee+/p6NGjunz5sm7fvi0fH5903VPSeQIDA3Xr1i3t27dP/fr1U/bs2R1m1Wfk3nv16qVWrVpp586datiwoVq0aKFatWqlqaY9e/boxx9/dGipY4xRYmKijh07psDAwBSPu/vnIDY2NtnLKWvXrp1qvznpr5kNAwcOtK/Hx8c7/MwCAAAAgFV9+umn99y/YcMGh3UXFxdFRkYqMjLynsc1adJETZo0+bvlAcC/yr8q5I6NjVWRIkUyfHx4eLjOnz+vSZMmyd/fX25ubqpZs2ayl/95eXn93VJ1+fJl5cuXL9m/1KTU246UKFFCcXFxOn36tPLly5eu62XJksVh3Waz2YPStLhy5YrCwsIUFham6Oho+fn56eTJkwoLC0vXyxGdnJxkjHHYllIrk7s/47Rc/+bNm1q5cqVeeeUVh2OTXvQhSWPHjtVTTz2lESNGaNSoUbp8+bKkv15OenfbkKS/Dvbdd9+pY8eOGjFihMLCwuTr66s5c+bYX/SZHgULFrTXEhgYqKNHj2rYsGEaPny43N3dM3zvTz75pE6cOKHly5drzZo1ql+/vvr06aNx48bdt6bLly+rZ8+eioiISLavUKFCqR73IH4O3Nzc5Obm9rfPAwAAAAAAgP+uf01P7q+//lp79+5Vq1atJP0VIJ46dUqnTp2yjzlw4IAuXryY7E3ESTZv3qyIiAg1btxYZcqUkZubm/74449011KqVCndvn1bO3bssG87dOiQLl68aF+vVKmSzpw5IxcXFxUvXtxhSa2XcuvWreXq6qq33347xf13nj89ihYtqixZsmjbtm32bXFxcTp8+LB9/eDBgzp//rzGjh2rxx9/XKVKlUrxpY+S9P3339v/+cKFCzp8+LB9NrCfn5/OnDnjEHTf64WI6bn+hg0blD17dpUvX/6e53rttdc0btw4/fbbb8qTJ4/y58+vn3/+Odn3kPQLky1btsjf31+vvvqqqlSpooCAAJ04ceK+NaeFs7Ozbt++fc9fFKT1s/fz81N4eLg+//xzTZw4UR9//HGaaqhUqZIOHDiQ7P6LFy+ebEb5vQQGBmrz5s0O2zZv3pzqzxsAAAAAAADwIFhyJveNGzd05swZJSQk6OzZs1q5cqXGjBmjJk2aqFOnTpKk0NBQBQUFqWPHjpo4caJu376t3r17Kzg4ONV2IwEBAZo1a5aqVKmi+Ph4DR48WB4eHumur2TJkmrUqJF69uypKVOmyMXFRQMGDHA4V2hoqGrWrKkWLVro7bffVokSJfTbb79p2bJlatmyZYo1FixYUBMmTFDfvn0VHx+vTp06qXDhwvrll1/02WefKWvWrBmaXezt7a3w8HANHjxYOXLkUO7cuRUZGSknJyd7e5RChQrJ1dVV77//vl544QXt27dPo0aNSvF8I0eOVM6cOZUnTx69+uqrypUrl1q0aCFJCgkJ0e+//663335brVu31sqVK7VixYr7tv5Iy/UXL16c6gsn71SzZk2VK1dOb775pj744AONGDFCERER8vX1VaNGjXTjxg1t375dFy5c0MCBAxUQEKCTJ09qzpw5qlq1qpYtW6aFCxem4ZNN7vz58zpz5oxu376tvXv3atKkSapXr9497z8t9/7666+rcuXKKlOmjG7cuKGlS5em2mbkbv/73/9Uo0YN9e3bV926dZOXl5cOHDigNWvW6IMPPkjzvQ0ePFht27ZVxYoVFRoaqiVLlmjBggVau3Ztms8BAAAAAAAApJclZ3KvXLlS+fLlU+HChdWoUSOtX79e7733nmJiYuwtJmw2m2JiYpQ9e3bVrVtXoaGhKlq0qObOnZvqeT/99FNduHBBlSpV0nPPPaeIiAjlzp07QzVGRUUpf/78Cg4O1tNPP60ePXo4nMtms2n58uWqW7euunTpohIlSuiZZ57RiRMnlCdPnlTP27t3b61evVq//vqrWrZsqVKlSqlbt27y8fHRoEGDMlSrJL377ruqWbOmmjRpotDQUNWuXVuBgYH2Fhp+fn6aMWOG5s2bp9KlS2vs2LGptsIYO3as+vfvr8qVK+vMmTNasmSJfUZwYGCgJk+erA8//FDly5fX1q1b01R3Wq6f1pBb+uuN1J988olOnTqlbt266ZNPPlFUVJSCgoIUHBysGTNm2GdyN2vWTC+++KL69u2rChUqaMuWLRo2bFiarnO30NBQ+7Pbo0cPNW7c+J7PZFrv3dXVVUOHDlW5cuVUt25dOTs7a86cOWmqqVy5ctq4caMOHz6sxx9/XBUrVtTrr7+u/Pnzp+veWrRooUmTJmncuHEqU6aMpk6dqqioKIWEhKTrPAAAAAAAAEB62MzdDZIB/dUHukCBAho/fry6du2apmM2bNigevXq6cKFC6n2FX9Ydu7cqSeeeEK///57sv7jsI74+Pj//8LPOEnpf7EnAAAAADwKSFoA4O9Lyoni4uLu2wXCku1K8ODt2rVLBw8eVLVq1RQXF6eRI0dKkpo3b57JlaXN7du39f777xNwAwAAAAAAAP8xhNywGzdunA4dOiRXV1dVrlxZmzZtSvUlmI+aatWqqVq1apldBgAAAAAAAIB/GO1KADwyaFcCAAAA4N+ApAUA/r70tCux5IsnAQAAAAAAAACQCLkBAAAAAAAAABZGyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAAAAAAAAAADLIuQGAAAAAAAAAFgWITcAAAAAAAAAwLIIuQEAAAAAAAAAlkXIDQAAAAAAAACwLEJuAAAAAAAAAIBlEXIDAAAAAAAAACyLkBsAAAAAAAAAYFmE3AAAAAAAAAAAyyLkBgAAAAAAAABYFiE3AAAAAAAAAMCyCLkBAAAAAAAAAJZFyA0AAAAAAAAAsCxCbgAAAAAAAACAZRFyAwAAAAAAAAAsi5AbAAAAAAAAAGBZhNwAAAAAAAAAAMsi5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWS6ZXQAA3C0uTvLxyewqAAAAAAAAYAXM5AYAAAAAAAAAWBYhNwAAAAAAAADAsgi5AQAAAAAAAACWRcgNAAAAAAAAALAsQm4AAAAAAAAAgGURcgMAAAAAAAAALIuQGwAAAAAAAABgWYTcAP5fe/cf9vV8////djpzVioJSaf1Y5Z+aKJkvZuF0ZQachi9e7cVMt4WFoa1z1IOm8V4T9bWYaQ2Y+W9odabLEYWdqi8I7QfNeS9ESPlzHams9f3D9/OY6d+snh5zuVyHM/jcD6fz9fzdT/PXi8O157n4wUAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYjco9AMA7tWxZ7gkAAAAAiqFUKvcE5edObgAAAAAACkvkBgAAAACgsERuAAAAAAAKS+QGAAAAAKCwRG4AAAAAAApL5AYAAAAAoLBEbgAAAAAACkvkBgAAAACgsERuAAAAAAAKS+QGAAAAAKCwRG4AAAAAAApL5AYAAAAAoLBEbgAAAAAACkvkBgAAAACgsERuAAAAAAAKS+QGAAAAAKCwRG4AAAAAAApL5AYAAAAAoLBEbgAAAAAACkvkBgAAAACgsERuAAAAAAAKS+QGAAAAAKCwRG4AAAAAAApL5AYAAAAAoLBEbgAAAAAACkvkBgAAAACgsERuAAAAAAAKS+QGAAAAAKCwRG4AAAAAAApL5AYAAAAAoLBEbgAAAAAACkvkBgAAAACgsERuAAAAAAAKS+QGAAAAAKCwRG4AAAAAAApL5AYAAAAAoLBEbgAAAAAACkvkBgAAAACgsERuAAAAAIACmzBhQioqKhpsXbt23er5N954Y/r165dWrVqlVatW6d+/fx577LEPcOKdS+QGAAAAACi47t2758UXX6zfFixYsNVzH3zwwQwbNiwPPPBAHn300bRr1y7HHnts/vznP3+AE+88jco9AAAAAAAA/5xGjRpl33333aFzb7311gZf33TTTfnFL36R+++/PyNGjHg/xntfuZP7PVi+fHmuvPLK/O1vfyv3KAAAAAAA+eMf/5jq6ursv//+GT58eFauXLnDj33zzTfz1ltvZc8993wfJ3z/iNzv0t///vd84QtfSHV1dZo2bVq/f8KECTnkkEPKN9gH7LTTTsuQIUPKPcaHxof5z/+5555LRUVFlixZkuTtX0epqKjI66+/vsPX6NixY6677rr3ZT4AAAAA/jl9+vTJ9OnTM3fu3EyZMiXPPvts+vXrlzfeeGOHHn/ppZemuro6/fv3f58nfX98pCP3aaedVr8Q+6677po2bdrkc5/7XG6++eZs3Lhxi48577zzMmTIkJx22mkf7LBJfvazn6WysjKjR4/+wJ/7nSZNmpTp06eXe4wtev7559O0adPU1NQ0WHS/srIy7dq1y1lnnZXXXnvtA51pU2jetFVVVaVTp0751re+lVKp9L4+d7t27fLiiy/mk5/85Hu+xsKFC3PWWWftxKkAAAAA2FmOO+64nHLKKenRo0cGDBiQu+++O6+//npuv/327T524sSJmTFjRu688840adLkA5h25/vIr8k9cODATJs2LXV1dVm1alXmzp2br371q/n5z3+e2bNnp1Gjhj+iG2+88X2b5a233squu+661eNTp07NJZdckhtuuCHXXnttWV50dXV1qaioSMuWLT/w595Rs2bNymc/+9k0b948yduL7t93332pq6vLsmXLcsYZZ2TNmjWZOXPmBz7bfffdl+7du6e2tjYLFizImWeembZt22bUqFFbPH/9+vWpqqr6p56zsrJyh9dj2prWrVtv8/j2XrsAAAAAfHD22GOPdO7cOcuXL9/meddcc00mTpyY++67Lz169PiAptv5PtJ3cidJ48aNs++++2a//fZLr1698o1vfCOzZs3KPffc0+BO5ZUrV+bEE09M8+bNs/vuu+fUU0/NqlWrtnrdhQsX5nOf+1z23nvvtGzZMkceeWQef/zxBudUVFRkypQpOeGEE9KsWbN8+9vf3ur1nn322TzyyCP5+te/ns6dO+eOO+5ocHz69OnZY489MmfOnHTp0iW77bZbvvCFL+TNN9/Mj3/843Ts2DGtWrXK+eefn7q6uvrH1dbW5mtf+1r222+/NGvWLH369MmDDz642XVnz56dAw88MI0bN87KlSs3W65k48aNufrqq9OpU6c0btw47du3b/D9XHrppencuXN222237L///hk3blzeeuut+uOblvu45ZZb0rFjx7Rs2TL//u//3uBXKmpra3P++ednn332SZMmTfKZz3wmCxcu3OxnNWvWrJxwwgn1X29adH+//fZL//79c8opp2TevHkNHnPTTTelW7duadKkSbp27Zof/vCHDY5vb/4dtddee2XfffdNhw4dMnz48Bx++OENXhebfq7f/va3U11dnS5duiRJbrnllvTu3TstWrTIvvvum//4j//Iyy+/XP+41atXZ/jw4WndunWaNm2aAw44INOmTUuy+XIlW7JgwYL069cvTZs2Tbt27XL++edn3bp19cffuVzJ1l67U6ZMySc+8YlUVVWlS5cuueWWW971zwgAAACAf05NTU1WrFiRtm3bbvWcq6++OldccUXmzp2b3r17f4DT7Xwf+ci9JUcffXQOPvjg+pC8cePGnHjiiXnttdcyf/78zJs3L3/6058ydOjQrV7jjTfeyMiRI7NgwYL89re/zQEHHJBBgwZttg7OhAkTctJJJ2Xp0qU544wztnq9adOmZfDgwWnZsmW++MUvZurUqZud8+abb+b666/PjBkzMnfu3Dz44IM56aSTcvfdd+fuu+/OLbfckhtuuCE///nP6x9z7rnn5tFHH82MGTPy5JNP5pRTTsnAgQPzxz/+scF1r7rqqtx00015+umns88++2z23GPHjs3EiRMzbty4PPPMM7ntttvSpk2b+uMtWrTI9OnT88wzz2TSpEm58cYb873vfa/BNVasWJG77rorc+bMyZw5czJ//vxMnDix/vgll1ySX/ziF/nxj3+cxx9/PJ06dcqAAQMaLD3y+uuvZ8GCBQ0i9z967rnncu+99za4O/rWW2/NZZddlm9/+9tZtmxZrrzyyowbNy4//vGP39X879aiRYuyePHi9OnTp8H++++/P7///e8zb968zJkzJ8nbd0pfccUVeeKJJ3LXXXflueeea7Bkzqaf+z333JNly5ZlypQp2XvvvXdojhUrVmTgwIE5+eST8+STT2bmzJlZsGBBzj333G0+7p2v3TvvvDNf/epXc9FFF+Wpp57K2WefndNPPz0PPPDAVq9RW1ubtWvXNtgAAAAAeHe+9rWvZf78+XnuuefyyCOP5KSTTkplZWWGDRuWJBkxYkTGjh1bf/5VV12VcePG5eabb07Hjh3z0ksv5aWXXkpNTU25voV/TukjbOTIkaUTTzxxi8eGDh1a6tatW6lUKpV+9atflSorK0srV66sP/7000+XkpQee+yxUqlUKo0fP7508MEHb/W56urqSi1atCj98pe/rN+XpDRmzJjtzllXV1dq165d6a677iqVSqXSK6+8Uqqqqir96U9/qj9n2rRppSSl5cuX1+87++yzS7vttlvpjTfeqN83YMCA0tlnn10qlUql559/vlRZWVn685//3OD5jjnmmNLYsWMbXHfJkiUNzvnHn93atWtLjRs3Lt14443b/V42+e53v1s69NBD678eP358abfddiutXbu2ft/FF19c6tOnT6lUKpVqampKu+66a+nWW2+tP75+/fpSdXV16eqrr67fd+utt5Z69+7d4Lq77LJLqVmzZqUmTZqUkpSSlP7rv/6r/pxPfOITpdtuu63BfFdccUWpb9++72r+bf35P/vss6UkpaZNm5aaNWtW2nXXXUtJSmeddVaD80aOHFlq06ZNqba2dqvXKpVKpYULF5aS1P/ZHn/88aXTTz99m8/9v//7v6VSqVR64IEHSklKq1evLpVKpdKoUaM2m+M3v/lNaZdddin97W9/K5VKpVKHDh1K3/ve9+qPb+m1++lPf7r05S9/ucG+U045pTRo0KCtfh/jx4+v/zNpuK0pJSWbzWaz2Ww2m81ms9lsNtt2tlLp7ZbZtm3bUlVVVWm//fYrDR06tEEnPPLII0sjR46s/7pDhw6lLTWZ8ePHb7XjfNDWrFlTSlJas2bNds/9yK/JvTWlUikVFRVJkmXLlqVdu3Zp165d/fEDDzwwe+yxR5YtW5bDDjtss8evWrUq3/zmN/Pggw/m5ZdfTl1dXd58882sXLmywXk78qsA8+bNy7p16zJo0KAkyd57713/AZlXXHFF/Xm77bZbPvGJT9R/3aZNm3Ts2LF+bepN+zYtc7F06dLU1dWlc+fODZ6vtrY2e+21V/3XVVVV21yTZ9myZamtrc0xxxyz1XNmzpyZ66+/PitWrEhNTU02bNiQ3XffvcE5HTt2TIsWLeq/btu2bf2sK1asyFtvvZXDDz+8/viuu+6aT33qU1m2bFn9vncuVZIkXbp0yezZs/P3v/89P/3pT7NkyZKcd955SZJ169ZlxYoVGTVqVL785S/XP2bDhg0N1h3fkfl3xMyZM9OtW7e89dZbeeqpp3LeeeelVatWDe5YP+iggzZbh3vx4sWZMGFCnnjiiaxevbr+g1FXrlyZAw88MOecc05OPvnkPP744zn22GMzZMiQfPrTn96hmZ544ok8+eSTufXWW+v3lUqlbNy4Mc8++2y6deu2xce987W7bNmyzT6c8vDDD8+kSZO2+txjx47NhRdeWP/12rVrG7zPAAAAANi+GTNmbPP4Py5PnLy92sG/EpF7K5YtW5aPf/zj7/nxI0eOzKuvvppJkyalQ4cOady4cfr27Zv169c3OK9Zs2bbvdbUqVPz2muvpWnTpvX7Nm7cmCeffDKXX355dtnl7VVn3vnBfxUVFVvctymQ1tTUpLKyMosXL05lZWWD8/4xjDdt2rQ++G/JP861JY8++miGDx+eyy+/PAMGDEjLli0zY8aMXHvttQ3O29asO2L9+vWZO3duvvGNbzTYX1VVlU6dOiV5+9NiBw8enMsvvzxXXHFF/a9g3HjjjZstG7LpZ7Kj8++Idu3a1c/SrVu3rFixIuPGjcuECRPqP0j0na+JdevWZcCAARkwYEBuvfXWtG7dOitXrsyAAQPqX0/HHXdcnn/++dx9992ZN29ejjnmmIwePTrXXHPNdmeqqanJ2WefnfPPP3+zY+3bt9/q43bktbs9jRs3TuPGjf/p6wAAAADw0SVyb8Gvf/3rLF26NBdccEGSt2PkCy+8kBdeeKH+LtNnnnkmr7/+eg488MAtXuPhhx/OD3/4w/q7r1944YX89a9/fdezvPrqq5k1a1ZmzJiR7t271++vq6vLZz7zmfzqV7/KwIED3/V1k6Rnz56pq6vLyy+/nH79+r2nayTJAQcckKZNm+b+++/PmWeeudnxRx55JB06dMj/+3//r37f888//66eY9OHGT788MPp0KFDkrfXqV64cGHGjBmT5O2/kWrVqlUOPvjgbV7rm9/8Zo4++uicc845qa6uTnV1df70pz9l+PDhWzx/Z8y/NZWVldmwYUPWr19fH7nf6Xe/+11effXVTJw4sf71t2jRos3Oa926dUaOHJmRI0emX79+ufjii3cocvfq1SvPPPNMfXx/r7p165aHH344I0eOrN/38MMPb/U9AgAAAAA7w0c+ctfW1uall15KXV1dVq1alblz5+Y73/lOPv/5z2fEiBFJkv79++eggw7K8OHDc91112XDhg35yle+kiOPPHKry40ccMABueWWW9K7d++sXbs2F1988XbveN6SW265JXvttVdOPfXUze6mHjRoUKZOnfqeI3fnzp0zfPjwjBgxItdee2169uyZV155Jffff3969OiRwYMH79B1mjRpkksvvTSXXHJJqqqqcvjhh+eVV17J008/nVGjRuWAAw7IypUrM2PGjBx22GH5n//5n9x5553vatZmzZrlnHPOycUXX5w999wz7du3z9VX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dVe5R4LC+s53vpPDDjssLVq0yD777JMhQ4bk97//fbnHgsKaMmVKevTokd133z277757+vbtm3vuuafcY8G/jIkTJ6aioiJjxowp9yhQSBMmTEhFRUWDrWvXruUeix0gcgNlN3PmzFx44YUZP358Hn/88Rx88MEZMGBAXn755XKPBoW0bt26HHzwwfnBD35Q7lGg8ObPn5/Ro0fnt7/9bebNm5e33norxx57bNatW1fu0aCQPvaxj2XixIlZvHhxFi1alKOPPjonnnhinn766XKPBoW3cOHC3HDDDenRo0e5R4FC6969e1588cX6bcGCBeUeiR1QUSqVSuUeAvho69OnTw477LBMnjw5SbJx48a0a9cu5513Xr7+9a+XeTootoqKitx5550ZMmRIuUeBfwmvvPJK9tlnn8yfPz9HHHFEuceBfwl77rlnvvvd72bUqFHlHgUKq6amJr169coPf/jDfOtb38ohhxyS6667rtxjQeFMmDAhd911V5YsWVLuUXiX3MkNlNX69euzePHi9O/fv37fLrvskv79++fRRx8t42QAsLk1a9YkeTvKAf+curq6zJgxI+vWrUvfvn3LPQ4U2ujRozN48OAG/18FvDd//OMfU11dnf333z/Dhw/PypUryz0SO6BRuQcAPtr++te/pq6uLm3atGmwv02bNvnd735XpqkAYHMbN27MmDFjcvjhh+eTn/xkuceBwlq6dGn69u2bv//972nevHnuvPPOHHjggeUeCwprxowZefzxx7Nw4cJyjwKF16dPn0yfPj1dunTJiy++mMsvvzz9+vXLU089lRYtWpR7PLZB5AYAgB0wevToPPXUU9ZlhH9Sly5dsmTJkqxZsyY///nPM3LkyMyfP1/ohvfghRdeyFe/+tXMmzcvTZo0Kfc4UHjHHXdc/T/36NEjffr0SYcOHXL77bdbVutDTuQGymrvvfdOZWVlVq1a1WD/qlWrsu+++5ZpKgBo6Nxzz82cOXPy0EMP5WMf+1i5x4FCq6qqSqdOnZIkhx56aBYuXJhJkyblhhtuKPNkUDyLFy/Oyy+/nF69etXvq6ury0MPPZTJkyentrY2lZWVZZwQim2PPfZI586ds3z58nKPwnZYkxsoq6qqqhx66KG5//776/dt3Lgx999/v7UZASi7UqmUc889N3feeWd+/etf5+Mf/3i5R4J/ORs3bkxtbW25x4BCOuaYY7J06dIsWbKkfuvdu3eGDx+eJUuWCNzwT6qpqcmKFSvStm3bco/CdriTGyi7Cy+8MCNHjkzv3r3zqU99Ktddd13WrVuX008/vdyjQSHV1NQ0uNPg2WefzZIlS7Lnnnumffv2ZZwMimf06NG57bbbMmvWrLRo0SIvvfRSkqRly5Zp2rRpmaeD4hk7dmyOO+64tG/fPm+88UZuu+22PPjgg7n33nvLPRoUUosWLTb7nIhmzZplr7328vkR8B587Wtfy/HHH58OHTrkL3/5S8aPH5/KysoMGzas3KOxHSI3UHZDhw7NK6+8kssuuywvvfRSDjnkkMydO3ezD6MEdsyiRYvy2c9+tv7rCy+8MEkycuTITJ8+vUxTQTFNmTIlSXLUUUc12D9t2rScdtppH/xAUHAvv/xyRowYkRdffDEtW7ZMjx49cu+99+Zzn/tcuUcDgPzf//1fhg0blldffTWtW7fOZz7zmfz2t79N69atyz0a21FRKpVK5R4CAAAAAADeC2tyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAC8T5577rlUVFRkyZIl7/tzHXXUURkzZsz7/jwAAB82IjcAAMB2PProo6msrMzgwYPf9+eaMGFCKioqUlFRkUaNGqVjx4654IILUlNTs83H3XHHHbniiive9/kAAD5sRG4AAIDtmDp1as4777w89NBD+ctf/vK+P1/37t3z4osv5rnnnstVV12VH/3oR7nooou2eO769euTJHvuuWdatGjxvs8GAPBhI3IDAABsQ01NTWbOnJlzzjkngwcPzvTp0xscX716dYYPH57WrVunadOmOeCAAzJt2rQtXquuri5nnHFGunbtmpUrV271ORs1apR99903H/vYxzJ06NAMHz48s2fPTvL2nd6HHHJIbrrppnz84x9PkyZNkmy+XEltbW0uvfTStGvXLo0bN06nTp0yderU+uNPPfVUjjvuuDRv3jxt2rTJl770pfz1r399jz8lAIDyEbkBAAC24fbbb0/Xrl3TpUuXfPGLX8zNN9+cUqlUf3zcuHF55plncs8992TZsmWZMmVK9t57782uU1tbm1NOOSVLlizJb37zm7Rv336HZ2jatGn9HdtJsnz58vziF7/IHXfcsdX1vkeMGJGf/exnuf7667Ns2bLccMMNad68eZLk9ddfz9FHH52ePXtm0aJFmTt3blatWpVTTz11h2cCAPiwaFTuAQAAAD7Mpk6dmi9+8YtJkoEDB2bNmjWZP39+jjrqqCTJypUr07Nnz/Tu3TtJ0rFjx82uUVNTk8GDB6e2tjYPPPBAWrZsucPPv3jx4tx22205+uij6/etX78+P/nJT9K6destPuYPf/hDbr/99sybNy/9+/dPkuy///71xydPnpyePXvmyiuvrN938803p127dvnDH/6Qzp077/B8AADl5k5uAACArfj973+fxx57LMOGDUvy9jIiQ4cObbDsxznnnJMZM2bkkEMOySWXXJJHHnlks+sMGzYs69aty69+9asdCtxLly5N8+bN07Rp03zqU59K3759M3ny5PrjHTp02GrgTpIlS5aksrIyRx555BaPP/HEE3nggQfSvHnz+q1r165JkhUrVmx3PgCADxN3cgMAAGzF1KlTs2HDhlRXV9fvK5VKady4cSZPnpyWLVvmuOOOy/PPP5+777478+bNyzHHHJPRo0fnmmuuqX/MoEGD8tOf/jSPPvpogzuyt6ZLly6ZPXt2GjVqlOrq6lRVVTU43qxZs20+vmnTpts8XlNTk+OPPz5XXXXVZsfatm273fkAAD5M3MkNAACwBRs2bMhPfvKTXHvttVmyZEn99sQTT6S6ujo/+9nP6s9t3bp1Ro4cmZ/+9Ke57rrr8qMf/ajBtc4555xMnDgxJ5xwQubPn7/d566qqkqnTp3SsWPHzQL3jjjooIOycePGrT5Xr1698vTTT6djx47p1KlTg217AR0A4MNG5AYAANiCOXPmZPXq1Rk1alQ++clPNthOPvnk+iVLLrvsssyaNSvLly/P008/nTlz5qRbt26bXe+8887Lt771rXz+85/PggUL3tfZO3bsmJEjR+aMM87IXXfdlWeffTYPPvhgbr/99iTJ6NGj89prr2XYsGFZuHBhVqxYkXvvvTenn3566urq3tfZAAB2NpEbAABgC6ZOnZr+/ftvcQ3tk08+OYsWLcqTTz6ZqqqqjB07Nj169MgRRxyRysrKzJgxY4vXHDNmTC6//PIMGjRoi2t370xTpkzJF77whXzlK19J165d8+Uvfznr1q1LklRXV+fhhx9OXV1djj322Bx00EEZM2ZM9thjj+yyi/9NBACKpaJUKpXKPQQAAAAAALwX/ooeAAAAAIDCErkBAAAAACgskRsAAAAAgMISuQEAAAAAKCyRGwAAAACAwhK5AQAAAAAoLJEbAAAAAIDCErkBAAAAACgskRsAAAAAgMISuQEAAAAAKCyRGwAAAACAwvr/AGFwzm11M+7HAAAAAElFTkSuQmCC)
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
4.3 What the top 10 like BRL in value?
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[10\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    import matplotlib.pyplot as plt

    query = """
        SELECT 
            name
            ,round(avg(ask),2) AvgAsk
        FROM df 
        where codein = 'BRL'
        and not code in ('BTC', 'ETH', 'LTC', 'DOGE')
        and ask >=1
        group by name
        order by avg(ask) desc limit 5
    """

    newDf = sqldf(query, locals())
    newDf.sort_values(by='AvgAsk', ascending=False, inplace=True)

    AvgAskByCurrency = newDf.plot(
        kind='barh', x='name', y='AvgAsk', 
        figsize=(15, 10), 
        legend=False, 
        color='blue', title='Top 10 Most Valuable Currencies by Ask Price', xlabel='Ask Price', ylabel='Symbol')


    # Adicionando rótulos aos dados
    for index, value in enumerate(newDf['AvgAsk']):
        plt.text(value, index, str(value))

    # Exibir o gráfico
    plt.show()
:::
:::
:::
:::
:::

::: {.jp-Cell-outputWrapper}
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::: {.jp-OutputArea .jp-Cell-outputArea}
::: {.jp-OutputArea-child}
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedImage .jp-OutputArea-output tabindex="0"}
![No description has been provided for this
image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABbkAAANXCAYAAAAYXFJxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAACC8ElEQVR4nOzdZ7QW5dk24HPTO4J0g6gIiAbsFRVUFBuWRLFFwIgYo2KJJho1oMZoLFFTNEYTMAZFxYIVRAPGLtZYsCGWGFsQARsozPfDj/26pW0QxUmOY61ZK8/MPTPXzDOb1/fc976moiiKIgAAAAAAUEI1VnQBAAAAAACwrITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAADAt9awYcNSUVHxtZ5jxIgRqaioyCOPPLLEsb169UqvXr2+1nr+1wwcODCrrbbaN3rO1VZbLbvuuus3es6v6pVXXklFRUXOPffcFXL+iRMnpqKiIhMnTlwh5weAxRFyAwBQChUVFdVavokA5uKLL87ee++dVVddNRUVFRk4cOAix77//vsZPHhwWrZsmYYNG2abbbbJY489Vq3z9OrVKxUVFenUqdNCt48fP77yukePHr0sl7JEt912W4YNG7bEce+8805q1aqVH/zgB4scM2vWrNSvXz/f+973lmOF/x0mTpyY733ve2nTpk3q1KmTVq1apW/fvrn++utXdGksB5MnT05FRUXq1auX999/f4XU8MV/J2vUqJF27dplhx12EFoD8F+h1oouAAAAquOKK66o8vmvf/1rxo8fv8D6rl27fu21/PrXv86sWbOyySab5M0331zkuHnz5mWXXXbJk08+meOPPz4tWrTIRRddlF69euXRRx9dZHj9RfXq1ctLL72Uhx9+OJtsskmVbSNHjky9evXyySeffOVrWpTbbrstf/jDH5YYdLdq1Srbb799xowZk48++igNGjRYYMz111+fTz75ZLFB+P+ioUOH5rTTTkunTp1y6KGHpkOHDpk2bVpuu+22fP/738/IkSOz//77r+gyvzaXXnpp5s2bt6LL+Fr97W9/S5s2bTJ9+vSMHj06gwYNWiF1bL/99unfv3+KosjUqVNz0UUXZdttt82tt96anXbaabH7br311vn4449Tp06db6haAKg+ITcAAKXw5WD0wQcfzPjx41dIYHr33XdXzuJu1KjRIseNHj06999/f6699trstddeSZJ+/fqlc+fOGTp0aK688solnqtjx4757LPPctVVV1UJuT/55JPccMMN2WWXXXLdddd99YtaDg444ICMHTs2N910U/bdd98Ftl955ZVp2rRpdtlllxVQ3bfT6NGjc9ppp2WvvfbKlVdemdq1a1duO/744zNu3Lh8+umny+Vci/rlw2effZZ58+atsPDyi9f836goilx55ZXZf//9M3Xq1IwcOXKFhdydO3eu8m/mnnvume7du+eCCy5YZMj9ySefpE6dOqlRo0bq1av3TZUKAEtFuxIAAP5rfPjhh/nJT36S9u3bp27duunSpUvOPffcFEVRZVxFRUWOOOKIjBw5Ml26dEm9evWy4YYb5h//+Ee1ztOhQ4dq9YkePXp0WrduXaU9R8uWLdOvX7+MGTMms2fPrtb59ttvv1x99dVVZrvefPPN+eijj9KvX7+F7vP4449np512SpMmTdKoUaNst912efDBB6uM+fTTT3PqqaemU6dOqVevXlZeeeVsueWWGT9+fJLPeyX/4Q9/SFK11cGi7LnnnmnYsOFCw/t33nknd911V/baa6/UrVs399xzT2XLl7p166Z9+/Y55phj8vHHHy/2XszvSzxixIgFtlVUVFSZcf7qq6/mxz/+cbp06ZL69etn5ZVXzt57751XXnllocf+6KOPcuihh2bllVdOkyZN0r9//0yfPn2x9STJ7NmzM3To0Ky55pqV1/LTn/60Wt/vKaeckubNm+cvf/nLQsPePn36VPaOnt87/Mv1L6xXcq9evfLd7343jz76aLbeeus0aNAgP//5z6v0db7gggvSsWPH1K1bN88++2yS5Lnnnstee+2V5s2bp169etloo41y0003VTnf/Druu+++HHvssZWtePbcc8+8++67C1zD7bffnp49e6Zx48Zp0qRJNt544yrPyMJ6cs+bNy8XXHBB1llnndSrVy+tW7fOoYceusD38cgjj6RPnz5p0aJF6tevn9VXXz0//OEPl3jf57vjjjuy3nrrpV69ell77bWrtId5+eWXU1FRkfPPP3+B/e6///5UVFTkqquuWuI57rvvvrzyyivZd999s+++++Yf//hH/vWvfy0wblmupSiKDB48OHXq1Fmm1jbdunVLixYtMnXq1CT/9yyNGjUqJ598clZZZZU0aNAgM2fOXGRP7oceeig777xzmjVrloYNG6Z79+658MILq4ypznMFAF+FmdwAAPxXKIoiu+22WyZMmJCDDz446623XsaNG5fjjz8+b7zxxgJB1d13352rr746Q4YMSd26dXPRRRdlxx13zMMPP5zvfve7y6Wmxx9/PBtssEFq1Kg6t2STTTbJn/70p7zwwgvp1q3bEo+z//77Z9iwYZk4cWK23XbbJJ/Pit5uu+3SqlWrBcY/88wz2WqrrdKkSZP89Kc/Te3atXPJJZekV69eufvuu7Ppppsm+fyljmeeeWYGDRqUTTbZJDNnzswjjzySxx57LNtvv30OPfTQ/Pvf/15oW5iFadiwYXbfffeMHj067733Xpo3b1657eqrr87cuXNzwAEHJEmuvfbafPTRRznssMOy8sor5+GHH87vfve7/Otf/8q11167xHNVx6RJk3L//fdn3333zXe+85288sorufjii9OrV688++yzC8xqPuKII7LSSitl2LBhef7553PxxRfn1VdfrQz3FmbevHnZbbfdcu+992bw4MHp2rVrnnrqqZx//vl54YUXcuONNy6yvhdffDHPPfdcfvjDH6Zx48bL5Zq/aNq0adlpp52y77775gc/+EFat25duW348OH55JNPMnjw4NStWzfNmzfPM888kx49emSVVVbJCSeckIYNG+aaa67JHnvskeuuuy577rlnleMfeeSRadasWYYOHZpXXnklF1xwQY444ohcffXVlWNGjBiRH/7wh1lnnXVy4oknZqWVVsrjjz+esWPHLrYFy6GHHpoRI0bkoIMOypAhQzJ16tT8/ve/z+OPP5777rsvtWvXzjvvvJMddtghLVu2zAknnJCVVlopr7zySrXD3hdffDH77LNPfvSjH2XAgAEZPnx49t5774wdOzbbb7991lhjjfTo0SMjR47MMcccU2XfkSNHpnHjxtl9992XeJ6RI0emY8eO2XjjjfPd7343DRo0yFVXXZXjjz++csyyXMvcuXPzwx/+MFdffXXlX3UsrenTp2f69OlZc801q6w//fTTU6dOnRx33HGZPXv2Imf5jx8/Prvuumvatm2bo446Km3atMnkyZNzyy235KijjkqSpX6uAGCZFAAAUEKHH3548cX/nL3xxhuLJMUvf/nLKuP22muvoqKionjppZcq1yUpkhSPPPJI5bpXX321qFevXrHnnnsuVR0NGzYsBgwYsMhtP/zhDxdYf+uttxZJirFjxy722D179izWWWedoiiKYqONNioOPvjgoiiKYvr06UWdOnWKyy+/vJgwYUKRpLj22msr99tjjz2KOnXqFFOmTKlc9+9//7to3LhxsfXWW1euW3fddYtddtllsTV8+T4vyfxru+SSS6qs32yzzYpVVlmlmDt3blEURfHRRx8tsO+ZZ55ZVFRUFK+++mrluqFDh1Y5/9SpU4skxfDhwxfYP0kxdOjQys8LO8cDDzxQJCn++te/Vq4bPnx4kaTYcMMNizlz5lSuP/vss4skxZgxYyrX9ezZs+jZs2fl5yuuuKKoUaNGcc8991Q5zx//+MciSXHfffctUMN8Y8aMKZIU559//iLHfNH8OqdOnVpl/fxnYMKECVXqTFL88Y9/rDJ2/v1r0qRJ8c4771TZtt122xXdunUrPvnkk8p18+bNK7bYYouiU6dOC9TRu3fvYt68eZXrjznmmKJmzZrF+++/XxRFUbz//vtF48aNi0033bT4+OOPq5zri/sNGDCg6NChQ+Xne+65p0hSjBw5sso+Y8eOrbL+hhtuKJIUkyZNWtQtW6QOHToUSYrrrruuct2MGTOKtm3bFuuvv37luksuuaRIUkyePLly3Zw5c4oWLVos8uf+i+bMmVOsvPLKxUknnVS5bv/99y/WXXfdKuOqcy3zv7tzzjmn+PTTT4t99tmnqF+/fjFu3LhqXPHnPx8HH3xw8e677xbvvPNO8dBDDxXbbbddkaQ477zziqL4v2dpjTXWWODn58vP2WeffVasvvrqRYcOHYrp06dXGfvF77e6zxUAfBXalQAA8F/htttuS82aNTNkyJAq63/yk5+kKIrcfvvtVdZvvvnm2XDDDSs/r7rqqtl9990zbty4zJ07d7nU9PHHH6du3boLrJ/f13ZJrTm+aP/998/111+fOXPmZPTo0alZs+ZCZ0DOnTs3d9xxR/bYY4+sscYalevbtm2b/fffP/fee29mzpyZJFlppZXyzDPP5MUXX1zaS1uk+bNRv9iOYurUqXnwwQez3377Vc5qr1+/fuX2Dz/8MP/5z3+yxRZbpCiKPP7448ulli+e49NPP820adOy5pprZqWVVspjjz22wPjBgwdXaRly2GGHpVatWrntttsWeY5rr702Xbt2zVprrZX//Oc/lcv8GfcTJkxY5L7zv4evYxZ3ktStWzcHHXTQQrd9//vfT8uWLSs/v/fee/n73/+efv36ZdasWZXXMW3atPTp0ycvvvhi3njjjSrHGDx4cJUZ7ltttVXmzp2bV199Ncnns3xnzZqVE044YYFezotre3PttdemadOm2X777avc0w033DCNGjWqvKcrrbRSkuSWW25Zpr7l7dq1q/IzNL9FzeOPP5633noryec99OvVq5eRI0dWjhs3blz+85//VOt9ALfffnumTZuW/fbbr3LdfvvtlyeffDLPPPNM5bqluZY5c+Zk7733zi233JLbbrstO+ywQ7WuN0n+/Oc/p2XLlmnVqlU23XTTypYzRx99dJVxAwYMqPLzszCPP/54pk6dmqOPPrqy/vnmf7/L8lwBwLIQcgMA8F/h1VdfTbt27RYIDLt27Vq5/Ys6deq0wDE6d+6cjz76aKF9hZdF/fr1F9qX+ZNPPqncXl377rtvZsyYkdtvvz0jR47MrrvuutBw9N13381HH32ULl26LLCta9eumTdvXl5//fUkyWmnnZb3338/nTt3Trdu3XL88cfnn//8Z7VrWphatWpln332yT333FMZXs0PvOe3KkmS1157LQMHDkzz5s3TqFGjtGzZMj179kySzJgx4yvVMN/HH3+cX/ziF5U92lu0aJGWLVvm/fffX+g5vvxMNGrUKG3btl1kD+/k85YXzzzzTFq2bFll6dy5c5LP21AsSpMmTZIks2bNWoarW7JVVlllkW0mVl999SqfX3rppRRFkVNOOWWBaxk6dGiSBa9l1VVXrfK5WbNmSVLZN3vKlClJstTtf1588cXMmDEjrVq1WqCWDz74oLKOnj175vvf/35OPfXUtGjRIrvvvnuGDx9e7V73a6655gJh+/zvbf53vtJKK6Vv375VfmkzcuTIrLLKKpW/yFicv/3tb1l99dVTt27dvPTSS3nppZfSsWPHNGjQoEpwvjTXcuaZZ+bGG2/M6NGj06tXr2pd63y77757xo8fnzvvvDMPPfRQ/vOf/+S8885boKXSl5+PhanO97sszxUALAs9uQEA4GvStm3bvPnmmwusn7+uXbt2S3WsXr165bzzzst9992X66677ivXt/XWW2fKlCkZM2ZM7rjjjlx22WU5//zz88c//jGDBg1a5uP+4Ac/yO9///tcddVVOe6443LVVVdl7bXXznrrrZfk89nm22+/fd5777387Gc/y1prrZWGDRvmjTfeyMCBA6u8YPPLFjUDeGGz74888sgMHz48Rx99dDbffPM0bdo0FRUV2XfffRd7jqUxb968dOvWLb/5zW8Wur19+/aL3HettdZKkjz11FPVOtfSXHuy+F+ifHnb/Ptx3HHHpU+fPgvd58t9m2vWrLnQccWXXvS6tObNm5dWrVpVCYG/aP4M9IqKiowePToPPvhgbr755owbNy4//OEPc9555+XBBx9Mo0aNvlId8/Xv3z/XXntt7r///nTr1i033XRTfvzjHy8QDH/ZzJkzc/PNN+eTTz5Z6C/VrrzyypxxxhmVL3St7rX06dMnY8eOzdlnn51evXotMEt+cb7zne+kd+/eSxy3NL+AW5xlea4AYFkIuQEA+K/QoUOH3HnnnZk1a1aVGc7PPfdc5fYvWliLjhdeeCENGjSo0sbhq1hvvfVyzz33ZN68eVUCsYceeigNGjSonDVaXfvvv38GDRqUlVZaKTvvvPNCx7Rs2TINGjTI888/v8C25557LjVq1KgSvDZv3jwHHXRQDjrooHzwwQfZeuutM2zYsMqQe3FtJRZl0003TceOHXPllVdm++23zzPPPJMzzjijcvtTTz2VF154IZdffnn69+9fuX78+PFLPPb82cLvv/9+lfVfnqmfJKNHj86AAQNy3nnnVa775JNPFth3vhdffDHbbLNN5ecPPvggb7755iLvdZJ07NgxTz75ZLbbbrulvledO3dOly5dMmbMmFx44YVLDGWX5tqX1vzWNrVr165WCFodHTt2TJI8/fTTSxVkduzYMXfeeWd69OhRrbB1s802y2abbZYzzjgjV155ZQ444ICMGjVqib+omT/L+Ivf2wsvvJAkWW211SrX7bjjjmnZsmVGjhyZTTfdNB999FEOPPDAJdZ1/fXX55NPPsnFF1+cFi1aVNn2/PPP5+STT859992XLbfccqmuZbPNNsuPfvSj7Lrrrtl7771zww03pFatb/7/tf/i97uoZ+breK4AYGG0KwEA4L/CzjvvnLlz5+b3v/99lfXnn39+KioqstNOO1VZ/8ADD1Tpy/z6669nzJgx2WGHHRY5Q3Vp7bXXXnn77bdz/fXXV677z3/+k2uvvTZ9+/ZdaL/uJR1v6NChueiiixbZhqJmzZrZYYcdMmbMmCptNt5+++1ceeWV2XLLLSvbZEybNq3Kvo0aNcqaa65ZpUVCw4YNkywYrC7JAQcckMcffzxDhw5NRUVF9t9//yo1JlVn/BZFkQsvvHCJx23SpElatGiRf/zjH1XWX3TRRQuMrVmz5gKzin/3u98tcubzn/70pyr9kC+++OJ89tlnCzw7X9SvX7+88cYbufTSSxfY9vHHH+fDDz9c7PWceuqpmTZtWgYNGpTPPvtsge133HFHbrnlliT/Fyp+8drnzp2bP/3pT4s9R3W0atUqvXr1yiWXXLLQvz5YlhY+O+ywQxo3bpwzzzyzskXPfIub7d2vX7/MnTs3p59++gLbPvvss8pncfr06QscZ/5fC1SnZcm///3v3HDDDZWfZ86cmb/+9a9Zb7310qZNm8r1tWrVyn777ZdrrrkmI0aMSLdu3dK9e/clHv9vf/tb1lhjjfzoRz/KXnvtVWU57rjj0qhRo8rZ6kt7Lb17986oUaMyduzYHHjggcvtLxOWxgYbbJDVV189F1xwwQL/Psy/lq/juQKAhTGTGwCA/wp9+/bNNttsk5NOOimvvPJK1l133dxxxx0ZM2ZMjj766MqAcL7vfve76dOnT4YMGZK6detWhqSnnnrqEs91880358knn0zy+QsN//nPf+aXv/xlkmS33XarDMD22muvbLbZZjnooIPy7LPPpkWLFrnooosyd+7cap3ny5o2bZphw4Ytcdwvf/nLjB8/PltuuWV+/OMfp1atWrnkkksye/bsnH322ZXj1l577fTq1SsbbrhhmjdvnkceeSSjR4/OEUccUTlm/ss5hwwZkj59+qRmzZrZd999l1jDD37wg5x22mkZM2ZMevToUWVm7FprrZWOHTvmuOOOyxtvvJEmTZrkuuuuq+zlvCSDBg3KWWedlUGDBmWjjTbKP/7xj8oZuF+066675oorrkjTpk2z9tpr54EHHsidd96ZlVdeeaHHnTNnTrbbbrv069cvzz//fC666KJsueWW2W233RZZy4EHHphrrrkmP/rRjzJhwoT06NEjc+fOzXPPPZdrrrkm48aNy0YbbbTI/ffZZ5889dRTOeOMM/L4449nv/32S4cOHTJt2rSMHTs2d911V2U/6HXWWSebbbZZTjzxxLz33ntp3rx5Ro0atdBwfFn84Q9/yJZbbplu3brlkEMOyRprrJG33347DzzwQP71r39VPvPV1aRJk5x//vkZNGhQNt544+y///5p1qxZnnzyyXz00Ue5/PLLF7pfz549c+ihh+bMM8/ME088kR122CG1a9fOiy++mGuvvTYXXnhh9tprr1x++eW56KKLsueee6Zjx46ZNWtWLr300jRp0mSxs+/n69y5cw4++OBMmjQprVu3zl/+8pe8/fbbGT58+AJj+/fvn9/+9reZMGFCfv3rXy/x2P/+978zYcKEBV6EO1/dunXTp0+fXHvttfntb3+7TNeyxx57ZPjw4enfv3+aNGmSSy65ZIl1LU81atTIxRdfnL59+2a99dbLQQcdlLZt2+a5557LM888k3HjxiVZ/s8VACxUAQAAJXT44YcXX/7P2VmzZhXHHHNM0a5du6J27dpFp06dinPOOaeYN29elXFJisMPP7z429/+VnTq1KmoW7dusf766xcTJkyo1rkHDBhQJFnoMnz48Cpj33vvveLggw8uVl555aJBgwZFz549i0mTJlXrPD179izWWWedxY6ZMGFCkaS49tprq6x/7LHHij59+hSNGjUqGjRoUGyzzTbF/fffX2XML3/5y2KTTTYpVlpppaJ+/frFWmutVZxxxhnFnDlzKsd89tlnxZFHHlm0bNmyqKioWOCeL87GG29cJCkuuuiiBbY9++yzRe/evYtGjRoVLVq0KA455JDiySefXOAeDh06dIFzfvTRR8XBBx9cNG3atGjcuHHRr1+/4p133imSFEOHDq0cN3369OKggw4qWrRoUTRq1Kjo06dP8dxzzxUdOnQoBgwYUDlu+PDhRZLi7rvvLgYPHlw0a9asaNSoUXHAAQcU06ZNq3Lunj17Fj179qyybs6cOcWvf/3rYp111inq1q1bNGvWrNhwww2LU089tZgxY0a17tVdd91V7L777kWrVq2KWrVqFS1btiz69u1bjBkzpsq4KVOmFL179y7q1q1btG7duvj5z39ejB8/vkhS5fld1LMzderUIklxzjnnLLSOKVOmFP379y/atGlT1K5du1hllVWKXXfdtRg9evQC9+vLz/H8Z/HLP0c33XRTscUWWxT169cvmjRpUmyyySbFVVddVbl9wIABRYcOHRao5U9/+lOx4YYbFvXr1y8aN25cdOvWrfjpT39a/Pvf/y6K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AgAAlENpZnJX5wVOAwcOrNafBa8oI0aMyEorrbSiy1hqEydOTEVFRd5///2v5fhL+3Kub6tevXrl6KOPXtFlLNSXn71hw4Yt8HKzxXnllVdSUVGx2D+hB6D65s6dm/333z+nnnpqOnfuXK19Dj/88Dz99NMZNWrU11wdAABAuazQkHvgwIGpqKhIRUVFateundatW2f77bfPX/7yl8ybN6/K2DfffDM77bTTCqq0HEaMGFF5P7+41KtX7ysdd4sttsibb775/3sll8Pll1+eLbfcMsnn4fMX70Xnzp1z5pln5ptuR//l76dRo0bZcMMNc/3113/t595nn33ywgsvLPP+7du3z5tvvmnmIMByMmvWrDzyyCM54ogjUqtWrdSqVSunnXZannzyydSqVSt///vfq4w/4ogjcsstt2TChAn5zne+s4KqBgAA+HZa4e1KdtxxxwwfPjxz587N22+/nbFjx+aoo47K6NGjc9NNN1X++W6bNm0We5xPP/30myj3W69JkyZ5/vnnq6yrqKj4SsesU6fOYu//3LlzU1FRkRo1vj1/GDBmzJjstttulZ8POeSQnHbaaZk9e3b+/ve/Z/DgwVlppZVy2GGHfaN1ffH7mTVrVoYPH55+/frlmWeeSZcuXRa6z5w5c1KnTp2vdN769eunfv36y7x/zZo1F/sMFEWRuXPnVuvP7QH4/P8ePPXUU1XWXXTRRfn73/+e0aNHZ/XVV0/y+b+vRx55ZG644YZMnDixcj0AAAD/Z4WnknXr1k2bNm2yyiqrZIMNNsjPf/7zjBkzJrfffntGjBhROe6LLS3mt064+uqr07Nnz9SrVy8jR46sHHvuueembdu2WXnllXP44YdXCcCvuOKKbLTRRmncuHHatGmT/fffP++8807l9vmtOcaNG5f1118/9evXz7bbbpt33nknt99+e7p27ZomTZpk//33z0cffbTYaxsxYkRWXXXVNGjQIHvuuWemTZu2wJiLL744HTt2TJ06ddKlS5dcccUVlduKosiwYcOy6qqrpm7dumnXrl2GDBmy2HNWVFSkTZs2VZbWrVtXbu/Vq1eOPPLIHH300WnWrFlat26dSy+9NB9++GEOOuigNG7cOGuuuWZuv/32Be7J/HYl81tf3HTTTVl77bVTt27dvPbaa5k0aVK23377tGjRIk2bNk3Pnj3z2GOPVanvxRdfzNZbb5169epl7bXXzvjx4xe4hqeeeirbbrtt6tevn5VXXjmDBw/OBx98UKWeTTbZJA0bNsxKK62UHj165NVXX63c/sknn+SOO+6oEnI3aNAgbdq0SYcOHXLQQQele/fuVc49e/bsHHfccVlllVXSsGHDbLrpppk4cWLl9mnTpmW//fbLKquskgYNGqRbt2656qqrFvtdLOn76dSpU375y1+mRo0a+ec//1k5ZrXVVsvpp5+e/v37p0mTJhk8eHCS5Gc/+1k6d+6cBg0aZI011sgpp5xS5dl+8skns80226Rx48Zp0qRJNtxwwzzyyCNJqtcq57LLLkvXrl1Tr169rLXWWrnooosqt325Xcn8Z+L222/PhhtumLp16+bee+/N7NmzM2TIkLRq1Sr16tXLlltumUmTJi3ynLNnz87MmTOrLABl9cEHH+SJJ56o/Ldy6tSpeeKJJ/Laa68lSU488cT0798/SVKjRo1897vfrbLM/7fzu9/9bho2bJjk8xYlf/vb33LllVemcePGeeutt/LWW2/l448/XiHXCAAA8G20wkPuhdl2222z7rrrLrGNwwknnJCjjjoqkydPTp8+fZIkEyZMyJQpUzJhwoRcfvnlGTFiRJWw/NNPP83pp5+eJ598MjfeeGNeeeWVDBw4cIFjDxs2LL///e9z//335/XXX0+/fv1ywQUX5Morr8ytt96aO+64I7/73e8WWdtDDz2Ugw8+OEcccUSeeOKJbLPNNvnlL39ZZcwNN9yQo446Kj/5yU/y9NNP59BDD81BBx2UCRMmJEmuu+66nH/++bnkkkvy4osv5sYbb0y3bt2qeRcX7fLLL0+LFi3y8MMP58gjj8xhhx2WvffeO1tssUUee+yx7LDDDjnwwAMXG+J/9NFH+fWvf53LLrsszzzzTFq1apVZs2ZlwIABuffee/Pggw+mU6dO2XnnnTNr1qwkn78w63vf+17q1KmThx56KH/84x/zs5/9rMpxP/zww/Tp0yfNmjXLpEmTcu211+bOO+/MEUcckST57LPPsscee6Rnz5755z//mQceeCCDBw+uMlv9rrvuyiqrrJK11lprgbqLosg999yT5557rsrs6COOOCIPPPBARo0alX/+85/Ze++9s+OOO+bFF19M8nlwvuGGG+bWW2/N008/ncGDB+fAAw/Mww8/vMzfw9y5c3P55ZcnSTbYYIMq284999ysu+66efzxx3PKKackSRo3bpwRI0bk2WefzYUXXphLL700559/fuU+BxxwQL7zne9k0qRJefTRR3PCCSekdu3a1apl5MiR+cUvfpEzzjgjkydPzq9+9auccsoplfUtygknnJCzzjorkydPTvfu3fPTn/401113XS6//PI89thjWXPNNdOnT5+89957C93/zDPPTNOmTSuX9u3bV6tegG+jRx55JOuvv37WX3/9JMmxxx6b9ddfP7/4xS+SfN56bX7gXV0XX3xxZsyYkV69eqVt27aVy9VXX73c6wcAACitYgUaMGBAsfvuuy902z777FN07dq18nOS4oYbbiiKoiimTp1aJCkuuOCCBY7XoUOH4rPPPqtct/feexf77LPPImuYNGlSkaSYNWtWURRFMWHChCJJceedd1aOOfPMM4skxZQpUyrXHXrooUWfPn0Wedz99tuv2HnnnRe4pqZNm1Z+3mKLLYpDDjmkypi99967cr/zzjuv6Ny5czFnzpxFnueLhg8fXiQpGjZsWGXZcccdK8f07Nmz2HLLLSs/f/bZZ0XDhg2LAw88sHLdm2++WSQpHnjggaIo/u+eTJ8+vcp5nnjiicXWM3fu3KJx48bFzTffXBRFUYwbN66oVatW8cYbb1SOuf3226t8t3/605+KZs2aFR988EHlmFtvvbWoUaNG8dZbbxXTpk0rkhQTJ05c5HkPOeSQ4rjjjqtyzbVr1y4aNmxY1K5du0hS1KtXr7jvvvuKoiiKV199tahZs2aVuoqiKLbbbrvixBNPXOR5dtlll+InP/lJlfMcddRRixz/5e+nRo0aRd26dYvhw4dXGdehQ4dijz32WORx5jvnnHOKDTfcsPJz48aNixEjRizy3F989oYOHVqsu+66lZ87duxYXHnllVX2Of3004vNN9+8KIr/+5l7/PHHi6L4v2fixhtvrBz/wQcfFLVr1y5GjhxZuW7OnDlFu3btirPPPnuhdX3yySfFjBkzKpfXX3+9SFIkM4qksFgsllIsAAAALH8zZswokhQzZsxY4thvbQPdoiiW2Et6o402WmDdOuusk5o1a1Z+btu2bZWel48++miGDRuWJ598MtOnT698weVrr72Wtddeu3Jc9+7dK/9369atK1tEfHHd4mbxTp48OXvuuWeVdZtvvnnGjh1bZcz8VhTz9ejRIxdeeGGSZO+9984FF1yQNdZYIzvuuGN23nnn9O3bd7F9jxs3brxAi5Av92L+4rXVrFkzK6+8cpUZ4vPbm3yxjcuX1alTp8pxkuTtt9/OySefnIkTJ+add97J3Llz89FHH1XOWps8eXLat2+fdu3aVbknXzR58uSsu+66lX+mPf+ezJs3L88//3y23nrrDBw4MH369Mn222+f3r17p1+/fmnbtm2Sz5+bm2++Oddcc02V4x5wwAE56aSTMn369AwdOjRbbLFFtthiiySft0eZO3duOnfuXGWf2bNnZ+WVV07y+azrX/3qV7nmmmvyxhtvZM6cOZk9e3YaNGiwyHu0MF/8fj766KPceeed+dGPfpSVV145ffv2rRy3sGf76quvzm9/+9tMmTIlH3zwQT777LM0adKkcvuxxx6bQYMG5Yorrkjv3r2z9957p2PHjkus6cMPP8yUKVNy8MEH55BDDqlc/9lnny3xZaNfrHPKlCn59NNP06NHj8p1tWvXziabbJLJkycvdP+6deumbt26S6wRAAAAABblWxtyT548eYkvV/piEDrfl9szVFRUVAbZ81th9OnTJyNHjkzLli3z2muvpU+fPpkzZ84ij1NRUbHY435d2rdvn+effz533nlnxo8fnx//+Mc555xzcvfddy+yDUWNGjWy5pprLva4C7uWL19vksVeX/369Rf4JcSAAQMybdq0XHjhhenQoUPq1q2bzTfffIF7+1UNHz48Q4YMydixY3P11Vfn5JNPzvjx47PZZpvl4YcfzmeffVYZYM/XtGnTyvtyzTXXZM0118xmm22W3r1754MPPkjNmjXz6KOPVvkFSZI0atQoSXLOOefkwgsvzAUXXJBu3bqlYcOGOfroo5f62r78/XTv3j133HFHfv3rX1cJub/8bD/wwAM54IADcuqpp6ZPnz5p2rRpRo0alfPOO69yzLBhw7L//vvn1ltvze23356hQ4dm1KhRC/yy5cvm9zu/9NJLs+mmm1bZ9uX78WUL+xkEAAAAgG/St7In99///vc89dRT+f73v79cj/vcc89l2rRpOeuss7LVVltlrbXWWuxs5a+ia9eueeihh6qse/DBBxcYc99991VZd99991WZUV6/fv307ds3v/3tbzNx4sQ88MADVWamf5vcd999GTJkSHbeeeess846qVu3bv7zn/9Ubu/atWtef/31vPnmm5XrFnZPnnzyyXz44YdVjlujRo106dKlct3666+fE088Mffff3+++93v5sorr0ySjBkzJrvssstiw9lGjRrlqKOOynHHHZeiKLL++utn7ty5eeedd7LmmmtWWdq0aVNZw+67754f/OAHWXfddbPGGmvkhRde+Go37P+rWbPmEl8gdv/996dDhw456aSTstFGG6VTp05VXrY5X+fOnXPMMcfkjjvuyPe+970MHz58iedv3bp12rVrl5dffnmB61/SL5q+aP4LVL/4TH/66aeZNGlSlWcaAAAAAJanFT6Te/bs2Xnrrbcyd+7cvP322xk7dmzOPPPM7Lrrrunfv/9yPdeqq66aOnXq5He/+11+9KMf5emnn87pp5++XM8x35AhQ9KjR4+ce+652X333TNu3LgqrUqS5Pjjj0+/fv2y/vrrp3fv3rn55ptz/fXX584770ySjBgxInPnzs2mm26aBg0a5G9/+1vq16+fDh06LPK8RVHkrbfeWmB9q1atUqPG1/s7jU6dOuWKK67IRhttlJkzZ+b444+v0iqld+/e6dy5cwYMGJBzzjknM2fOzEknnVTlGAcccECGDh2aAQMGZNiwYXn33Xdz5JFH5sADD0zr1q0zderU/OlPf8puu+2Wdu3a5fnnn8+LL75Y+azcdNNNOe2005ZY66GHHprTTz891113Xfbaa68ccMAB6d+/f84777ysv/76effdd3PXXXele/fu2WWXXdKpU6eMHj06999/f5o1a5bf/OY3efvtt5c6vP3i9/Pxxx9n/PjxGTduXOVLyRZ3b1977bWMGjUqG2+8cW699dbccMMNlds//vjjHH/88dlrr72y+uqr51//+lcmTZpU7V8UnXrqqRkyZEiaNm2aHXfcMbNnz84jjzyS6dOn59hjj63WMRo2bJjDDjssxx9/fJo3b55VV101Z599dj766KMcfPDB1ToGAAAAACytFT6Te+zYsWnbtm1WW2217LjjjpkwYUJ++9vfZsyYMUtslbC0WrZsmREjRuTaa6/N2muvnbPOOivnnnvucj3HfJtttlkuvfTSXHjhhVl33XVzxx135OSTT64yZo899siFF16Yc889N+uss04uueSSDB8+PL169UqSrLTSSrn00kvTo0ePdO/ePXfeeWduvvnmyj7RCzNz5sy0bdt2geXrmrH+RX/+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5aIAAAAAAKA6lqkn96mnnpp99tkn//jHPyp7ct9333256667Fhp+AwAAAADA12GZZnJ///vfz0MPPZQWLVrkxhtvzI033pgWLVrk4Ycfzp577rm8awQAAAAAgIVaphdPAnwdvHgSAAD4byBpAfjqlubFk8vUriRJ5s6dmxtuuCGTJ09Okqy99trZfffdU6vWMh8SAAAAAACWyjK1K3nmmWfSuXPnDBgwIDfccENuuOGGDBgwIJ06dcrTTz+9vGsEAAAAKJWLL7443bt3T5MmTdKkSZNsvvnmuf322xe7zwUXXJAuXbqkfv36ad++fY455ph88sknVca88cYb+cEPfpCVV1459evXT7du3fLII498nZcC8K23TNOuBw0alHXWWSePPPJImjVrliSZPn16Bg4cmMGDB+f+++9frkUCAAAAlMl3vvOdnHXWWenUqVOKosjll1+e3XffPY8//njWWWedBcZfeeWVOeGEE/KXv/wlW2yxRV544YUMHDgwFRUV+c1vfpPk8+ylR48e2WabbXL77benZcuWefHFFyuzGYD/VcvUk7t+/fp55JFHFvhH+emnn87GG2+cjz/+eLkVCPzv0JMbAAD4b7CopKV58+Y555xzcvDBBy+w7YgjjsjkyZNz1113Va77yU9+koceeij33ntvkuSEE07Ifffdl3vuuedrqRvg22RpenIvU7uSzp075+23315g/TvvvJM111xzWQ4JAAAA8F9p7ty5GTVqVD788MNsvvnmCx2zxRZb5NFHH83DDz+cJHn55Zdz2223Zeedd64cc9NNN2WjjTbK3nvvnVatWmX99dfPpZde+o1cA8C3WbVD7pkzZ1YuZ555ZoYMGZLRo0fnX//6V/71r39l9OjROfroo/PrX//666x3mb300kv51a9+ZZY5AAAA8I146qmn0qhRo9StWzc/+tGPcsMNN2Tttdde6Nj9998/p512WrbccsvUrl07HTt2TK9evfLzn/+8cszLL7+ciy++OJ06dcq4ceNy2GGHZciQIbn88su/qUsC+Faqdsi90korpVmzZmnWrFn69u2bZ599Nv369UuHDh3SoUOH9OvXL08//XT69u37dda7TD755JPstddeadeuXerXr1+5ftiwYVlvvfW+sTpWW221XHDBBV/7eUaMGJGVVlrpaz8P/+ebfpaWxiuvvJKKioo88cQTSZKJEyemoqIi77//frWP8U09uwAAAP9NunTpkieeeCIPPfRQDjvssAwYMCDPPvvsQsdOnDgxv/rVr3LRRRflsccey/XXX59bb701p59+euWYefPmZYMNNsivfvWrrL/++hk8eHAOOeSQ/PGPf/ymLgngW6naL56cMGHC11lHtQ0cOLDyN5S1atVK8+bN07179+y3334ZOHBgatRYMLc/8sgjs8cee2TgwIHfcLVfjwkTJuScc87JQw89lI8//jirrbZadtpppxx77LFZZZVVss8++1T5c6b/Na+++mrWWmutvPvuuzn33HNz6qmnJklq1KiRdu3aZaeddspZZ52V5s2bf2M1vfLKK1l99dUrP9euXTurrrpqBg4cmJNOOikVFRVf27nbt2+fN998My1atFjmY0yaNCkNGzZcjlUBAAD896tTp05lW9cNN9wwkyZNyoUXXphLLrlkgbGnnHJKDjzwwAwaNChJ0q1bt3z44YcZPHhwTjrppNSoUSNt27ZdYCZ4165dc9111339FwPwLVbtkLtnz55fZx1LZccdd8zw4cMzd+7cvP322xk7dmyOOuqojB49OjfddFNq1ap6WV9nf6pPP/00tWvX/tqO/2WXXHJJfvzjH2fAgAG57rrrstpqq+W1117LX//615x33nn5zW9+k/r161eZsV52c+bMSZ06dao9fsyYMdlmm23SqFGjJMk666yTO++8M3Pnzs3kyZPzwx/+MDNmzMjVV1/9dZW8SHfeeWfWWWedzJ49O/fee28GDRqUtm3bLvSlI8nSX/vC1KxZM23atPlKx2jZsuVit3/TPwcAAABlNG/evMyePXuh2z766KMFJu7VrFkzSVL8/zdZ9ujRI88//3yVMS+88EI6dOjwNVQLUB7L9OLJ5PMWIA8//HBuueWW3HTTTVWWr1vdunXTpk2brLLKKtlggw3y85//PGPGjMntt9+eESNGVI577bXXsvvuu6dRo0Zp0qRJ+vXrt9AXZs43adKkbL/99mnRokWaNm2anj175rHHHqsypqKiIhdffHF22223NGzYMGecccZCj/XOO++kb9++qV+/flZfffWMHDlygTHvv/9+Bg0alJYtW6ZJkybZdttt8+STTy6yvn/9618ZMmRIhgwZkr/85S/p1atXVltttWy99da57LLL8otf/CLJgu1K5rfSuOKKK7LaaquladOm2XfffTNr1qzKMbNmzcoBBxyQhg0bpm3btjn//PPTq1evHH300ZVjrrjiimy00UZp3Lhx2rRpk/333z/vvPNO5fb5bTBuvfXWdO/ePfXq1ctmm22Wp59+eoFavuiCCy7IaqutVvl54MCB2WOPPXLGGWekXbt26dKlS7XOP9+YMWOy2267VX6uVatW5fPSu3fv7L333hk/fnyVfS677LJ07do19erVy1prrZWLLrqoyvaf/exn6dy5cxo0aJA11lgjp5xySj799NNFfFOLtvLKK6dNmzbp0KFDDjjggPTo0aPKM7as1z59+vQccMABadmyZerXr59OnTpl+PDhSRZsV7Iw9957b7baaqvUr18/7du3z5AhQ/Lhhx9Wbv9yu5JF/RxcfPHF6dixY+rUqZMuXbrkiiuuWOp7BAAA8N/gxBNPzD/+8Y+88soreeqpp3LiiSdm4sSJOeCAA5Ik/fv3z4knnlg5vm/fvrn44oszatSoTJ06NePHj88pp5ySvn37VobdxxxzTB588MH86le/yksvvZQrr7wyf/rTn3L44YevkGsE+Lao9kzuLxo7dmz69++f//znPwtsq6ioyNy5c79yYUtr2223zbrrrpvrr78+gwYNyrx58yoD7rvvvjufffZZDj/88Oyzzz6ZOHHiQo8xa9asDBgwIL/73e9SFEXOO++87LzzznnxxRfTuHHjynHDhg3LWWedlQsuuGCBWePzDRw4MP/+978zYcKE1K5dO0OGDFkgkN17771Tv3793H777WnatGkuueSSbLfddnnhhRcW2krj2muvzZw5c/LTn/50oedcXB/uKVOm5MYbb8wtt9yS6dOnp1+/fjnrrLMqw8ljjz029913X2666aa0bt06v/jFL/LYY49VCaQ//fTTnH766enSpUveeeedHHvssRk4cGBuu+22Kuc6/vjjc+GFF6ZNmzb5+c9/nr59++aFF15Yqpm+d911V5o0aVIljK7O+d9///3ce++9iwxXX3nllYwbN67K7OiRI0fmF7/4RX7/+99n/fXXz+OPP55DDjkkDRs2zIABA5IkjRs3zogRI9KuXbs89dRTOeSQQ9K4ceNFfhfV8cgjj+TRRx9N//79v/K1n3LKKXn22Wdz++23p0WLFnnppZeq/ZLVKVOmZMcdd8wvf/nL/OUvf8m7776bI444IkcccURlUL4wX/45uOGGG3LUUUflggsuSO/evXPLLbfkoIMOyne+851ss802Cz3G7Nmzq8ximDlzZrVqBgAA+LZ755130r9//7z55ptp2rRpunfvnnHjxmX77bdP8vnEvC/O3D755JNTUVGRk08+OW+88UZatmyZvn37Vplct/HGG+eGG27IiSeemNNOOy2rr756LrjggsrgHOB/VrEM1lxzzeLHP/5x8dZbby3L7l/JgAEDit13332h2/bZZ5+ia9euRVEUxR133FHUrFmzeO211yq3P/PMM0WS4uGHHy6KoiiGDh1arLvuuos819y5c4vGjRsXN998c+W6JMXRRx+92Bqff/75KucpiqKYPHlykaQ4//zzi6Ioinvuuado0qRJ8cknn1TZt2PHjsUll1yy0OMedthhRZMmTRZ77qIoiuHDhxdNmzat/Dx06NCiQYMGxcyZMyvXHX/88cWmm25aFEVRzJw5s6hdu3Zx7bXXVm5///33iwYNGhRHHXXUIs8zadKkIkkxa9asoiiKYsKECUWSYtSoUZVjpk2bVtSvX7+4+uqrK2v58j0///zziw4dOlR+HjBgQNG6deti9uzZi73OL5+/KIpi5MiRxUYbbVTl2mvUqFE0bNiwqFevXpGkSFL85je/qRzTsWPH4sorr6xy7NNPP73YfPPNF3nuc845p9hwww2rnGdxz9LUqVOLJEX9+vWLhg0bFrVr1y6SFIMHD64yblmvvW/fvsVBBx202HM//vjjRVH83/c0ffr0oiiK4uCDD16gjnvuuaeoUaNG8fHHHxdFURQdOnSofHaLYuE/B1tssUVxyCGHVFm39957FzvvvPMir2Po0KGV30nVZUaRFBaLxWKxWCwWi8VSygWAr27GjBlFkmLGjBlLHLtM7UrefvvtHHvssWnduvVXiNeXv6IoKl/gN3ny5LRv3z7t27ev3L722mtnpZVWyuTJkxe6/9tvv51DDjkknTp1StOmTdOkSZN88MEHee2116qM22ijjRZbx+TJk1OrVq1suOGGlevWWmutKjOtn3zyyXzwwQdZeeWV06hRo8pl6tSpmTJlyhKvb2mtttpqVWajt23btnJm+csvv5xPP/00m2yySeX2pk2bVrbKmO/RRx9N3759s+qqq6Zx48aVfdq/fH8233zzyv/dvHnzdOnSZZH3fFG6deu2QC/q6pz/y61Kkv97m/WkSZPys5/9LH369MmRRx6ZJPnwww8zZcqUHHzwwVW+h1/+8pdVvoerr746PXr0SJs2bdKoUaOcfPLJC1x3dVx99dV54okn8uSTT+aaa67JmDFjcsIJJ3zlaz/ssMMyatSorLfeevnpT3+a+++/v9o1PfnkkxkxYkSV6+/Tp0/mzZuXqVOnLnK/L/8cTJ48OT169KiyrkePHov97k888cTMmDGjcnn99derXTcAAAAAJMvYrmSvvfbKxIkT07Fjx+Vdz1cyefLkrL766su8/4ABAzJt2rRceOGF6dChQ+rWrZvNN988c+bMqTKuYcOGX7XUfPDBB2nbtu1CW6csqu1I586dM2PGjLz55ptp27btUp3vy61CKioqMm/evGrv/+GHH6ZPnz7p06dPRo4cmZYtW+a1115Lnz59Frg/i1OjRo0URVFl3cJ6W3/5Hlfn/HPmzMnYsWPz85//vMq+X3yb9VlnnZVddtklp556ak4//fR88MEHST5/Oemmm25aZb/5Pc8eeOCBHHDAATn11FPTp0+fNG3aNKNGjcp5551X7euer3379pW1dO3aNVOmTMkpp5ySYcOGpV69est87TvttFNeffXV3HbbbRk/fny22267HH744Tn33HOXWNMHH3yQQw89NEOGDFlg26qrrrrI/ZbHz0HdunVTt27dr3wcAAAAAP53LVPI/fvf/z5777137rnnnnTr1m2BAHVhYdnX7e9//3ueeuqpHHPMMUk+DxBff/31vP7665WzuZ999tm8//77WXvttRd6jPvuuy8XXXRRdt555yTJ66+/vtC+40uy1lpr5bPPPsujjz6ajTfeOEny/PPP5/33368cs8EGG+Stt95KrVq1qrx0cXH22muvnHDCCTn77LNz/vnnL7D9/fffX2xf7kVZY401Urt27UyaNKky1JwxY0ZeeOGFbL311kmS5557LtOmTctZZ51VeT8feeSRhR7vwQcfrDzO9OnT88ILL6Rr165JkpYtW+att96qMit9cS9EnK865584cWKaNWuWddddd7HHOvnkk7PtttvmsMMOS7t27dKuXbu8/PLLi+xhdv/996dDhw456aSTKte9+uqrS6y5OmrWrJnPPvssc+bMqQy5v6y6975ly5YZMGBABgwYkK222irHH398tULuDTbYIM8++2xl+L6sunbtmvvuu6+yj3ny+c/Uon7eAAAAAGB5WKaQ+6qrrsodd9yRevXqZeLEiVVaaFRUVHztIffs2bPz1ltvZe7cuXn77bczduzYnHnmmdl1110rX+LXu3fvdOvWLQcccEAuuOCCfPbZZ/nxj3+cnj17LrLdSKdOnXLFFVdko402ysyZM3P88cenfv36S11fly5dsuOOO+bQQw/NxRdfnFq1auXoo4+ucqzevXtn8803zx577JGzzz47nTt3zr///e/ceuut2XPPPRdaY/v27XP++efniCOOyMyZM9O/f/+sttpq+de//pW//vWvadSo0TLNLm7cuHEGDBiQ448/Ps2bN0+rVq0ydOjQ1KhRo/K7XXXVVVOnTp387ne/y49+9KM8/fTTOf300xd6vNNOOy0rr7xyWrdunZNOOiktWrTIHnvskSTp1atX3n333Zx99tnZa6+9Mnbs2Nx+++1p0qTJYmuszvlvuummBVqVLMzmm2+e7t2751e/+lV+//vf59RTT82QIUPStGnT7Ljjjpk9e3YeeeSRTJ8+Pccee2w6deqU1157LaNGjcrGG2+cW2+9NTfccEM17uyCpk2blrfeeiufffZZnnrqqVx44YXZZpttFnv91bn2X/ziF9lwww2zzjrrZPbs2bnlllsqf7GwJD/72c+y2Wab5YgjjsigQYPSsGHDPPvssxk/fnx+//vfV/vajj/++PTr1y/rr79+evfunZtvvjnXX3997rzzzmofAwAAAACW1jL15D7ppJNy6qmnZsaMGXnllVcyderUyuXll19e3jUuYOzYsWnbtm1WW2217LjjjpkwYUJ++9vfZsyYMZUtJioqKjJmzJg0a9YsW2+9dXr37p011lgjV1999SKP++c//znTp0/PBhtskAMPPDBDhgxJq1atlqnG4cOHp127dunZs2e+973vZfDgwVWOVVFRkdtuuy1bb711DjrooHTu3Dn77rtvXn311cX2Ov/xj3+cO+64I2+88Ub23HPPrLXWWhk0aFCaNGmS4447bplqTZLf/OY32XzzzbPrrrumd+/e6dGjR7p27Vo5u7hly5YZMWJErr322qy99to566yzFjlL+KyzzspRRx2VDTfcMG+99VZuvvnmyh7TXbt2zUUXXZQ//OEPWXfddfPwww9Xq+7qnL+6IXeSHHPMMbnsssvy+uuvZ9CgQbnssssyfPjwdOvWLT179syIESMqW9/stttuOeaYY3LEEUdkvfXWy/33359TTjmlWuf5st69e1c+u4MHD87OO++82Geyutdep06dnHjiienevXu23nrr1KxZM6NGjapWTd27d8/dd9+dF154IVtttVXWX3/9/OIXv0i7du2W6tr22GOPXHjhhTn33HOzzjrr5JJLLsnw4cPTq1evpToOAAAAACyNiuLLDZKroXnz5pk0adK3ric3y8+HH36YVVZZJeedd14OPvjgau0zceLEbLPNNpk+ffoytU35Kh577LFsu+22effddxdon0N5zJw5M02bNk0yI8niZ/cDAAB8Wy190gLAl83PiWbMmLHELhDLNJN7wIABS5x9Srk8/vjjueqqqzJlypQ89thjlf2pd9999xVcWfV89tln+d3vfifgBgAAAID/McvUk3vu3Lk5++yzM27cuHTv3n2BYPE3v/nNcimOb9a5556b559/PnXq1MmGG26Ye+65Jy1atFjRZVXLJptskk022WRFlwEAAAAAfMOWqV3JNttss+gDVlTk73//+1cqCvjfpF0JAADw30C7EoCvbmnalSzTTO4JEyYsU2EAAAAAALA8LVNP7uHDh+fjjz9e3rUAAAAAAMBSWaaQ+4QTTkjr1q1z8MEH5/7771/eNQEAAAAAQLUsU8j9xhtv5PLLL89//vOf9OrVK2uttVZ+/etf56233lre9QEAAAAAwCItU8hdq1at7LnnnhkzZkxef/31HHLIIRk5cmRWXXXV7LbbbhkzZkzmzZu3vGsFAAAAAIAqlink/qLWrVtnyy23zOabb54aNWrkqaeeyoABA9KxY8dMnDhxOZQIAAAAAAALt8wh99tvv51zzz0366yzTnr16pWZM2fmlltuydSpU/PGG2+kX79+GTBgwPKsFQAAAAAAqqgoiqJY2p369u2bcePGpXPnzhk0aFD69++f5s2bVxnzzjvvpE2bNtqWANU2c+bMNG3aNMmMJE1WdDkAAADLZOmTFgC+bH5ONGPGjDRpsvicqNaynKBVq1a5++67s/nmmy9yTMuWLTN16tRlOTwAAAAAAFTLUrUreeCBB3LLLbfkz3/+c2XA/de//jWrr756WrVqlcGDB2f27NlJkoqKinTo0GH5VwwAAAAAAP/fUoXcp512Wp555pnKz0899VQOPvjg9O7dOyeccEJuvvnmnHnmmcu9SAAAAAAAWJilCrmfeOKJbLfddpWfR40alU033TSXXnppjj322Pz2t7/NNddcs9yLBAAAAACAhVmqkHv69Olp3bp15ee77747O+20U+XnjTfeOK+//vryqw4AAAAAABZjqULu1q1bV75Mcs6cOXnsscey2WabVW6fNWtWateuvXwrBAAAAACARViqkHvnnXfOCSeckHvuuScnnnhiGjRokK222qpy+z//+c907NhxuRcJAAAAAAALU2tpBp9++un53ve+l549e6ZRo0a5/PLLU6dOncrtf/nLX7LDDjss9yIBAAAAAGBhKoqiKJZ2pxkzZqRRo0apWbNmlfXvvfdeGjVqVCX4BqiumTNnpmnTpklmJGmyossBAABYJkuftADwZfNzohkzZqRJk8XnREs1k3u+z0OoBTVv3nxZDgcAAAAAAMtkqXpyAwAAAADAt4mQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKq9aKLgDgy2bMSJo0WdFVAAAAAFAGZnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUVq0VXQDAlzVtuqIrAAAAACiHoljRFax4ZnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAAAlNmzYsFRUVFRZ1lprrUWOv/TSS7PVVlulWbNmadasWXr37p2HH374G6x4+RJyAwAAAACU3DrrrJM333yzcrn33nsXOXbixInZb7/9MmHChDzwwANp3759dthhh7zxxhvfYMXLT60VXQAAAAAAAF9NrVq10qZNm2qNHTlyZJXPl112Wa677rrcdddd6d+//9dR3tfKTO5l8NJLL+VXv/pVPv744xVdCgAAAABAXnzxxbRr1y5rrLFGDjjggLz22mvV3vejjz7Kp59+mubNm3+NFX59hNxL6ZNPPslee+2Vdu3apX79+pXrhw0blvXWW2/FFfYNGzhwYPbYY48VXca3xrf5+3/llVdSUVGRJ554Isnnf45SUVGR999/v9rHWG211XLBBRd8LfUBAAAA8NVsuummGTFiRMaOHZuLL744U6dOzVZbbZVZs2ZVa/+f/exnadeuXXr37v01V/r1+J8OuQcOHFjZiL127dpp3bp1tt9++/zlL3/JvHnzFrrPkUcemT322CMDBw78ZotNctVVV6VmzZo5/PDDv/Fzf9mFF16YESNGrOgyFurVV19N/fr188EHH1Rpul+zZs20b98+gwcPznvvvfeN1jQ/aJ6/1KlTJ2uuuWZ++ctfpiiKr/Xc7du3z5tvvpnvfve7y3yMSZMmZfDgwcuxKgAAAACWl5122il77713unfvnj59+uS2227L+++/n2uuuWaJ+5511lkZNWpUbrjhhtSrV+8bqHb5+5/vyb3jjjtm+PDhmTt3bt5+++2MHTs2Rx11VEaPHp2bbroptWpVvUWXXnrp11bLp59+mtq1ay9y+5///Of89Kc/zSWXXJLzzjtvhTx0c+fOTUVFRZo2bfqNn7u6xowZk2222SaNGjVK8nnT/TvvvDNz587N5MmT88Mf/jAzZszI1Vdf/Y3Xduedd2adddbJ7Nmzc++992bQoEFp27ZtDj744IWOnzNnTurUqfOVzlmzZs1q92NalJYtWy52+5KeXQAAAAC+OSuttFI6d+6cl156abHjzj333Jx11lm58847071792+ouuXvf3omd5LUrVs3bdq0ySqrrJINNtggP//5zzNmzJjcfvvtVWYqv/baa9l9993TqFGjNGnSJP369cvbb7+9yONOmjQp22+/fVq0aJGmTZumZ8+eeeyxx6qMqaioyMUXX5zddtstDRs2zBlnnLHI402dOjX3339/TjjhhHTu3DnXX399le0jRozISiutlFtuuSVdunRJgwYNstdee+Wjjz7K5ZdfntVWWy3NmjXLkCFDMnfu3Mr9Zs+eneOOOy6rrLJKGjZsmE033TQTJ05c4Lg33XRT1l577dStWzevvfbaAu1K5s2bl7PPPjtrrrlm6tatm1VXXbXK9fzsZz9L586d06BBg6yxxho55ZRT8umnn1Zun9/u44orrshqq62Wpk2bZt99963yJxWzZ8/OkCFD0qpVq9SrVy9bbrllJk2atMC9GjNmTHbbbbfKz/Ob7q+yyirp3bt39t5774wfP77KPpdddlm6du2aevXqZa211spFF11UZfuS6q+ulVdeOW3atEmHDh1ywAEHpEePHlWei/n39Ywzzki7du3SpUuXJMkVV1yRjTbaKI0bN06bNm2y//7755133qncb/r06TnggAPSsmXL1K9fP506dcrw4cOTLNiuZGHuvffebLXVVqlfv37at2+fIUOG5MMPP6zc/uV2JYt6di+++OJ07NgxderUSZcuXXLFFVcs9T0CAAAA4Kv54IMPMmXKlLRt23aRY84+++ycfvrpGTt2bDbaaKNvsLrl738+5F6YbbfdNuuuu25lkDxv3rzsvvvuee+993L33Xdn/Pjxefnll7PPPvss8hizZs3KgAEDcu+99+bBBx9Mp06dsvPOOy/QB2fYsGHZc88989RTT+WHP/zhIo83fPjw7LLLLmnatGl+8IMf5M9//vMCYz766KP89re/zahRozJ27NhMnDgxe+65Z2677bbcdtttueKKK3LJJZdk9OjRlfscccQReeCBBzJq1Kj885//zN57750dd9wxL774YpXj/vrXv85ll12WZ555Jq1atVrg3CeeeGLOOuusnHLKKXn22Wdz5ZVXpnXr1pXbGzdunBEjRuTZZ5/NhRdemEsvvTTnn39+lWNMmTIlN954Y2655Zbccsstufv/tXfvQVrVh/3438vqIiLgDY1buWhQRCMKXigxXiJUFGJihkaGIbI1aCxBDWrU0gaQITWYaCuGxDERMYkasI232HihRjFeMgJ2FZRoJSq0EUWC4JJmkeX8/vDnM1m5G/w+HH29Zj4zPuec55z37j4Hh/d++Jw5czJlypTK/ssuuyw///nP8+Mf/zhPP/10evTokUGDBrVaeuStt97KY4891qrk/nOvvPJKHnjggVazo2+99dZMmDAh//zP/5xFixblyiuvzPjx4/PjH/94m/Jvq3nz5mX+/Pnp169fq+0PPfRQXnjhhcyePTv33ntvkndnSk+ePDnPPPNM7rrrrrzyyiutlsx57/t+3333ZdGiRbn++uuz9957b1WOxYsX59RTT83QoUPz7LPPZtasWXnsscdy/vnnb/Z97//s3nnnnfn617+eSy65JAsXLsx5552Xs88+Ow8//PAmz9Hc3JzVq1e3GgAAAABsm2984xuZM2dOXnnllTzxxBP54he/mNra2gwfPjxJMnLkyIwbN65y/FVXXZXx48fnpptuSvfu3bNs2bIsW7YsTU1N1foS/jLFx1hDQ0PxhS98YaP7hg0bVvTq1asoiqJ48MEHi9ra2mLJkiWV/c8991yRpHjqqaeKoiiKiRMnFkccccQmr9XS0lJ06NCh+MUvflHZlqQYO3bsFnO2tLQUXbp0Ke66666iKIpi+fLlRV1dXfG73/2ucsyMGTOKJMVLL71U2XbeeecVu+66a/H2229Xtg0aNKg477zziqIoildffbWora0t/vd//7fV9QYMGFCMGzeu1XkbGxtbHfPn37vVq1cXbdu2LX70ox9t8Wt5z3e/+93iqKOOqryeOHFiseuuuxarV6+ubLv00kuLfv36FUVRFE1NTcXOO+9c3HrrrZX9a9euLerr64vvfOc7lW233nprcfTRR7c6b5s2bYr27dsXu+yyS5GkSFL8y7/8S+WYT37yk8Vtt93WKt/kyZOL/v37b1P+zf38X3755SJJ0a5du6J9+/bFzjvvXCQpvvrVr7Y6rqGhodh3332L5ubmTZ6rKIpi7ty5RZLKz/b0008vzj777M1e+7/+67+KoiiKhx9+uEhSrFy5siiKohg1atQGOX79618Xbdq0Kf7v//6vKIqi6NatW/Gv//qvlf0b++x++tOfLs4999xW2770pS8VgwcP3uTXMXHixMrPpPVYVSSFYRiGYRiGYRiGYRiGsYVRFO92mfvtt19RV1dX/NVf/VUxbNiwVj3hiSeeWDQ0NFRed+vWrdhYJzNx4sRN9jj/r61atapIUqxatWqLx37s1+TelKIoUlNTkyRZtGhRunTpki5dulT2H3roodl9992zaNGiHHPMMRu8//XXX883v/nNPPLII3njjTfS0tKSP/7xj1myZEmr47bmnwLMnj07a9asyeDBg5Mke++9d+UBmZMnT64ct+uuu+aTn/xk5fW+++6b7t27V9amfm/be8tcLFiwIC0tLTn44INbXa+5uTl77bVX5XVdXd1m1+RZtGhRmpubM2DAgE0eM2vWrFx33XVZvHhxmpqasm7dunTs2LHVMd27d0+HDh0qr/fbb79K1sWLF+edd97JcccdV9m/884759hjj82iRYsq296/VEmS9OzZM/fcc0/+9Kc/5ZZbbkljY2MuuOCCJMmaNWuyePHijBo1Kueee27lPevWrWu17vjW5N8as2bNSq9evfLOO+9k4cKFueCCC7LHHnu0mrF++OGHb7AO9/z583PFFVfkmWeeycqVKysPRl2yZEkOPfTQjB49OkOHDs3TTz+dU045JWeccUY+/elPb1WmZ555Js8++2xuvfXWyraiKLJ+/fq8/PLL6dWr10bf9/7P7qJFizZ4OOVxxx2XqVOnbvLa48aNy8UXX1x5vXr16lb3GQAAAABbNnPmzM3u//PliZN3Vzv4KFFyb8KiRYtywAEHfOD3NzQ0ZMWKFZk6dWq6deuWtm3bpn///lm7dm2r49q3b7/Fc02fPj1/+MMf0q5du8q29evX59lnn82kSZPSps27q868/8F/NTU1G932XkHa1NSU2trazJ8/P7W1ta2O+/NivF27dpXCf2P+PNfGPPnkkxkxYkQmTZqUQYMGpVOnTpk5c2auueaaVsdtLuvWWLt2be6///784z/+Y6vtdXV16dGjR5J3nxY7ZMiQTJo0KZMnT678E4wf/ehHGywb8t73ZGvzb40uXbpUsvTq1SuLFy/O+PHjc8UVV1QeJPr+z8SaNWsyaNCgDBo0KLfeems6d+6cJUuWZNCgQZXP02mnnZZXX301v/zlLzN79uwMGDAgY8aMydVXX73FTE1NTTnvvPNy4YUXbrCva9eum3zf1nx2t6Rt27Zp27btX3weAAAAAD6+lNwb8atf/SoLFizIRRddlOTdMnLp0qVZunRpZZbp888/n7feeiuHHnroRs/x+OOP5wc/+EFl9vXSpUvz5ptvbnOWFStW5O67787MmTNz2GGHVba3tLTkM5/5TB588MGceuqp23zeJOnTp09aWlryxhtv5Pjjj/9A50iSgw46KO3atctDDz2Uc845Z4P9TzzxRLp165Z/+qd/qmx79dVXt+ka7z3M8PHHH0+3bt2SvLtO9dy5czN27Ngk7/5Gao899sgRRxyx2XN985vfzMknn5zRo0envr4+9fX1+d3vfpcRI0Zs9PjtkX9Tamtrs27duqxdu7ZScr/fb3/726xYsSJTpkypfP7mzZu3wXGdO3dOQ0NDGhoacvzxx+fSSy/dqpK7b9++ef755yvl+wfVq1evPP7442loaKhse/zxxzd5jwAAAADA9vCxL7mbm5uzbNmytLS05PXXX8/999+fb3/72/nc5z6XkSNHJkkGDhyYww8/PCNGjMi1116bdevW5Wtf+1pOPPHETS43ctBBB+WnP/1pjj766KxevTqXXnrpFmc8b8xPf/rT7LXXXjnzzDM3mE09ePDgTJ8+/QOX3AcffHBGjBiRkSNH5pprrkmfPn2yfPnyPPTQQ+ndu3eGDBmyVefZZZddcvnll+eyyy5LXV1djjvuuCxfvjzPPfdcRo0alYMOOihLlizJzJkzc8wxx+Q//uM/cuedd25T1vbt22f06NG59NJLs+eee6Zr1675zne+kz/+8Y8ZNWpUkuSee+7Z5AMn/1z//v3Tu3fvXHnllZk2bVomTZqUCy+8MJ06dcqpp56a5ubmzJs3LytXrszFF1+8XfK/Z8WKFVm2bFnWrVuXBQsWZOrUqfnsZz+72aVPunbtmrq6unzve9/L3//932fhwoWtlqlJkgkTJuSoo47KYYcdlubm5tx7772bXGbk/S6//PL89V//dc4///ycc845ad++fZ5//vnMnj0706ZN2+qv7dJLL82ZZ56ZPn36ZODAgfnFL36RO+64I//5n/+51ecAAAAAgG3VptoBqu3+++/Pfvvtl+7du+fUU0/Nww8/nOuuuy533313ZbmKmpqa3H333dljjz1ywgknZODAgTnwwAMza9asTZ53+vTpWblyZfr27ZuzzjorF154YfbZZ59tznfTTTfli1/84kaXCxk6dGjuueeeDzRD/D0zZszIyJEjc8kll6Rnz54544wzMnfu3M0uU7Ex48ePzyWXXJIJEyakV69eGTZsWGU97c9//vO56KKLcv755+fII4/ME088kfHjx29z1ilTpmTo0KE566yz0rdv37z00kt54IEHssceeyTZ+pI7SS666KLceOONWbp0ac4555zceOONmTFjRg4//PCceOKJufnmmyvL1Wyv/Mm7vzB57/P21a9+NYMHD97s5yh5d4b2zTffnH/7t3/LoYcemilTpmwwQ7uuri7jxo1L7969c8IJJ6S2tnaLazG9p3fv3pkzZ05efPHFHH/88enTp08mTJiQ+vr6bfrazjjjjEydOjVXX311DjvssNxwww2ZMWNGTjrppG06DwAAAABsi5qiKIpqh4C/1NNPP52TTz45y5cv32Btb8pj9erV//8DP1cl2fYHewIAAAB83HxU2933eqJVq1ZtdhWExExuPiLWrVuX733vewpuAAAAAPiYMZMb2GGYyQ0AAACwbT6q7a6Z3AAAAAAAfCwouQEAAAAAKC0lNwAAAAAApaXkBgAAAACgtJTcAAAAAACUlpIbAAAAAIDSUnIDAAAAAFBaSm4AAAAAAEpLyQ0AAAAAQGkpuQEAAAAAKC0lNwAAAAAApaXkBgAAAACgtJTcAAAAAACUlpIbAAAAAIDSUnIDAAAAAFBaSm4AAAAAAEpLyQ0AAAAAQGkpuQEAAAAAKC0lNwAAAAAApaXkBgAAAACgtJTcAAAAAACUlpIbAAAAAIDSUnIDAAAAAFBaSm4AAAAAAEpLyQ0AAAAAQGkpuQEAAAAAKC0lNwAAAAAApaXkBgAA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2dlll12qHQdK77TTTqv8d+/evdOvX79069Ytt99+u2W1dnBKbqCq9t5779TW1ub1119vtf3111/PJz7xiSqlAoDWzj///Nx777159NFHs//++1c7DpRaXV1devTokSQ56qijMnfu3EydOjU33HBDlZNB+cyfPz9vvPFG+vbtW9nW0tKSRx99NNOmTUtzc3Nqa2urmBDKbffdd8/BBx+cl156qdpR2AJrcgNVVVdXl6OOOioPPfRQZdv69evz0EMPWZsRgKoriiLnn39+7rzzzvzqV7/KAQccUO1I8JGzfv36NDc3VzsGlNKAAQOyYMGCNDY2VsbRRx+dESNGpLGxUcENf6GmpqYsXrw4++23X7WjsAVmcgNVd/HFF6ehoSFHH310jj322Fx77bVZs2ZNzj777GpHg1JqampqNdPg5ZdfTmNjY/bcc8907dq1ismgfMaMGZPbbrstd999dzp06JBly5YlSTp16pR27dpVOR2Uz7hx43Laaaela9euefvtt3PbbbflkUceyQMPPFDtaFBKHTp02OA5Ee3bt89ee+3l+RHwAXzjG9/I6aefnm7duuX3v/99Jk6cmNra2gwfPrza0dgCJTdQdcOGDcvy5cszYcKELFu2LEceeWTuv//+DR5GCWydefPm5bOf/Wzl9cUXX5wkaWhoyM0331ylVFBO119/fZLkpJNOarV9xowZ+bu/+7v/94Gg5N54442MHDkyr732Wjp16pTevXvngQceyN/8zd9UOxoA5H/+538yfPjwrFixIp07d85nPvOZ/OY3v0nnzp2rHY0tqCmKoqh2CAAAAAAA+CCsyQ0AAAAAQGkpuQEAAAAAKC0lNwAAAAAApaXkBgAAAACgtJTcAAAAAACUlpIbAAAAAIDSUnIDAAAAAFBaSm4AAAAAAEpLyQ0AAPAheeWVV1JTU5PGxsYP/VonnXRSxo4d+6FfBwBgR6PkBgAA2IInn3wytbW1GTJkyId+rSuuuCI1NTWpqanJTjvtlO7du+eiiy5KU1PTZt93xx13ZPLkyR96PgCAHY2SGwAAYAumT5+eCy64II8++mh+//vff+jXO+yww/Laa6/llVdeyVVXXZUf/vCHueSSSzZ67Nq1a5Mke+65Zzp06PChZwMA2NEouQEAADajqakps2bNyujRozNkyJDcfPPNrfavXLkyI0aMSOfOndOuXbscdNBBmTFjxkbP1dLSkq985Ss55JBDsmTJkk1ec6eddsonPvGJ7L///hk2bFhGjBiRe+65J8m7M72PPPLI3HjjjTnggAOyyy67JNlwuZLm5uZcfvnl6dKlS9q2bZsePXpk+vTplf0LFy7Maaedlt122y377rtvzjrrrLz55psf8LsEAFA9Sm4AAIDNuP3223PIIYekZ8+e+fKXv5ybbropRVFU9o8fPz7PP/987rvvvixatCjXX3999t577w3O09zcnC996UtpbGzMr3/963Tt2nWrM7Rr164yYztJXnrppfz85z/PHXfcscn1vkeOHJmf/exnue6667Jo0aLccMMN2W233ZIkb731Vk4++eT06dMn8+bNy/3335/XX389Z5555lZnAgDYUexU7QAAAAA7sunTp+fLX/5ykuTUU0/NqlWrMmfOnJx00klJkiVLlqRPnz45+uijkyTdu3ff4BxNTU0ZMmRImpub8/DDD6dTp05bff358+fntttuy8knn1zZtnbt2vzkJz9J586dN/qeF198Mbfffntmz56dgQMHJkkOPPDAyv5p06alT58+ufLKKyvbbrrppnTp0iUvvvhiDj744K3OBwBQbWZyAwAAbMILL7yQp556KsOHD0/y7jIiw4YNa7Xsx+jRozNz5swceeSRueyyy/LEE09scJ7hw4dnzZo1efDBB7eq4F6wYEF22223tGvXLscee2z69++fadOmVfZ369ZtkwV3kjQ2Nqa2tjYnnnjiRvc/88wzefjhh7PbbrtVxiGHHJIkWbx48RbzAQDsSMzkBgAA2ITp06dn3bp1qa+vr2wriiJt27bNtGnT0qlTp5x22ml59dVX88tf/jKzZ8/OgAEDMmbMmFx99dWV9wwePDi33HJLnnzyyVYzsjelZ8+eueeee7LTTjulvr4+dXV1rfa3b99+s+9v167dZvc3NTXl9NNPz1VXXbXBvv3222+L+QAAdiRmcgMAAGzEunXr8pOf/CTXXHNNGhsbK+OZZ55JfX19fvazn1WO7dy5cxoaGnLLLbfk2muvzQ9/+MNW5xo9enSmTJmSz3/+85kzZ84Wr11XV5cePXqke/fuGxTcW+Pwww/P+vXrN3mtvn375rnnnkv37t3To0ePVmNLBToAwI5GyQ0AALAR9957b1auXJlRo0blU5/6VKsxdOjQypIlEyZMyN13352XXnopzz33XO6999706tVrg/NdcMEF+da3vpXPfe5zeeyxxz7U7N27d09DQ0O+8pWv5K677srLL7+cRx55JLfffnuSZMyYMfnDH/6Q4cOHZ+7cuVm8eHEeeOCBnH322WlpaflQswEAbG9KbgAAgI2YPn16Bg4cuNE1tIcOHZp58+bl2WefTV1dXcaNG5fevXvnhBNOSG1tbWbOnLnRc44dOzaTJk3K4MGDN7p29/Z0/fXX52//9m/zta99LYccckjOPffcrFmzJklSX1+fxx9/PC0tLTnllFNy+OGHZ+zYsdl9993Tpo2/JgIA5VJTFEVR7RAAAAAAAPBB+BU9AAAAAAClpeQGAAAAAKC0lNwAAAAAAJSWkhsAAAAAgNJScgMAAAAAUFpKbgAAAAAASkvJDQAAAABAaSm5AQAAAAAoLSU3AAAAAAClpeQGAAAAAKC0lNwAAAAAAJTW/wfPRDIY5cbbSAAAAABJRU5ErkJggg==)
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
4.4 Average Ask By Day
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[11\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    import matplotlib.pyplot as plt

    ## Query to get the average ASK and BID by day
    query = """
        SELECT 
            create_date DT_REF
            ,round(avg(ask),2) AvgAsk
            ,round(avg(bid),2) Avgbid
        FROM df 
        where not code in ('BTC', 'ETH', 'LTC', 'DOGE')
        group by 1
        order by 1 
    """

    newDf = sqldf(query, locals())
    newDf.sort_values(by='DT_REF', ascending=True, inplace=True)

    cht = newDf.plot(
        kind='line', x='DT_REF', y='AvgAsk',
        figsize=(15, 10), 
        legend=False, 
        color='blue', title='Average ASK tendence by Day', xlabel='Date', ylabel='AvgAsk')

    #exibir o grafico
    plt.show()
:::
:::
:::
:::
:::

::: {.jp-Cell-outputWrapper}
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::: {.jp-OutputArea .jp-Cell-outputArea}
::: {.jp-OutputArea-child}
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedImage .jp-OutputArea-output tabindex="0"}
![No description has been provided for this
image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABOcAAANXCAYAAAB+DztKAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAC++klEQVR4nOzdd5xcdbk/8Gc3lZaEliYxhA4SqtcYkCZIKIJRrvSiRLEEpV1AFDXAvaIgTaWIIigGKQq5iAiEIoiJAoHQBBQMcIEEVCALAdL2/P6Y39mdybaZ3dnsnDPv9+u1r505c2bmO0v0zPmc5/l+G5IkSQIAAAAAWOka+3oAAAAAAFCvhHMAAAAA0EeEcwAAAADQR4RzAAAAANBHhHMAAAAA0EeEcwAAAADQR4RzAAAAANBHhHMAAAAA0EeEcwAAAADQR4RzAADUtF133TV23XXXvh5Gj62//vrx8Y9/vK+HAQDUGOEcALDSXHLJJdHQ0BATJkzo66HUrOXLl8fo0aOjoaEhfv/733e43/333x977713vO9974vBgwfH+9///thvv/3immuuKdmvoaEhjj322DbP/853vhMNDQ1x9NFHR3Nzc4fv853vfCdmzJjR7c/DyvX8889HQ0NDy8+AAQNinXXWiR122CG+/vWvx4svvtjXQwQAViCcAwBWmunTp8f6668fDzzwQDz77LN9PZyadPfdd8f8+fNj/fXXj+nTp7e7zw033BA777xzvPrqq3HcccfFD3/4wzj88MPjjTfeiJ/85Cddvsd3v/vd+MY3vhFHHXVU/PSnP43Gxo6/EgrnsumQQw6Jq6++Oq644or45je/GRtssEFceOGFsfnmm8e1117b18MDAIr07+sBAAD1Yd68eTFr1qy48cYb4wtf+EJMnz49vv3tb6/UMTQ3N8eSJUti8ODBK/V9K/HLX/4ytttuuzjqqKPi61//eixatChWW221kn2mTZsWW2yxRfz5z3+OgQMHljz22muvdfr65557bpx22mlx5JFHxs9+9rNOgzmya7vttovDDz+8ZNsLL7wQe+65Zxx11FGx+eabx9Zbb91HowMAivk2BgCsFNOnT48111wz9t133/jP//zPkqqwpUuXxlprrRWf/exn2zyvqakpBg8eHP/1X//Vsm3x4sXx7W9/OzbaaKMYNGhQjBkzJk455ZRYvHhxyXPTls7p06fHBz7wgRg0aFDcdtttERHx/e9/P3bYYYdYe+21Y5VVVontt98+fv3rX7d5/3fffTe++tWvxjrrrBNrrLFG7L///vHyyy9HQ0NDTJs2rWTfl19+OY4++ugYMWJEDBo0KD7wgQ/Ez372s7L/Ru+++27cdNNNcfDBB8eBBx4Y7777bvzv//5vm/2ee+65+I//+I82wVxExPDhwzt8/fPPPz9OOeWUOPzww+PKK6/sMphraGiIRYsWxc9//vOWNsnPfOYzFX3eP/zhD9HQ0BDXX399/M///E+st956MXjw4Nh9993brZ68/PLLY8MNN4xVVlklPvShD8Uf//jHdsdW6b+BGTNmxJZbbtkyzvTfQbGXX345pkyZEqNHj45BgwbFuHHj4ktf+lIsWbKkZZ8333wzjj/++BgzZkwMGjQoNtpoo/je977XaWvwiu64447YZpttYvDgwbHFFlvEjTfe2PLYP/7xj2hoaIgLLrigzfNmzZoVDQ0N8atf/ars9yo2duzYuOqqq2LJkiVxzjnntGx//fXX47/+679i/Pjxsfrqq8eQIUNi7733jkcffbRln7fffjtWW221OO6449q87ksvvRT9+vWLs88+u1vjAoC6lwAArASbbbZZMmXKlCRJkuS+++5LIiJ54IEHWh4/+uijk2HDhiWLFy8ued7Pf/7zJCKSBx98MEmSJFm+fHmy5557Jquuumpy/PHHJz/+8Y+TY489Nunfv3/yiU98ouS5EZFsvvnmybrrrpucccYZycUXX5w88sgjSZIkyXrrrZd8+ctfTn70ox8l559/fvKhD30oiYjklltuKXmNAw88MImI5Igjjkguvvji5MADD0y23nrrJCKSb3/72y37LViwIFlvvfWSMWPGJGeeeWZy6aWXJvvvv38SEckFF1xQ1t/o2muvTRoaGpIXX3wxSZIk+ehHP5rss88+bfbbZJNNkjFjxiT/93//1+VrRkQyderU5MILL0wiIjn00EOTZcuWlTWeq6++Ohk0aFCy0047JVdffXVy9dVXJ7Nmzaro895zzz1JRCTbbrttsv322ycXXHBBMm3atGTVVVdNPvShD5W8309/+tMkIpIddtgh+cEPfpAcf/zxybBhw5INNtgg2WWXXVr2q/TfwNZbb52MGjUqOeuss5ILL7ww2WCDDZJVV101+de//tWy38svv5yMHj265TUvu+yy5Jvf/Gay+eabJ2+88UaSJEmyaNGiZKuttkrWXnvt5Otf/3py2WWXJUceeWTS0NCQHHfccV3+PceOHZtssskmybBhw5Kvfe1ryfnnn5+MHz8+aWxsTO64446W/Xbcccdk++23b/P8L3/5y8kaa6yRLFq0qMP3mDdvXhIRybnnntvhPhtuuGGy7rrrttx/8MEHkw033DD52te+lvz4xz9OzjzzzOR973tfMnTo0OTll19u2e+www5LRowY0ebfzznnnJM0NDQkL7zwQpd/AwCgLeEcANDrHnrooSQikpkzZyZJkiTNzc3JeuutVxJo3H777UlEJL/97W9LnrvPPvskG2ywQcv9q6++OmlsbEz++Mc/lux32WWXJRGR/OlPf2rZFhFJY2Nj8uSTT7YZ0zvvvFNyf8mSJcmWW26ZfPSjH23ZNmfOnCQikuOPP75k38985jNtwrkpU6Yko0aNKgl8kiRJDj744GTo0KFt3q89H//4x5Mdd9yx5f7ll1+e9O/fP3nttddK9rviiiuSiEgGDhyY7Lbbbsk3v/nN5I9//GOyfPnyNq8ZEcnYsWOTiEgOOeSQsoO51GqrrZYcddRRbbaX+3nTcG7zzTcvCV4vuuiiJCKSxx9/PEmSwt9/+PDhyTbbbFOy3+WXX55EREk4V+m/gYEDBybPPvtsy7ZHH300iYjkhz/8Ycu2I488MmlsbGwJgYs1NzcnSZIkZ511VrLaaqslf/vb30oe/9rXvpb069evJVTtSPrf4Te/+U3LtoULFyajRo1Ktt1225ZtP/7xj5OISJ566qmWbUuWLEnWWWeddv9bFCsnnPvEJz6RRESycOHCJEmS5L333mvzb2fevHnJoEGDkjPPPLNlW/q/0d///vcl+2611VYl/30AgMpoawUAet306dNjxIgRsdtuu0VEodXwoIMOimuvvTaWL18eEREf/ehHY5111onrrruu5XlvvPFGzJw5Mw466KCWbTfccENsvvnmsdlmm8W//vWvlp+PfvSjERFxzz33lLz3LrvsEltssUWbMa2yyiol77Nw4cLYaaed4uGHH27ZnrY+fvnLXy557le+8pWS+0mSxG9+85vYb7/9IkmSknFNmjQpFi5cWPK67fn3v/8dt99+exxyyCEt2w444ICWltBiRx99dNx2222x6667xv333x9nnXVW7LTTTrHxxhvHrFmz2rz2q6++GhER48aNi379+nU6jnJ05/N+9rOfLWnD3WmnnSKi0MYZEfHQQw/Fa6+9Fl/84hdL9vvMZz4TQ4cOLXmtSv8N7LHHHrHhhhu23N9qq61iyJAhLe/d3NwcM2bMiP322y8++MEPtvm8DQ0NLe+70047xZprrlnyvnvssUcsX7487rvvvi7/dqNHj45PfvKTLfeHDBkSRx55ZDzyyCOxYMGCiIg48MADY/DgwSWt37fffnv861//ajOPXHesvvrqERHx1ltvRUTEoEGDWlqcly9fHv/+979j9dVXj0033bTkv+Mee+wRo0ePLhnXE088EY899lhVxgUA9cqCEABAr1q+fHlce+21sdtuu8W8efNatk+YMCHOO++8uOuuu2LPPfeM/v37xwEHHBDXXHNNLF68OAYNGhQ33nhjLF26tCSc+/vf/x5PPfVUrLvuuu2+34oLIowbN67d/W655Zb47//+75g7d27JPGVpEBNRmEC/sbGxzWtstNFGJff/+c9/xptvvhmXX355XH755WWNa0XXXXddLF26NLbddtuSudgmTJgQ06dPj6lTp5bsP2nSpJg0aVK88847MWfOnLjuuuvisssui49//OPx9NNPl8w9d9RRR8Urr7wS3/nOd2KdddaJE044odOxdKU7n/f9739/yf0111wzIgrBaEThbx0RsfHGG5fsN2DAgNhggw1KtlX6b2DF907fP33vf/7zn9HU1BRbbrllu69X/L6PPfZY2e/bno022qjk31hExCabbBIREc8//3yMHDkyhg0bFvvtt19cc801cdZZZ0VEIeB+3/ve1xJA9sTbb78dERFrrLFGRBTCyYsuuiguueSSmDdvXktgHhGx9tprt9xubGyMww47LC699NJ45513YtVVV43p06fH4MGD49Of/nSPxwUA9Uo4BwD0qrvvvjvmz58f1157bVx77bVtHp8+fXrsueeeERFx8MEHx49//OP4/e9/H5MnT47rr78+Nttss5JVJZubm2P8+PFx/vnnt/t+Y8aMKblfXCGX+uMf/xj7779/7LzzznHJJZfEqFGjYsCAAXHllVfGNddcU/FnTBcDOPzww+Ooo45qd5+tttqq09dIq5F23HHHdh//xz/+0SakiohYddVVY6eddoqddtop1llnnTjjjDPi97//fck4+vfvH9dff33stddecdJJJ8WwYcPaXXyjXN35vB1V7CVJ0q33r+TfQLXeu7m5OT72sY/FKaec0u7jachWDUceeWTccMMNMWvWrBg/fnzcfPPN8eUvf7kqq+s+8cQTMXz48BgyZEhERHznO9+Jb37zm3H00UfHWWedFWuttVY0NjbG8ccf32ahiyOPPDLOPffcmDFjRhxyyCFxzTXXxMc//vE21Y0AQPmEcwBAr5o+fXoMHz48Lr744jaP3XjjjXHTTTfFZZddFqusskrsvPPOMWrUqLjuuuviIx/5SNx9993xjW98o+Q5G264YTz66KOx++67t6lAKtdvfvObGDx4cNx+++0xaNCglu1XXnllyX5jx46N5ubmmDdvXklF14qrjK677rqxxhprxPLly2OPPfaoeDzz5s2LWbNmxbHHHhu77LJLyWPNzc1xxBFHxDXXXBOnn356p6+TtmTOnz+/zWODBw+Om2++OXbbbbf4/Oc/H8OGDStpr+xIe3/jnn7e9owdOzYiCtVpxdVhS5cujXnz5pUEtNX4N1Bs3XXXjSFDhsQTTzzR6X4bbrhhvP322z36zM8++2wkSVIy7r/97W8REbH++uu3bNtrr71i3XXXjenTp8eECRPinXfeiSOOOKLb75uaPXt2PPfccyVtqL/+9a9jt912iyuuuKJk3zfffDPWWWedkm1bbrllbLvttjF9+vRYb7314sUXX4wf/vCHPR4XANQzc84BAL3m3XffjRtvvDE+/vGPx3/+53+2+Tn22GPjrbfeiptvvjkiCm1z//mf/xm//e1v4+qrr45ly5aVtLRGFObjevnll+MnP/lJu++3aNGiLsfVr1+/aGhoKGnfe/7552PGjBkl+02aNCkiIi655JKS7SuGEf369YsDDjggfvOb37Qb8Pzzn//sdDxp1dwpp5zS5m904IEHxi677FIyz9ddd93V7uvceuutERGx6aabtvv4kCFD4rbbbouNNtooDjnkkA5fp9hqq60Wb775Zsm2nn7e9nzwgx+MddddNy677LJYsmRJy/arrrqqzftX499AscbGxpg8eXL89re/jYceeqjN42mF3YEHHhizZ8+O22+/vc0+b775ZixbtqzL93rllVfipptuarnf1NQUv/jFL2KbbbaJkSNHtmzv379/HHLIIXH99dfHVVddFePHj++y+rIrL7zwQnzmM5+JgQMHxsknn9yyvV+/fm2qCG+44YZ4+eWX232dI444Iu6444648MILY+2114699967R+MCgHqncg4A6DU333xzvPXWW7H//vu3+/iHP/zhluqgNIQ76KCD4oc//GF8+9vfjvHjx8fmm29e8pwjjjgirr/++vjiF78Y99xzT+y4446xfPnyePrpp+P666+P22+/vd1J/Yvtu+++cf7558dee+0Vhx56aLz22mtx8cUXx0YbbRSPPfZYy37bb799HHDAAXHhhRfGv//97/jwhz8c9957b0ulU3H103e/+9245557YsKECfH5z38+tthii3j99dfj4YcfjjvvvDNef/31Dsczffr02Gabbdq0Y6b233//+MpXvhIPP/xwbLfddvGJT3wixo0bF/vtt19suOGGsWjRorjzzjvjt7/9bfzHf/xH7Lfffh2+17rrrhszZ86MHXfcMSZPnhx33XVXfOhDH+pw/+233z7uvPPOOP/882P06NExbty4mDBhQo8+b3sGDBgQ//3f/x1f+MIX4qMf/WgcdNBBMW/evLjyyivbtPNW49/Air7zne/EHXfcEbvsskscc8wxsfnmm8f8+fPjhhtuiPvvvz+GDRsWJ598ctx8883x8Y9/PD7zmc/E9ttvH4sWLYrHH388fv3rX8fzzz/fptJsRZtssklMmTIlHnzwwRgxYkT87Gc/i1dffbVN1WZEoYX0Bz/4Qdxzzz3xve99r6LP8/DDD8cvf/nLaG5ujjfffDMefPDB+M1vfhMNDQ1x9dVXlwR9H//4x+PMM8+Mz372s7HDDjvE448/HtOnT2+3jToi4tBDD41TTjklbrrppvjSl74UAwYMqGhsAMAK+mydWAAg9/bbb79k8ODByaJFizrc5zOf+UwyYMCA5F//+leSJEnS3NycjBkzJomI5L//+7/bfc6SJUuS733ve8kHPvCBZNCgQcmaa66ZbL/99skZZ5yRLFy4sGW/iEimTp3a7mtcccUVycYbb5wMGjQo2WyzzZIrr7wy+fa3v52s+PVo0aJFydSpU5O11lorWX311ZPJkycnzzzzTBIRyXe/+92SfV999dVk6tSpyZgxY5IBAwYkI0eOTHbffffk8ssv7/Dzz5kzJ4mI5Jvf/GaH+zz//PNJRCQnnHBCkiRJ8qtf/So5+OCDkw033DBZZZVVksGDBydbbLFF8o1vfCNpamoqeW5H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0sfbc/bZZ8fQoUNbfsaMGdOzDwsAZSoO4rS1AgBAtvVpW2tXDj744Jbb48ePj6222io23HDD+MMf/hC77757H44s4rTTTosTTzyx5X5TU5OADoCVojiI09YKAADZVtOVcyvaYIMNYp111olnn302IiJGjhwZr732Wsk+y5Yti9dff71lnrqRI0fGq6++WrJPer+rfTqa6y6iMBfekCFDSn4AYGUorpzT1goAANmWqXDupZdein//+98xatSoiIiYOHFivPnmmzFnzpyWfe6+++5obm6OCRMmtOxz3333xdKlS1v2mTlzZmy66aax5pprtuxz1113lbzXzJkzY+LEib39kQCgYsVVctpaAQAg2/o0nHv77bdj7ty5MXfu3IiImDdvXsydOzdefPHFePvtt+Pkk0+OP//5z/H888/HXXfdFZ/4xCdio402ikmTJkVExOabbx577bVXfP7zn48HHngg/vSnP8Wxxx4bBx98cIwePToiIg499NAYOHBgTJkyJZ588sm47rrr4qKLLippST3uuOPitttui/POOy+efvrpmDZtWjz00ENx7LHHrvS/CQB0RTgHAAD50afh3EMPPRTbbrttbLvtthERceKJJ8a2224b3/rWt6Jfv37x2GOPxf777x+bbLJJTJkyJbbffvv44x//GIPSHp6ImD59emy22Wax++67xz777BMf+chH4vLLL295fOjQoXHHHXfEvHnzYvvtt4+TTjopvvWtb8UxxxzTss8OO+wQ11xzTVx++eWx9dZbx69//euYMWNGbLnllivvjwEAZSpuYR0woO02AAAgOxqSJEn6ehB50NTUFEOHDo2FCxeafw6AXvXyyxHrrRfRv3/EdddFHHBAxEc+EvHHP/b1yAAAgFS5WVGm5pwDAFpbWPv3L/wUbwMAALJFOAcAGZO2sPbrV/gp3gYAAGSLcA4AMkblHAAA5IdwDgAyRjgHAAD5IZwDgIzR1goAAPkhnAOAjFE5BwAA+SGcA4CMEc4BAEB+COcAIGO0tQIAQH4I5wAgY1TOAQBAfgjnACBjhHMAAJAfwjkAyBhtrQAAkB/COQDIGJVzAACQH8I5AMgY4RwAAOSHcA4AMqa9tlbhHAAAZJNwDgAypr3KOXPOAQBANgnnACBjtLUCAEB+COcAIGPaa2tNkojm5r4bEwAA0D3COQDImPYq5yK0tgIAQBYJ5wAgYzoK57S2AgBA9gjnACBjhHMAAJAfwjkAyJj25pwr3g4AAGSHcA4AMqa4cq44nFM5BwAA2SOcA4CMKQ7nGhsLP8XbAQCA7BDOAUDGFLe1Fv/W1goAANkjnAOAjCmunCv+rXIOAACyRzgHABkjnAMAgPwQzgFAxmhrBQCA/BDOAUDGqJwDAID8EM4BQMYI5wAAID+EcwCQMdpaAQAgP4RzAJAxKucAACA/hHMAkDHCOQAAyA/hHABkjLZWAADID+EcAGSMyjkAAMgP4RwAZIxwDgAA8kM4BwAZ01Fbq3AOAACyRzgHABnTUeWcOecAACB7hHMAkDHaWgEAID+EcwCQMdpaAQAgP4RzAJAx2loBACA/hHMAkDHaWgEAID+EcwCQMdpaAQAgP4RzAJAx2loBACA/hHMAkDHaWgEAID+EcwCQMcI5AADID+EcAGRMR3POaWsFAIDsEc4BQMaonAMAgPwQzgFAxgjnAAAgP4RzAJAx2loBACA/hHMAkDEq5wAAID+EcwCQMcI5AADID+EcAGSMtlYAAMgP4RwAZIzKOQAAyA/hHABkjHAOAADyQzgHABmjrRUAAPJDOAcAGaNyDgAA8kM4BwAZI5wDAID8EM4BQMZoawUAgPwQzgFAxqicAwCA/BDOAUDGCOcAACA/hHMAkDEdtbUK5wAAIHuEcwCQIUnSceWcOecAACB7hHMAkCHNza23tbUCAED2CecAIEOKq+O0tQIAQPYJ5wAgQ4oDOG2tAACQfcI5AMiQzsI5lXMAAJA9wjkAyBDhHAAA5ItwDgAypLM557S1AgBA9gjnACBD0uq4xsaIhobCbZVzAACQXcI5AMiQNIBLA7ni28I5AADIHuEcAGRI2rqatrIW39bWCgAA2SOcA4AMUTkHAAD5IpwDgAwRzgEAQL4I5wAgQ7S1AgBAvgjnACBDVM4BAEC+COcAIEOEcwAAkC/COQDIEG2tAACQL8I5AMgQlXMAAJAvwjkAyBDhHAAA5ItwDgAyRFsrAADki3AOADJE5RwAAOSLcA4AMkQ4BwAA+SKcA4AM6aytVTgHAADZI5wDgAzprHLOnHMAAJA9wjkAyBBtrQAAkC/COQDIkK5Wa02SlT8mAACg+4RzAJAhnVXORUQ0N6/c8QAAAD0jnAOADOkqnNPaCgAA2SKcA4AMaa+tVTgHAADZJZwDgAxpr3KuOKizYisAAGRLn4Zz9913X+y3334xevToaGhoiBkzZrQ8tnTp0jj11FNj/Pjxsdpqq8Xo0aPjyCOPjFdeeaXkNdZff/1oaGgo+fnud79bss9jjz0WO+20UwwePDjGjBkT55xzTpux3HDDDbHZZpvF4MGDY/z48XHrrbf2ymcGgJ7Q1goAAPnSp+HcokWLYuutt46LL764zWPvvPNOPPzww/HNb34zHn744bjxxhvjmWeeif3337/NvmeeeWbMnz+/5ecrX/lKy2NNTU2x5557xtixY2POnDlx7rnnxrRp0+Lyyy9v2WfWrFlxyCGHxJQpU+KRRx6JyZMnx+TJk+OJJ57onQ8OAN3UXjjX2Nj2cQAAIBv6d71L79l7771j7733bvexoUOHxsyZM0u2/ehHP4oPfehD8eKLL8b73//+lu1rrLFGjBw5st3XmT59eixZsiR+9rOfxcCBA+MDH/hAzJ07N84///w45phjIiLioosuir322itOPvnkiIg466yzYubMmfGjH/0oLrvssmp8VACoivbmnGtoKNxfvlxbKwAAZE2m5pxbuHBhNDQ0xLBhw0q2f/e734211147tt122zj33HNjWVHZwOzZs2PnnXeOgQMHtmybNGlSPPPMM/HGG2+07LPHHnuUvOakSZNi9uzZHY5l8eLF0dTUVPIDAL2tvcq54vsq5wAAIFv6tHKuEu+9916ceuqpccghh8SQIUNatn/1q1+N7bbbLtZaa62YNWtWnHbaaTF//vw4//zzIyJiwYIFMW7cuJLXGjFiRMtja665ZixYsKBlW/E+CxYs6HA8Z599dpxxxhnV+ngAUJbOwrnFi4VzAACQNZkI55YuXRoHHnhgJEkSl156acljJ554YsvtrbbaKgYOHBhf+MIX4uyzz45Bgwb12phOO+20kvduamqKMWPG9Nr7AUBE+22txfe1tQIAQLbUfDiXBnMvvPBC3H333SVVc+2ZMGFCLFu2LJ5//vnYdNNNY+TIkfHqq6+W7JPeT+ep62ifjuaxi4gYNGhQr4Z/ANAeba0AAJAvNT3nXBrM/f3vf48777wz1l577S6fM3fu3GhsbIzhw4dHRMTEiRPjvvvui6VLl7bsM3PmzNh0001jzTXXbNnnrrvuKnmdmTNnxsSJE6v4aQCg54RzAACQL31aOff222/Hs88+23J/3rx5MXfu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zY0ePTpOOumk+K//+q+IiFi4cGGMGDEirrrqqjj44IPjqaeeii222CIefPDB+OAHPxgREbfddlvss88+8dJLL8Xo0aPj0ksvjW984xuxYMGCGDhwYEREfO1rX4sZM2bE008/HRERBx10UCxatChuueWWlvF8+MMfjm222SYuu+yyssbf1NQUQ4cOjYULF8aQIUOq9WcBgBYjRkS89lrEY49FjB/f9vHTT4/4n/+J+OpXIy66aOWPDwAAaFVuVlSzc87NmzcvFixYEHvssUfLtqFDh8aECRNi9uzZERExe/bsGDZsWEswFxGxxx57RGNjY/zlL39p2WfnnXduCeYiIiZNmhTPPPNMvPHGGy37FL9Puk/6Pu1ZvHhxNDU1lfwAQG8qt61V5RwAAGRHzYZzCxYsiIiIESNGlGwfMWJEy2MLFiyI4cOHlzzev3//WGuttUr2ae81it+jo33Sx9tz9tlnx9ChQ1t+xowZU+lHBICKlNvWas45AADIjpoN52rdaaedFgsXLmz5+b//+7++HhIAOWfOOQAAyJ+aDedGjhwZERGvvvpqyfZXX3215bGRI0fGa6+9VvL4smXL4vXXXy/Zp73XKH6PjvZJH2/PoEGDYsiQISU/ANCbtLUCAED+1Gw4N27cuBg5cmTcddddLduampriL3/5S0ycODEiIiZOnBhvvvlmzJkzp2Wfu+++O5qbm2PChAkt+9x3332xdOnSln1mzpwZm266aay55pot+xS/T7pP+j4AUAu0tQIAQP70aTj39ttvx9y5c2Pu3LkRUVgEYu7cufHiiy9GQ0NDHH/88fHf//3fcfPNN8fjjz8eRx55ZIwePbplRdfNN9889tprr/j85z8fDzzwQPzpT3+KY489Ng4++OAYPXp0REQceuihMXDgwJgyZUo8+eSTcd1118VFF10UJ554Yss4jjvuuLjtttvivPPOi6effjqmTZsWDz30UBx77LEr+08CAB3S1goAAPnTwdf7leOhhx6K3XbbreV+GpgdddRRcdVVV8Upp5wSixYtimOOOSbefPPN+MhHPhK33XZbDB48uOU506dPj2OPPTZ23333aGxsjAMOOCB+8IMftDw+dOjQuOOOO2Lq1Kmx/fbbxzrrrBPf+ta34phjjmnZZ4cddohrrrkmTj/99Pj6178eG2+8ccyYMSO23HLLlfBXAICuNTe33tbWCgAA+dGQJEnS14PIg6amphg6dGgsXLjQ/HMAVN2SJRGDBhVuv/FGxLBhbff58Y8jvvjFiE9+MuLGG1fq8AAAgBWUmxXV7JxzAECr4mo4ba0AAJAfwjkAyIDiRR46amsVzgEAQPYI5wAgA8qpnEtDO6u1AgBAdgjnACADisM5lXMAAJAfwjkAyIC0Gq6xsfDTHuEcAABkj3AOADIgDdw6qporfkxbKwAAZIdwDgAyIA3nOppvrvgxlXMAAJAdwjkAyADhHAAA5JNwDgAyIG1V1dYKAAD5IpwDgAxQOQcAAPkknAOADBDOAQBAPgnnACADtLUCAEA+CecAIANUzgEAQD4J5wAgA4RzAACQT8I5AMgAba0AAJBPwjkAyACVcwAAkE/COQDIAOEcAADkk3AOADKgkrZW4RwAAGSHcA4AMqCSyjlzzgEAQHYI5wAgA7S1AgBAPgnnACADtLUCAEA+CecAIAMqbWtNkt4fEwAA0HPCOaBmPfBAxB//2NejgNpQSTgXEdHc3LvjAQAAqqOTr/gAfae5OWLPPSPeey/i3/+OWG21vh4R9K1K2lojCmFeZ/sCAAC1QeUcUJPeey9i4cKIxYsLv6HeVVo5Z8VWAADIBuEcUJMWL27/NtSrSsM5i0IAAEA2COeAmlQcyL33Xt+NA2pFWgknnAMAgHypOJxramrq8LFnn322R4MBSBUHcirnoDVs62weucaio7q2VgAAyIaKw7l99903FrdzpvzMM8/ErrvuWo0xAaicgxWU09ba0NAa3qmcAwCAbKg4nFt99dXjk5/8ZCwr+tb/1FNPxa677hoHHHBAVQcH1C+Vc1CqnLbW4seFcwAAkA0Vh3M33nhjLFy4MA477LBIkiSeeOKJ2HXXXeOQQw6Jiy66qDfGCNQhlXNQqpy21uLHtbUCAEA2VBzOrbLKKvG73/0unnnmmTjwwANj9913jyOPPDLOP//83hgfUKes1gqlymlrLX5c5RwAAGRDF1/xC1ZcBKKxsTGuu+66+NjHPhYHHHBAfPOb32zZZ8iQIdUfJVB3tLVCKeEcAADkU1nh3LBhw6KhoaHN9iRJ4rLLLosf//jHkSRJNDQ0xHJ9NEAVaGuFUunhVVsrAADkS1nh3D333NPb4wAooa0VSqmcAwCAfCornNtll116exwAJYqr5VTOgXAOAADyquIFIW677ba4//77W+5ffPHFsc0228Shhx4ab7zxRlUHB9QvlXNQSlsrAADkU8Xh3Mknn9yy+MPjjz8eJ554Yuyzzz4xb968OPHEE6s+QKA+qZyDUirnAAAgn8pqay02b9682GKLLSIi4je/+U3st99+8Z3vfCcefvjh2Geffao+QKA+qZyDUsI5AADIp4or5wYOHBjvvPNORETceeedseeee0ZExFprrdVSUQfQU1ZrhVKVtrUK5wAAIBsqrpz7yEc+EieeeGLsuOOO8cADD8R1110XERF/+9vfYr311qv6AIH6VBzIqZyDyivnzDkHAADZUHHl3I9+9KPo379//PrXv45LL7003ve+90VExO9///vYa6+9qj5AoD6pnINS2loBACCfKq6ce//73x+33HJLm+0XXHBBvP7661UZFIA556CUtlYAAMiniivn2nPHHXfEQQcd1FJFB9BTVmuFUtpaAQAgn7odzr3wwgvx7W9/O9Zff/349Kc/HQ0NDfGLX/yimmMD6pjKOSilrRUAAPKporbWJUuWxI033hg//elP409/+lPsscce8dJLL8UjjzwS48eP760xAnVI5RyU0tYKAAD5VHbl3Fe+8pUYPXp0XHTRRfHJT34yXnrppfjtb38bDQ0N0a+rMwWACqmcg1LaWgEAIJ/Krpy79NJL49RTT42vfe1rscYaa/TmmACEc7ACba0AAJBPZVfOXX311fHAAw/EqFGj4qCDDopbbrkllrssD/QSba1Qqty2VuEcAABkS9nh3CGHHBIzZ86Mxx9/PDbbbLOYOnVqjBw5Mpqbm+Ovf/1rb44RqEMq56BUuZVzaXjn+hkAAGRDxau1jhs3Ls4444x4/vnn45e//GUccMABcfjhh8d6660XX/3qV3tjjEAdKg7kVM6BtlYAAMirilZrLdbQ0BCTJk2KSZMmxeuvvx6/+MUv4sorr6zm2IA6VhzIqZyD1ko44RwAAORLxZVz7VlrrbXi+OOPj0cffbQaLwegcg5WkIZtXc05p60VAACypeLKuRNPPLHd7Q0NDTF48ODYaKON4hOf+ESstdZaPR4cUL9UzkEpba0AAJBPFYdzjzzySDz88MOxfPny2HTTTSMi4m9/+1v069cvNttss7jkkkvipJNOivvvvz+22GKLqg8YqA8q56CUcA4AAPKp4rbWT3ziE7HHHnvEK6+8EnPmzIk5c+bESy+9FB/72MfikEMOiZdffjl23nnnOOGEE3pjvECdKA7nli6NaG7uu7FALUjbVLW1AgBAvlQczp177rlx1llnxZAhQ1q2DR06NKZNmxbnnHNOrLrqqvGtb30r5syZU9WBAvVlxWo5ra3UO5VzAACQTxWHcwsXLozXXnutzfZ//vOf0dTUFBERw4YNiyVLlvR8dEDdWjGME85R74RzAACQT91qaz366KPjpptuipdeeileeumluOmmm2LKlCkxefLkiIh44IEHYpNNNqn2WIE6sWxZ2zZW885R77S1AgBAPlW8IMSPf/zjOOGEE+Lggw+OZf//snz//v3jqKOOigsuuCAiIjbbbLP46U9/Wt2RAnWjvSBO5Rz1TuUcAADkU8Xh3Oqrrx4/+clP4oILLoh//OMfERGxwQYbxOqrr96yzzbbbFO1AQL1pziIW331iLffFs6BcA4AAPKp4rbWX/7yl/HOO+/E6quvHltttVVstdVWJcEcQE+llXP9+0estlrpNqhXlba1CucAACAbKg7nTjjhhBg+fHgceuihceutt8Zyk9oAVZZWyQ0aVPgp3gb1qtLKOYdnAADIhorDufnz58e1114bDQ0NceCBB8aoUaNi6tSpMWvWrN4YH1CHisO5wYMLt1XOUe+0tQIAQD5VHM71798/Pv7xj8f06dPjtddeiwsuuCCef/752G233WLDDTfsjTECdSYN4gYPVjkHKW2tAACQTxUvCFFs1VVXjUmTJsUbb7wRL7zwQjz11FPVGhdQx1TOQVvaWgEAIJ8qrpyLiHjnnXdi+vTpsc8++8T73ve+uPDCC+OTn/xkPPnkk9UeH1CHzDkHbWlrBQCAfKo4nDv44INj+PDhccIJJ8QGG2wQf/jDH+LZZ5+Ns846K5Y5EwCqoLitVeUcRCRJRHNz4ba2VgAAyJeK21r79esX119/fUyaNCn69esXb731Vlx++eVxxRVXxEMPPWT1VqDHVM5BqeJDq7ZWAADIl4rDuenTp0dExH333RdXXHFF/OY3v4nRo0fHpz71qfjRj35U9QEC9ae9BSFUzlHPiqvgtLUCAEC+VBTOLViwIK666qq44ooroqmpKQ488MBYvHhxzJgxI7bYYoveGiNQZ9pbEELlHPWsuAquq7ZW4RwAAGRL2XPO7bfffrHpppvGo48+GhdeeGG88sor8cMf/rA3xwbUqfbaWlXOUc8qqZxLwzttrQAAkA1lV879/ve/j69+9avxpS99KTbeeOPeHBNQ59pbEELlHPVMWysAAORX2ZVz999/f7z11lux/fbbx4QJE+JHP/pR/Otf/+rNsQF1SuUclCqugmvs4sgtnAMAgGwpO5z78Ic/HD/5yU9i/vz58YUvfCGuvfbaGD16dDQ3N8fMmTPjrbfe6s1xAnXEnHNQKg3a+vWLaGjofF9trQAAkC1lh3Op1VZbLY4++ui4//774/HHH4+TTjopvvvd78bw4cNj//33740xAnWmvdVahXPUszSc66qltXgflXMAAJANFYdzxTbddNM455xz4qWXXopf/epX1RoTUOfaq5zT1ko9S6vghHMAAJA/PQrnUv369YvJkyfHzTffXI2XA+qcyjkoVdzW2hVtrQAAkC1VCecAqknlHJTS1goAAPklnANqTnurtaqco54J5wAAIL+Ec0DNKW5rVTkHrS2q2loBACB/hHNAzVE5B6VUzgEAQH4J54Ca0144p3KOeiacAwCA/BLOATWnvbZWlXPUs+60tQrnAAAgG4RzQM1ROQelulM5Z845AADIBuEcUHNUzkEpba0AAJBfwjmg5qicg1LaWgEAIL+Ec0DNKQ7nVM6BtlYAAMgz4RxQc4rbWtPKOeEc9UxbKwAA5JdwDqg57VXOvfdeRJL03ZigL2lrBQCA/BLOATWnvTnnIiKWLu2b8UBf09YKAAD5VfPh3Prrrx8NDQ1tfqZOnRoREbvuumubx774xS+WvMaLL74Y++67b6y66qoxfPjwOPnkk2PZCiUFf/jDH2K77baLQYMGxUYbbRRXXXXVyvqIwAraW621eDvUm+6Ec83NhR8AAKC2lfE1v289+OCDsbzo8v8TTzwRH/vYx+LTn/50y7bPf/7zceaZZ7bcX3XVVVtuL1++PPbdd98YOXJkzJo1K+bPnx9HHnlkDBgwIL7zne9ERMS8efNi3333jS9+8Ysxffr0uOuuu+Jzn/tcjBo1KiZNmrQSPiWQSpLSyrmBA1sfM+8c9ao7ba3p8xpr/jIcAADUt5oP59Zdd92S+9/97ndjww03jF122aVl26qrrhojR45s9/l33HFH/PWvf40777wzRowYEdtss02cddZZceqpp8a0adNi4MCBcdlll8W4cePivPPOi4iIzTffPO6///644IILhHOwki1Z0np78OBCsDBwYGG7yjnqVXcq5yIK4dyAAb0zJgAAoDoydT19yZIl8ctf/jKOPvroaGhoaNk+ffr0WGeddWLLLbeM0047Ld55552Wx2bPnh3jx4+PESNGtGybNGlSNDU1xZNPPtmyzx577FHyXpMmTYrZs2d3OJbFixdHU1NTyQ/Qc8XVcel8c1Zspd51N5yzKAQAANS+mq+cKzZjxox488034zOf+UzLtkMPPTTGjh0bo0ePjsceeyxOPfXUeOaZZ+LGG2+MiIgFCxaUBHMR0XJ/wYIFne7T1NQU7777bqyyyiptxnL22WfHGWecUc2PB0RpAJe2tA4eHPHWWyrnqF9pW6twDgAA8idT4dwVV1wRe++9d4wePbpl2zHHHNNye/z48TFq1KjYfffd47nnnosNN9yw18Zy2mmnxYknnthyv6mpKcaMGdNr7wf1Ig3gBg5snStL5Rz1Lg3ZujPnHAAAUNsyE8698MILceedd7ZUxHVkwoQJERHx7LPPxoYbbhgjR46MBx54oGSfV199NSKiZZ66kSNHtmwr3mfIkCHtVs1FRAwaNCgGpYkBUDXFi0Gk0tsq56hXlbS1NjZGNDQUFldROQcAALUvM3POXXnllTF8+PDYd999O91v7ty5ERExatSoiIiYOHFiPP744/Haa6+17DNz5swYMmRIbLHFFi373HXXXSWvM3PmzJg4cWIVPwFQjvbCucGDSx+DelNJW2vxfsI5AACofZkI55qbm+PKK6+Mo446KvoXnZk899xzcdZZZ8WcOXPi+eefj5tvvjmOPPLI2HnnnWOrrbaKiIg999wztthiizjiiCPi0Ucfjdtvvz1OP/30mDp1akvl2xe/+MX4xz/+Eaeccko8/fTTcckll8T1118fJ5xwQp98XqhnaXVcGshFqJyDStpai/fT1goAALUvE+HcnXfeGS+++GIcffTRJdsHDhwYd955Z+y5556x2WabxUknnRQHHHBA/Pa3v23Zp1+/fnHLLbdEv379YuLEiXH44YfHkUceGWeeeWbLPuPGjYvf/e53MXPmzNh6663jvPPOi5/+9KcxadKklfYZgQKVc9BWJW2txfupnAMAgNqXiTnn9txzz0iSpM32MWPGxL333tvl88eOHRu33nprp/vsuuuu8cgjj3R7jEB1pAGcyjlopa0VAADyKxOVc0D9SAM4lXPQSlsrAHnz0EMRXaz1B1A3MlE5B9SPzlZrFc5Rr7S1ApA3Bx4YMW9exAsvRLz//X09GoC+pXIOqCntLQiR3tbWSr0SzgGQN6+9Vvj9r3/17TgAaoFwDqgpKuegrbQ9VVsrAHmQJBHvvlu4nf4GqGfCOaCmdLZaq8o56pXKOQDyZOnSiObmwm3hHIBwDqgx7bW1qpyj3gnnAMiT4kBOOAcgnANqjMo5aKu7ba3COQBqUfF3Ot/vAIRzQI1JwzmVc9Cqu5Vz5pwDoBapnAMoJZwDakp69bS9BSFcWaVeaWsFIE+EcwClhHP02K23Rkyf3tejIC86a2tVOUe90tYKQJ5oawUoVeY1eGhfkkQcfHDE229H7LVXxNpr9/WIyLrOFoTw5Y16pa0VgDxROQdQSuUcPbJ0acRbbxVCujff7OvRkAcq56Atba0A5IlwDqCUcI4ecWCl2toL51TOUe+0tQKQJ9paAUoJ5+iR4oPpO+/03TjIj/baWlXOUe+0tQKQJy7wA5QSztEjxQdT4RzV0FnlnHCOeqWtFYA8Ec4BlBLO0SMOrFRbGsC1Vzmn7YF6VWlbq3AOgFrmHAKglHCOHlE5R7WlAZzKOWhVaeVcGuJpawWgFplzDqCUcI4ecdWLautstVZf3qhX2loByBPnEAClhHP0iMo5qq29BSFUzlHv0go44RwAeSCcAyglnKNHhHNUm8o5aCsN2cqdc05bKwC1TFsrQCnhHD3iqhfVZrVWaEtbKwB54hwCoJRwjh5ROUe1ddbW6soq9UpbKwB5IpwDKCWco0ccWKm2ztpam5uFDdQnba0A5Im2VoBSwjl6ROUc1ZaGc+1VzkX4Akd90tYKQJ64wA9QSjhHjziwUm1p+NbenHMR5p2jPgnnAMgT5xAApYRz9IjKOaqpuTli6dLC7eJArn//1jY9lXPUo7Q9VVsrAHkgnAMoJZyjR4RzVFNxVVxxW2vxfZVz1COVcwDkSfHF1mXLHK8AhHP0iKteVFNx8FZcOVd8XzhHPRLOAZAnK5436IwA6p1wjh5ROUc1FQdvAwaUPpZWzvnyRj3qblurcA6AWrRiOOciP1DvhHP0iMo5qikN3gYPjmhoKH1M5Rz1rLuVc+acA6AWrXix1cVXoN4J5+gRlXNUUxq8rdjSGqFyjvqmrRWAPFE5B1BKOEePqJyjmtJwbsXFICJUzlHftLUCkCfCOYBSwjl6ROUc1ZRWxamcg1LaWgHIk/T7XHq88v0OqHfCOXpEOEc1ddbWqnKOeqatFYC8WL48YsmSwu011yz8VjkH1DvhHD2yYltrkvTdWMi+4gUhVpSGc66sUo+0tQKQF8Xf5dZaq/BbOAfUO+EcPbLigVRwQk+UsyCEyjnqTXNz64UPba0AZF3x+cOwYW23AdQj4Rw9YjJXqqmcBSEEwNSb4uo3ba0AZF3xfHOrr166DaBeCefokRXDOPPO0RPlLAihco56U1z9Vm5bq3AOgFqVnj+sskrhp3gbQL0SztEjwjmqqZwFIVxZpd50p3IuDfG0tQJQa4RzAG0J5+i25ubWMCU9YXRgpSc6a2tVOUe90tYKQJ4ULwCWfr9z8RWod8I5uq29lZZUztETnbW1qpyjXmlrBSBPVM4BtCWco9uKD6KWQacarNYKbaUBW0NDRGOZR21trQDUKuEcQFvCObotPYj27x8xZEjhtso5eqK4zWFFaWAnnKPepOFcuS2txfuqnAOg1qTf94rDOZ0RQL0TztFtrnpRbeVUzvnyRr1Jq9+EcwDkQXq+UDznnHMIoN4J5+i24nBu1VULt1XO0ROdLQihco56lQZs5c43V7yvtlYAao0L/ABtCefotvYOrMI5eqKzBSFUzlGvtLUCkCfCOYC2hHN0W3uVcw6s9ERnba0q56hX2loByJPiOYZdfAUoEM7RbSrnqLbO2lp9eaNeaWsFIE9UzgG0JZyj21TOUW2dtbWqnKNeaWsFIE+EcwBtCefoNgtCUG3ltLWqnKPeCOcAyBNtrQBtCefoNle9qLbiL2srSrepnKPepK2p3WlrFc4BUGucQwC0JZyj21TOUW0q56CtnlTOmXMOgFojnANoSzhHt1kQgmorZ0EIlXPUG22tAORJeqG1+BzCxVeg3gnn6DYLQlBt5SwI4csb9UZbKwB5kp4vFM855xwCqHfCObpN5RzV1llbq8o56pW2VgDyRFsrQFvCObpN5RzV1llbaxrYCeeoN9paAciT9sK5996LSJK+GxNAXxPO0W0WhKDaOmtrTQO7pUsjmptX3pigr2lrBSBP0u97xW2tES7AAvVNOEe3aWul2spZrbV4P6gH2loByJP2ziGKtwPUI+Ec3aatlWorvpK6ouJtFoWgnvS0rVWbEAC1pPgcYsCA1mpv5xFAPRPO0W0q56i2zirn+vePaGgo3Q/qQU/aWiO0gQNQW1a8GJv+dvEVqGfCObpN5RzVtGxZawjRXuVcQ4Mvb9SnnlTORWhtBaC2FJ9DFP92HgHUM+Ec3dZe5dzixU4E6Z7iarj2KueKt6uco570NJyzKAQAtUQ4B9CWcI5uS6uXiivnirdDJSoJ5/wbo550p61VOAdALUqS0nOI4t++3wH1TDhHtxVf9SpuQzTvHN2RhnP9+nVcIZT+O1M5Rz3pTuVccZCnmhmAWrFkSetCRSvOOadyDqhnwjm6rTica2xsPbAK5+iO9GppR1VzxY+5sko96Wk4p3IOgFpRHMBpawVoJZyj21acL8KiEPREZyu1plTOUY/SyrdKwrmGhtaATjgHQK1IzxMaGiIGDizcFs4BCOfogY4mc1U5R3ek1XDtrdSaUjlHPUrDtUrmnCveX1srALWi+PteQ0Pr7eLHAOqRcI5uUzlHNamcg/Z1p621eH+VcwDUihXPH4pvO4cA6plwjm5ZurS1GkPlHNWQBm4q56BUd9pai/cXzgFQK4RzAO0TztEt7U3mqnKOnihnQQiVc9Qjba0A5EV705hoawUQztFNxZO5pmFKGs6pnKM7ymlrTR8TzlFPtLUCkBcq5wDaJ5yjW9KDZ/Fkrtpa6Yly2lpdWaUeaWsFIC+EcwDtE87RLe0dWLW10hPltLWqnKMeaWsFIC/S73vthXMuvgL1TDhHt3R21UvlHN1RyWqtvrxRT7S1ApAXxd03qfS2C/xAPRPO0S0q56i29iYIXpHKOeqRcA6AvNDWCtA+4RzdonKOaqtkQQiVc9STtC21u22twjkAaoVwDqB9wjm6pbPKOeEc3VHJghAq56gnPa2cM+ccALWivU4J05YACOfoJm2tVFslC0L48kY90dYKQF6onANon3CObtHWSrVVsiCEyjnqibZWAPJCOAfQPuEc3aJyjmorp61V5Rz1SFsrAHmhrRWgfcI5ukXlHNVWTluryjnqkbZWAPJC5RxA+4RzdIvKOarNaq3QPm2tAOSFcA6gfcI5uiU9eBaXpFutlZ5or81hRSrnqEfaWgHIi/T7XnvhnIuvQD0TztEt2lqptkoq54Rz1BNtrQDkRXsX+NPbKueAeiaco1u0tVJt5SwIYcJg6lF321qFcwDUGm2tAO0TztEtKueotnIWhFA5Rz3qbuVcGuZpawWgVnR2DrF8ecTSpSt/TAC1QDhHt6ico9rKaWtVOUc90tYKQF60N8dw8W3f8YB6JZyjW1TOUW3ltLWqnKMepZVvwjkAsq69c4ji734u8gP1SjhHt3RWObdsmZJ0KldJW6urqtSTNFyrdM45ba0A1Jr2ziEaGiwKASCco1s6C+eKH4dyVdLWqnKOeqKtFYC8aK+ttfi+C7BAvarpcG7atGnR0NBQ8rPZZpu1PP7ee+/F1KlTY+21147VV189DjjggHj11VdLXuPFF1+MfffdN1ZdddUYPnx4nHzyybFshTOVP/zhD7HddtvFoEGDYqONNoqrrrpqZXy8TGsvnBs4sHDlK0JrK5Xr6MtaseK21iTp/TFBLdDWCkBetHcOUXzfBX6gXtV0OBcR8YEPfCDmz5/f8nP//fe3PHbCCSfEb3/727jhhhvi3nvvjVdeeSU+9alPtTy+fPny2HfffWPJkiUxa9as+PnPfx5XXXVVfOtb32rZZ968ebHvvvvGbrvtFnPnzo3jjz8+Pve5z8Xtt9++Uj9n1nRUkm5RCLqrksq5iIglS3p3PFArtLUCkBfCOYD2VXgdfuXr379/jBw5ss32hQsXxhVXXBHXXHNNfPSjH42IiCuvvDI233zz+POf/xwf/vCH44477oi//vWvceedd8aIESNim222ibPOOitOPfXUmDZtWgwcODAuu+yyGDduXJx33nkREbH55pvH/fffHxdccEFMmjRppX7WLOnswLpokco5KlfJghARhUq7zoI8yAttrQDkwbJlrcekjsI5ba1Avar5yrm///3vMXr06Nhggw3isMMOixdffDEiIubMmRNLly6NPfbYo2XfzTbbLN7//vfH7NmzIyJi9uzZMX78+BgxYkTLPpMmTYqmpqZ48sknW/Ypfo10n/Q1OrJ48eJoamoq+aknHYVzKuforkoWhIgw7xz1Q1srAHlQHLx1NOeccwigXtV0ODdhwoS46qqr4rbbbotLL7005s2bFzvttFO89dZbsWDBghg4cGAMGzas5DkjRoyIBQsWRETEggULSoK59PH0sc72aWpqinc7OTqcffbZMXTo0JafMWPG9PTjZkpXJekq56hEkpTX1trQUJjbMMKVVeqHtlYA8qD41EpbK0Cpmm5r3XvvvVtub7XVVjFhwoQYO3ZsXH/99bHKiv+PvpKddtppceKJJ7bcb2pqqquArqvKOeEclVi2rHWBh87aWtPHlyxROUf90NYKQB6k5w8DB0Y0rlAiIpwD6l1NV86taNiwYbHJJpvEs88+GyNHjowlS5bEm2++WbLPq6++2jJH3ciRI9us3pre72qfIUOGdBoADho0KIYMGVLyUy+am1uDEW2tVENxFVxX88ilj6uco14I5wDIg/S7W3sXYtNtvt8B9SpT4dzbb78dzz33XIwaNSq23377GDBgQNx1110tjz/zzDPx4osvxsSJEyMiYuLEifH444/Ha6+91rLPzJkzY8iQIbHFFlu07FP8Guk+6WvQVvFBU1sr1VBcBddVOJd+eVM5R71I21K729YqnAOgFnTUeVO8zQV+oF7VdDj3X//1X3HvvffG888/H7NmzYpPfvKT0a9fvzjkkENi6NChMWXKlDjxxBPjnnvuiTlz5sRnP/vZmDhxYnz4wx+OiIg999wztthiizjiiCPi0Ucfjdtvvz1OP/30mDp1agz6/wnAF7/4xfjHP/4Rp5xySjz99NNxySWXxPXXXx8nnHBCX370mtbZfBEq5+iONPAdMKBtm8OK0vBOOEe96GnlnDnnAKgFwjmAjtX0nHMvvfRSHHLIIfHvf/871l133fjIRz4Sf/7zn2PdddeNiIgLLrggGhsb44ADDojFixfHpEmT4pJLLml5fr9+/eKWW26JL33pSzFx4sRYbbXV4qijjoozzzyzZZ9x48bF7373uzjhhBPioosuivXWWy9++tOfxqRJk1b6582K9KDZv3/bk0WVc3RHOYtBpLQ9UG+0tQKQB9paATpW0+Hctdde2+njgwcPjosvvjguvvjiDvcZO3Zs3HrrrZ2+zq677hqPPPJIt8ZYjzq76qVyju5Iw7muFoOIUDlH/dHWCkAeqJwD6FhNt7VSm8o5sKqcoxLpVVKVc9CWtlYA8kA4B9Ax4RwVK6dyTjhHJSppa1U5R73R1gpAHqQXVoVzAG0J56iYtlaqrTttrSrnqBfaWgHIg/T8wJxzAG0J56iYtlaqrTttrSrnqAdJ0hrOaWsFIMu0tQJ0TDhHxVTOUW3daWt1ZZV6UBysaWsFIMuEcwAdE85RMZVzVFsatJXT1qpyjnpSHM5pawUgyzr7vqetFah3wjkqZkEIqk3lHLSvOFjT1gpAlqmcA+iYcI6KObBSbZUsCKFyjnpSjXBO5RwAtcA5BEDHhHNUTOUc1VbJghAq56gnPWlrFc4BUEu0tQJ0TDhHxdKDpgUhqJZK2lpVzlFPioO17s45p60VgFqgcg6gY8I5KmZBCKqtkrbWNMATzlEP0nCuX7+IhobKnqtyDoBaIpwD6JhwjoqV09bqwEolKmlr1fZAPUmr3iqdb674OcI5AGqBcA6gY8I5KqZyjmrrzmqtKueoB8WVc5XS1gpALTHnHEDHhHNUrNwFIZJk5Y2JbOvsy9qKfHmjnqThnMo5ALKunAv8ixdHNDevvDEB1ArhHBUr58CaJBFLlqy8MZFtKuegfdpaAciLcs4hIlyABeqTcI6KlVM5F6G1lfJ1Z0EIX9yoB9paAciLctpai/cDqCfCOSrWWTg3YEBrtYYJXSlXdxaEUDlHPdDWCkBedHYO0b+/cwigvgnnqFhnB9bi7SrnKFd32lpdVaUeaGsFIC/KPYcQzgH1SDhHxbo6sKatrQ6slKuStlaVc9STarS1CucAqAVdLQBm0S+gngnnqJjKOaqtkrZWlXPUk2q0tZpzDoBaoHIOoGPCOSpWbuWccI5yVdLWqnKOemLOOQDyIElaL6wK5wDaEs5RMVe9qLau2hyKqZyjnqRVb9paAciy4u9tziEA2hLOUTGVc1Sbyjlon7ZWAPKgOJwz5xxAW8I5KmZBCKqtkgUhiivnkqT3xgS1QFsrAHmQnhc0NkYMGND+PirngHomnKMiS5e2VmFYEIJqqWRBiDTASxKhA/mnrRWAPCi+uN/Q0P4+wjmgngnnqEjxwVJbK9VSSVtr8T5aW8k7ba0A5EE58wtrawXqmXCOiqThXENDx0GKq15UqjttrRG+vJF/2loByIOupsUpfsw5BFCPhHNUJD1YDh7ccUm6yjkqVUlba79+raGDyjnyrhptrc3N5mcEoG8J5wA6J5yjIg6sVFuSRCxZUrhdTjhXvJ/KOfKuGpVzEVpbAehb2loBOiecoyLFlXMdUTlHJdJgLqK8ttbi/VTOkXfVCue0tgLQl1zgB+iccI6KlHNgTcM5B1bKUXx1VOUclOpJW6twDoBaIZwD6JxwjopUcmBVOUc5iqvfBg4s7zkq56gXPamcKw70tLUC0JeEcwCdE85RkUoq54RzlKN4MYiOFhlZkco56oW2VgDywJxzAJ0TzlERV72otrT6rdyW1giVc9SPtOKtO+FcY2Nr4C2cA6AvOYcA6JxwjoqonKPa0oCt3MUgIlTOUT/SUK07c84VP09bKwB9STgH0DnhHBWxIATVVtzWWi6Vc9SLnrS1Fj9P5RwAfUlbK0DnhHNUxIIQVFt32lpVzlEvetLWWvw84RwAfUnlHEDnhHNUROUc1dadtlaVc9QLba0A5IFwDqBzwjkqonKOautOW2u6r3COvNPWCkAeaGsF6JxwjopYEIJq60nlnC9v5J22VgDyQOUcQOeEc1SkkgPre+9FNDf3/pjINpVz0LFqtbUK5wDoS8I5gM4J56hIJZVzESqb6JoFIaBj1WprNeccAH1JOAfQOeEcFankwFq8P3TEghDQMXPOAZAHlc45lyS9PyaAWiKcoyLlhHP9+kUMHFi4bd45utKTtlaVc+RdWvGmrRWALKvkAn9zc8TSpb0/JoBaIpyjIuUcWCMsCkH5utPWqnKOeqGtFYA80H0D0DnhHBUpN5wzZwTl6k5bq8o56oW2VgDyoJy21oEDIxoaSvcHqBfCOSqico5q605bq8o56oW2VgDyoJxziIaG1u94LvAD9UY4R0VUzlFtKuegY9paAcgD5xAAnRPOURGVc1SbyjnomLZWAPKgnLbW4sddgAXqjXCOilQazrnqRVe6syCEyjnqhbZWAPJA5RxA54RzVKTSA6vKObrSnbZWlXPUC22tAGTd0qWtxyHhHED7hHNURFsr1dadtlaVc9QLba0AZF1x0CacA2ifcI6yNTe3Vio5sFIt3WlrVTlHvehpW6twDoC+Vnwxtavve+acA+qVcI6yFR8kVc5RLT1ZrVU4R971tHIuDfW0tQLQV9KL9YMGRTR2cfbpAj9Qr4RzlE1JOr1BWyt0TFsrAFlX7rQ4xfs4hwDqjXCOsqUHyf79uz5RVDlHuSwIAR1LK96EcwBkVXoxtZzvetpagXolnKNslVz1SsO53rzqNW9exK9/HZEkvfce9D6Vc9CxNFTr7pxz2loB6Gsq5wC6JpyjbN05sPZm5dwxx0R8+tMR99/fe+9B77MgBHRMWysAWSecA+iacI6ypVVKlVTO9WY4N29e4ffzz/fee9D7erIgxLJlKoLIN22tAGSdtlaArgnnKFutXfX6979Lf5NN3WlrLf5yp3qOPNPWCkDW1do5BEAtEs5Rtu7MOddblXPLl0e8+Wbh9uuv9857sHJ0p621eF9XVskzba0AZJ1wDqBrwjnKVksH1jfeaL2tci7butPW2r9/RGNj6fMhj7S1ApB1tXQOAVCrhHOUrZYq54qr5VTOZVt32lobGqzYSn3Q1gpA1plzDqBrwjnKVkvhXHG1nMq57Fq+vDV8qKRyrnh/lXPkmbZWALJO5RxA14RzlK2WDqwq5/KhOFirpHKueH9XVskzba0AZF0tnUMA1CrhHGVTOUe19SScUzlHPahWW6twDoC+oq0VoGvCOcpWS1e9igM5lXPZlQZrjY2VVwalYZ5wjjyrVlurOecA6Cu1dA4BUKuEc5StO5VzS5b0zklhcSDX1BSxdGn134PeV7wYRENDZc91ZZV6YM45ALJOOAfQNeEcZevOgbX4edW0YivrG29U/z3ofWnVW6UtrcXPUTlHnqUXN7S1ApBV2loBuiaco2yVhHPFB9/emHduxVZW885lUxqsVbpSa4QFIagP2loByDqVcwBdE85RtkoOrI2Nrfv1Rji3YhgnnMum4rbWSlkQgnqgrRWArBPOAXRNOEfZKjmwFu/XGwfXFSvnLAqRTSrnoHPaWgHIOuEcQNeEc5St0nAuXRSiNyvn1lyz9D7ZonIOOqetFYCs686cc0uXOnYB9UU4R9lqsXJuk01K75Mt1VgQQuUcedXcHJEkhdvaWgHIqu4uKuc7HlBPhHOUrVYq55YsiXjrrcLtjTcu/FY5l009aWtVOUfeFVcMaGsFIKu6u6ic1lagngjnKFutVM6lVXINDREbbFC6jWzpSVuryjnyrjhQ09YKQFZV0tbar1/EgAGlzwOoB8I5ylYrlXNpELfmmhHrrlu4rXIum3rS1qpyjryrZjincg6AvlIrF/gBaplwjrKlB8hyWxB7K5xLg7i11ir8RKicyyqrtULHqtHWKpwDoK8J5wC6JpyjbLVyYE2DuLXXLvxEqJzLKqu1QseqUTmXhnraWgHoK5W0tRbv5wIsUE+Ec5StVtpa26ucE85lk8o56FgazjU0RDR282itcg6AvtTc3Pp9r68v8APUMuEcZavlyjltrdmkcg46lla7dbdqrvi5wjkA+kLxRdS+PocAqGXCOcqydGnriWItVs69844KqizqyYIQ6XOEc+RVGqh1d7654udqawWgLxQHbMI5gI4J5yhLdw6svR3Orb12xNChrSefqueyR1srdCwN51TOAZBV6fe0fv3KP56Zcw6oR8I5ylIczpUbpKyMttaGhog11yzcN+9c9mhrhY5pawUg6yqdFqd4X5VzQD0RzlGW9OA4eHAhECvHymhrjTDvXJZVo63VVVXySlsrAFknnAMoj3COstTSgbW4cq74t8q57OlJW6vKOfJOWysAWZdeRK3ku562VqAeCecoS3fCuZVVOZf+VjmXPT1pa1U5R95pawUg62rpAj9ALRPOUZZaOrCqnMsPlXPQsWq2tQrnAOgLtXQOAVDLhHOUpVYq5959t3UsKueyT+UcdKyaba3mnAOgL2hrBSiPcI6y1Eo4lwZw/ftHDBlSuK1yLrt6siCEyjnyTlsrAFmncg6gPMI5ylIrB9bi+ebSVWPTyjnhXPb0pK1V5Rx5p60VgKyrlXMIgFpX0+Hc2WefHf/xH/8Ra6yxRgwfPjwmT54czzzzTMk+u+66azQ0NJT8fPGLXyzZ58UXX4x99903Vl111Rg+fHicfPLJsWyFM5U//OEPsd1228WgQYNio402iquuuqq3P16m1Erl3IqLQUS0Vs5pa82enrS1qpwj77S1ApB1wjmA8tR0OHfvvffG1KlT489//nPMnDkzli5dGnvuuWcsWrSoZL/Pf/7zMX/+/Jafc845p+Wx5cuXx7777htLliyJWbNmxc9//vO46qqr4lvf+lbLPvPmzYt99903dtttt5g7d24cf/zx8bnPfS5uv/32lfZZa12tHFhXXAwiQuVcllWjcm7Jkojm5uqNCWpFNcM5lXMA9AVzzgGUpwdf+XvfbbfdVnL/qquuiuHDh8ecOXNi5513btm+6qqrxsiRI9t9jTvuuCP++te/xp133hkjRoyIbbbZJs4666w49dRTY9q0aTFw4MC47LLLYty4cXHeeedFRMTmm28e999/f1xwwQUxadKk3vuAGdLTyrkkaW1D7QmVc/lSjTnnIgoBXXcCPqhlabWbtlYAsqpWLvAD1Lqarpxb0cKFCyMiYq3iZCYipk+fHuuss05sueWWcdppp8U7RX2Us2fPjvHjx8eIESNatk2aNCmampriySefbNlnjz32KHnNSZMmxezZszscy+LFi6OpqankJ896cmBdvjxi6dLqjKO9yrniBSGSpDrvw8pRjdVaI7S2kk/aWgHIOuEcQHlqunKuWHNzcxx//PGx4447xpZbbtmy/dBDD42xY8fG6NGj47HHHotTTz01nnnmmbjxxhsjImLBggUlwVxEtNxfsGBBp/s0NTXFu+++G6u0czQ5++yz44wzzqjqZ6xlPamcS58/cGDPx9Fe5Vx6e8mSQpXeaqv1/H1YOXrS1lr87+m99yKGDq3OmKBWaGsFIOu0tQKUJzPh3NSpU+OJJ56I+++/v2T7Mccc03J7/PjxMWrUqNh9993jueeeiw033LDXxnPaaafFiSee2HK/qakpxowZ02vv19e6E84NHBjR2FiYD+ydd6oTnrRXObfaaoX3WrKkEN4J57KjJ5VzDQ2F5y1erHKOfNLWCkDWqZwDKE8m2lqPPfbYuOWWW+Kee+6J9dZbr9N9J0yYEBERzz77bEREjBw5Ml599dWSfdL76Tx1He0zZMiQdqvmIiIGDRoUQ4YMKfnJs+4cWBsaqn9wba9yrqGh9b5557KlJ3POFT/PlVXyqJqVcxEWTgFg5RPOAZSnpsO5JEni2GOPjZtuuinuvvvuGDduXJfPmTt3bkREjBo1KiIiJk6cGI8//ni89tprLfvMnDkzhgwZEltssUXLPnfddVfJ68ycOTMmTpxYpU+Sfd05sEaULgpRDWk4V1w5V3zfiq3ZsWxZa1jQ3cUc0uepnCOPqh3OqZ4DYGXrSVurcA6oJzUdzk2dOjV++ctfxjXXXBNrrLFGLFiwIBYsWBDv/v//p37uuefirLPOijlz5sTzzz8fN998cxx55JGx8847x1ZbbRUREXvuuWdsscUWccQRR8Sjjz4at99+e5x++ukxderUGPT/y26++MUvxj/+8Y845ZRT4umnn45LLrkkrr/++jjhhBP67LPXmu6Gc9W+8tVeW2uEyrksKq52UzkHbVWjrVU4B0Bf6knlnO93QD2p6XDu0ksvjYULF8auu+4ao0aNavm57rrrIiJi4MCBceedd8aee+4Zm222WZx00klxwAEHxG9/+9uW1+jXr1/ccsst0a9fv5g4cWIcfvjhceSRR8aZZ57Zss+4cePid7/7XcycOTO23nrrOO+88+KnP/1pTJo0aaV/5lpVa5VzKyzYq3Iug4qr3bobzqmcI8+qUTlXHOxZsRWAlU1bK0B5anpBiCRJOn18zJgxce+993b5OmPHjo1bb72103123XXXeOSRRyoaXz3paeVcNcK5JOm6ck44lx1poNa/f/crg1TOkWfaWgHIup6Gc0lSmF8aIO9qunKO2tHTyrlqXPl6++2IpUsLtzuqnNPWmh09Wak1pXKOPEsr3apVOSecA2Bl68mccxERS5ZUdzwAtUo4R1lqoa01Dd4GDWp93ZS21uxJA7XuLgYRoXKOfEvDtJ7MOdfQENH4/4/02loBWNl6UjlX/HyAvBPOUZZaWBCieL65FcvbLQiRPSrnoHPVaGstfr7KOQBWtu6cQwwY0HphSTgH1AvhHGWppcq5FeebK96mci470kCtJ+GcyjnyrBptrcXPF84BsLJ1p621oaF1f9/xgHohnKMs6YGxFirn2gvnVM5lTzXaWlXOkWfVaGstfr62VgBWtlrovgHIAuEcZamFyrnittYVqZzLnmq0tabPFc6RR9paAcg64RxAeYRzlKWnB9bebmstrpxLkp6/F73PghDQOW2tAGRZknSvrbV4f+EcUC+Ec3Sp+MDa3cq5ai8IsaJ02/LlEU1NPX8vel815pzT1kqeVbutVTgHwMq0dGlEc3Phdncv8LsAC9QL4RxdKj4o1uqCEKus0jo2885lQzXbWn1xI4+q3dZqzjkAVqbii/PaWgE6J5yjS7VyYO2sci7CvHNZY0EI6Jy2VgCyrPj7f6UXY4VzQL0RztGl9KDYv3/lJ4krq3IuojW0E85lg8o56Jy2VgCyrHi+uYaGyp6bXoD1HQ+oF8I5utTdxSCKn9Pbq7VGtIZ22lqzwZxz0DltrQBkWTXOIVTOAfVCOEeXenJg7Y0FITqqnNPWmi1Wa4XOVTucUzkHwMoknAMon3COLtVC5Vxzc8QbbxRud9XWqnIuG6rR1qpyjjxLK920tQKQRcVtrZXS1grUG+EcXaqFyrmFC1uXYrcgRD6onIPOaWsFIMtUzgGUTzhHl6oRzvW0ci6thltttY4rrVTOZYs556Bz2loByDLhHED5hHN0qRYOrF0tBhGhci5rrNYKndPWCkCWVaOtVTgH1AvhHF2qpcq5juabi1A5lzXVaGtVOUeeaWsFIMuqcYHfBVigXgjn6FK1FoRIku6PQeVc/qicg85pawUgy2qh+wYgK4RzdKkalXMRPatuUjmXP+acg85pawUgy4RzAOUTztGlahxYI3rW2ppWw3UWzqWPvfGG9q0sqOZqrcI58khbKwBZVo0553RHAPVCOEeXehLODRjQemLYkytf5bS1po8lScSbb3b/vVg5tLVC57S1ApBlKucAyieco0s9ObBGVGdRiHLaWgcMiFhjjdL9qV0WhIDOVautVTgHQF8QzkG+vfVWxDHHRMyc2dcjyQfhHF1KD4rdDVGqcXAtp3IuwqIQWVKNOedUzpFn1aqcS8M9ba0ArEzaWiHfrr024ic/idh//4hHHunr0WSfcI4uZaVyLsKiEFlSjbbW4sq5nqwGDLVIWysAWaZyDvLtqacKv997L2Ly5Ih//rNPh5N5wjm61NNwLn1eNRaEUDmXH9VcECJJIpYu7fmYoJaklW7COQCySDgH+fbMM4XfjY0RL74YcdBBvm/2hHCOLlWrcq4nB1eVc/lTzcq5CPPOkT/pl5uezjmnrRWAvtCTqXHS5wjnoHY9/XTh9w9/GLH66hH33BNx8sl9O6YsE87Rpb6unFu2rHX1VZVz+VHNOecizElC/mhrBSDL0u9mPamc8/0OatN770U8/3zh9qc+FfHznxduX3hhxNVX99Wosk04R5f6unLujTdab3cVzqmcy45qtLU2NhZW6S1+PcgLba0AZJm2VsivZ5+NaG6OGDIkYsSIQkB3+umFx445JmLOnL4dXxYJ5+hSXy8IkQZtQ4d2fZKqci47qtHWWvx8V1bJG22tAGRZNcK5ZctcXIJalM43t9lmEQ0NhdtnnBGx776F87JPfjLitdf6bnxZJJyjS33d1lruYhDF+6icq21JUp3KueLnq5wjb7S1ApBl6YXTnsw5V/w6QO1I55vbdNPWbY2NEb/8ZcTGG0f83/9FHHigRfsqIZyjS33d1lruYhDF+6icq23F/yetcg7ap60VgCzryTlEcTintRVqT3HlXLFhwyL+938j1lgj4t57I/7rv1b60DJLOEeXslQ5J5zLhuIgrafhnMo58qraba3COQBWpp6cQzQ2tn5HFM5B7Wmvci61+eati0L84Aeti0XQOeEcXcpS5Zy21mwoDtKqVTknnCNvqt3Was45AFamnrS1Fj9PdwTUliTpuHIu9YlPRHzrW4XbX/hCxIMPrpyxZZlwji719YIQ3amca2rS317L0i9ZAwe2TiDaXdpaySttrQBkWbW6b1TOQW159dXC+XZjY8RGG3W837e/HbHffoUiik99qvA8Oiaco0t9fWCtpHJu2LDWsOeNN7r3fvS+tMqtp1VzEdpayS9trQBkWV+fQwC9I21pXX/9zs/n0gUiNt004qWXIr761ZUyvMwSztGppUtbqzf6unKunHCuX79CQFf8PGpPtVZqjVA5R35pawUgq5Yvb+1i6Wlbq3AOaktXLa3FhgyJ+MlPCrf/8IdeG1IuCOfoVPHBMAsLQhTvZ9652pUGaSrnoGPVDudUzgGwshRfNO3pOYQLsFBbOlsMoj3bbVfobnvttcIP7RPO0anicK67V71W5oIQxfupnKtdKuega2mlm7ZWALKmmhf4Vc5Bbamkci4iYrXVIjbYoHD7iSd6Z0x5IJyjU+nBcPDg7k/cr3KOFZlzDrqmrRWArErPIQYM6P5FJuEc1KZKK+ciIrbcsvBbONcx4Ryd6ulErhEq52irmm2tKufIoySxWisA2ZV+L+tJl0T6XN/xoHa8917E888XbpdbORcRMX584ffjj1d9SLkhnKNT1QznulM5t2RJxNtvF26XWzmXhnMq52pXNdtaVc6RR83Nrbe1tQKQNdU4h1A5t/LdeWfEiy/29SioZc8+W7iIPHRoxPDh5T9P5VzXhHN0qq8PrGnA1tDQugprV9IQT+Vc7VI5B50rDtK0tQKQNX19DkHl/vSniI99LOLQQ/t6JNSy4pbWSqa9Sivnnnii9CI0rYRzdKqvK+fSgG3NNSMay/zXqq219plzDjrXG+GcyjkAVhZtrdlz992F33/5i+/VdKzSxSBSG29cmIPy7bdVZ3ZEOEenqnnVqyfhXLnzzUVYECILrNYKnSuucutpW6twDoCVTeVc9vz5z4Xfy5ZpPaRj3VkMIqIQzG2+eeG2eefaJ5yjU9WsnFu8uPIS1koXgyjeV+Vc7apmW6vKOfKompVzabinrRWAlUU4ly1JUqiYSz3ySN+NhdrW3cq5CPPOdUU4R6eqeWAtfr1ypQFbuYtBFO+rcq52qZyDzhWHcyrnAMia9Dt/NdpahXO977nnSgsbHn6478ZC7UqS7lfORVixtSvCOTrV1+Gcyrl8quacc+lrqJwjT9Iqt379Kptstz3COQBWtvSiaTXOIVyA7X1pS2v6nUPlHO1ZsCDirbcKc8FvtFHlz1c51znhHJ2qRjjXr19rgFLpvHM9qZx75x0H81qlrRU6lwZpPa2aK34Nba0ArCzaWrMlbWnda6/C70cf9b2BttKquXHjuncel4ZzTz8dsXRp9caVF8I5OlWNA2vx8ysN57pTOTd0aOvJqNbW2qStFTqXhnM9nW+u+DVUzgGwsgjnsiWtnDv88IjVViv8zdO5xSCV/pvoTktrRMTYsRGrr14I5v72t+qNKy+Ec3SqWuFcuijEyphzrqHBvHO1rpptrSrnyKP0arVwDoAsSi+aVmPOORdge9e770bMnVu4vcMOEdtsU7ht3jlW1JPFICIK5+laWzsmnKNTWayci2gN58w7V5uq2daqco480tYKQJapnGvr8ccj9tkn4sEH+3okpR55pPC9Y/jwQmXTttu2bodiPVkMImVRiI5V4Zo8eVYrlXOVhnMWhaht1WxrVTlHHmlrBSDLhHNtnX9+xO9/X1gZ9fHHIwYO7OsRFaQtrR/+cKGyabvtCvdVzrGinlbORaic64zKOTpVjZWWip+/MhaEKN5fW2ttUjkHndPWCkCWaWtt649/LPz+298ifvCDvh1LsXQxiAkTCr/Tyrm5cyOSpE+GRA16992I558v3FY51zuEc3SqryvnutvWmrXKuddei2hu7utRrDwq56BzvdHWKpwDYGVROVdq/vxCxVzqzDMjFizou/EUK66ci4jYYotCVd+bb7aGMfDss4WwdtiwQgt0d6WVc//4R8SiRVUZWm4I5+hUtcO5Sirn3nmn9UpZnivnZsyIGDEi4txz+3okK081F4RQOUce9UZbqznnAFhZhHOl7r+/8Hv8+IgPfjDirbcivv71vh1TRCE0fPHFQjvrf/xHYdvAga0BitZWUsXzzTU0dP911l23cO4bEfHXv/Z8XHkinKNTfbkgRBqs9e8fscYalb1flirnfvnLwu/p0/t2HCtTNdtaVc6RR9paAciy9ByiGm2teQjn0pbWXXZpbWm98sq+XxwibWn9wAdKz7fSeecsCpENSRLx8su9+x7pfHM9aWlNpeGv1tZSwjk61ZdtrcXzzVWazmelcq65OeKeewq3H3+80N5aD6rZ1qpyjjzS1gpAllVj3ur0uXn4jpeGczvtFDFxYsThhxfuH3dc387rtmJLayqdd07lXDZccknEeutFXHpp771HNRaDSKXzzlkUopRwjk7VQuVcpfPNFT+n1ivnHn20NEBMg7q8q2Zbq8o58khbKwBZVs221vfey/bCBAsXRjz2WOH2Rz5S+P2970WstlrE7Nl92z2z4mIQqTScUzmXDWkn1ve/33vzmBe3tfaUyrn2CefoVK1UzlUqK5Vzd9/d+f286o3VWpcvVxlEfmhrBSDLqhnORWS7em727EJgssEGEaNHF7aNHh3x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QkKCdpmEhIRC34u5OivHZGraZ2XGNlKybdmUtWvXioiICOHq6ioefPBBsWXLFoPXld9yS9tycfYjo0eP1u6bAgMDxRNPPCGOHDli8N7FaSMrVqwQTZo00Z5Ptm7dWqxbt87iOqhM2EYqTxsRQiYWREdHCzc3N9GgQQMxbdo0gwuXxsda5upifDx28eJF8cwzzwhvb28RGBgohg4dWmEu8jgIUQVH6yYiIiIiIiIiIioHeLdWIiIiIiIiIiIiO2FwjoiIiIiIiIiIyE4YnCMiIiIiIiIiIrITBueIiIiIiIiIiIjshME5IiIiIiIiIiIiO2FwjoiIiIiIiIiIyE4YnCMiIiIiIiIiIrITBueIiIiIiIiIiIjshME5IiIiIiIiIiIiO2FwjoiIiIgKGTp0KBwcHODg4AAXFxcEBgaia9eu+Oyzz6DRaFSXs2LFCvj7+5deRYmIiIgqOAbniIiIiMikHj16ICMjA2lpadi2bRs6d+6MUaNGoWfPnsjPz7d39YiIiIgqBQbniIiIiMgkNzc31K5dG8HBwWjRogVef/11bNy4Edu2bcOKFSsAAPPnz8fDDz8MLy8vhISEYPjw4cjOzgYAJCUlITY2Frdu3dJm4U2ZMgUAkJOTg3HjxiE4OBheXl6Ijo5GUlKSfT4oERERkR0xOEdEREREqj322GOIiopCYmIiAMDR0RGLFy9GamoqPv/8c+zatQvjx48HALRt2xYLFy6Er68vMjIykJGRgXHjxgEARowYgQMHDmDNmjU4evQonnvuOfTo0QNnz56122cjIiIisgcHIYSwdyWIiIiIqHwZOnQoMjMz8e233xZ6rX///jh69ChOnDhR6LX169cjLi4O//zzDwA55tzo0aORmZmpXeavv/5CgwYN8NdffyEoKEg7v0uXLmjdujWmT59u889DREREVF4527sCRERERFSxCCHg4OAAAPjxxx8xY8YMnDp1Crdv30Z+fj7u37+Pu3fvwtPT0+T/Hzt2DAUFBYiIiDCYn5OTgxo1apR6/YmIiIjKEwbniIiIiMgqJ0+eRP369ZGWloaePXvilVdewbRp01C9enXs27cPw4YNQ25urtngXHZ2NpycnJCcnAwnJyeD17y9vcviIxARERGVGwzOEREREZFqu3btwrFjxzBmzBgkJydDo9Fg3rx5cHSUQxmvXbvWYHlXV1cUFBQYzGvevDkKCgpw9epVtG/fvszqTkRERFQeMThHRERERCbl5OTg8uXLKCgowJUrV7B9+3bMmDEDPXv2RExMDI4fP468vDwsWbIETz31FH7++WcsW7bMoIywsDBkZ2dj586diIqKgqenJyIiIjBw4EDExMRg3rx5aN68Oa5du4adO3eiadOmePLJJ+30iYmIiIjKHu/WSkREREQmbd++HXXq1EFYWBh69OiB3bt3Y/Hixdi4cSOcnJwQFRWF+fPnY9asWXjooYewevVqzJgxw6CMtm3bIi4uDv369UOtWrUwe/ZsAMDy5csRExOD//3vf4iMjESfPn1w+PBh1KtXzx4flYiIiMhueLdWIiIiIiIiIiIiO2HmHBERERERERERkZ0wOEdERERERERERGQnDM4RERERERERERHZCYNzREREREREREREdsLgHBERERERERERkZ0wOEdERERERERERGQnDM4RERERERERERHZCYNzREREREREREREdsLgHBERERERERERkZ0wOEdERERERERERGQnDM4RERERERERERHZyf8BTwMURqWFqyYAAAAASUVORK5CYII=)
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
4.5 Average Bid By Day
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[12\]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
    import matplotlib.pyplot as plt

    query = """
        SELECT 
            create_date DT_REF
            ,round(avg(ask),2) AvgAsk
            ,round(avg(bid),2) Avgbid
        FROM df 
        where not code in ('BTC', 'ETH', 'LTC', 'DOGE')
        group by 1
        order by 1 
    """

    newDf = sqldf(query, locals())
    newDf.sort_values(by='DT_REF', ascending=True, inplace=True)

    cht = newDf.plot(
        kind='line', x='DT_REF', y='Avgbid',
        figsize=(15, 10), 
        legend=False, 
        color='blue', title='Average BID tendence by Day', xlabel='Date', ylabel='Avgbid')

    #exibir o grafico
    plt.show()
:::
:::
:::
:::
:::

::: {.jp-Cell-outputWrapper}
::: {.jp-Collapser .jp-OutputCollapser .jp-Cell-outputCollapser}
:::

::: {.jp-OutputArea .jp-Cell-outputArea}
::: {.jp-OutputArea-child}
::: {.jp-OutputPrompt .jp-OutputArea-prompt}
:::

::: {.jp-RenderedImage .jp-OutputArea-output tabindex="0"}
![No description has been provided for this
image](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABOcAAANXCAYAAAB+DztKAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAADDLUlEQVR4nOzdd5icZbk/8Hs3FQgJoSQhhxhCMfTqT4hIE0wCEcwRpEpRFDgGqSJyDgeDqDQBo1JEQY4SDuVQBEQwFCkSBAKhClICHJWACCTUtJ3fH3Pe3Zlsm5md+s7nc1177ezMOzPPhvBmnu9738/TkslkMgEAAAAAVF1rrQcAAAAAAM1KOAcAAAAANSKcAwAAAIAaEc4BAAAAQI0I5wAAAACgRoRzAAAAAFAjwjkAAAAAqBHhHAAAAADUiHAOAAAAAGpEOAcAQF26/PLLo6WlJV5++eVaD6VPpk+fHi0tLfHmm2/WeigAQB0SzgEAVXfhhRdGS0tLbLPNNrUeSt1Ze+21o6Wlpf1r8ODBsf7668eJJ54Yb731Vt6xXYU+hx56aN7zhwwZEuuss07svffecd1110VbW1tB47j11ltj+vTp5fzVqLCddtqp/b97a2trDB06NMaPHx8HHXRQzJo1q9bDAwC60b/WAwAAms/MmTNj7bXXjoceeiheeOGFWG+99Wo9pLqyxRZbxAknnBARER999FHMmTMnfvSjH8U999wTDz30UK/PHzRoUPziF7+IiIgPP/wwXnnllbj55ptj7733jp122il+85vfxNChQ3t8jVtvvTUuuOACAV2DWWutteKMM86IiIj3338/Xnjhhbj++uvjiiuuiH322SeuuOKKGDBgQI1HCQDkEs4BAFU1b968eOCBB+L666+PI444ImbOnBnf+c53qjqGtra2WLx4cQwePLiq71uof/mXf4kvfelL7T9/9atfjSFDhsQPf/jDeP7552P99dfv8fn9+/fPe35ExPe+970488wz4+STT46vfe1rcfXVV1dk7NTWsGHDOv23P/PMM+Poo4+OCy+8MNZee+0466yzajQ6AKAr2loBgKqaOXNmDB8+PKZMmRJ77713zJw5s/2xJUuWxKqrrhpf/vKXOz1v4cKFMXjw4PjmN7/Zft+iRYviO9/5Tqy33noxaNCgGDNmTHzrW9+KRYsW5T23paUljjrqqJg5c2ZsvPHGMWjQoLjtttsiIuKHP/xhfOpTn4rVVlstVlhhhdh6663jf/7nfzq9/4cffhhHH310rL766rHyyivHnnvuGX/729+ipaWlU3XZ3/72t/jKV74SI0eOjEGDBsXGG28cl112WV/+2GLUqFERkQ3eSvXtb387Jk6cGNdee2385S9/6fa4Qw89NC644IKIiLwW2URbW1v86Ec/io033jgGDx4cI0eOjCOOOCLefvvtvNdZe+2143Of+1zcf//98clPfjIGDx4c66yzTvzqV7/q9J5PP/10fOYzn4kVVlgh1lprrfje977XbQvu7373u9h+++1jpZVWipVXXjmmTJkSTz/9dKffYciQIfG3v/0tpk6dGkOGDIk11lgjvvnNb8ayZcvyjm1ra4sZM2bEpptuGoMHD4411lgjJk+eHI888kjecVdccUVsvfXWscIKK8Sqq64a++23X/zv//5vt3+Oy3vzzTdjn332iaFDh8Zqq60WxxxzTHz00Uftj++4446x+eabd/nc8ePHx6RJkwp+r1z9+vWLH//4x7HRRhvFT3/601iwYEH7Y7/85S/jM5/5TIwYMSIGDRoUG220UVx00UV5zz/kkENi9dVXjyVLlnR67YkTJ8b48eNLGhcAkCWcAwCqaubMmfGFL3whBg4cGPvvv388//zz8fDDD0dExIABA+Jf//Vf48Ybb4zFixfnPe/GG2+MRYsWxX777RcR2UBlzz33jB/+8Iexxx57xE9+8pOYOnVqnH/++bHvvvt2et+77rorjjvuuNh3331jxowZsfbaa0dExIwZM2LLLbeM7373u/GDH/wg+vfvH1/84hfjt7/9bd7zDz300PjJT34Su+++e5x11lmxwgorxJQpUzq9z+uvvx7bbrtt3HHHHXHUUUfFjBkzYr311ovDDjssfvSjHxX0Z7RkyZJ48803480334y//vWvcfPNN8d5550XO+ywQ4wbN66g1+jOQQcdFJlMpsc1yI444oj47Gc/GxERv/71r9u/ch8/8cQTY7vttosZM2bEl7/85Zg5c2ZMmjSpU4DzwgsvxN577x2f/exn49xzz43hw4fHoYcemhemzZ8/P3beeeeYO3dufPvb345jjz02fvWrX8WMGTM6je3Xv/51TJkyJYYMGRJnnXVW/Od//mc888wz8elPf7rTxhHLli2LSZMmxWqrrRY//OEPY8cdd4xzzz03LrnkkrzjDjvssDj22GNjzJgxcdZZZ8W3v/3tGDx4cDz44IPtx3z/+9+Pgw8+ONZff/0477zz4thjj40777wzdthhh3jnnXd6/XOPiNhnn33io48+ijPOOCN23333+PGPfxyHH354++MHHXRQPPHEE/HUU0/lPe/hhx+Ov/zlL50q4orRr1+/2H///eODDz6I+++/v/3+iy66KMaOHRv//u//Hueee26MGTMmvv71r7eHs8m4/vnPf8btt9+e95rz58+Pu+66q0/jAgAiIgMAUCWPPPJIJiIys2bNymQymUxbW1tmrbXWyhxzzDHtx9x+++2ZiMjcfPPNec/dfffdM+uss077z7/+9a8zra2tmfvuuy/vuIsvvjgTEZk//vGP7fdFRKa1tTXz9NNPdxrTBx98kPfz4sWLM5tssknmM5/5TPt9c+bMyURE5thjj8079tBDD81EROY73/lO+32HHXZYZs0118y8+eabecfut99+mWHDhnV6v+WNHTs2ExGdvrbbbrtOr/md73wnExGZf/zjH+33HXLIIZmVVlqp29d/7LHHMhGROe6443ocx7Rp0zJdfVS87777MhGRmTlzZt79t912W6f7k9/l3nvvbb/vjTfeyAwaNChzwgkntN937LHHZiIi86c//SnvuGHDhmUiIjNv3rxMJpPJvPvuu5lVVlkl87WvfS3vvefPn58ZNmxY3v2HHHJIJiIy3/3ud/OO3XLLLTNbb711+8933XVXJiIyRx99dKffta2tLZPJZDIvv/xypl+/fpnvf//7eY8/+eSTmf79+3e6f3nJf6c999wz7/6vf/3rmYjIPP7445lMJpN55513MoMHD86cdNJJeccdffTRmZVWWinz3nvv9fg+O+64Y2bjjTfu9vEbbrghExGZGTNmtN/X1d/HSZMm5f2/tmzZssxaa62V2XffffOOO++88zItLS2Zl156qcdxAQA9UzkHAFTNzJkzY+TIkbHzzjtHRLZlct99942rrrqqvdXwM5/5TKy++up5a6K9/fbbMWvWrLyKuGuvvTY23HDD2GCDDdqrzN588834zGc+ExERd999d95777jjjrHRRht1GtMKK6yQ9z4LFiyI7bffPh599NH2+5MW2K9//et5z/3GN76R93Mmk4nrrrsu9thjj8hkMnnjmjRpUixYsCDvdbuzzTbbxKxZs2LWrFlxyy23xPe///14+umnY88994wPP/yw1+f3ZMiQIRER8e6775b0/GuvvTaGDRsWn/3sZ/N+v6233jqGDBnS6c99o402iu2337795zXWWCPGjx8fL730Uvt9t956a2y77bbxyU9+Mu+4Aw88MO+1Zs2aFe+8807sv//+ee/dr1+/2GabbTq9d0TEkUcemffz9ttvn/fe1113XbS0tHS57mHSynv99ddHW1tb7LPPPnnvO2rUqFh//fW7fN+uTJs2Le/n5O/PrbfeGhHZ9eI+//nPx3//939HJpOJiGz139VXXx1Tp06NlVZaqaD36U5X/+1z//4vWLAg3nzzzdhxxx3jpZdeam9/bW1tjQMPPDBuuummvOfOnDkzPvWpT/W5mhMAmp0NIQCAqli2bFlcddVVsfPOO8e8efPa799mm23i3HPPjTvvvDMmTpwY/fv3j7322iuuvPLKWLRoUQwaNCiuv/76WLJkSV449/zzz8ef//znWGONNbp8vzfeeCPv5+4ChFtuuSW+973vxdy5c/PWqstdY+2VV16J1tbWTq+x/C6z//jHP+Kdd96JSy65pFPrZHfj6srqq68eu+66a/vPU6ZMifHjx8fee+8dv/jFLzqFgsV47733IiJi5ZVXLun5zz//fCxYsCBGjBjR5ePL/34f+9jHOh0zfPjwvPXpXnnlldhmm206Hbf8WmbPP/98RER7ALu85XegTdaP6+m9X3zxxRg9enSsuuqqXb5m8r6ZTKbbjTgK3f10+eevu+660dramteOe/DBB8fVV18d9913X+ywww5xxx13xOuvvx4HHXRQQe/Rk67+2//xj3+M73znOzF79uz44IMP8o5fsGBBDBs2rH1cZ511Vtxwww1x8MEHx3PPPRdz5syJiy++uM/jAoBmJ5wDAKrirrvuitdeey2uuuqquOqqqzo9PnPmzJg4cWJEROy3337xs5/9LH73u9/F1KlT45prrokNNtggb7H8tra22HTTTeO8887r8v3GjBmT93NuhVDivvvuiz333DN22GGHuPDCC2PNNdeMAQMGxC9/+cu48sori/4dkw0MvvSlL8UhhxzS5TGbbbZZ0a8bEbHLLrtERMS9997bp3AuWc9s+WCxUG1tbTFixIi8jTxyLR+G9evXr8vjksqwYt87IrvuXLJBRq7lN8vo7r1Led+Wlpb43e9+1+VrJhVpxcoNgBOTJk2KkSNHxhVXXBE77LBDXHHFFTFq1Ki8sLZUy/+3f/HFF2OXXXaJDTbYIM4777wYM2ZMDBw4MG699dY4//zz8zbk2GijjWLrrbeOK664Ig4++OC44oorYuDAgbHPPvv0eVwA0OyEcwBAVcycOTNGjBiRt9B84vrrr48bbrghLr744lhhhRVihx12iDXXXDOuvvrq+PSnPx133XVX/Md//Efec9Zdd914/PHHY5ddduky5CjEddddF4MHD47bb789Bg0a1H7/L3/5y7zjxo4dG21tbTFv3ry86qcXXngh77g11lgjVl555Vi2bFlZwpRcS5cujYiO6qdS/frXv46Wlpb2DR+6092f6brrrht33HFHbLfddl0GnqUYO3Zse1Vcrueee67Te0dEjBgxomx/vuuuu27cfvvt8dZbb3VbPbfuuutGJpOJcePGxcc//vGS3+v555/Pq7584YUXoq2trX1zkohsoHjAAQfE5ZdfHmeddVbceOON8bWvfa3PQeOyZcviyiuvjBVXXDE+/elPR0TEzTffHIsWLYqbbropr8Kxuzbdgw8+OI4//vh47bXX4sorr4wpU6bE8OHD+zQuAMBurQBAFXz44Ydx/fXXx+c+97nYe++9O30dddRR8e6778ZNN90UEdk1rvbee++4+eab49e//nUsXbq00w6s++yzT/ztb3+Ln//8512+3/vvv9/ruPr16xctLS3t691FRLz88stx44035h03adKkiIi48MIL8+7/yU9+0un19tprr7juuus67bgZkW17LdXNN98cEZFXPVisM888M37/+9/Hvvvu222LZiJZ32z5nUj32WefWLZsWZx++umdnrN06dKCdy7Ntfvuu8eDDz4YDz30UPt9//jHPzpV502aNCmGDh0aP/jBDzrtCps8p1h77bVXZDKZOO200zo9llT3feELX4h+/frFaaed1qniL5PJxD//+c+C3mv5YDr5+7Pbbrvl3X/QQQfF22+/HUcccUS89957fd4NddmyZXH00UfHn//85zj66KPb23+TwC/3d1qwYEGncDqx//77R0tLSxxzzDHx0ksv2aUVAMpE5RwAUHHJQvJ77rlnl49vu+22scYaa8TMmTPbQ7h99903fvKTn8R3vvOd2HTTTWPDDTfMe85BBx0U11xzTRx55JFx9913x3bbbRfLli2LZ599Nq655pq4/fbb4xOf+ESP45oyZUqcd955MXny5DjggAPijTfeiAsuuCDWW2+9eOKJJ9qP23rrrWOvvfaKH/3oR/HPf/4ztt1227jnnnviL3/5S0TkV5mdeeaZcffdd8c222wTX/va12KjjTaKt956Kx599NG444474q233ur1z+tvf/tbXHHFFRERsXjx4nj88cfjZz/7Way++uoFtbQuXbq0/fkfffRRvPLKK3HTTTfFE088ETvvvHO36+Hl2nrrrSMi4uijj45JkyZFv379Yr/99osdd9wxjjjiiDjjjDNi7ty5MXHixBgwYEA8//zzce2118aMGTNi77337vX1c33rW9+KX//61zF58uQ45phjYqWVVopLLrkkxo4dm/ffYejQoXHRRRfFQQcdFFtttVXst99+scYaa8Srr74av/3tb2O77baLn/70p0W998477xwHHXRQ/PjHP47nn38+Jk+eHG1tbXHffffFzjvvHEcddVSsu+668b3vfS9OPvnkePnll2Pq1Kmx8sorx7x58+KGG26Iww8/PL75zW/2+l7z5s2LPffcMyZPnhyzZ8+OK664Ig444IBOgeuWW24Zm2yySfumJ1tttVXBv8+CBQva/9t/8MEH8cILL8T1118fL774Yuy33355oerEiRNj4MCBsccee7QHgT//+c9jxIgR8dprr3V67TXWWCMmT54c1157bayyyioxZcqUgscFAPSgRrvEAgBNZI899sgMHjw48/7773d7zKGHHpoZMGBA5s0338xkMplMW1tbZsyYMZmIyHzve9/r8jmLFy/OnHXWWZmNN944M2jQoMzw4cMzW2+9dea0007LLFiwoP24iMhMmzaty9e49NJLM+uvv35m0KBBmQ022CDzy1/+MvOd73wns/zHpPfffz8zbdq0zKqrrpoZMmRIZurUqZnnnnsuExGZM888M+/Y119/PTNt2rTMmDFjMgMGDMiMGjUqs8suu2QuueSSXv+sxo4dm4mI9q/W1tbMiBEjMvvvv3/mhRdeyDs2Gec//vGP9vsOOeSQvOevuOKKmbXXXjuz1157Zf7nf/4ns2zZsl7HkMlkMkuXLs184xvfyKyxxhqZlpaWTn8el1xySWbrrbfOrLDCCpmVV145s+mmm2a+9a1vZf7+97/n/S5Tpkzp9No77rhjZscdd8y774knnsjsuOOOmcGDB2f+5V/+JXP66adnLr300kxEZObNm5d37N13352ZNGlSZtiwYZnBgwdn1l133cyhhx6aeeSRR/L+HFZaaaVO793Vf9ulS5dmzjnnnMwGG2yQGThwYGaNNdbI7Lbbbpk5c+bkHXfddddlPv3pT2dWWmmlzEorrZTZYIMNMtOmTcs899xzPf5ZJu/5zDPPZPbee+/MyiuvnBk+fHjmqKOOynz44YddPufss8/ORETmBz/4QY+vnWvHHXfM+28/ZMiQzPrrr5/50pe+lPn973/f5XNuuummzGabbZYZPHhwZu21186cddZZmcsuu6zLP/dMJpO55pprMhGROfzwwwseFwDQs5ZMpoTVeAEAiLlz58aWW24ZV1xxRRx44IG1Hg4pMmPGjDjuuOPi5Zdf7nLH21r5zW9+E1OnTo177703tt9++1oPBwBSQTgHAFCADz/8sNMGCIceemj8+te/jpdffrnT7rBQqkwmE5tvvnmsttpq3W7OUCuf+9zn4s9//nO88MILJW/EAgDks+YcAEABzj777JgzZ07svPPO0b9///jd734Xv/vd7+Lwww8XzFEW77//ftx0001x9913x5NPPhm/+c1vaj2kdldddVU88cQT8dvf/jZmzJghmAOAMlI5BwBQgFmzZsVpp50WzzzzTLz33nvxsY99LA466KD4j//4j+jf3/VO+u7ll1+OcePGxSqrrBJf//rX4/vf/36th9SupaUlhgwZEvvuu29cfPHF/s4DQBkJ5wAAAACgRlprPQAAAAAAaFbCOQAAAACoEYtFlElbW1v8/e9/j5VXXtkCuQAAAABNLpPJxLvvvhujR4+O1tbu6+OEc2Xy97//3U5tAAAAAOT53//931hrrbW6fVw4VyYrr7xyRGT/wIcOHVrj0QAAAABQSwsXLowxY8a0Z0bdEc6VSdLKOnToUOEcAAAAABERvS5/ZkMIAAAAAKgR4RwAAAAA1IhwDgAAAABqRDgHAAAAADUinAMAAACAGhHOAQAAAECNCOcAAAAAoEaEcwAAAABQI8I5AAAAAKgR4RwAAAAA1IhwDgAAAABqRDgHAAAAADUinAMAAACAGhHOAQAAAECNCOcAAAAAoEZqGs7de++9sccee8To0aOjpaUlbrzxxrzHW1pauvw655xz2o9Ze+21Oz1+5pln5r3OE088Edtvv30MHjw4xowZE2effXansVx77bWxwQYbxODBg2PTTTeNW2+9tSK/MwAAAAAkahrOvf/++7H55pvHBRdc0OXjr732Wt7XZZddFi0tLbHXXnvlHffd734377hvfOMb7Y8tXLgwJk6cGGPHjo05c+bEOeecE9OnT49LLrmk/ZgHHngg9t9//zjssMPisccei6lTp8bUqVPjqaeeqswvDgAAAAAR0ZLJZDK1HkREtkruhhtuiKlTp3Z7zNSpU+Pdd9+NO++8s/2+tddeO4499tg49thju3zORRddFP/xH/8R8+fPj4EDB0ZExLe//e248cYb49lnn42IiH333Tfef//9uOWWW9qft+2228YWW2wRF198cUHjX7hwYQwbNiwWLFgQQ4cOLeg5AAAAAKRToVlRw6w59/rrr8dvf/vbOOywwzo9duaZZ8Zqq60WW265ZZxzzjmxdOnS9sdmz54dO+ywQ3swFxExadKkeO655+Ltt99uP2bXXXfNe81JkybF7Nmzux3PokWLYuHChXlfAAAAAFCM/rUeQKH+67/+K1ZeeeX4whe+kHf/0UcfHVtttVWsuuqq8cADD8TJJ58cr732Wpx33nkRETF//vwYN25c3nNGjhzZ/tjw4cNj/vz57fflHjN//vxux3PGGWfEaaedVo5fDQAAAIAm1TDh3GWXXRYHHnhgDB48OO/+448/vv32ZpttFgMHDowjjjgizjjjjBg0aFDFxnPyySfnvffChQtjzJgxFXs/AAAAANKnIcK5++67L5577rm4+uqrez12m222iaVLl8bLL78c48ePj1GjRsXrr7+ed0zy86hRo9q/d3VM8nhXBg0aVNHwDwAAAID0a4g15y699NLYeuutY/PNN+/12Llz50Zra2uMGDEiIiImTJgQ9957byxZsqT9mFmzZsX48eNj+PDh7cfkbjKRHDNhwoQy/hYAAAAAkK+m4dx7770Xc+fOjblz50ZExLx582Lu3Lnx6quvth+zcOHCuPbaa+OrX/1qp+fPnj07fvSjH8Xjjz8eL730UsycOTOOO+64+NKXvtQevB1wwAExcODAOOyww+Lpp5+Oq6++OmbMmJHXknrMMcfEbbfdFueee248++yzMX369HjkkUfiqKOOquwfAAAAAABNrSWTyWRq9eZ/+MMfYuedd+50/yGHHBKXX355RERccsklceyxx8Zrr70Ww4YNyzvu0Ucfja9//evx7LPPxqJFi2LcuHFx0EEHxfHHH5/XcvrEE0/EtGnT4uGHH47VV189vvGNb8RJJ52U91rXXnttnHLKKfHyyy/H+uuvH2effXbsvvvuBf8uhW6PCwAAAED6FZoV1TScSxPhHAAAAACJQrOihlhzDgAAAADSSDgHAAAAADUinAMAAACAGhHOAQAAAECNCOcAoEG9/37Eww9H2NoJAAAal3AOABrUMcdEfPKTEXfeWeuRAAAApRLOAUCDevXV/O8AAEDjEc4BQINatiz/OwAA0HiEcwDQoJYuzf8OAAA0HuEcADQo4RwAADQ+4RwANChtrQAA0PiEcwDQoFTOAQBA4xPOAUCDEs4BAEDjE84BQIPS1goAAI1POAcADUrlHAAAND7hHAA0KOEcAAA0PuEcADQoba0AAND4hHMA0KBUzgEAQOMTzgFAgxLOAQBA4xPOAUCD0tYKAACNTzgHAA1K5RwAADQ+4RwANCjhHAAAND7hHAA0KG2tAADQ+IRzANCgVM4BAEDjE84BQIMSzgEAQOMTzgFAA8pkOtpZhXMAANC4hHMA0IDa2jpuW3MOAAAal3AOABpQbrWcyjkAAGhcwjkAaEDCOQAASAfhHAA0oNxWVm2tAADQuIRzANCAVM4BAEA6COcAoAEJ5wAAIB2EcwDQgLS1AgBAOgjnAKABqZwDAIB0EM4BQAMSzgEAQDoI5wCgAWlrBQCAdBDOAUADUjkHAADpIJwDgAYknAMAgHQQzgFAA9LWCgAA6SCcA4AGpHIOAADSQTgHAA1IOAcAAOkgnAOABqStFQAA0kE4BwANSOUcAACkg3AOABqQcA4AANJBOAcADUhbKwAApINwDgAakMo5AABIB+EcADQg4RwAAKSDcA4AGlBuK6twDgAAGpdwDgAaUG4gZ805AABoXMI5AGhAy4dzmUztxgIAAJROOEef/eUvEY89VutRADSX5VtZVc8BAEBj6l/rAdD4dtop4u23I954I2LllWs9GoDmsHwYt2xZRH//qgMAQMNROUefZDIRr70W8dFHEe+8U+vRADSP5SvnbAoBAACNSThHn9gtEKA2hHMAAJAOwjn6JHcyaGIIUD1dtbUCAACNRzhHnwjnAGpD5RwAAKSDcI4+Ec4B1IZwDgAA0kE4R58I5wBqQ1srAACkg3COPhHOAdSGyjkAAEgH4Rx9YrdWgNoQzgEAQDoI5+gTlXMAtaGtFQAA0kE4R58I5wBqQ+UcAACkg3COPsmdDC5ZUrtxADQb4RwAAKSDcI4+UTkHUBvaWgEAIB2Ec/SJcA6gNlTOAQBAOgjn6BPhHEBtCOcAACAdhHP0iXAOoDa0tQIAQDoI5+gT4RxAbaicAwCAdBDO0SfCOYDaEM4BAEA6COfoE+EcQG1oawUAgHQQztEnwjmA2lA5BwAA6SCco0+EcwC1IZwDAIB0EM7RJ8I5gNpYvo3VORgAABqTcI4+Ec4B1Mby51xrzgEAQGMSztEnwjmA2tDWCgAA6SCco0+EcwC1IZwDAIB0EM7RJ7ltVCaGANWzfBurtlYAAGhMwjn6ROUcQG2onAMAgHQQztEnwjmA2kjOuS0t+T8DAACNRThHnwjnAGojaWMdPDj/ZwAAoLEI5+gT4RxAbSTn3EGD8n8GAAAai3COPhHOAdRGcs5NKuecgwEAoDEJ5+iT3MngkiW1GwdAs0naWJPKOW2tAADQmIRz9InKOYDa0NYKAADpIJyjT4RzALWhrRUAANJBOEefCOcAakNbKwAApINwjj4RzgHUhrZWAABIB+EcfSKcA6gNba0AAJAOwjn6RDgHUBvaWgEAIB2Ec/SJcA6gNrS1AgBAOgjn6BPhHEBtaGsFAIB0qGk4d++998Yee+wRo0ePjpaWlrjxxhvzHj/00EOjpaUl72vy5Ml5x7z11ltx4IEHxtChQ2OVVVaJww47LN577728Y5544onYfvvtY/DgwTFmzJg4++yzO43l2muvjQ022CAGDx4cm266adx6661l/33TSDgHUBvaWgEAIB1qGs69//77sfnmm8cFF1zQ7TGTJ0+O1157rf3rv//7v/MeP/DAA+Ppp5+OWbNmxS233BL33ntvHH744e2PL1y4MCZOnBhjx46NOXPmxDnnnBPTp0+PSy65pP2YBx54IPbff/847LDD4rHHHoupU6fG1KlT46mnnir/L50yuZNB4RxA9WhrBQCAdOhfyzffbbfdYrfdduvxmEGDBsWoUaO6fOzPf/5z3HbbbfHwww/HJz7xiYiI+MlPfhK77757/PCHP4zRo0fHzJkzY/HixXHZZZfFwIEDY+ONN465c+fGeeed1x7izZgxIyZPnhwnnnhiREScfvrpMWvWrPjpT38aF198cRl/4/RROQdQG9paAQAgHep+zbk//OEPMWLEiBg/fnz827/9W/zzn/9sf2z27NmxyiqrtAdzERG77rprtLa2xp/+9Kf2Y3bYYYcYOHBg+zGTJk2K5557Lt5+++32Y3bddde89500aVLMnj2723EtWrQoFi5cmPfVjIRzALWxfFurczAAADSmug7nJk+eHL/61a/izjvvjLPOOivuueee2G233WLZ/81I5s+fHyNGjMh7Tv/+/WPVVVeN+fPntx8zcuTIvGOSn3s7Jnm8K2eccUYMGzas/WvMmDF9+2UblHAOoPra2rJfEdacAwCARlfTttbe7Lfffu23N91009hss81i3XXXjT/84Q+xyy671HBkESeffHIcf/zx7T8vXLiwKQM64RxA9eUGcdpaAQCgsdV15dzy1llnnVh99dXjhRdeiIiIUaNGxRtvvJF3zNKlS+Ott95qX6du1KhR8frrr+cdk/zc2zHdrXUXkV0Lb+jQoXlfzUg4B1B9uedbba0AANDYGiqc++tf/xr//Oc/Y80114yIiAkTJsQ777wTc+bMaT/mrrvuira2tthmm23aj7n33ntjyZIl7cfMmjUrxo8fH8OHD28/5s4778x7r1mzZsWECRMq/Ss1POEcQPXlVs5pawUAgMZW03Duvffei7lz58bcuXMjImLevHkxd+7cePXVV+O9996LE088MR588MF4+eWX484774zPf/7zsd5668WkSZMiImLDDTeMyZMnx9e+9rV46KGH4o9//GMcddRRsd9++8Xo0aMjIuKAAw6IgQMHxmGHHRZPP/10XH311TFjxoy8ltRjjjkmbrvttjj33HPj2WefjenTp8cjjzwSRx11VNX/TBqNcA6g+nLPt9paAQCgsdU0nHvkkUdiyy23jC233DIiIo4//vjYcsst49RTT41+/frFE088EXvuuWd8/OMfj8MOOyy23nrruO+++2JQUiYQETNnzowNNtggdtlll9h9993j05/+dFxyySXtjw8bNix+//vfx7x582LrrbeOE044IU499dQ4/PDD24/51Kc+FVdeeWVccsklsfnmm8f//M//xI033hibbLJJ9f4wGpRwDqD6hHMAAJAeLZlMJlPrQaTBwoULY9iwYbFgwYKmWn9uxx0j7r03e3uttSL+939rOx6AZvD66xHJsqhXXx2x774RO+0UcffdNR0WAACQo9CsqKHWnKP+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MX369Ljkkkvaj3nggQdi//33j8MOOywee+yxmDp1akydOjWeeuqpyvziKZBM/rpqqzIxBKicrsK51tbOjwMAAI2hf++HVM5uu+0Wu+22W5ePDRs2LGbNmpV3309/+tP45Cc/Ga+++mp87GMfa79/5ZVXjlGjRnX5OjNnzozFixfHZZddFgMHDoyNN9445s6dG+edd14cfvjhERExY8aMmDx5cpx44okREXH66afHrFmz4qc//WlcfPHF5fhVU0dbK0BtdLXmXEtL9udly7S1AgBAo2moNecWLFgQLS0tscoqq+Tdf+aZZ8Zqq60WW265ZZxzzjmxNCcdmj17duywww4xcODA9vsmTZoUzz33XLz99tvtx+y66655rzlp0qSYPXt2t2NZtGhRLFy4MO+rmQjnAGqjq/Nv7s/OwQAA0FhqWjlXjI8++ihOOumk2H///WPo0KHt9x999NGx1VZbxaqrrhoPPPBAnHzyyfHaa6/FeeedFxER8+fPj3HjxuW91siRI9sfGz58eMyfP7/9vtxj5s+f3+14zjjjjDjttNPK9es1HOEcQG30FM4tWuQcDAAAjaYhwrklS5bEPvvsE5lMJi666KK8x44//vj225tttlkMHDgwjjjiiDjjjDNi0KBBFRvTySefnPfeCxcujDFjxlTs/eqNcA6gNrpqa839WVsrAAA0lroP55Jg7pVXXom77rorr2quK9tss00sXbo0Xn755Rg/fnyMGjUqXn/99bxjkp+Tdeq6O6a7dewiIgYNGlTR8K/eCecAakNbKwAApEtdrzmXBHPPP/983HHHHbHaaqv1+py5c+dGa2trjBgxIiIiJkyYEPfee28sWbKk/ZhZs2bF+PHjY/jw4e3H3HnnnXmvM2vWrJgwYUIZf5t06Smcy/mjBqDMhHMAAJAuNa2ce++99+KFF15o/3nevHkxd+7cWHXVVWPNNdeMvffeOx599NG45ZZbYtmyZe1rwK266qoxcODAmD17dvzpT3+KnXfeOVZeeeWYPXt2HHfccfGlL32pPXg74IAD4rTTTovDDjssTjrppHjqqadixowZcf7557e/7zHHHBM77rhjnHvuuTFlypS46qqr4pFHHolLLrmkun8gDUTlHEBtaGsFAIB0qWk498gjj8TOO+/c/nOyhtshhxwS06dPj5tuuikiIrbYYou85919992x0047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MU888URsv/32MXjw4BgzZkycffbZncZy7bXXxgYbbBCDBw+OTTfdNG699day/75poXIOoDaEcwAAkD41Defef//92HzzzeOCCy7o8vGzzz47fvzjH8fFF18cf/rTn2KllVaKSZMmxUcffdR+zIEHHhhPP/10zJo1K2655Za499574/DDD29/fOHChTFx4sQYO3ZszJkzJ84555yYPn16XHLJJe3HPPDAA7H//vvHYYcdFo899lhMnTo1pk6dGk899VTlfvkGJpwDqA1trQAAkD7dXHuvjt122y122223Lh/LZDLxox/9KE455ZT4/Oc/HxERv/rVr2LkyJFx4403xn777Rd//vOf47bbbouHH344PvGJT0RExE9+8pPYfffd44c//GGMHj06Zs6cGYsXL47LLrssBg4cGBtvvHHMnTs3zjvvvPYQb8aMGTF58uQ48cQTIyLi9NNPj1mzZsVPf/rTuPjii6vwJ9FYkuCtq8mhcA6gclTOAQBA+tTtmnPz5s2L+fPnx6677tp+37Bhw2KbbbaJ2bNnR0TE7NmzY5VVVmkP5iIidt1112htbY0//elP7cfssMMOMXDgwPZjJk2aFM8991y8/fbb7cfkvk9yTPI+XVm0aFEsXLgw76tZqJwDqA3hHAAApE/dhnPz58+PiIiRI0fm3T9y5Mj2x+bPnx8jRozIe7x///6x6qqr5h3T1Wvkvkd3xySPd+WMM86IYcOGtX+NGTOm2F+xYRUSzrW1Zb8AKJ9C21qFcwAA0DjqNpyrdyeffHIsWLCg/et///d/az2kqikknMs9DoDyKLRyzppzAADQOOo2nBs1alRERLz++ut597/++uvtj40aNSreeOONvMeXLl0ab731Vt4xXb1G7nt0d0zyeFcGDRoUQ4cOzftqFsI5gNrQ1goAAOlTt+HcuHHjYtSoUXHnnXe237dw4cL405/+FBMmTIiIiAkTJsQ777wTc+bMaT/mrrvuira2tthmm23aj7n33ntjyZIl7cfMmjUrxo8fH8OHD28/Jvd9kmOS9yGfcA6gNrS1AgBA+tQ0nHvvvfdi7ty5MXfu3IjIbgIxd+7cePXVV6OlpSWOPfbY+N73vhc33XRTPPnkk3HwwQfH6NGjY+rUqRERseGGG8bkyZPja1/7Wjz00EPxxz/+MY466qjYb7/9YvTo0RERccABB8TAgQPj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eSXuuOOO+OpXv9rjcdtss01ERLzwwgsRETFq1Kh4/fXX845Jfk7WqevumKFDh3ZZNRcRMWjQoBg6dGjeV9oJ56iGpDqupaWjpTVZZ07lHM2qmGUFll9zDgAAqG8NE8798pe/jBEjRsSUKVN6PG7u3LkREbHmmmtGRMSECRPiySefjDfeeKP9mFmzZsXQoUNjo402aj/mzjvvzHudWbNmxYQJE8r4GzS+YsK5JFQRzlGs3M0gkqUlkwo6lXM0q2LOv62tHf/vOAcDAED9a4hwrq2tLX75y1/GIYccEv1zZiYvvvhinH766TFnzpx4+eWX46abboqDDz44dthhh9hss80iImLixImx0UYbxUEHHRSPP/543H777XHKKafEtGnTYtD/zfiPPPLIeOmll+Jb3/pWPPvss3HhhRfGNddcE8cdd1xNft96pXKOasgN5xIq52h2xbS15h7nHAwAAPWvIcK5O+64I1599dX4yle+knf/wIED44477oiJEyfGBhtsECeccELstddecfPNN7cf069fv7jllluiX79+MWHChPjSl74UBx98cHz3u99tP2bcuHHx29/+NmbNmhWbb755nHvuufGLX/wiJk2aVLXfsREI56iGJIBLArkIlXNQTFtr7nHaWgEAoP41xIYQEydOjEwm0+n+MWPGxD333NPr88eOHRu33nprj8fstNNO8dhjj5U8xmYgnKMaVM5BZ8Wcf3OPcw4GAID61xCVc9QH4RzVoHIOOtPWCgAA6SWco2DCOaqhq8q55LbKOZqVtlYAAEgv4RwFE85RDT21taqco1lpawUAgPQSzlGwYtqqTAwpVU9trSrnaFbCOQAASC/hHAVTOUc1qJyDzpKLI9paAUiL//iPiMmTzRcAIhpkt1bqg3COakgCOBtCQAeVcwCkzUUXRbz9dsSf/xyx6aa1Hg1Abamco2DCOaohaV3tqnJOWyvNSjgHQNp88EH2+4cf1nYcAPVAOEfBhHNUQ0+7taqco1mV2tbqHAxAPWpr6/hcJ5wDEM5RhFLCuSVLKjce0qmrDSFUztHsSq2cs+YcAPUo9zOdcA5AOEcRkslhIZUbKucolco56ExbKwBpkhvOufgKIJyjCNpaqYaedmv14Y1mpa0VgDTJrZZTOQcgnKMIwjmqoau2VpVzNDttrQCkiXAOIJ9wjoIJ56gGlXPQmbZWANJE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+umnx0knnRTTp0+PgQMHxsUXXxzjxo2Lc889NyIiNtxww7j//vvj/PPPj0mTJlX1d61npYZzAwbkPx+6U8yGEBHZMG/FFSs7JqgHLo4AkBbCOYCu1X3l3PPPPx+jR4+OddZZJw488MB49dVXIyJizpw5sWTJkth1113bj91ggw3iYx/7WMyePTsiImbPnh2bbrppjBw5sv2YSZMmxcKFC+Ppp59uPyb3NZJjktfozqJFi2LhwoV5X2lmckilFVM5F2FNEpqHtlYA0iCTEc4BdKeuw7ltttkmLr/88rjtttvioosuinnz5sX2228f7777bsyfPz8GDhwYq6yySt5zRo4cGfPnz4+IiPnz5+cFc8njyWM9HbNw4cL4sId/Hc4444wYNmxY+9eYMWP6+uvWtVLbqkwOKVQhG0L07x/R2pp/PKSdtlYA0mDp0oi2tuzt5T/vJT+7+Ao0q7pua91tt93ab2+22WaxzTbbxNixY+Oaa66JFZa/3FJlJ598chx//PHtPy9cuDDVAZ3KOSqprS1iyZLs7Z4q51paso9/+KFwjubh/AtAGuTWPaicA8hX15Vzy1tllVXi4x//eLzwwgsxatSoWLx4cbzzzjt5x7z++uvta9SNGjWq0+6tyc+9HTN06NAeA8BBgwbF0KFD877SzOSQSsoN2noK5yJcWaX5OP8CkAa5wdvylXPCOaDZNVQ4995778WLL74Ya665Zmy99dYxYMCAuPPOO9sff+655+LVV1+NCRMmRETEhAkT4sknn4w33nij/ZhZs2bF0KFDY6ONNmo/Jvc1kmOS1yDL5JBKyg3nemprjegI71TO0SySttRS21qdfwGoB0nwNnhwthsil3AOaHZ1Hc5985vfjHvuuSdefvnleOCBB+Jf//Vfo1+/frH//vvHsGHD4rDDDovjjz8+7r777pgzZ058+ctfjgkTJsS2224bERETJ06MjTbaKA466KB4/PHH4/bbb49TTjklpk2bFoP+b4Z/5JFHxksvvRTf+ta34tlnn40LL7wwrrnmmjjuuONq+avXHeEclZRUwbW09P53TOUczaav519rzgFQD5LPbl1diPX5Dmh2db3m3F//+tfYf//945///GesscYa8elPfzoefPDBWGONNSIi4vzzz4/W1tbYa6+9YtGiRTFp0qS48MIL25/fr1+/uOWWW+Lf/u3fYsKE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LeL000+Pk046KaZPnx4DBw6Miy++OMaNGxfnnntuRERsuOGGcf/998f5558fkyZNqtwv2ADqbXK4/HpzubeFc42nHGvOtbVl/2715e8o1KOk2k1bKwCNSlsrQGHqunJueQsWLIiIiFVzy6YiYubMmbH66qvHJptsEieffHJ88MEH7Y/Nnj07Nt100xg5cmT7fZMmTYqFCxfG008/3X7MrrvumveakyZNitmzZ3c7lkWLFsXChQvzvtKokcK5pOWVxlGO3VojXFklnbS1AtDohHMAhWmYWpO2trY49thjY7vttotNNtmk/f4DDjggxo4dG6NHj44nnngiTjrppHjuuefi+uuvj4iI+fPn5wVzEdH+8/z583s8ZuHChfHhhx/GCl38a3LGGWfEaaedVtbfsR6VY0FylXN0py9trbnPWbQoYsiQ8owJ6kW9XRwBgGIJ5wAK0zDh3LRp0+Kpp56K+++/P+/+ww8/vP32pptuGmuuuWbssssu8eKLL8a6665bsfGcfPLJcfzxx7f/vHDhwhgzZkzF3q9W6m1y2FM49/bb2RbH1oaqB21ufamc69cv+7Vsmco50klbKwCNLvmMVsqGED7fAc2kIWKMo446Km655Za4++67Y6211urx2G222SYiIl544YWIiBg1alS8/vrrecckPyfr1HV3zNChQ7usmouIGDRoUAwdOjTvK40aIZxLupzb2iLeeafv70H19KVyLqLjw5sdW0mjcp5/I7LnSACoJpVzAIWp63Auk8nEUUcdFTfccEPcddddMW7cuF6fM3fu3IiIWHPNNSMiYsKECfHkk0/GG2+80X7MrFmzYujQobHRRhu1H3PnnXfmvc6sWbNiwoQJZfpNGlcjhHMDB3a0NGptbRzJRg4RpYdzyfNcWSWNyh3OqZ4DoNqEcwCFqetwbtq0aXHFFVfElVdeGSuvvHLMnz8/5s+fHx/+35n6xRdfjNNPPz3mzJkTL7/8ctx0001x8MEHxw477BCbbbZZRERMnDgxNtpoozjooIPi8ccfj9tvvz1OOeWUmDZtWgz6v5n9kUceGS+99FJ861vfimeffTYuvPDCuOaaa+K4446r2e9eL+otnEs2fcgN53J/Fs41jtxqt1LaWnOfp3KONCpHW6twDoBaEs4BFKauw7mLLrooFixYEDvttFOsueaa7V9XX311REQMHDgw7rjj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xx/PH2MS1KWdyjnombZWABpZudtaG31tqiSc23HHiE9+MmLatOzPX/96bT/DLr/eXMKmEI3l1FMjjjwy4sQTK/ceSeWccK5yhHN0qxKTwyVLCn9OqZtB5D6n3ivn7rqr55/TqpwbQiSvsXhx439wg4S2VgAaWTnDuba24uYQ9WbhwohHH83e3mGH7PfvfS9izTUjnn8+4owzaje25debSwjnGsstt2S//+pX2b9vlVCuttaI/E0h6CCco1u1rpxLgrWkCq4YjRLO3Xln9vtnPpP/c9qVs601t/pOaytpoa0VgEZWznAu9/Ua0QMPZAPGddaJWGut7H3DhkXMmJG9fcYZHS2D1dTWFvHgg9nby1fObbVV9rtNIerfCy9EvPRS9vb770f8+tflf49ly7IbQkSUt3LumWd8Ps0lnKNb9RLOpbVybvHijhL36dOzE+gXX+zYojrNytnWmhvwCedIC22tADSycmwIMXBgdm223NdrRPfck/2eVM0l9t47Yvfds1WBRx5Z/Q6QP/85u1bZSit1hCWJYcM6Fu1XPVffbr89+z35vHfRReX/uzRvXnbuOnhwxMc+1vfXW2ediBVXzBZsvPBC318vLYRzdKuclRu1Cufeead+J6QPP5y9urH66hHbbZddfyKiOdadK2fl3MCBHbffey/itdciHnss4rbbIi6/POKssyKOOy7igAOyFYoHHijEo/7V+uIIAPRFOTaEaGlJx9rCuevN5Wppibjgguyf0T33ZFsSqylZb+6Tn+z684bW1sZw223Z79/8ZjbwevrpiPvvL+97JJWd48eXJxtobY3YeOPsba2tHYRzdKvWk8O+hHNJK2wmE/H228U/vxqSFtadd86eoJLW1mZYd66ca861tHS8zlprRYwenS3F3223iC9/OeLb34740Y8i/vu/s8HnlVdG/OY3fX9fqKTkooK2VgAaUTnaWnOf36iVcx98kL0gH9G5ci4iYu21I77zneztE06IePPNqg2t2/XmEsK5+rd4cUdhxz77ZIsQIiIuvLC871PO9eYS1p3rTDhHt8oZzg0YkP+ahehLONe/f7YcO/d16k0SwiWhXO66c2nf2KCcba0R+aX4ra0Ro0ZFbL55xMSJEQcfnN256Ic/jNhrr+wx//M/5XlfqJRKXBxpa0v/uQWA+iCcy3rwwWzb6lprRYwb1/Uxxx8fsckm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Y489pgICApS/v7968skn1Z49e6xuH3v/H7mDcwcOHFBt27ZV9913n9Lr9apmzZpq0KBBFkHw0q6slpPWrVtbzXO/fv2M62j/u/bWKUi6SsnFTY0aNZSPj49q2rRpnv25X79+FrW9bR0vzde5e/euGj9+vIqMjFS+vr4qPDxcvfLKKxb/+QU9RuXk5Kjq1as73P1FacIyUvxlxJFtnruMKJX/uZStY1h8fLxxnfj4+Dy/i608a+dkjpTP0oxlpHD7sjXLly9XUVFRysfHRz300ENqw4YNFq9r/+X29uWCHEdee+0147GpSpUq6qmnnlL79u2z+OyClJHFixerunXrGq8nmzZtqlasWGF3G5QmLCOlp4woJRULYmJilF6vV7Vr11YTJ060uHGZ+1zLVl5yn4+dP39ePffcc6pcuXKqSpUqqn///vfMTR6dUmWwt24iIiIiIiIiIqISgKO1EhERERERERERuQmDc0RERERERERERG7C4BwREREREREREZGbMDhHRERERERERETkJgzOERERERERERERuQmDc0RERERERERERG7C4BwREREREREREZGbMDhHRERERERERETkJgzOERERERERERERuQmDc0RERESUR//+/aHT6aDT6eDt7Y0qVaqgffv2+Oyzz2AwGBxOZ/HixQgODi66jBIRERHd4xicIyIiIiKrOnXqhNTUVCQnJ2PTpk1o27YtXn31VXTu3BnZ2dnuzh4RERFRqcDgHBERERFZpdfrUbVqVYSFhaFx48Z46623sGbNGmzatAmLFy8GAMycORMPP/wwAgICEB4ejldeeQU3btwAACQkJCAuLg7Xr1831sIbP348ACAzMxNvvPEGwsLCEBAQgJiYGCQkJLjnixIRERG5EYNzREREROSwJ554Ag0aNMCqVasAAB4eHpg7dy4OHz6Mzz//HFu3bsXIkSMBAM2bN8fs2bMRGBiI1NRUpKam4o033gAADB06FLt378ayZctw4MABPP/88+jUqRNOnjzptu9GRERE5A46pZRydyaIiIiIqGTp378/0tLS8N133+V5rVevXjhw4ACOHDmS57WVK1di0KBB+OuvvwBIn3OvvfYa0tLSjOv8+eefqF27Nv7880+EhoYal7dr1w5NmzbFpEmTXP59iIiIiEoqL3dngIiIiIjuLUop6HQ6AMBPP/2EyZMn49ixY0hPT0d2djbu3LmDW7duwd/f3+r7Dx48iJycHERFRVksz8zMRMWKFYs8/0REREQlCYNzREREROSUo0ePolatWkhOTkbnzp0xePBgTJw4Effddx927tyJAQMGICsry2Zw7saNG/D09ERiYiI8PT0tXitXrlxxfAUiIiKiEoPBOSIiIiJy2NatW3Hw4EG8/vrrSExMhMFgwIwZM+DhIV0ZL1++3GJ9Hx8f5OTkWCxr1KgRcnJycPnyZbRs2bLY8k5ERERUEjE4R0RERERWZWZm4uLFi8jJycGlS5fw/fffY/LkyejcuTNiY2Nx6NAh3L17F/PmzUOXLl3wyy+/YMGCBRZp1KxZEzdu3MCWLVvQoEED+Pv7IyoqCn369EFsbCxmzJiBRo0a4cqVK9iyZQvq16+Pp59+2k3fmIiIiKj4cbRWIiIiIrLq+++/R7Vq1VCzZk106tQJ27Ztw9y5c7FmzRp4enqiQYMGmDlzJt5//33Uq1cPS5cuxeTJky3SaN68OQYNGoSePXuicuXKmDp1KgBg0aJFiI2Nxb///W9ER0ejW7du+PXXX1GjRg13fFUiIiIit+ForURERERERERERG7CmnNERERERERERERuwuAcERERERERERGRmzA4R0RERERERERE5CYMzhEREREREREREbkJg3NERERERERERERuwuAcERERERERERGRmzA4R0RERERERERE5CYMzhEREREREREREbkJg3NERERERERERERuwuAcERERERERERGRmzA4R0RERERERERE5Cb/Dy6OJrEHbXhVAAAAAElFTkSuQmCC)
:::
:::
:::
:::
:::

::: {.jp-Cell .jp-MarkdownCell .jp-Notebook-cell}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
:::

::: {.jp-RenderedHTMLCommon .jp-RenderedMarkdown .jp-MarkdownOutput mime-type="text/markdown"}
:::
:::
:::
:::

::: {.jp-Cell .jp-CodeCell .jp-Notebook-cell .jp-mod-noOutputs}
::: {.jp-Cell-inputWrapper tabindex="0"}
::: {.jp-Collapser .jp-InputCollapser .jp-Cell-inputCollapser}
:::

::: {.jp-InputArea .jp-Cell-inputArea}
::: {.jp-InputPrompt .jp-InputArea-prompt}
In \[ \]:
:::

::: {.jp-CodeMirrorEditor .jp-Editor .jp-InputArea-editor data-type="inline"}
::: {.cm-editor .cm-s-jupyter}
::: {.highlight .hl-ipython3}
     
:::
:::
:::
:::
:::
:::
:::
<!DOCTYPE html>

<html lang="en">
<head><meta charset="utf-8"/>
<meta content="width=device-width, initial-scale=1.0" name="viewport"/>
<title>data_explorer</title><script src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js"></script>
<style type="text/css">
    pre { line-height: 125%; }
td.linenos .normal { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
span.linenos { color: inherit; background-color: transparent; padding-left: 5px; padding-right: 5px; }
td.linenos .special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
span.linenos.special { color: #000000; background-color: #ffffc0; padding-left: 5px; padding-right: 5px; }
.highlight .hll { background-color: var(--jp-cell-editor-active-background) }
.highlight { background: var(--jp-cell-editor-background); color: var(--jp-mirror-editor-variable-color) }
.highlight .c { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment */
.highlight .err { color: var(--jp-mirror-editor-error-color) } /* Error */
.highlight .k { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword */
.highlight .o { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator */
.highlight .p { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation */
.highlight .ch { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Hashbang */
.highlight .cm { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Multiline */
.highlight .cp { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Preproc */
.highlight .cpf { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.PreprocFile */
.highlight .c1 { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Single */
.highlight .cs { color: var(--jp-mirror-editor-comment-color); font-style: italic } /* Comment.Special */
.highlight .kc { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Constant */
.highlight .kd { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Declaration */
.highlight .kn { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Namespace */
.highlight .kp { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Pseudo */
.highlight .kr { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Reserved */
.highlight .kt { color: var(--jp-mirror-editor-keyword-color); font-weight: bold } /* Keyword.Type */
.highlight .m { color: var(--jp-mirror-editor-number-color) } /* Literal.Number */
.highlight .s { color: var(--jp-mirror-editor-string-color) } /* Literal.String */
.highlight .ow { color: var(--jp-mirror-editor-operator-color); font-weight: bold } /* Operator.Word */
.highlight .pm { color: var(--jp-mirror-editor-punctuation-color) } /* Punctuation.Marker */
.highlight .w { color: var(--jp-mirror-editor-variable-color) } /* Text.Whitespace */
.highlight .mb { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Bin */
.highlight .mf { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Float */
.highlight .mh { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Hex */
.highlight .mi { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer */
.highlight .mo { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Oct */
.highlight .sa { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Affix */
.highlight .sb { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Backtick */
.highlight .sc { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Char */
.highlight .dl { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Delimiter */
.highlight .sd { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Doc */
.highlight .s2 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Double */
.highlight .se { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Escape */
.highlight .sh { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Heredoc */
.highlight .si { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Interpol */
.highlight .sx { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Other */
.highlight .sr { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Regex */
.highlight .s1 { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Single */
.highlight .ss { color: var(--jp-mirror-editor-string-color) } /* Literal.String.Symbol */
.highlight .il { color: var(--jp-mirror-editor-number-color) } /* Literal.Number.Integer.Long */
  </style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
 * Mozilla scrollbar styling
 */

/* use standard opaque scrollbars for most nodes */
[data-jp-theme-scrollbars='true'] {
  scrollbar-color: rgb(var(--jp-scrollbar-thumb-color))
    var(--jp-scrollbar-background-color);
}

/* for code nodes, use a transparent style of scrollbar. These selectors
 * will match lower in the tree, and so will override the above */
[data-jp-theme-scrollbars='true'] .CodeMirror-hscrollbar,
[data-jp-theme-scrollbars='true'] .CodeMirror-vscrollbar {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
}

/* tiny scrollbar */

.jp-scrollbar-tiny {
  scrollbar-color: rgba(var(--jp-scrollbar-thumb-color), 0.5) transparent;
  scrollbar-width: thin;
}

/* tiny scrollbar */

.jp-scrollbar-tiny::-webkit-scrollbar,
.jp-scrollbar-tiny::-webkit-scrollbar-corner {
  background-color: transparent;
  height: 4px;
  width: 4px;
}

.jp-scrollbar-tiny::-webkit-scrollbar-thumb {
  background: rgba(var(--jp-scrollbar-thumb-color), 0.5);
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:horizontal {
  border-left: 0 solid transparent;
  border-right: 0 solid transparent;
}

.jp-scrollbar-tiny::-webkit-scrollbar-track:vertical {
  border-top: 0 solid transparent;
  border-bottom: 0 solid transparent;
}

/*
 * Lumino
 */

.lm-ScrollBar[data-orientation='horizontal'] {
  min-height: 16px;
  max-height: 16px;
  min-width: 45px;
  border-top: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] {
  min-width: 16px;
  max-width: 16px;
  min-height: 45px;
  border-left: 1px solid #a0a0a0;
}

.lm-ScrollBar-button {
  background-color: #f0f0f0;
  background-position: center center;
  min-height: 15px;
  max-height: 15px;
  min-width: 15px;
  max-width: 15px;
}

.lm-ScrollBar-button:hover {
  background-color: #dadada;
}

.lm-ScrollBar-button.lm-mod-active {
  background-color: #cdcdcd;
}

.lm-ScrollBar-track {
  background: #f0f0f0;
}

.lm-ScrollBar-thumb {
  background: #cdcdcd;
}

.lm-ScrollBar-thumb:hover {
  background: #bababa;
}

.lm-ScrollBar-thumb.lm-mod-active {
  background: #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal'] .lm-ScrollBar-thumb {
  height: 100%;
  min-width: 15px;
  border-left: 1px solid #a0a0a0;
  border-right: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='vertical'] .lm-ScrollBar-thumb {
  width: 100%;
  min-height: 15px;
  border-top: 1px solid #a0a0a0;
  border-bottom: 1px solid #a0a0a0;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-left);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='horizontal']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-right);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='decrement'] {
  background-image: var(--jp-icon-caret-up);
  background-size: 17px;
}

.lm-ScrollBar[data-orientation='vertical']
  .lm-ScrollBar-button[data-action='increment'] {
  background-image: var(--jp-icon-caret-down);
  background-size: 17px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Widget {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
}

.lm-Widget.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.lm-AccordionPanel[data-orientation='horizontal'] > .lm-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  display: flex;
  flex-direction: column;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-CommandPalette-search {
  flex: 0 0 auto;
}

.lm-CommandPalette-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  min-height: 0;
  overflow: auto;
  list-style-type: none;
}

.lm-CommandPalette-header {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-CommandPalette-item {
  display: flex;
  flex-direction: row;
}

.lm-CommandPalette-itemIcon {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemContent {
  flex: 1 1 auto;
  overflow: hidden;
}

.lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemLabel {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.lm-close-icon {
  border: 1px solid transparent;
  background-color: transparent;
  position: absolute;
  z-index: 1;
  right: 3%;
  top: 0;
  bottom: 0;
  margin: auto;
  padding: 7px 0;
  display: none;
  vertical-align: middle;
  outline: 0;
  cursor: pointer;
}
.lm-close-icon:after {
  content: 'X';
  display: block;
  width: 15px;
  height: 15px;
  text-align: center;
  color: #000;
  font-weight: normal;
  font-size: 12px;
  cursor: pointer;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-DockPanel {
  z-index: 0;
}

.lm-DockPanel-widget {
  z-index: 0;
}

.lm-DockPanel-tabBar {
  z-index: 1;
}

.lm-DockPanel-handle {
  z-index: 2;
}

.lm-DockPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-DockPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-DockPanel-handle[data-orientation='horizontal'] {
  cursor: ew-resize;
}

.lm-DockPanel-handle[data-orientation='vertical'] {
  cursor: ns-resize;
}

.lm-DockPanel-handle[data-orientation='horizontal']:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-DockPanel-handle[data-orientation='vertical']:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

.lm-DockPanel-overlay {
  z-index: 3;
  box-sizing: border-box;
  pointer-events: none;
}

.lm-DockPanel-overlay.lm-mod-hidden {
  display: none !important;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-Menu {
  z-index: 10000;
  position: absolute;
  white-space: nowrap;
  overflow-x: hidden;
  overflow-y: auto;
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-Menu-content {
  margin: 0;
  padding: 0;
  display: table;
  list-style-type: none;
}

.lm-Menu-item {
  display: table-row;
}

.lm-Menu-item.lm-mod-hidden,
.lm-Menu-item.lm-mod-collapsed {
  display: none !important;
}

.lm-Menu-itemIcon,
.lm-Menu-itemSubmenuIcon {
  display: table-cell;
  text-align: center;
}

.lm-Menu-itemLabel {
  display: table-cell;
  text-align: left;
}

.lm-Menu-itemShortcut {
  display: table-cell;
  text-align: right;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-MenuBar {
  outline: none;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-MenuBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  list-style-type: none;
}

.lm-MenuBar-item {
  box-sizing: border-box;
}

.lm-MenuBar-itemIcon,
.lm-MenuBar-itemLabel {
  display: inline-block;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-ScrollBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-ScrollBar[data-orientation='horizontal'] {
  flex-direction: row;
}

.lm-ScrollBar[data-orientation='vertical'] {
  flex-direction: column;
}

.lm-ScrollBar-button {
  box-sizing: border-box;
  flex: 0 0 auto;
}

.lm-ScrollBar-track {
  box-sizing: border-box;
  position: relative;
  overflow: hidden;
  flex: 1 1 auto;
}

.lm-ScrollBar-thumb {
  box-sizing: border-box;
  position: absolute;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-SplitPanel-child {
  z-index: 0;
}

.lm-SplitPanel-handle {
  z-index: 1;
}

.lm-SplitPanel-handle.lm-mod-hidden {
  display: none !important;
}

.lm-SplitPanel-handle:after {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  content: '';
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle {
  cursor: ew-resize;
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle {
  cursor: ns-resize;
}

.lm-SplitPanel[data-orientation='horizontal'] > .lm-SplitPanel-handle:after {
  left: 50%;
  min-width: 8px;
  transform: translateX(-50%);
}

.lm-SplitPanel[data-orientation='vertical'] > .lm-SplitPanel-handle:after {
  top: 50%;
  min-height: 8px;
  transform: translateY(-50%);
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabBar {
  display: flex;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.lm-TabBar[data-orientation='horizontal'] {
  flex-direction: row;
  align-items: flex-end;
}

.lm-TabBar[data-orientation='vertical'] {
  flex-direction: column;
  align-items: flex-end;
}

.lm-TabBar-content {
  margin: 0;
  padding: 0;
  display: flex;
  flex: 1 1 auto;
  list-style-type: none;
}

.lm-TabBar[data-orientation='horizontal'] > .lm-TabBar-content {
  flex-direction: row;
}

.lm-TabBar[data-orientation='vertical'] > .lm-TabBar-content {
  flex-direction: column;
}

.lm-TabBar-tab {
  display: flex;
  flex-direction: row;
  box-sizing: border-box;
  overflow: hidden;
  touch-action: none; /* Disable native Drag/Drop */
}

.lm-TabBar-tabIcon,
.lm-TabBar-tabCloseIcon {
  flex: 0 0 auto;
}

.lm-TabBar-tabLabel {
  flex: 1 1 auto;
  overflow: hidden;
  white-space: nowrap;
}

.lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
}

.lm-TabBar-tab.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar-addButton.lm-mod-hidden {
  display: none !important;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab {
  position: relative;
}

.lm-TabBar.lm-mod-dragging[data-orientation='horizontal'] .lm-TabBar-tab {
  left: 0;
  transition: left 150ms ease;
}

.lm-TabBar.lm-mod-dragging[data-orientation='vertical'] .lm-TabBar-tab {
  top: 0;
  transition: top 150ms ease;
}

.lm-TabBar.lm-mod-dragging .lm-TabBar-tab.lm-mod-dragging {
  transition: none;
}

.lm-TabBar-tabLabel .lm-TabBar-tabInput {
  user-select: all;
  width: 100%;
  box-sizing: border-box;
  background: inherit;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-TabPanel-tabBar {
  z-index: 1;
}

.lm-TabPanel-stackedPanel {
  z-index: 0;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapse {
  display: flex;
  flex-direction: column;
  align-items: stretch;
}

.jp-Collapse-header {
  padding: 1px 12px;
  background-color: var(--jp-layout-color1);
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  align-items: center;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  text-transform: uppercase;
  user-select: none;
}

.jp-Collapser-icon {
  height: 16px;
}

.jp-Collapse-header-collapsed .jp-Collapser-icon {
  transform: rotate(-90deg);
  margin: auto 0;
}

.jp-Collapser-title {
  line-height: 25px;
}

.jp-Collapse-contents {
  padding: 0 12px;
  background-color: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* This file was auto-generated by ensureUiComponents() in @jupyterlab/buildutils */

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

/* Icons urls */

:root {
  --jp-icon-add-above: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5MikiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik00Ljc1IDQuOTMwNjZINi42MjVWNi44MDU2NkM2LjYyNSA3LjAxMTkxIDYuNzkzNzUgNy4xODA2NiA3IDcuMTgwNjZDNy4yMDYyNSA3LjE4MDY2IDcuMzc1IDcuMDExOTEgNy4zNzUgNi44MDU2NlY0LjkzMDY2SDkuMjVDOS40NTYyNSA0LjkzMDY2IDkuNjI1IDQuNzYxOTEgOS42MjUgNC41NTU2NkM5LjYyNSA0LjM0OTQxIDkuNDU2MjUgNC4xODA2NiA5LjI1IDQuMTgwNjZINy4zNzVWMi4zMDU2NkM3LjM3NSAyLjA5OTQxIDcuMjA2MjUgMS45MzA2NiA3IDEuOTMwNjZDNi43OTM3NSAxLjkzMDY2IDYuNjI1IDIuMDk5NDEgNi42MjUgMi4zMDU2NlY0LjE4MDY2SDQuNzVDNC41NDM3NSA0LjE4MDY2IDQuMzc1IDQuMzQ5NDEgNC4zNzUgNC41NTU2NkM0LjM3NSA0Ljc2MTkxIDQuNTQzNzUgNC45MzA2NiA0Ljc1IDQuOTMwNjZaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC43Ii8+CjwvZz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTExLjUgOS41VjExLjVMMi41IDExLjVWOS41TDExLjUgOS41Wk0xMiA4QzEyLjU1MjMgOCAxMyA4LjQ0NzcyIDEzIDlWMTJDMTMgMTIuNTUyMyAxMi41NTIzIDEzIDEyIDEzTDIgMTNDMS40NDc3MiAxMyAxIDEyLjU1MjMgMSAxMlY5QzEgOC40NDc3MiAxLjQ0NzcxIDggMiA4TDEyIDhaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5MiI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KC0xIDAgMCAxIDEwIDEuNTU1NjYpIi8+CjwvY2xpcFBhdGg+CjwvZGVmcz4KPC9zdmc+Cg==);
  --jp-icon-add-below: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPGcgY2xpcC1wYXRoPSJ1cmwoI2NsaXAwXzEzN18xOTQ5OCkiPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGQ9Ik05LjI1IDEwLjA2OTNMNy4zNzUgMTAuMDY5M0w3LjM3NSA4LjE5NDM0QzcuMzc1IDcuOTg4MDkgNy4yMDYyNSA3LjgxOTM0IDcgNy44MTkzNEM2Ljc5Mzc1IDcuODE5MzQgNi42MjUgNy45ODgwOSA2LjYyNSA4LjE5NDM0TDYuNjI1IDEwLjA2OTNMNC43NSAxMC4wNjkzQzQuNTQzNzUgMTAuMDY5MyA0LjM3NSAxMC4yMzgxIDQuMzc1IDEwLjQ0NDNDNC4zNzUgMTAuNjUwNiA0LjU0Mzc1IDEwLjgxOTMgNC43NSAxMC44MTkzTDYuNjI1IDEwLjgxOTNMNi42MjUgMTIuNjk0M0M2LjYyNSAxMi45MDA2IDYuNzkzNzUgMTMuMDY5MyA3IDEzLjA2OTNDNy4yMDYyNSAxMy4wNjkzIDcuMzc1IDEyLjkwMDYgNy4zNzUgMTIuNjk0M0w3LjM3NSAxMC44MTkzTDkuMjUgMTAuODE5M0M5LjQ1NjI1IDEwLjgxOTMgOS42MjUgMTAuNjUwNiA5LjYyNSAxMC40NDQzQzkuNjI1IDEwLjIzODEgOS40NTYyNSAxMC4wNjkzIDkuMjUgMTAuMDY5M1oiIGZpbGw9IiM2MTYxNjEiIHN0cm9rZT0iIzYxNjE2MSIgc3Ryb2tlLXdpZHRoPSIwLjciLz4KPC9nPgo8cGF0aCBjbGFzcz0ianAtaWNvbjMiIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMi41IDUuNUwyLjUgMy41TDExLjUgMy41TDExLjUgNS41TDIuNSA1LjVaTTIgN0MxLjQ0NzcyIDcgMSA2LjU1MjI4IDEgNkwxIDNDMSAyLjQ0NzcyIDEuNDQ3NzIgMiAyIDJMMTIgMkMxMi41NTIzIDIgMTMgMi40NDc3MiAxMyAzTDEzIDZDMTMgNi41NTIyOSAxMi41NTIzIDcgMTIgN0wyIDdaIiBmaWxsPSIjNjE2MTYxIi8+CjxkZWZzPgo8Y2xpcFBhdGggaWQ9ImNsaXAwXzEzN18xOTQ5OCI+CjxyZWN0IGNsYXNzPSJqcC1pY29uMyIgd2lkdGg9IjYiIGhlaWdodD0iNiIgZmlsbD0id2hpdGUiIHRyYW5zZm9ybT0ibWF0cml4KDEgMS43NDg0NmUtMDcgMS43NDg0NmUtMDcgLTEgNCAxMy40NDQzKSIvPgo8L2NsaXBQYXRoPgo8L2RlZnM+Cjwvc3ZnPgo=);
  --jp-icon-add: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDEzaC02djZoLTJ2LTZINXYtMmg2VjVoMnY2aDZ2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bell: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE2IDE2IiB2ZXJzaW9uPSIxLjEiPgogICA8cGF0aCBjbGFzcz0ianAtaWNvbjIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzMzMzMzIgogICAgICBkPSJtOCAwLjI5Yy0xLjQgMC0yLjcgMC43My0zLjYgMS44LTEuMiAxLjUtMS40IDMuNC0xLjUgNS4yLTAuMTggMi4yLTAuNDQgNC0yLjMgNS4zbDAuMjggMS4zaDVjMC4wMjYgMC42NiAwLjMyIDEuMSAwLjcxIDEuNSAwLjg0IDAuNjEgMiAwLjYxIDIuOCAwIDAuNTItMC40IDAuNi0xIDAuNzEtMS41aDVsMC4yOC0xLjNjLTEuOS0wLjk3LTIuMi0zLjMtMi4zLTUuMy0wLjEzLTEuOC0wLjI2LTMuNy0xLjUtNS4yLTAuODUtMS0yLjItMS44LTMuNi0xLjh6bTAgMS40YzAuODggMCAxLjkgMC41NSAyLjUgMS4zIDAuODggMS4xIDEuMSAyLjcgMS4yIDQuNCAwLjEzIDEuNyAwLjIzIDMuNiAxLjMgNS4yaC0xMGMxLjEtMS42IDEuMi0zLjQgMS4zLTUuMiAwLjEzLTEuNyAwLjMtMy4zIDEuMi00LjQgMC41OS0wLjcyIDEuNi0xLjMgMi41LTEuM3ptLTAuNzQgMTJoMS41Yy0wLjAwMTUgMC4yOCAwLjAxNSAwLjc5LTAuNzQgMC43OS0wLjczIDAuMDAxNi0wLjcyLTAuNTMtMC43NC0wLjc5eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-bug-dot: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiPgogICAgICAgIDxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTcuMTkgOEgyMFYxMEgxNy45MUMxNy45NiAxMC4zMyAxOCAxMC42NiAxOCAxMVYxMkgyMFYxNEgxOC41SDE4VjE0LjAyNzVDMTUuNzUgMTQuMjc2MiAxNCAxNi4xODM3IDE0IDE4LjVDMTQgMTkuMjA4IDE0LjE2MzUgMTkuODc3OSAxNC40NTQ5IDIwLjQ3MzlDMTMuNzA2MyAyMC44MTE3IDEyLjg3NTcgMjEgMTIgMjFDOS43OCAyMSA3Ljg1IDE5Ljc5IDYuODEgMThINFYxNkg2LjA5QzYuMDQgMTUuNjcgNiAxNS4zNCA2IDE1VjE0SDRWMTJINlYxMUM2IDEwLjY2IDYuMDQgMTAuMzMgNi4wOSAxMEg0VjhINi44MUM3LjI2IDcuMjIgNy44OCA2LjU1IDguNjIgNi4wNEw3IDQuNDFMOC40MSAzTDEwLjU5IDUuMTdDMTEuMDQgNS4wNiAxMS41MSA1IDEyIDVDMTIuNDkgNSAxMi45NiA1LjA2IDEzLjQyIDUuMTdMMTUuNTkgM0wxNyA0LjQxTDE1LjM3IDYuMDRDMTYuMTIgNi41NSAxNi43NCA3LjIyIDE3LjE5IDhaTTEwIDE2SDE0VjE0SDEwVjE2Wk0xMCAxMkgxNFYxMEgxMFYxMloiIGZpbGw9IiM2MTYxNjEiLz4KICAgICAgICA8cGF0aCBkPSJNMjIgMTguNUMyMiAyMC40MzMgMjAuNDMzIDIyIDE4LjUgMjJDMTYuNTY3IDIyIDE1IDIwLjQzMyAxNSAxOC41QzE1IDE2LjU2NyAxNi41NjcgMTUgMTguNSAxNUMyMC40MzMgMTUgMjIgMTYuNTY3IDIyIDE4LjVaIiBmaWxsPSIjNjE2MTYxIi8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-bug: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yMCA4aC0yLjgxYy0uNDUtLjc4LTEuMDctMS40NS0xLjgyLTEuOTZMMTcgNC40MSAxNS41OSAzbC0yLjE3IDIuMTdDMTIuOTYgNS4wNiAxMi40OSA1IDEyIDVjLS40OSAwLS45Ni4wNi0xLjQxLjE3TDguNDEgMyA3IDQuNDFsMS42MiAxLjYzQzcuODggNi41NSA3LjI2IDcuMjIgNi44MSA4SDR2MmgyLjA5Yy0uMDUuMzMtLjA5LjY2LS4wOSAxdjFINHYyaDJ2MWMwIC4zNC4wNC42Ny4wOSAxSDR2MmgyLjgxYzEuMDQgMS43OSAyLjk3IDMgNS4xOSAzczQuMTUtMS4yMSA1LjE5LTNIMjB2LTJoLTIuMDljLjA1LS4zMy4wOS0uNjYuMDktMXYtMWgydi0yaC0ydi0xYzAtLjM0LS4wNC0uNjctLjA5LTFIMjBWOHptLTYgOGgtNHYtMmg0djJ6bTAtNGgtNHYtMmg0djJ6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-build: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE0LjkgMTcuNDVDMTYuMjUgMTcuNDUgMTcuMzUgMTYuMzUgMTcuMzUgMTVDMTcuMzUgMTMuNjUgMTYuMjUgMTIuNTUgMTQuOSAxMi41NUMxMy41NCAxMi41NSAxMi40NSAxMy42NSAxMi40NSAxNUMxMi40NSAxNi4zNSAxMy41NCAxNy40NSAxNC45IDE3LjQ1Wk0yMC4xIDE1LjY4TDIxLjU4IDE2Ljg0QzIxLjcxIDE2Ljk1IDIxLjc1IDE3LjEzIDIxLjY2IDE3LjI5TDIwLjI2IDE5LjcxQzIwLjE3IDE5Ljg2IDIwIDE5LjkyIDE5LjgzIDE5Ljg2TDE4LjA5IDE5LjE2QzE3LjczIDE5LjQ0IDE3LjMzIDE5LjY3IDE2LjkxIDE5Ljg1TDE2LjY0IDIxLjdDMTYuNjIgMjEuODcgMTYuNDcgMjIgMTYuMyAyMkgxMy41QzEzLjMyIDIyIDEzLjE4IDIxLjg3IDEzLjE1IDIxLjdMMTIuODkgMTkuODVDMTIuNDYgMTkuNjcgMTIuMDcgMTkuNDQgMTEuNzEgMTkuMTZMOS45NjAwMiAxOS44NkM5LjgxMDAyIDE5LjkyIDkuNjIwMDIgMTkuODYgOS41NDAwMiAxOS43MUw4LjE0MDAyIDE3LjI5QzguMDUwMDIgMTcuMTMgOC4wOTAwMiAxNi45NSA4LjIyMDAyIDE2Ljg0TDkuNzAwMDIgMTUuNjhMOS42NTAwMSAxNUw5LjcwMDAyIDE0LjMxTDguMjIwMDIgMTMuMTZDOC4wOTAwMiAxMy4wNSA4LjA1MDAyIDEyLjg2IDguMTQwMDIgMTIuNzFMOS41NDAwMiAxMC4yOUM5LjYyMDAyIDEwLjEzIDkuODEwMDIgMTAuMDcgOS45NjAwMiAxMC4xM0wxMS43MSAxMC44NEMxMi4wNyAxMC41NiAxMi40NiAxMC4zMiAxMi44OSAxMC4xNUwxMy4xNSA4LjI4OTk4QzEzLjE4IDguMTI5OTggMTMuMzIgNy45OTk5OCAxMy41IDcuOTk5OThIMTYuM0MxNi40NyA3Ljk5OTk4IDE2LjYyIDguMTI5OTggMTYuNjQgOC4yODk5OEwxNi45MSAxMC4xNUMxNy4zMyAxMC4zMiAxNy43MyAxMC41NiAxOC4wOSAxMC44NEwxOS44MyAxMC4xM0MyMCAxMC4wNyAyMC4xNyAxMC4xMyAyMC4yNiAxMC4yOUwyMS42NiAxMi43MUMyMS43NSAxMi44NiAyMS43MSAxMy4wNSAyMS41OCAxMy4xNkwyMC4xIDE0LjMxTDIwLjE1IDE1TDIwLjEgMTUuNjhaIi8+CiAgICA8cGF0aCBkPSJNNy4zMjk2NiA3LjQ0NDU0QzguMDgzMSA3LjAwOTU0IDguMzM5MzIgNi4wNTMzMiA3LjkwNDMyIDUuMjk5ODhDNy40NjkzMiA0LjU0NjQzIDYuNTA4MSA0LjI4MTU2IDUuNzU0NjYgNC43MTY1NkM1LjM5MTc2IDQuOTI2MDggNS4xMjY5NSA1LjI3MTE4IDUuMDE4NDkgNS42NzU5NEM0LjkxMDA0IDYuMDgwNzEgNC45NjY4MiA2LjUxMTk4IDUuMTc2MzQgNi44NzQ4OEM1LjYxMTM0IDcuNjI4MzIgNi41NzYyMiA3Ljg3OTU0IDcuMzI5NjYgNy40NDQ1NFpNOS42NTcxOCA0Ljc5NTkzTDEwLjg2NzIgNC45NTE3OUMxMC45NjI4IDQuOTc3NDEgMTEuMDQwMiA1LjA3MTMzIDExLjAzODIgNS4xODc5M0wxMS4wMzg4IDYuOTg4OTNDMTEuMDQ1NSA3LjEwMDU0IDEwLjk2MTYgNy4xOTUxOCAxMC44NTUgNy4yMTA1NEw5LjY2MDAxIDcuMzgwODNMOS4yMzkxNSA4LjEzMTg4TDkuNjY5NjEgOS4yNTc0NUM5LjcwNzI5IDkuMzYyNzEgOS42NjkzNCA5LjQ3Njk5IDkuNTc0MDggOS41MzE5OUw4LjAxNTIzIDEwLjQzMkM3LjkxMTMxIDEwLjQ5MiA3Ljc5MzM3IDEwLjQ2NzcgNy43MjEwNSAxMC4zODI0TDYuOTg3NDggOS40MzE4OEw2LjEwOTMxIDkuNDMwODNMNS4zNDcwNCAxMC4zOTA1QzUuMjg5MDkgMTAuNDcwMiA1LjE3MzgzIDEwLjQ5MDUgNS4wNzE4NyAxMC40MzM5TDMuNTEyNDUgOS41MzI5M0MzLjQxMDQ5IDkuNDc2MzMgMy4zNzY0NyA5LjM1NzQxIDMuNDEwNzUgOS4yNTY3OUwzLjg2MzQ3IDguMTQwOTNMMy42MTc0OSA3Ljc3NDg4TDMuNDIzNDcgNy4zNzg4M0wyLjIzMDc1IDcuMjEyOTdDMi4xMjY0NyA3LjE5MjM1IDIuMDQwNDkgNy4xMDM0MiAyLjA0MjQ1IDYuOTg2ODJMMi4wNDE4NyA1LjE4NTgyQzIuMDQzODMgNS4wNjkyMiAyLjExOTA5IDQuOTc5NTggMi4yMTcwNCA0Ljk2OTIyTDMuNDIwNjUgNC43OTM5M0wzLjg2NzQ5IDQuMDI3ODhMMy40MTEwNSAyLjkxNzMxQzMuMzczMzcgMi44MTIwNCAzLjQxMTMxIDIuNjk3NzYgMy41MTUyMyAyLjYzNzc2TDUuMDc0MDggMS43Mzc3NkM1LjE2OTM0IDEuNjgyNzYgNS4yODcyOSAxLjcwNzA0IDUuMzU5NjEgMS43OTIzMUw2LjExOTE1IDIuNzI3ODhMNi45ODAwMSAyLjczODkzTDcuNzI0OTYgMS43ODkyMkM3Ljc5MTU2IDEuNzA0NTggNy45MTU0OCAxLjY3OTIyIDguMDA4NzkgMS43NDA4Mkw5LjU2ODIxIDIuNjQxODJDOS42NzAxNyAyLjY5ODQyIDkuNzEyODUgMi44MTIzNCA5LjY4NzIzIDIuOTA3OTdMOS4yMTcxOCA0LjAzMzgzTDkuNDYzMTYgNC4zOTk4OEw5LjY1NzE4IDQuNzk1OTNaIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iOS45LDEzLjYgMy42LDcuNCA0LjQsNi42IDkuOSwxMi4yIDE1LjQsNi43IDE2LjEsNy40ICIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNS45TDksOS43bDMuOC0zLjhsMS4yLDEuMmwtNC45LDVsLTQuOS01TDUuMiw1Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-caret-down: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik01LjIsNy41TDksMTEuMmwzLjgtMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-left: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik0xMC44LDEyLjhMNy4xLDlsMy44LTMuOGwwLDcuNkgxMC44eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-right: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiIHNoYXBlLXJlbmRlcmluZz0iZ2VvbWV0cmljUHJlY2lzaW9uIj4KICAgIDxwYXRoIGQ9Ik03LjIsNS4yTDEwLjksOWwtMy44LDMuOFY1LjJINy4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-caret-up-empty-thin: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwb2x5Z29uIGNsYXNzPSJzdDEiIHBvaW50cz0iMTUuNCwxMy4zIDkuOSw3LjcgNC40LDEzLjIgMy42LDEyLjUgOS45LDYuMyAxNi4xLDEyLjYgIi8+Cgk8L2c+Cjwvc3ZnPgo=);
  --jp-icon-caret-up: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSIgc2hhcGUtcmVuZGVyaW5nPSJnZW9tZXRyaWNQcmVjaXNpb24iPgoJCTxwYXRoIGQ9Ik01LjIsMTAuNUw5LDYuOGwzLjgsMy44SDUuMnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-case-sensitive: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWFjY2VudDIiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTcuNiw4aDAuOWwzLjUsOGgtMS4xTDEwLDE0SDZsLTAuOSwySDRMNy42LDh6IE04LDkuMUw2LjQsMTNoMy4yTDgsOS4xeiIvPgogICAgPHBhdGggZD0iTTE2LjYsOS44Yy0wLjIsMC4xLTAuNCwwLjEtMC43LDAuMWMtMC4yLDAtMC40LTAuMS0wLjYtMC4yYy0wLjEtMC4xLTAuMi0wLjQtMC4yLTAuNyBjLTAuMywwLjMtMC42LDAuNS0wLjksMC43Yy0wLjMsMC4xLTAuNywwLjItMS4xLDAuMmMtMC4zLDAtMC41LDAtMC43LTAuMWMtMC4yLTAuMS0wLjQtMC4yLTAuNi0wLjNjLTAuMi0wLjEtMC4zLTAuMy0wLjQtMC41IGMtMC4xLTAuMi0wLjEtMC40LTAuMS0wLjdjMC0wLjMsMC4xLTAuNiwwLjItMC44YzAuMS0wLjIsMC4zLTAuNCwwLjQtMC41QzEyLDcsMTIuMiw2LjksMTIuNSw2LjhjMC4yLTAuMSwwLjUtMC4xLDAuNy0wLjIgYzAuMy0wLjEsMC41LTAuMSwwLjctMC4xYzAuMiwwLDAuNC0wLjEsMC42LTAuMWMwLjIsMCwwLjMtMC4xLDAuNC0wLjJjMC4xLTAuMSwwLjItMC4yLDAuMi0wLjRjMC0xLTEuMS0xLTEuMy0xIGMtMC40LDAtMS40LDAtMS40LDEuMmgtMC45YzAtMC40LDAuMS0wLjcsMC4yLTFjMC4xLTAuMiwwLjMtMC40LDAuNS0wLjZjMC4yLTAuMiwwLjUtMC4zLDAuOC0wLjNDMTMuMyw0LDEzLjYsNCwxMy45LDQgYzAuMywwLDAuNSwwLDAuOCwwLjFjMC4zLDAsMC41LDAuMSwwLjcsMC4yYzAuMiwwLjEsMC40LDAuMywwLjUsMC41QzE2LDUsMTYsNS4yLDE2LDUuNnYyLjljMCwwLjIsMCwwLjQsMCwwLjUgYzAsMC4xLDAuMSwwLjIsMC4zLDAuMmMwLjEsMCwwLjIsMCwwLjMsMFY5Ljh6IE0xNS4yLDYuOWMtMS4yLDAuNi0zLjEsMC4yLTMuMSwxLjRjMCwxLjQsMy4xLDEsMy4xLTAuNVY2Ljl6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik05IDE2LjE3TDQuODMgMTJsLTEuNDIgMS40MUw5IDE5IDIxIDdsLTEuNDEtMS40MXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-circle-empty: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDJDNi40NyAyIDIgNi40NyAyIDEyczQuNDcgMTAgMTAgMTAgMTAtNC40NyAxMC0xMFMxNy41MyAyIDEyIDJ6bTAgMThjLTQuNDEgMC04LTMuNTktOC04czMuNTktOCA4LTggOCAzLjU5IDggOC0zLjU5IDgtOCA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-circle: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iOSIgY3k9IjkiIHI9IjgiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-clear: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8bWFzayBpZD0iZG9udXRIb2xlIj4KICAgIDxyZWN0IHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgZmlsbD0id2hpdGUiIC8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSI4IiBmaWxsPSJibGFjayIvPgogIDwvbWFzaz4KCiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxyZWN0IGhlaWdodD0iMTgiIHdpZHRoPSIyIiB4PSIxMSIgeT0iMyIgdHJhbnNmb3JtPSJyb3RhdGUoMzE1LCAxMiwgMTIpIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIxMCIgbWFzaz0idXJsKCNkb251dEhvbGUpIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-close: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1ub25lIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIGpwLWljb24zLWhvdmVyIiBmaWxsPSJub25lIj4KICAgIDxjaXJjbGUgY3g9IjEyIiBjeT0iMTIiIHI9IjExIi8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIGpwLWljb24tYWNjZW50Mi1ob3ZlciIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMTkgNi40MUwxNy41OSA1IDEyIDEwLjU5IDYuNDEgNSA1IDYuNDEgMTAuNTkgMTIgNSAxNy41OSA2LjQxIDE5IDEyIDEzLjQxIDE3LjU5IDE5IDE5IDE3LjU5IDEzLjQxIDEyeiIvPgogIDwvZz4KCiAgPGcgY2xhc3M9ImpwLWljb24tbm9uZSBqcC1pY29uLWJ1c3kiIGZpbGw9Im5vbmUiPgogICAgPGNpcmNsZSBjeD0iMTIiIGN5PSIxMiIgcj0iNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code-check: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBzaGFwZS1yZW5kZXJpbmc9Imdlb21ldHJpY1ByZWNpc2lvbiI+CiAgICA8cGF0aCBkPSJNNi41OSwzLjQxTDIsOEw2LjU5LDEyLjZMOCwxMS4xOEw0LjgyLDhMOCw0LjgyTDYuNTksMy40MU0xMi40MSwzLjQxTDExLDQuODJMMTQuMTgsOEwxMSwxMS4xOEwxMi40MSwxMi42TDE3LDhMMTIuNDEsMy40MU0yMS41OSwxMS41OUwxMy41LDE5LjY4TDkuODMsMTZMOC40MiwxNy40MUwxMy41LDIyLjVMMjMsMTNMMjEuNTksMTEuNTlaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-code: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTExLjQgMTguNkw2LjggMTRMMTEuNCA5LjRMMTAgOEw0IDE0TDEwIDIwTDExLjQgMTguNlpNMTYuNiAxOC42TDIxLjIgMTRMMTYuNiA5LjRMMTggOEwyNCAxNEwxOCAyMEwxNi42IDE4LjZWMTguNloiLz4KCTwvZz4KPC9zdmc+Cg==);
  --jp-icon-collapse-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNNiAxM3YyaDh2LTJ6IiAvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-console: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwMCAyMDAiPgogIDxnIGNsYXNzPSJqcC1jb25zb2xlLWljb24tYmFja2dyb3VuZC1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMjg4RDEiPgogICAgPHBhdGggZD0iTTIwIDE5LjhoMTYwdjE1OS45SDIweiIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtY29uc29sZS1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIj4KICAgIDxwYXRoIGQ9Ik0xMDUgMTI3LjNoNDB2MTIuOGgtNDB6TTUxLjEgNzdMNzQgOTkuOWwtMjMuMyAyMy4zIDEwLjUgMTAuNSAyMy4zLTIzLjNMOTUgOTkuOSA4NC41IDg5LjQgNjEuNiA2Ni41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copy: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTExLjksMUgzLjJDMi40LDEsMS43LDEuNywxLjcsMi41djEwLjJoMS41VjIuNWg4LjdWMXogTTE0LjEsMy45aC04Yy0wLjgsMC0xLjUsMC43LTEuNSwxLjV2MTAuMmMwLDAuOCwwLjcsMS41LDEuNSwxLjVoOCBjMC44LDAsMS41LTAuNywxLjUtMS41VjUuNEMxNS41LDQuNiwxNC45LDMuOSwxNC4xLDMuOXogTTE0LjEsMTUuNWgtOFY1LjRoOFYxNS41eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-copyright: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGVuYWJsZS1iYWNrZ3JvdW5kPSJuZXcgMCAwIDI0IDI0IiBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCI+CiAgPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0xMS44OCw5LjE0YzEuMjgsMC4wNiwxLjYxLDEuMTUsMS42MywxLjY2aDEuNzljLTAuMDgtMS45OC0xLjQ5LTMuMTktMy40NS0zLjE5QzkuNjQsNy42MSw4LDksOCwxMi4xNCBjMCwxLjk0LDAuOTMsNC4yNCwzLjg0LDQuMjRjMi4yMiwwLDMuNDEtMS42NSwzLjQ0LTIuOTVoLTEuNzljLTAuMDMsMC41OS0wLjQ1LDEuMzgtMS42MywxLjQ0QzEwLjU1LDE0LjgzLDEwLDEzLjgxLDEwLDEyLjE0IEMxMCw5LjI1LDExLjI4LDkuMTYsMTEuODgsOS4xNHogTTEyLDJDNi40OCwyLDIsNi40OCwyLDEyczQuNDgsMTAsMTAsMTBzMTAtNC40OCwxMC0xMFMxNy41MiwyLDEyLDJ6IE0xMiwyMGMtNC40MSwwLTgtMy41OS04LTggczMuNTktOCw4LThzOCwzLjU5LDgsOFMxNi40MSwyMCwxMiwyMHoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-cut: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkuNjQgNy42NGMuMjMtLjUuMzYtMS4wNS4zNi0xLjY0IDAtMi4yMS0xLjc5LTQtNC00UzIgMy43OSAyIDZzMS43OSA0IDQgNGMuNTkgMCAxLjE0LS4xMyAxLjY0LS4zNkwxMCAxMmwtMi4zNiAyLjM2QzcuMTQgMTQuMTMgNi41OSAxNCA2IDE0Yy0yLjIxIDAtNCAxLjc5LTQgNHMxLjc5IDQgNCA0IDQtMS43OSA0LTRjMC0uNTktLjEzLTEuMTQtLjM2LTEuNjRMMTIgMTRsNyA3aDN2LTFMOS42NCA3LjY0ek02IDhjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTAgMTJjLTEuMSAwLTItLjg5LTItMnMuOS0yIDItMiAyIC44OSAyIDItLjkgMi0yIDJ6bTYtNy41Yy0uMjggMC0uNS0uMjItLjUtLjVzLjIyLS41LjUtLjUuNS4yMi41LjUtLjIyLjUtLjUuNXpNMTkgM2wtNiA2IDIgMiA3LTdWM3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-delete: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2cHgiIGhlaWdodD0iMTZweCI+CiAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIiAvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjI2MjYyIiBkPSJNNiAxOWMwIDEuMS45IDIgMiAyaDhjMS4xIDAgMi0uOSAyLTJWN0g2djEyek0xOSA0aC0zLjVsLTEtMWgtNWwtMSAxSDV2MmgxNFY0eiIgLz4KPC9zdmc+Cg==);
  --jp-icon-download: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE5IDloLTRWM0g5djZINWw3IDcgNy03ek01IDE4djJoMTR2LTJINXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-duplicate: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBmaWxsLXJ1bGU9ImV2ZW5vZGQiIGNsaXAtcnVsZT0iZXZlbm9kZCIgZD0iTTIuNzk5OTggMC44NzVIOC44OTU4MkM5LjIwMDYxIDAuODc1IDkuNDQ5OTggMS4xMzkxNCA5LjQ0OTk4IDEuNDYxOThDOS40NDk5OCAxLjc4NDgyIDkuMjAwNjEgMi4wNDg5NiA4Ljg5NTgyIDIuMDQ4OTZIMy4zNTQxNUMzLjA0OTM2IDIuMDQ4OTYgMi43OTk5OCAyLjMxMzEgMi43OTk5OCAyLjYzNTk0VjkuNjc5NjlDMi43OTk5OCAxMC4wMDI1IDIuNTUwNjEgMTAuMjY2NyAyLjI0NTgyIDEwLjI2NjdDMS45NDEwMyAxMC4yNjY3IDEuNjkxNjUgMTAuMDAyNSAxLjY5MTY1IDkuNjc5NjlWMi4wNDg5NkMxLjY5MTY1IDEuNDAzMjggMi4xOTA0IDAuODc1IDIuNzk5OTggMC44NzVaTTUuMzY2NjUgMTEuOVY0LjU1SDExLjA4MzNWMTEuOUg1LjM2NjY1Wk00LjE0MTY1IDQuMTQxNjdDNC4xNDE2NSAzLjY5MDYzIDQuNTA3MjggMy4zMjUgNC45NTgzMiAzLjMyNUgxMS40OTE3QzExLjk0MjcgMy4zMjUgMTIuMzA4MyAzLjY5MDYzIDEyLjMwODMgNC4xNDE2N1YxMi4zMDgzQzEyLjMwODMgMTIuNzU5NCAxMS45NDI3IDEzLjEyNSAxMS40OTE3IDEzLjEyNUg0Ljk1ODMyQzQuNTA3MjggMTMuMTI1IDQuMTQxNjUgMTIuNzU5NCA0LjE0MTY1IDEyLjMwODNWNC4xNDE2N1oiIGZpbGw9IiM2MTYxNjEiLz4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNOS40MzU3NCA4LjI2NTA3SDguMzY0MzFWOS4zMzY1QzguMzY0MzEgOS40NTQzNSA4LjI2Nzg4IDkuNTUwNzggOC4xNTAwMiA5LjU1MDc4QzguMDMyMTcgOS41NTA3OCA3LjkzNTc0IDkuNDU0MzUgNy45MzU3NCA5LjMzNjVWOC4yNjUwN0g2Ljg2NDMxQzYuNzQ2NDUgOC4yNjUwNyA2LjY1MDAyIDguMTY4NjQgNi42NTAwMiA4LjA1MDc4QzYuNjUwMDIgNy45MzI5MiA2Ljc0NjQ1IDcuODM2NSA2Ljg2NDMxIDcuODM2NUg3LjkzNTc0VjYuNzY1MDdDNy45MzU3NCA2LjY0NzIxIDguMDMyMTcgNi41NTA3OCA4LjE1MDAyIDYuNTUwNzhDOC4yNjc4OCA2LjU1MDc4IDguMzY0MzEgNi42NDcyMSA4LjM2NDMxIDYuNzY1MDdWNy44MzY1SDkuNDM1NzRDOS41NTM2IDcuODM2NSA5LjY1MDAyIDcuOTMyOTIgOS42NTAwMiA4LjA1MDc4QzkuNjUwMDIgOC4xNjg2NCA5LjU1MzYgOC4yNjUwNyA5LjQzNTc0IDguMjY1MDdaIiBmaWxsPSIjNjE2MTYxIiBzdHJva2U9IiM2MTYxNjEiIHN0cm9rZS13aWR0aD0iMC41Ii8+Cjwvc3ZnPgo=);
  --jp-icon-edit: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMgMTcuMjVWMjFoMy43NUwxNy44MSA5Ljk0bC0zLjc1LTMuNzVMMyAxNy4yNXpNMjAuNzEgNy4wNGMuMzktLjM5LjM5LTEuMDIgMC0xLjQxbC0yLjM0LTIuMzRjLS4zOS0uMzktMS4wMi0uMzktMS40MSAwbC0xLjgzIDEuODMgMy43NSAzLjc1IDEuODMtMS44M3oiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-ellipses: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPGNpcmNsZSBjeD0iNSIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxMiIgY3k9IjEyIiByPSIyIi8+CiAgICA8Y2lyY2xlIGN4PSIxOSIgY3k9IjEyIiByPSIyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-error: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj48Y2lyY2xlIGN4PSIxMiIgY3k9IjE5IiByPSIyIi8+PHBhdGggZD0iTTEwIDNoNHYxMmgtNHoiLz48L2c+CjxwYXRoIGZpbGw9Im5vbmUiIGQ9Ik0wIDBoMjR2MjRIMHoiLz4KPC9zdmc+Cg==);
  --jp-icon-expand-all: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTggMmMxIDAgMTEgMCAxMiAwczIgMSAyIDJjMCAxIDAgMTEgMCAxMnMwIDItMiAyQzIwIDE0IDIwIDQgMjAgNFMxMCA0IDYgNGMwLTIgMS0yIDItMnoiIC8+CiAgICAgICAgPHBhdGgKICAgICAgICAgICAgZD0iTTE4IDhjMC0xLTEtMi0yLTJTNSA2IDQgNnMtMiAxLTIgMmMwIDEgMCAxMSAwIDEyczEgMiAyIDJjMSAwIDExIDAgMTIgMHMyLTEgMi0yYzAtMSAwLTExIDAtMTJ6bS0yIDB2MTJINFY4eiIgLz4KICAgICAgICA8cGF0aCBkPSJNMTEgMTBIOXYzSDZ2MmgzdjNoMnYtM2gzdi0yaC0zeiIgLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-extension: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwLjUgMTFIMTlWN2MwLTEuMS0uOS0yLTItMmgtNFYzLjVDMTMgMi4xMiAxMS44OCAxIDEwLjUgMVM4IDIuMTIgOCAzLjVWNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAydjMuOEgzLjVjMS40OSAwIDIuNyAxLjIxIDIuNyAyLjdzLTEuMjEgMi43LTIuNyAyLjdIMlYyMGMwIDEuMS45IDIgMiAyaDMuOHYtMS41YzAtMS40OSAxLjIxLTIuNyAyLjctMi43IDEuNDkgMCAyLjcgMS4yMSAyLjcgMi43VjIySDE3YzEuMSAwIDItLjkgMi0ydi00aDEuNWMxLjM4IDAgMi41LTEuMTIgMi41LTIuNVMyMS44OCAxMSAyMC41IDExeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-fast-forward: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTQgMThsOC41LTZMNCA2djEyem05LTEydjEybDguNS02TDEzIDZ6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-file-upload: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTkgMTZoNnYtNmg0bC03LTctNyA3aDR6bS00IDJoMTR2Mkg1eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-file: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuMyA4LjJsLTUuNS01LjVjLS4zLS4zLS43LS41LTEuMi0uNUgzLjljLS44LjEtMS42LjktMS42IDEuOHYxNC4xYzAgLjkuNyAxLjYgMS42IDEuNmgxNC4yYy45IDAgMS42LS43IDEuNi0xLjZWOS40Yy4xLS41LS4xLS45LS40LTEuMnptLTUuOC0zLjNsMy40IDMuNmgtMy40VjQuOXptMy45IDEyLjdINC43Yy0uMSAwLS4yIDAtLjItLjJWNC43YzAtLjIuMS0uMy4yLS4zaDcuMnY0LjRzMCAuOC4zIDEuMWMuMy4zIDEuMS4zIDEuMS4zaDQuM3Y3LjJzLS4xLjItLjIuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-filter-dot: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgogIDxnIGNsYXNzPSJqcC1pY29uLWRvdCIgZmlsbD0iI0ZGRiI+CiAgICA8Y2lyY2xlIGN4PSIxOCIgY3k9IjE3IiByPSIzIj48L2NpcmNsZT4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-filter-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEwIDE4aDR2LTJoLTR2MnpNMyA2djJoMThWNkgzem0zIDdoMTJ2LTJINnYyeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-filter: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiNGRkYiPgogICAgPHBhdGggZD0iTTE0LDEyVjE5Ljg4QzE0LjA0LDIwLjE4IDEzLjk0LDIwLjUgMTMuNzEsMjAuNzFDMTMuMzIsMjEuMSAxMi42OSwyMS4xIDEyLjMsMjAuNzFMMTAuMjksMTguN0MxMC4wNiwxOC40NyA5Ljk2LDE4LjE2IDEwLDE3Ljg3VjEySDkuOTdMNC4yMSw0LjYyQzMuODcsNC4xOSAzLjk1LDMuNTYgNC4zOCwzLjIyQzQuNTcsMy4wOCA0Ljc4LDMgNSwzVjNIMTlWM0MxOS4yMiwzIDE5LjQzLDMuMDggMTkuNjIsMy4yMkMyMC4wNSwzLjU2IDIwLjEzLDQuMTkgMTkuNzksNC42MkwxNC4wMywxMkgxNFoiIC8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-folder-favorite: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgwVjB6IiBmaWxsPSJub25lIi8+PHBhdGggY2xhc3M9ImpwLWljb24zIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxNjE2MSIgZD0iTTIwIDZoLThsLTItMkg0Yy0xLjEgMC0yIC45LTIgMnYxMmMwIDEuMS45IDIgMiAyaDE2YzEuMSAwIDItLjkgMi0yVjhjMC0xLjEtLjktMi0yLTJ6bS0yLjA2IDExTDE1IDE1LjI4IDEyLjA2IDE3bC43OC0zLjMzLTIuNTktMi4yNCAzLjQxLS4yOUwxNSA4bDEuMzQgMy4xNCAzLjQxLjI5LTIuNTkgMi4yNC43OCAzLjMzeiIvPgo8L3N2Zz4K);
  --jp-icon-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY4YzAtMS4xLS45LTItMi0yaC04bC0yLTJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-home: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjRweCIgdmlld0JveD0iMCAwIDI0IDI0IiB3aWR0aD0iMjRweCIgZmlsbD0iIzAwMDAwMCI+CiAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPjxwYXRoIGNsYXNzPSJqcC1pY29uMyBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xMCAyMHYtNmg0djZoNXYtOGgzTDEyIDMgMiAxMmgzdjh6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-html5: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uMCBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiMwMDAiIGQ9Ik0xMDguNCAwaDIzdjIyLjhoMjEuMlYwaDIzdjY5aC0yM1Y0NmgtMjF2MjNoLTIzLjJNMjA2IDIzaC0yMC4zVjBoNjMuN3YyM0gyMjl2NDZoLTIzbTUzLjUtNjloMjQuMWwxNC44IDI0LjNMMzEzLjIgMGgyNC4xdjY5aC0yM1YzNC44bC0xNi4xIDI0LjgtMTYuMS0yNC44VjY5aC0yMi42bTg5LjItNjloMjN2NDYuMmgzMi42VjY5aC01NS42Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2U0NGQyNiIgZD0iTTEwNy42IDQ3MWwtMzMtMzcwLjRoMzYyLjhsLTMzIDM3MC4yTDI1NS43IDUxMiIvPgogIDxwYXRoIGNsYXNzPSJqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNmMTY1MjkiIGQ9Ik0yNTYgNDgwLjVWMTMxaDE0OC4zTDM3NiA0NDciLz4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNlYmViZWIiIGQ9Ik0xNDIgMTc2LjNoMTE0djQ1LjRoLTY0LjJsNC4yIDQ2LjVoNjB2NDUuM0gxNTQuNG0yIDIyLjhIMjAybDMuMiAzNi4zIDUwLjggMTMuNnY0Ny40bC05My4yLTI2Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZS1pbnZlcnNlIiBmaWxsPSIjZmZmIiBkPSJNMzY5LjYgMTc2LjNIMjU1Ljh2NDUuNGgxMDkuNm0tNC4xIDQ2LjVIMjU1Ljh2NDUuNGg1NmwtNS4zIDU5LTUwLjcgMTMuNnY0Ny4ybDkzLTI1LjgiLz4KPC9zdmc+Cg==);
  --jp-icon-image: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1icmFuZDQganAtaWNvbi1zZWxlY3RhYmxlLWludmVyc2UiIGZpbGw9IiNGRkYiIGQ9Ik0yLjIgMi4yaDE3LjV2MTcuNUgyLjJ6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzNGNTFCNSIgZD0iTTIuMiAyLjJ2MTcuNWgxNy41bC4xLTE3LjVIMi4yem0xMi4xIDIuMmMxLjIgMCAyLjIgMSAyLjIgMi4ycy0xIDIuMi0yLjIgMi4yLTIuMi0xLTIuMi0yLjIgMS0yLjIgMi4yLTIuMnpNNC40IDE3LjZsMy4zLTguOCAzLjMgNi42IDIuMi0zLjIgNC40IDUuNEg0LjR6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-info: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUwLjk3OCA1MC45NzgiPgoJPGcgY2xhc3M9ImpwLWljb24zIiBmaWxsPSIjNjE2MTYxIj4KCQk8cGF0aCBkPSJNNDMuNTIsNy40NThDMzguNzExLDIuNjQ4LDMyLjMwNywwLDI1LjQ4OSwwQzE4LjY3LDAsMTIuMjY2LDIuNjQ4LDcuNDU4LDcuNDU4CgkJCWMtOS45NDMsOS45NDEtOS45NDMsMjYuMTE5LDAsMzYuMDYyYzQuODA5LDQuODA5LDExLjIxMiw3LjQ1NiwxOC4wMzEsNy40NThjMCwwLDAuMDAxLDAsMC4wMDIsMAoJCQljNi44MTYsMCwxMy4yMjEtMi42NDgsMTguMDI5LTcuNDU4YzQuODA5LTQuODA5LDcuNDU3LTExLjIxMiw3LjQ1Ny0xOC4wM0M1MC45NzcsMTguNjcsNDguMzI4LDEyLjI2Niw0My41Miw3LjQ1OHoKCQkJIE00Mi4xMDYsNDIuMTA1Yy00LjQzMiw0LjQzMS0xMC4zMzIsNi44NzItMTYuNjE1LDYuODcyaC0wLjAwMmMtNi4yODUtMC4wMDEtMTIuMTg3LTIuNDQxLTE2LjYxNy02Ljg3MgoJCQljLTkuMTYyLTkuMTYzLTkuMTYyLTI0LjA3MSwwLTMzLjIzM0MxMy4zMDMsNC40NCwxOS4yMDQsMiwyNS40ODksMmM2LjI4NCwwLDEyLjE4NiwyLjQ0LDE2LjYxNyw2Ljg3MgoJCQljNC40MzEsNC40MzEsNi44NzEsMTAuMzMyLDYuODcxLDE2LjYxN0M0OC45NzcsMzEuNzcyLDQ2LjUzNiwzNy42NzUsNDIuMTA2LDQyLjEwNXoiLz4KCQk8cGF0aCBkPSJNMjMuNTc4LDMyLjIxOGMtMC4wMjMtMS43MzQsMC4xNDMtMy4wNTksMC40OTYtMy45NzJjMC4zNTMtMC45MTMsMS4xMS0xLjk5NywyLjI3Mi0zLjI1MwoJCQljMC40NjgtMC41MzYsMC45MjMtMS4wNjIsMS4zNjctMS41NzVjMC42MjYtMC43NTMsMS4xMDQtMS40NzgsMS40MzYtMi4xNzVjMC4zMzEtMC43MDcsMC40OTUtMS41NDEsMC40OTUtMi41CgkJCWMwLTEuMDk2LTAuMjYtMi4wODgtMC43NzktMi45NzljLTAuNTY1LTAuODc5LTEuNTAxLTEuMzM2LTIuODA2LTEuMzY5Yy0xLjgwMiwwLjA1Ny0yLjk4NSwwLjY2Ny0zLjU1LDEuODMyCgkJCWMtMC4zMDEsMC41MzUtMC41MDMsMS4xNDEtMC42MDcsMS44MTRjLTAuMTM5LDAuNzA3LTAuMjA3LDEuNDMyLTAuMjA3LDIuMTc0aC0yLjkzN2MtMC4wOTEtMi4yMDgsMC40MDctNC4xMTQsMS40OTMtNS43MTkKCQkJYzEuMDYyLTEuNjQsMi44NTUtMi40ODEsNS4zNzgtMi41MjdjMi4xNiwwLjAyMywzLjg3NCwwLjYwOCw1LjE0MSwxLjc1OGMxLjI3OCwxLjE2LDEuOTI5LDIuNzY0LDEuOTUsNC44MTEKCQkJYzAsMS4xNDItMC4xMzcsMi4xMTEtMC40MSwyLjkxMWMtMC4zMDksMC44NDUtMC43MzEsMS41OTMtMS4yNjgsMi4yNDNjLTAuNDkyLDAuNjUtMS4wNjgsMS4zMTgtMS43MywyLjAwMgoJCQljLTAuNjUsMC42OTctMS4zMTMsMS40NzktMS45ODcsMi4zNDZjLTAuMjM5LDAuMzc3LTAuNDI5LDAuNzc3LTAuNTY1LDEuMTk5Yy0wLjE2LDAuOTU5LTAuMjE3LDEuOTUxLTAuMTcxLDIuOTc5CgkJCUMyNi41ODksMzIuMjE4LDIzLjU3OCwzMi4yMTgsMjMuNTc4LDMyLjIxOHogTTIzLjU3OCwzOC4yMnYtMy40ODRoMy4wNzZ2My40ODRIMjMuNTc4eiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-inspector: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaW5zcGVjdG9yLWljb24tY29sb3IganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNEg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMThjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY2YzAtMS4xLS45LTItMi0yem0tNSAxNEg0di00aDExdjR6bTAtNUg0VjloMTF2NHptNSA1aC00VjloNHY5eiIvPgo8L3N2Zz4K);
  --jp-icon-json: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtanNvbi1pY29uLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0Y5QTgyNSI+CiAgICA8cGF0aCBkPSJNMjAuMiAxMS44Yy0xLjYgMC0xLjcuNS0xLjcgMSAwIC40LjEuOS4xIDEuMy4xLjUuMS45LjEgMS4zIDAgMS43LTEuNCAyLjMtMy41IDIuM2gtLjl2LTEuOWguNWMxLjEgMCAxLjQgMCAxLjQtLjggMC0uMyAwLS42LS4xLTEgMC0uNC0uMS0uOC0uMS0xLjIgMC0xLjMgMC0xLjggMS4zLTItMS4zLS4yLTEuMy0uNy0xLjMtMiAwLS40LjEtLjguMS0xLjIuMS0uNC4xLS43LjEtMSAwLS44LS40LS43LTEuNC0uOGgtLjVWNC4xaC45YzIuMiAwIDMuNS43IDMuNSAyLjMgMCAuNC0uMS45LS4xIDEuMy0uMS41LS4xLjktLjEgMS4zIDAgLjUuMiAxIDEuNyAxdjEuOHpNMS44IDEwLjFjMS42IDAgMS43LS41IDEuNy0xIDAtLjQtLjEtLjktLjEtMS4zLS4xLS41LS4xLS45LS4xLTEuMyAwLTEuNiAxLjQtMi4zIDMuNS0yLjNoLjl2MS45aC0uNWMtMSAwLTEuNCAwLTEuNC44IDAgLjMgMCAuNi4xIDEgMCAuMi4xLjYuMSAxIDAgMS4zIDAgMS44LTEuMyAyQzYgMTEuMiA2IDExLjcgNiAxM2MwIC40LS4xLjgtLjEgMS4yLS4xLjMtLjEuNy0uMSAxIDAgLjguMy44IDEuNC44aC41djEuOWgtLjljLTIuMSAwLTMuNS0uNi0zLjUtMi4zIDAtLjQuMS0uOS4xLTEuMy4xLS41LjEtLjkuMS0xLjMgMC0uNS0uMi0xLTEuNy0xdi0xLjl6Ii8+CiAgICA8Y2lyY2xlIGN4PSIxMSIgY3k9IjEzLjgiIHI9IjIuMSIvPgogICAgPGNpcmNsZSBjeD0iMTEiIGN5PSI4LjIiIHI9IjIuMSIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-julia: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDMyNSAzMDAiPgogIDxnIGNsYXNzPSJqcC1icmFuZDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjY2IzYzMzIj4KICAgIDxwYXRoIGQ9Ik0gMTUwLjg5ODQzOCAyMjUgQyAxNTAuODk4NDM4IDI2Ni40MjE4NzUgMTE3LjMyMDMxMiAzMDAgNzUuODk4NDM4IDMwMCBDIDM0LjQ3NjU2MiAzMDAgMC44OTg0MzggMjY2LjQyMTg3NSAwLjg5ODQzOCAyMjUgQyAwLjg5ODQzOCAxODMuNTc4MTI1IDM0LjQ3NjU2MiAxNTAgNzUuODk4NDM4IDE1MCBDIDExNy4zMjAzMTIgMTUwIDE1MC44OTg0MzggMTgzLjU3ODEyNSAxNTAuODk4NDM4IDIyNSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzM4OTgyNiI+CiAgICA8cGF0aCBkPSJNIDIzNy41IDc1IEMgMjM3LjUgMTE2LjQyMTg3NSAyMDMuOTIxODc1IDE1MCAxNjIuNSAxNTAgQyAxMjEuMDc4MTI1IDE1MCA4Ny41IDExNi40MjE4NzUgODcuNSA3NSBDIDg3LjUgMzMuNTc4MTI1IDEyMS4wNzgxMjUgMCAxNjIuNSAwIEMgMjAzLjkyMTg3NSAwIDIzNy41IDMzLjU3ODEyNSAyMzcuNSA3NSIvPgogIDwvZz4KICA8ZyBjbGFzcz0ianAtYnJhbmQwIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzk1NThiMiI+CiAgICA8cGF0aCBkPSJNIDMyNC4xMDE1NjIgMjI1IEMgMzI0LjEwMTU2MiAyNjYuNDIxODc1IDI5MC41MjM0MzggMzAwIDI0OS4xMDE1NjIgMzAwIEMgMjA3LjY3OTY4OCAzMDAgMTc0LjEwMTU2MiAyNjYuNDIxODc1IDE3NC4xMDE1NjIgMjI1IEMgMTc0LjEwMTU2MiAxODMuNTc4MTI1IDIwNy42Nzk2ODggMTUwIDI0OS4xMDE1NjIgMTUwIEMgMjkwLjUyMzQzOCAxNTAgMzI0LjEwMTU2MiAxODMuNTc4MTI1IDMyNC4xMDE1NjIgMjI1Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-jupyter-favicon: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTUyIiBoZWlnaHQ9IjE2NSIgdmlld0JveD0iMCAwIDE1MiAxNjUiIHZlcnNpb249IjEuMSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgPGcgY2xhc3M9ImpwLWp1cHl0ZXItaWNvbi1jb2xvciIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA3ODk0NywgMTEwLjU4MjkyNykiIGQ9Ik03NS45NDIyODQyLDI5LjU4MDQ1NjEgQzQzLjMwMjM5NDcsMjkuNTgwNDU2MSAxNC43OTY3ODMyLDE3LjY1MzQ2MzQgMCwwIEM1LjUxMDgzMjExLDE1Ljg0MDY4MjkgMTUuNzgxNTM4OSwyOS41NjY3NzMyIDI5LjM5MDQ5NDcsMzkuMjc4NDE3MSBDNDIuOTk5Nyw0OC45ODk4NTM3IDU5LjI3MzcsNTQuMjA2NzgwNSA3NS45NjA1Nzg5LDU0LjIwNjc4MDUgQzkyLjY0NzQ1NzksNTQuMjA2NzgwNSAxMDguOTIxNDU4LDQ4Ljk4OTg1MzcgMTIyLjUzMDY2MywzOS4yNzg0MTcxIEMxMzYuMTM5NDUzLDI5LjU2Njc3MzIgMTQ2LjQxMDI4NCwxNS44NDA2ODI5IDE1MS45MjExNTgsMCBDMTM3LjA4Nzg2OCwxNy42NTM0NjM0IDEwOC41ODI1ODksMjkuNTgwNDU2MSA3NS45NDIyODQyLDI5LjU4MDQ1NjEgTDc1Ljk0MjI4NDIsMjkuNTgwNDU2MSBaIiAvPgogICAgPHBhdGggdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMzczNjgsIDAuNzA0ODc4KSIgZD0iTTc1Ljk3ODQ1NzksMjQuNjI2NDA3MyBDMTA4LjYxODc2MywyNC42MjY0MDczIDEzNy4xMjQ0NTgsMzYuNTUzNDQxNSAxNTEuOTIxMTU4LDU0LjIwNjc4MDUgQzE0Ni40MTAyODQsMzguMzY2MjIyIDEzNi4xMzk0NTMsMjQuNjQwMTMxNyAxMjIuNTMwNjYzLDE0LjkyODQ4NzggQzEwOC45MjE0NTgsNS4yMTY4NDM5IDkyLjY0NzQ1NzksMCA3NS45NjA1Nzg5LDAgQzU5LjI3MzcsMCA0Mi45OTk3LDUuMjE2ODQzOSAyOS4zOTA0OTQ3LDE0LjkyODQ4NzggQzE1Ljc4MTUzODksMjQuNjQwMTMxNyA1LjUxMDgzMjExLDM4LjM2NjIyMiAwLDU0LjIwNjc4MDUgQzE0LjgzMzA4MTYsMzYuNTg5OTI5MyA0My4zMzg1Njg0LDI0LjYyNjQwNzMgNzUuOTc4NDU3OSwyNC42MjY0MDczIEw3NS45Nzg0NTc5LDI0LjYyNjQwNzMgWiIgLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-jupyter: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzkiIGhlaWdodD0iNTEiIHZpZXdCb3g9IjAgMCAzOSA1MSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgtMTYzOCAtMjI4MSkiPgogICAgIDxnIGNsYXNzPSJqcC1qdXB5dGVyLWljb24tY29sb3IiIGZpbGw9IiNGMzc3MjYiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5Ljc0IDIzMTEuOTgpIiBkPSJNIDE4LjI2NDYgNy4xMzQxMUMgMTAuNDE0NSA3LjEzNDExIDMuNTU4NzIgNC4yNTc2IDAgMEMgMS4zMjUzOSAzLjgyMDQgMy43OTU1NiA3LjEzMDgxIDcuMDY4NiA5LjQ3MzAzQyAxMC4zNDE3IDExLjgxNTIgMTQuMjU1NyAxMy4wNzM0IDE4LjI2OSAxMy4wNzM0QyAyMi4yODIzIDEzLjA3MzQgMjYuMTk2MyAxMS44MTUyIDI5LjQ2OTQgOS40NzMwM0MgMzIuNzQyNCA3LjEzMDgxIDM1LjIxMjYgMy44MjA0IDM2LjUzOCAwQyAzMi45NzA1IDQuMjU3NiAyNi4xMTQ4IDcuMTM0MTEgMTguMjY0NiA3LjEzNDExWiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM5LjczIDIyODUuNDgpIiBkPSJNIDE4LjI3MzMgNS45MzkzMUMgMjYuMTIzNSA1LjkzOTMxIDMyLjk3OTMgOC44MTU4MyAzNi41MzggMTMuMDczNEMgMzUuMjEyNiA5LjI1MzAzIDMyLjc0MjQgNS45NDI2MiAyOS40Njk0IDMuNjAwNEMgMjYuMTk2MyAxLjI1ODE4IDIyLjI4MjMgMCAxOC4yNjkgMEMgMTQuMjU1NyAwIDEwLjM0MTcgMS4yNTgxOCA3LjA2ODYgMy42MDA0QyAzLjc5NTU2IDUuOTQyNjIgMS4zMjUzOSA5LjI1MzAzIDAgMTMuMDczNEMgMy41Njc0NSA4LjgyNDYzIDEwLjQyMzIgNS45MzkzMSAxOC4yNzMzIDUuOTM5MzFaIi8+CiAgICA8L2c+CiAgICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjY5LjMgMjI4MS4zMSkiIGQ9Ik0gNS44OTM1MyAyLjg0NEMgNS45MTg4OSAzLjQzMTY1IDUuNzcwODUgNC4wMTM2NyA1LjQ2ODE1IDQuNTE2NDVDIDUuMTY1NDUgNS4wMTkyMiA0LjcyMTY4IDUuNDIwMTUgNC4xOTI5OSA1LjY2ODUxQyAzLjY2NDMgNS45MTY4OCAzLjA3NDQ0IDYuMDAxNTEgMi40OTgwNSA1LjkxMTcxQyAxLjkyMTY2IDUuODIxOSAxLjM4NDYzIDUuNTYxNyAwLjk1NDg5OCA1LjE2NDAxQyAwLjUyNTE3IDQuNzY2MzMgMC4yMjIwNTYgNC4yNDkwMyAwLjA4MzkwMzcgMy42Nzc1N0MgLTAuMDU0MjQ4MyAzLjEwNjExIC0wLjAyMTIzIDIuNTA2MTcgMC4xNzg3ODEgMS45NTM2NEMgMC4zNzg3OTMgMS40MDExIDAuNzM2ODA5IDAuOTIwODE3IDEuMjA3NTQgMC41NzM1MzhDIDEuNjc4MjYgMC4yMjYyNTkgMi4yNDA1NSAwLjAyNzU5MTkgMi44MjMyNiAwLjAwMjY3MjI5QyAzLjYwMzg5IC0wLjAzMDcxMTUgNC4zNjU3MyAwLjI0OTc4OSA0Ljk0MTQyIDAuNzgyNTUxQyA1LjUxNzExIDEuMzE1MzEgNS44NTk1NiAyLjA1Njc2IDUuODkzNTMgMi44NDRaIi8+CiAgICAgIDxwYXRoIHRyYW5zZm9ybT0idHJhbnNsYXRlKDE2MzkuOCAyMzIzLjgxKSIgZD0iTSA3LjQyNzg5IDMuNTgzMzhDIDcuNDYwMDggNC4zMjQzIDcuMjczNTUgNS4wNTgxOSA2Ljg5MTkzIDUuNjkyMTNDIDYuNTEwMzEgNi4zMjYwNyA1Ljk1MDc1IDYuODMxNTYgNS4yODQxMSA3LjE0NDZDIDQuNjE3NDcgNy40NTc2MyAzLjg3MzcxIDcuNTY0MTQgMy4xNDcwMiA3LjQ1MDYzQyAyLjQyMDMyIDcuMzM3MTIgMS43NDMzNiA3LjAwODcgMS4yMDE4NCA2LjUwNjk1QyAwLjY2MDMyOCA2LjAwNTIgMC4yNzg2MSA1LjM1MjY4IDAuMTA1MDE3IDQuNjMyMDJDIC0wLjA2ODU3NTcgMy45MTEzNSAtMC4wMjYyMzYxIDMuMTU0OTQgMC4yMjY2NzUgMi40NTg1NkMgMC40Nzk1ODcgMS43NjIxNyAwLjkzMTY5NyAxLjE1NzEzIDEuNTI1NzYgMC43MjAwMzNDIDIuMTE5ODMgMC4yODI5MzUgMi44MjkxNCAwLjAzMzQzOTUgMy41NjM4OSAwLjAwMzEzMzQ0QyA0LjU0NjY3IC0wLjAzNzQwMzMgNS41MDUyOSAwLjMxNjcwNiA2LjIyOTYxIDAuOTg3ODM1QyA2Ljk1MzkzIDEuNjU4OTYgNy4zODQ4NCAyLjU5MjM1IDcuNDI3ODkgMy41ODMzOEwgNy40Mjc4OSAzLjU4MzM4WiIvPgogICAgICA8cGF0aCB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxNjM4LjM2IDIyODYuMDYpIiBkPSJNIDIuMjc0NzEgNC4zOTYyOUMgMS44NDM2MyA0LjQxNTA4IDEuNDE2NzEgNC4zMDQ0NSAxLjA0Nzk5IDQuMDc4NDNDIDAuNjc5MjY4IDMuODUyNCAwLjM4NTMyOCAzLjUyMTE0IDAuMjAzMzcxIDMuMTI2NTZDIDAuMDIxNDEzNiAyLjczMTk4IC0wLjA0MDM3OTggMi4yOTE4MyAwLjAyNTgxMTYgMS44NjE4MUMgMC4wOTIwMDMxIDEuNDMxOCAwLjI4MzIwNCAxLjAzMTI2IDAuNTc1MjEzIDAuNzEwODgzQyAwLjg2NzIyMiAwLjM5MDUxIDEuMjQ2OTEgMC4xNjQ3MDggMS42NjYyMiAwLjA2MjA1OTJDIDIuMDg1NTMgLTAuMDQwNTg5NyAyLjUyNTYxIC0wLjAxNTQ3MTQgMi45MzA3NiAwLjEzNDIzNUMgMy4zMzU5MSAwLjI4Mzk0MSAzLjY4NzkyIDAuNTUxNTA1IDMuOTQyMjIgMC45MDMwNkMgNC4xOTY1MiAxLjI1NDYyIDQuMzQxNjkgMS42NzQzNiA0LjM1OTM1IDIuMTA5MTZDIDQuMzgyOTkgMi42OTEwNyA0LjE3Njc4IDMuMjU4NjkgMy43ODU5NyAzLjY4NzQ2QyAzLjM5NTE2IDQuMTE2MjQgMi44NTE2NiA0LjM3MTE2IDIuMjc0NzEgNC4zOTYyOUwgMi4yNzQ3MSA0LjM5NjI5WiIvPgogICAgPC9nPgogIDwvZz4+Cjwvc3ZnPgo=);
  --jp-icon-jupyterlab-wordmark: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyMDAiIHZpZXdCb3g9IjAgMCAxODYwLjggNDc1Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0RTRFNEUiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDQ4MC4xMzY0MDEsIDY0LjI3MTQ5MykiPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC4wMDAwMDAsIDU4Ljg3NTU2NikiPgogICAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgwLjA4NzYwMywgMC4xNDAyOTQpIj4KICAgICAgICA8cGF0aCBkPSJNLTQyNi45LDE2OS44YzAsNDguNy0zLjcsNjQuNy0xMy42LDc2LjRjLTEwLjgsMTAtMjUsMTUuNS0zOS43LDE1LjVsMy43LDI5IGMyMi44LDAuMyw0NC44LTcuOSw2MS45LTIzLjFjMTcuOC0xOC41LDI0LTQ0LjEsMjQtODMuM1YwSC00Mjd2MTcwLjFMLTQyNi45LDE2OS44TC00MjYuOSwxNjkuOHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMTU1LjA0NTI5NiwgNTYuODM3MTA0KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuNTYyNDUzLCAxLjc5OTg0MikiPgogICAgICAgIDxwYXRoIGQ9Ik0tMzEyLDE0OGMwLDIxLDAsMzkuNSwxLjcsNTUuNGgtMzEuOGwtMi4xLTMzLjNoLTAuOGMtNi43LDExLjYtMTYuNCwyMS4zLTI4LDI3LjkgYy0xMS42LDYuNi0yNC44LDEwLTM4LjIsOS44Yy0zMS40LDAtNjktMTcuNy02OS04OVYwaDM2LjR2MTEyLjdjMCwzOC43LDExLjYsNjQuNyw0NC42LDY0LjdjMTAuMy0wLjIsMjAuNC0zLjUsMjguOS05LjQgYzguNS01LjksMTUuMS0xNC4zLDE4LjktMjMuOWMyLjItNi4xLDMuMy0xMi41LDMuMy0xOC45VjAuMmgzNi40VjE0OEgtMzEyTC0zMTIsMTQ4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgzOTAuMDEzMzIyLCA1My40Nzk2MzgpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS43MDY0NTgsIDAuMjMxNDI1KSI+CiAgICAgICAgPHBhdGggZD0iTS00NzguNiw3MS40YzAtMjYtMC44LTQ3LTEuNy02Ni43aDMyLjdsMS43LDM0LjhoMC44YzcuMS0xMi41LDE3LjUtMjIuOCwzMC4xLTI5LjcgYzEyLjUtNywyNi43LTEwLjMsNDEtOS44YzQ4LjMsMCw4NC43LDQxLjcsODQuNywxMDMuM2MwLDczLjEtNDMuNywxMDkuMi05MSwxMDkuMmMtMTIuMSwwLjUtMjQuMi0yLjItMzUtNy44IGMtMTAuOC01LjYtMTkuOS0xMy45LTI2LjYtMjQuMmgtMC44VjI5MWgtMzZ2LTIyMEwtNDc4LjYsNzEuNEwtNDc4LjYsNzEuNHogTS00NDIuNiwxMjUuNmMwLjEsNS4xLDAuNiwxMC4xLDEuNywxNS4xIGMzLDEyLjMsOS45LDIzLjMsMTkuOCwzMS4xYzkuOSw3LjgsMjIuMSwxMi4xLDM0LjcsMTIuMWMzOC41LDAsNjAuNy0zMS45LDYwLjctNzguNWMwLTQwLjctMjEuMS03NS42LTU5LjUtNzUuNiBjLTEyLjksMC40LTI1LjMsNS4xLTM1LjMsMTMuNGMtOS45LDguMy0xNi45LDE5LjctMTkuNiwzMi40Yy0xLjUsNC45LTIuMywxMC0yLjUsMTUuMVYxMjUuNkwtNDQyLjYsMTI1LjZMLTQ0Mi42LDEyNS42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSg2MDYuNzQwNzI2LCA1Ni44MzcxMDQpIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMC43NTEyMjYsIDEuOTg5Mjk5KSI+CiAgICAgICAgPHBhdGggZD0iTS00NDAuOCwwbDQzLjcsMTIwLjFjNC41LDEzLjQsOS41LDI5LjQsMTIuOCw0MS43aDAuOGMzLjctMTIuMiw3LjktMjcuNywxMi44LTQyLjQgbDM5LjctMTE5LjJoMzguNUwtMzQ2LjksMTQ1Yy0yNiw2OS43LTQzLjcsMTA1LjQtNjguNiwxMjcuMmMtMTIuNSwxMS43LTI3LjksMjAtNDQuNiwyMy45bC05LjEtMzEuMSBjMTEuNy0zLjksMjIuNS0xMC4xLDMxLjgtMTguMWMxMy4yLTExLjEsMjMuNy0yNS4yLDMwLjYtNDEuMmMxLjUtMi44LDIuNS01LjcsMi45LTguOGMtMC4zLTMuMy0xLjItNi42LTIuNS05LjdMLTQ4MC4yLDAuMSBoMzkuN0wtNDQwLjgsMEwtNDQwLjgsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoODIyLjc0ODEwNCwgMC4wMDAwMDApIj4KICAgICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoMS40NjQwNTAsIDAuMzc4OTE0KSI+CiAgICAgICAgPHBhdGggZD0iTS00MTMuNywwdjU4LjNoNTJ2MjguMmgtNTJWMTk2YzAsMjUsNywzOS41LDI3LjMsMzkuNWM3LjEsMC4xLDE0LjItMC43LDIxLjEtMi41IGwxLjcsMjcuN2MtMTAuMywzLjctMjEuMyw1LjQtMzIuMiw1Yy03LjMsMC40LTE0LjYtMC43LTIxLjMtMy40Yy02LjgtMi43LTEyLjktNi44LTE3LjktMTIuMWMtMTAuMy0xMC45LTE0LjEtMjktMTQuMS01Mi45IFY4Ni41aC0zMVY1OC4zaDMxVjkuNkwtNDEzLjcsMEwtNDEzLjcsMHoiLz4KICAgICAgPC9nPgogICAgPC9nPgogICAgPGcgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOTc0LjQzMzI4NiwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDAuOTkwMDM0LCAwLjYxMDMzOSkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDQ1LjgsMTEzYzAuOCw1MCwzMi4yLDcwLjYsNjguNiw3MC42YzE5LDAuNiwzNy45LTMsNTUuMy0xMC41bDYuMiwyNi40IGMtMjAuOSw4LjktNDMuNSwxMy4xLTY2LjIsMTIuNmMtNjEuNSwwLTk4LjMtNDEuMi05OC4zLTEwMi41Qy00ODAuMiw0OC4yLTQ0NC43LDAtMzg2LjUsMGM2NS4yLDAsODIuNyw1OC4zLDgyLjcsOTUuNyBjLTAuMSw1LjgtMC41LDExLjUtMS4yLDE3LjJoLTE0MC42SC00NDUuOEwtNDQ1LjgsMTEzeiBNLTMzOS4yLDg2LjZjMC40LTIzLjUtOS41LTYwLjEtNTAuNC02MC4xIGMtMzYuOCwwLTUyLjgsMzQuNC01NS43LDYwLjFILTMzOS4yTC0zMzkuMiw4Ni42TC0zMzkuMiw4Ni42eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgICA8ZyB0cmFuc2Zvcm09InRyYW5zbGF0ZSgxMjAxLjk2MTA1OCwgNTMuNDc5NjM4KSI+CiAgICAgIDxnIHRyYW5zZm9ybT0idHJhbnNsYXRlKDEuMTc5NjQwLCAwLjcwNTA2OCkiPgogICAgICAgIDxwYXRoIGQ9Ik0tNDc4LjYsNjhjMC0yMy45LTAuNC00NC41LTEuNy02My40aDMxLjhsMS4yLDM5LjloMS43YzkuMS0yNy4zLDMxLTQ0LjUsNTUuMy00NC41IGMzLjUtMC4xLDcsMC40LDEwLjMsMS4ydjM0LjhjLTQuMS0wLjktOC4yLTEuMy0xMi40LTEuMmMtMjUuNiwwLTQzLjcsMTkuNy00OC43LDQ3LjRjLTEsNS43LTEuNiwxMS41LTEuNywxNy4ydjEwOC4zaC0zNlY2OCBMLTQ3OC42LDY4eiIvPgogICAgICA8L2c+CiAgICA8L2c+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi13YXJuMCIgZmlsbD0iI0YzNzcyNiI+CiAgICA8cGF0aCBkPSJNMTM1Mi4zLDMyNi4yaDM3VjI4aC0zN1YzMjYuMnogTTE2MDQuOCwzMjYuMmMtMi41LTEzLjktMy40LTMxLjEtMy40LTQ4Ljd2LTc2IGMwLTQwLjctMTUuMS04My4xLTc3LjMtODMuMWMtMjUuNiwwLTUwLDcuMS02Ni44LDE4LjFsOC40LDI0LjRjMTQuMy05LjIsMzQtMTUuMSw1My0xNS4xYzQxLjYsMCw0Ni4yLDMwLjIsNDYuMiw0N3Y0LjIgYy03OC42LTAuNC0xMjIuMywyNi41LTEyMi4zLDc1LjZjMCwyOS40LDIxLDU4LjQsNjIuMiw1OC40YzI5LDAsNTAuOS0xNC4zLDYyLjItMzAuMmgxLjNsMi45LDI1LjZIMTYwNC44eiBNMTU2NS43LDI1Ny43IGMwLDMuOC0wLjgsOC0yLjEsMTEuOGMtNS45LDE3LjItMjIuNywzNC00OS4yLDM0Yy0xOC45LDAtMzQuOS0xMS4zLTM0LjktMzUuM2MwLTM5LjUsNDUuOC00Ni42LDg2LjItNDUuOFYyNTcuN3ogTTE2OTguNSwzMjYuMiBsMS43LTMzLjZoMS4zYzE1LjEsMjYuOSwzOC43LDM4LjIsNjguMSwzOC4yYzQ1LjQsMCw5MS4yLTM2LjEsOTEuMi0xMDguOGMwLjQtNjEuNy0zNS4zLTEwMy43LTg1LjctMTAzLjcgYy0zMi44LDAtNTYuMywxNC43LTY5LjMsMzcuNGgtMC44VjI4aC0zNi42djI0NS43YzAsMTguMS0wLjgsMzguNi0xLjcsNTIuNUgxNjk4LjV6IE0xNzA0LjgsMjA4LjJjMC01LjksMS4zLTEwLjksMi4xLTE1LjEgYzcuNi0yOC4xLDMxLjEtNDUuNCw1Ni4zLTQ1LjRjMzkuNSwwLDYwLjUsMzQuOSw2MC41LDc1LjZjMCw0Ni42LTIzLjEsNzguMS02MS44LDc4LjFjLTI2LjksMC00OC4zLTE3LjYtNTUuNS00My4zIGMtMC44LTQuMi0xLjctOC44LTEuNy0xMy40VjIwOC4yeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzYxNjE2MSIgZD0iTTE1IDlIOXY2aDZWOXptLTIgNGgtMnYtMmgydjJ6bTgtMlY5aC0yVjdjMC0xLjEtLjktMi0yLTJoLTJWM2gtMnYyaC0yVjNIOXYySDdjLTEuMSAwLTIgLjktMiAydjJIM3YyaDJ2MkgzdjJoMnYyYzAgMS4xLjkgMiAyIDJoMnYyaDJ2LTJoMnYyaDJ2LTJoMmMxLjEgMCAyLS45IDItMnYtMmgydi0yaC0ydi0yaDJ6bS00IDZIN1Y3aDEwdjEweiIvPgo8L3N2Zz4K);
  --jp-icon-keyboard: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMjAgNUg0Yy0xLjEgMC0xLjk5LjktMS45OSAyTDIgMTdjMCAxLjEuOSAyIDIgMmgxNmMxLjEgMCAyLS45IDItMlY3YzAtMS4xLS45LTItMi0yem0tOSAzaDJ2MmgtMlY4em0wIDNoMnYyaC0ydi0yek04IDhoMnYySDhWOHptMCAzaDJ2Mkg4di0yem0tMSAySDV2LTJoMnYyem0wLTNINVY4aDJ2MnptOSA3SDh2LTJoOHYyem0wLTRoLTJ2LTJoMnYyem0wLTNoLTJWOGgydjJ6bTMgM2gtMnYtMmgydjJ6bTAtM2gtMlY4aDJ2MnoiLz4KPC9zdmc+Cg==);
  --jp-icon-launch: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMzIgMzIiIHdpZHRoPSIzMiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik0yNiwyOEg2YTIuMDAyNywyLjAwMjcsMCwwLDEtMi0yVjZBMi4wMDI3LDIuMDAyNywwLDAsMSw2LDRIMTZWNkg2VjI2SDI2VjE2aDJWMjZBMi4wMDI3LDIuMDAyNywwLDAsMSwyNiwyOFoiLz4KICAgIDxwb2x5Z29uIHBvaW50cz0iMjAgMiAyMCA0IDI2LjU4NiA0IDE4IDEyLjU4NiAxOS40MTQgMTQgMjggNS40MTQgMjggMTIgMzAgMTIgMzAgMiAyMCAyIi8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-launcher: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkgMTlINVY1aDdWM0g1YTIgMiAwIDAwLTIgMnYxNGEyIDIgMCAwMDIgMmgxNGMxLjEgMCAyLS45IDItMnYtN2gtMnY3ek0xNCAzdjJoMy41OWwtOS44MyA5LjgzIDEuNDEgMS40MUwxOSA2LjQxVjEwaDJWM2gtN3oiLz4KPC9zdmc+Cg==);
  --jp-icon-line-form: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGZpbGw9IndoaXRlIiBkPSJNNS44OCA0LjEyTDEzLjc2IDEybC03Ljg4IDcuODhMOCAyMmwxMC0xMEw4IDJ6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-link: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTMuOSAxMmMwLTEuNzEgMS4zOS0zLjEgMy4xLTMuMWg0VjdIN2MtMi43NiAwLTUgMi4yNC01IDVzMi4yNCA1IDUgNWg0di0xLjlIN2MtMS43MSAwLTMuMS0xLjM5LTMuMS0zLjF6TTggMTNoOHYtMkg4djJ6bTktNmgtNHYxLjloNGMxLjcxIDAgMy4xIDEuMzkgMy4xIDMuMXMtMS4zOSAzLjEtMy4xIDMuMWgtNFYxN2g0YzIuNzYgMCA1LTIuMjQgNS01cy0yLjI0LTUtNS01eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-list: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xOSA1djE0SDVWNWgxNG0xLjEtMkgzLjljLS41IDAtLjkuNC0uOS45djE2LjJjMCAuNC40LjkuOS45aDE2LjJjLjQgMCAuOS0uNS45LS45VjMuOWMwLS41LS41LS45LS45LS45ek0xMSA3aDZ2MmgtNlY3em0wIDRoNnYyaC02di0yem0wIDRoNnYyaC02ek03IDdoMnYySDd6bTAgNGgydjJIN3ptMCA0aDJ2Mkg3eiIvPgo8L3N2Zz4K);
  --jp-icon-markdown: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDAganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjN0IxRkEyIiBkPSJNNSAxNC45aDEybC02LjEgNnptOS40LTYuOGMwLTEuMy0uMS0yLjktLjEtNC41LS40IDEuNC0uOSAyLjktMS4zIDQuM2wtMS4zIDQuM2gtMkw4LjUgNy45Yy0uNC0xLjMtLjctMi45LTEtNC4zLS4xIDEuNi0uMSAzLjItLjIgNC42TDcgMTIuNEg0LjhsLjctMTFoMy4zTDEwIDVjLjQgMS4yLjcgMi43IDEgMy45LjMtMS4yLjctMi42IDEtMy45bDEuMi0zLjdoMy4zbC42IDExaC0yLjRsLS4zLTQuMnoiLz4KPC9zdmc+Cg==);
  --jp-icon-move-down: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMTIuNDcxIDcuNTI4OTlDMTIuNzYzMiA3LjIzNjg0IDEyLjc2MzIgNi43NjMxNiAxMi40NzEgNi40NzEwMVY2LjQ3MTAxQzEyLjE3OSA2LjE3OTA1IDExLjcwNTcgNi4xNzg4NCAxMS40MTM1IDYuNDcwNTRMNy43NSAxMC4xMjc1VjEuNzVDNy43NSAxLjMzNTc5IDcuNDE0MjEgMSA3IDFWMUM2LjU4NTc5IDEgNi4yNSAxLjMzNTc5IDYuMjUgMS43NVYxMC4xMjc1TDIuNTk3MjYgNi40NjgyMkMyLjMwMzM4IDYuMTczODEgMS44MjY0MSA2LjE3MzU5IDEuNTMyMjYgNi40Njc3NFY2LjQ2Nzc0QzEuMjM4MyA2Ljc2MTcgMS4yMzgzIDcuMjM4MyAxLjUzMjI2IDcuNTMyMjZMNi4yOTI4OSAxMi4yOTI5QzYuNjgzNDIgMTIuNjgzNCA3LjMxNjU4IDEyLjY4MzQgNy43MDcxMSAxMi4yOTI5TDEyLjQ3MSA3LjUyODk5WiIgZmlsbD0iIzYxNjE2MSIvPgo8L3N2Zz4K);
  --jp-icon-move-up: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTQiIGhlaWdodD0iMTQiIHZpZXdCb3g9IjAgMCAxNCAxNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggY2xhc3M9ImpwLWljb24zIiBkPSJNMS41Mjg5OSA2LjQ3MTAxQzEuMjM2ODQgNi43NjMxNiAxLjIzNjg0IDcuMjM2ODQgMS41Mjg5OSA3LjUyODk5VjcuNTI4OTlDMS44MjA5NSA3LjgyMDk1IDIuMjk0MjYgNy44MjExNiAyLjU4NjQ5IDcuNTI5NDZMNi4yNSAzLjg3MjVWMTIuMjVDNi4yNSAxMi42NjQyIDYuNTg1NzkgMTMgNyAxM1YxM0M3LjQxNDIxIDEzIDcuNzUgMTIuNjY0MiA3Ljc1IDEyLjI1VjMuODcyNUwxMS40MDI3IDcuNTMxNzhDMTEuNjk2NiA3LjgyNjE5IDEyLjE3MzYgNy44MjY0MSAxMi40Njc3IDcuNTMyMjZWNy41MzIyNkMxMi43NjE3IDcuMjM4MyAxMi43NjE3IDYuNzYxNyAxMi40Njc3IDYuNDY3NzRMNy43MDcxMSAxLjcwNzExQzcuMzE2NTggMS4zMTY1OCA2LjY4MzQyIDEuMzE2NTggNi4yOTI4OSAxLjcwNzExTDEuNTI4OTkgNi40NzEwMVoiIGZpbGw9IiM2MTYxNjEiLz4KPC9zdmc+Cg==);
  --jp-icon-new-folder: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIwIDZoLThsLTItMkg0Yy0xLjExIDAtMS45OS44OS0xLjk5IDJMMiAxOGMwIDEuMTEuODkgMiAyIDJoMTZjMS4xMSAwIDItLjg5IDItMlY4YzAtMS4xMS0uODktMi0yLTJ6bS0xIDhoLTN2M2gtMnYtM2gtM3YtMmgzVjloMnYzaDN2MnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-not-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI1IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMTkgMTcuMTg0NCAyLjk2OTY4IDE0LjMwMzIgMS44NjA5NCAxMS40NDA5WiIvPgogICAgPHBhdGggY2xhc3M9ImpwLWljb24yIiBzdHJva2U9IiMzMzMzMzMiIHN0cm9rZS13aWR0aD0iMiIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOS4zMTU5MiA5LjMyMDMxKSIgZD0iTTcuMzY4NDIgMEwwIDcuMzY0NzkiLz4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDkuMzE1OTIgMTYuNjgzNikgc2NhbGUoMSAtMSkiIGQ9Ik03LjM2ODQyIDBMMCA3LjM2NDc5Ii8+Cjwvc3ZnPgo=);
  --jp-icon-notebook: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtbm90ZWJvb2staWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiNFRjZDMDAiPgogICAgPHBhdGggZD0iTTE4LjcgMy4zdjE1LjRIMy4zVjMuM2gxNS40bTEuNS0xLjVIMS44djE4LjNoMTguM2wuMS0xOC4zeiIvPgogICAgPHBhdGggZD0iTTE2LjUgMTYuNWwtNS40LTQuMy01LjYgNC4zdi0xMWgxMXoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-numbering: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjIiIGhlaWdodD0iMjIiIHZpZXdCb3g9IjAgMCAyOCAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTQgMTlINlYxOS41SDVWMjAuNUg2VjIxSDRWMjJIN1YxOEg0VjE5Wk01IDEwSDZWNkg0VjdINVYxMFpNNCAxM0g1LjhMNCAxNS4xVjE2SDdWMTVINS4yTDcgMTIuOVYxMkg0VjEzWk05IDdWOUgyM1Y3SDlaTTkgMjFIMjNWMTlIOVYyMVpNOSAxNUgyM1YxM0g5VjE1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-offline-bolt: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyIDIuMDJjLTUuNTEgMC05Ljk4IDQuNDctOS45OCA5Ljk4czQuNDcgOS45OCA5Ljk4IDkuOTggOS45OC00LjQ3IDkuOTgtOS45OFMxNy41MSAyLjAyIDEyIDIuMDJ6TTExLjQ4IDIwdi02LjI2SDhMMTMgNHY2LjI2aDMuMzVMMTEuNDggMjB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-palette: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE4IDEzVjIwSDRWNkg5LjAyQzkuMDcgNS4yOSA5LjI0IDQuNjIgOS41IDRINEMyLjkgNCAyIDQuOSAyIDZWMjBDMiAyMS4xIDIuOSAyMiA0IDIySDE4QzE5LjEgMjIgMjAgMjEuMSAyMCAyMFYxNUwxOCAxM1pNMTkuMyA4Ljg5QzE5Ljc0IDguMTkgMjAgNy4zOCAyMCA2LjVDMjAgNC4wMSAxNy45OSAyIDE1LjUgMkMxMy4wMSAyIDExIDQuMDEgMTEgNi41QzExIDguOTkgMTMuMDEgMTEgMTUuNDkgMTFDMTYuMzcgMTEgMTcuMTkgMTAuNzQgMTcuODggMTAuM0wyMSAxMy40MkwyMi40MiAxMkwxOS4zIDguODlaTTE1LjUgOUMxNC4xMiA5IDEzIDcuODggMTMgNi41QzEzIDUuMTIgMTQuMTIgNCAxNS41IDRDMTYuODggNCAxOCA1LjEyIDE4IDYuNUMxOCA3Ljg4IDE2Ljg4IDkgMTUuNSA5WiIvPgogICAgPHBhdGggZmlsbC1ydWxlPSJldmVub2RkIiBjbGlwLXJ1bGU9ImV2ZW5vZGQiIGQ9Ik00IDZIOS4wMTg5NEM5LjAwNjM5IDYuMTY1MDIgOSA2LjMzMTc2IDkgNi41QzkgOC44MTU3NyAxMC4yMTEgMTAuODQ4NyAxMi4wMzQzIDEySDlWMTRIMTZWMTIuOTgxMUMxNi41NzAzIDEyLjkzNzcgMTcuMTIgMTIuODIwNyAxNy42Mzk2IDEyLjYzOTZMMTggMTNWMjBINFY2Wk04IDhINlYxMEg4VjhaTTYgMTJIOFYxNEg2VjEyWk04IDE2SDZWMThIOFYxNlpNOSAxNkgxNlYxOEg5VjE2WiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-paste: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE5IDJoLTQuMThDMTQuNC44NCAxMy4zIDAgMTIgMGMtMS4zIDAtMi40Ljg0LTIuODIgMkg1Yy0xLjEgMC0yIC45LTIgMnYxNmMwIDEuMS45IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjRjMC0xLjEtLjktMi0yLTJ6bS03IDBjLjU1IDAgMSAuNDUgMSAxcy0uNDUgMS0xIDEtMS0uNDUtMS0xIC40NS0xIDEtMXptNyAxOEg1VjRoMnYzaDEwVjRoMnYxNnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-pdf: url(data:image/svg+xml;base64,PHN2ZwogICB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCAyMiAyMiIgd2lkdGg9IjE2Ij4KICAgIDxwYXRoIHRyYW5zZm9ybT0icm90YXRlKDQ1KSIgY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI0ZGMkEyQSIKICAgICAgIGQ9Im0gMjIuMzQ0MzY5LC0zLjAxNjM2NDIgaCA1LjYzODYwNCB2IDEuNTc5MjQzMyBoIC0zLjU0OTIyNyB2IDEuNTA4NjkyOTkgaCAzLjMzNzU3NiBWIDEuNjUwODE1NCBoIC0zLjMzNzU3NiB2IDMuNDM1MjYxMyBoIC0yLjA4OTM3NyB6IG0gLTcuMTM2NDQ0LDEuNTc5MjQzMyB2IDQuOTQzOTU0MyBoIDAuNzQ4OTIgcSAxLjI4MDc2MSwwIDEuOTUzNzAzLC0wLjYzNDk1MzUgMC42NzgzNjksLTAuNjM0OTUzNSAwLjY3ODM2OSwtMS44NDUxNjQxIDAsLTEuMjA0NzgzNTUgLTAuNjcyOTQyLC0xLjgzNDMxMDExIC0wLjY3Mjk0MiwtMC42Mjk1MjY1OSAtMS45NTkxMywtMC42Mjk1MjY1OSB6IG0gLTIuMDg5Mzc3LC0xLjU3OTI0MzMgaCAyLjIwMzM0MyBxIDEuODQ1MTY0LDAgMi43NDYwMzksMC4yNjU5MjA3IDAuOTA2MzAxLDAuMjYwNDkzNyAxLjU1MjEwOCwwLjg5MDAyMDMgMC41Njk4MywwLjU0ODEyMjMgMC44NDY2MDUsMS4yNjQ0ODAwNiAwLjI3Njc3NCwwLjcxNjM1NzgxIDAuMjc2Nzc0LDEuNjIyNjU4OTQgMCwwLjkxNzE1NTEgLTAuMjc2Nzc0LDEuNjM4OTM5OSAtMC4yNzY3NzUsMC43MTYzNTc4IC0wLjg0NjYwNSwxLjI2NDQ4IC0wLjY1MTIzNCwwLjYyOTUyNjYgLTEuNTYyOTYyLDAuODk1NDQ3MyAtMC45MTE3MjgsMC4yNjA0OTM3IC0yLjczNTE4NSwwLjI2MDQ5MzcgaCAtMi4yMDMzNDMgeiBtIC04LjE0NTg1NjUsMCBoIDMuNDY3ODIzIHEgMS41NDY2ODE2LDAgMi4zNzE1Nzg1LDAuNjg5MjIzIDAuODMwMzI0LDAuNjgzNzk2MSAwLjgzMDMyNCwxLjk1MzcwMzE0IDAsMS4yNzUzMzM5NyAtMC44MzAzMjQsMS45NjQ1NTcwNiBRIDkuOTg3MTk2MSwyLjI3NDkxNSA4LjQ0MDUxNDUsMi4yNzQ5MTUgSCA3LjA2MjA2ODQgViA1LjA4NjA3NjcgSCA0Ljk3MjY5MTUgWiBtIDIuMDg5Mzc2OSwxLjUxNDExOTkgdiAyLjI2MzAzOTQzIGggMS4xNTU5NDEgcSAwLjYwNzgxODgsMCAwLjkzODg2MjksLTAuMjkzMDU1NDcgMC4zMzEwNDQxLC0wLjI5ODQ4MjQxIDAuMzMxMDQ0MSwtMC44NDExNzc3MiAwLC0wLjU0MjY5NTMxIC0wLjMzMTA0NDEsLTAuODM1NzUwNzQgLTAuMzMxMDQ0MSwtMC4yOTMwNTU1IC0wLjkzODg2MjksLTAuMjkzMDU1NSB6IgovPgo8L3N2Zz4K);
  --jp-icon-python: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iLTEwIC0xMCAxMzEuMTYxMzYxNjk0MzM1OTQgMTMyLjM4ODk5OTkzODk2NDg0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMzA2OTk4IiBkPSJNIDU0LjkxODc4NSw5LjE5Mjc0MjFlLTQgQyA1MC4zMzUxMzIsMC4wMjIyMTcyNyA0NS45NTc4NDYsMC40MTMxMzY5NyA0Mi4xMDYyODUsMS4wOTQ2NjkzIDMwLjc2MDA2OSwzLjA5OTE3MzEgMjguNzAwMDM2LDcuMjk0NzcxNCAyOC43MDAwMzUsMTUuMDMyMTY5IHYgMTAuMjE4NzUgaCAyNi44MTI1IHYgMy40MDYyNSBoIC0yNi44MTI1IC0xMC4wNjI1IGMgLTcuNzkyNDU5LDAgLTE0LjYxNTc1ODgsNC42ODM3MTcgLTE2Ljc0OTk5OTgsMTMuNTkzNzUgLTIuNDYxODE5OTgsMTAuMjEyOTY2IC0yLjU3MTAxNTA4LDE2LjU4NjAyMyAwLDI3LjI1IDEuOTA1OTI4Myw3LjkzNzg1MiA2LjQ1NzU0MzIsMTMuNTkzNzQ4IDE0LjI0OTk5OTgsMTMuNTkzNzUgaCA5LjIxODc1IHYgLTEyLjI1IGMgMCwtOC44NDk5MDIgNy42NTcxNDQsLTE2LjY1NjI0OCAxNi43NSwtMTYuNjU2MjUgaCAyNi43ODEyNSBjIDcuNDU0OTUxLDAgMTMuNDA2MjUzLC02LjEzODE2NCAxMy40MDYyNSwtMTMuNjI1IHYgLTI1LjUzMTI1IGMgMCwtNy4yNjYzMzg2IC02LjEyOTk4LC0xMi43MjQ3NzcxIC0xMy40MDYyNSwtMTMuOTM3NDk5NyBDIDY0LjI4MTU0OCwwLjMyNzk0Mzk3IDU5LjUwMjQzOCwtMC4wMjAzNzkwMyA1NC45MTg3ODUsOS4xOTI3NDIxZS00IFogbSAtMTQuNSw4LjIxODc1MDEyNTc5IGMgMi43Njk1NDcsMCA1LjAzMTI1LDIuMjk4NjQ1NiA1LjAzMTI1LDUuMTI0OTk5NiAtMmUtNiwyLjgxNjMzNiAtMi4yNjE3MDMsNS4wOTM3NSAtNS4wMzEyNSw1LjA5Mzc1IC0yLjc3OTQ3NiwtMWUtNiAtNS4wMzEyNSwtMi4yNzc0MTUgLTUuMDMxMjUsLTUuMDkzNzUgLTEwZS03LC0yLjgyNjM1MyAyLjI1MTc3NCwtNS4xMjQ5OTk2IDUuMDMxMjUsLTUuMTI0OTk5NiB6Ii8+CiAgPHBhdGggY2xhc3M9ImpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iI2ZmZDQzYiIgZD0ibSA4NS42Mzc1MzUsMjguNjU3MTY5IHYgMTEuOTA2MjUgYyAwLDkuMjMwNzU1IC03LjgyNTg5NSwxNi45OTk5OTkgLTE2Ljc1LDE3IGggLTI2Ljc4MTI1IGMgLTcuMzM1ODMzLDAgLTEzLjQwNjI0OSw2LjI3ODQ4MyAtMTMuNDA2MjUsMTMuNjI1IHYgMjUuNTMxMjQ3IGMgMCw3LjI2NjM0NCA2LjMxODU4OCwxMS41NDAzMjQgMTMuNDA2MjUsMTMuNjI1MDA0IDguNDg3MzMxLDIuNDk1NjEgMTYuNjI2MjM3LDIuOTQ2NjMgMjYuNzgxMjUsMCA2Ljc1MDE1NSwtMS45NTQzOSAxMy40MDYyNTMsLTUuODg3NjEgMTMuNDA2MjUsLTEzLjYyNTAwNCBWIDg2LjUwMDkxOSBoIC0yNi43ODEyNSB2IC0zLjQwNjI1IGggMjYuNzgxMjUgMTMuNDA2MjU0IGMgNy43OTI0NjEsMCAxMC42OTYyNTEsLTUuNDM1NDA4IDEzLjQwNjI0MSwtMTMuNTkzNzUgMi43OTkzMywtOC4zOTg4ODYgMi42ODAyMiwtMTYuNDc1Nzc2IDAsLTI3LjI1IC0xLjkyNTc4LC03Ljc1NzQ0MSAtNS42MDM4NywtMTMuNTkzNzUgLTEzLjQwNjI0MSwtMTMuNTkzNzUgeiBtIC0xNS4wNjI1LDY0LjY1NjI1IGMgMi43Nzk0NzgsM2UtNiA1LjAzMTI1LDIuMjc3NDE3IDUuMDMxMjUsNS4wOTM3NDcgLTJlLTYsMi44MjYzNTQgLTIuMjUxNzc1LDUuMTI1MDA0IC01LjAzMTI1LDUuMTI1MDA0IC0yLjc2OTU1LDAgLTUuMDMxMjUsLTIuMjk4NjUgLTUuMDMxMjUsLTUuMTI1MDA0IDJlLTYsLTIuODE2MzMgMi4yNjE2OTcsLTUuMDkzNzQ3IDUuMDMxMjUsLTUuMDkzNzQ3IHoiLz4KPC9zdmc+Cg==);
  --jp-icon-r-kernel: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjE5NkYzIiBkPSJNNC40IDIuNWMxLjItLjEgMi45LS4zIDQuOS0uMyAyLjUgMCA0LjEuNCA1LjIgMS4zIDEgLjcgMS41IDEuOSAxLjUgMy41IDAgMi0xLjQgMy41LTIuOSA0LjEgMS4yLjQgMS43IDEuNiAyLjIgMyAuNiAxLjkgMSAzLjkgMS4zIDQuNmgtMy44Yy0uMy0uNC0uOC0xLjctMS4yLTMuN3MtMS4yLTIuNi0yLjYtMi42aC0uOXY2LjRINC40VjIuNXptMy43IDYuOWgxLjRjMS45IDAgMi45LS45IDIuOS0yLjNzLTEtMi4zLTIuOC0yLjNjLS43IDAtMS4zIDAtMS42LjJ2NC41aC4xdi0uMXoiLz4KPC9zdmc+Cg==);
  --jp-icon-react: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMTUwIDE1MCA1NDEuOSAyOTUuMyI+CiAgPGcgY2xhc3M9ImpwLWljb24tYnJhbmQyIGpwLWljb24tc2VsZWN0YWJsZSIgZmlsbD0iIzYxREFGQiI+CiAgICA8cGF0aCBkPSJNNjY2LjMgMjk2LjVjMC0zMi41LTQwLjctNjMuMy0xMDMuMS04Mi40IDE0LjQtNjMuNiA4LTExNC4yLTIwLjItMTMwLjQtNi41LTMuOC0xNC4xLTUuNi0yMi40LTUuNnYyMi4zYzQuNiAwIDguMy45IDExLjQgMi42IDEzLjYgNy44IDE5LjUgMzcuNSAxNC45IDc1LjctMS4xIDkuNC0yLjkgMTkuMy01LjEgMjkuNC0xOS42LTQuOC00MS04LjUtNjMuNS0xMC45LTEzLjUtMTguNS0yNy41LTM1LjMtNDEuNi01MCAzMi42LTMwLjMgNjMuMi00Ni45IDg0LTQ2LjlWNzhjLTI3LjUgMC02My41IDE5LjYtOTkuOSA1My42LTM2LjQtMzMuOC03Mi40LTUzLjItOTkuOS01My4ydjIyLjNjMjAuNyAwIDUxLjQgMTYuNSA4NCA0Ni42LTE0IDE0LjctMjggMzEuNC00MS4zIDQ5LjktMjIuNiAyLjQtNDQgNi4xLTYzLjYgMTEtMi4zLTEwLTQtMTkuNy01LjItMjktNC43LTM4LjIgMS4xLTY3LjkgMTQuNi03NS44IDMtMS44IDYuOS0yLjYgMTEuNS0yLjZWNzguNWMtOC40IDAtMTYgMS44LTIyLjYgNS42LTI4LjEgMTYuMi0zNC40IDY2LjctMTkuOSAxMzAuMS02Mi4yIDE5LjItMTAyLjcgNDkuOS0xMDIuNyA4Mi4zIDAgMzIuNSA0MC43IDYzLjMgMTAzLjEgODIuNC0xNC40IDYzLjYtOCAxMTQuMiAyMC4yIDEzMC40IDYuNSAzLjggMTQuMSA1LjYgMjIuNSA1LjYgMjcuNSAwIDYzLjUtMTkuNiA5OS45LTUzLjYgMzYuNCAzMy44IDcyLjQgNTMuMiA5OS45IDUzLjIgOC40IDAgMTYtMS44IDIyLjYtNS42IDI4LjEtMTYuMiAzNC40LTY2LjcgMTkuOS0xMzAuMSA2Mi0xOS4xIDEwMi41LTQ5LjkgMTAyLjUtODIuM3ptLTEzMC4yLTY2LjdjLTMuNyAxMi45LTguMyAyNi4yLTEzLjUgMzkuNS00LjEtOC04LjQtMTYtMTMuMS0yNC00LjYtOC05LjUtMTUuOC0xNC40LTIzLjQgMTQuMiAyLjEgMjcuOSA0LjcgNDEgNy45em0tNDUuOCAxMDYuNWMtNy44IDEzLjUtMTUuOCAyNi4zLTI0LjEgMzguMi0xNC45IDEuMy0zMCAyLTQ1LjIgMi0xNS4xIDAtMzAuMi0uNy00NS0xLjktOC4zLTExLjktMTYuNC0yNC42LTI0LjItMzgtNy42LTEzLjEtMTQuNS0yNi40LTIwLjgtMzkuOCA2LjItMTMuNCAxMy4yLTI2LjggMjAuNy0zOS45IDcuOC0xMy41IDE1LjgtMjYuMyAyNC4xLTM4LjIgMTQuOS0xLjMgMzAtMiA0NS4yLTIgMTUuMSAwIDMwLjIuNyA0NSAxLjkgOC4zIDExLjkgMTYuNCAyNC42IDI0LjIgMzggNy42IDEzLjEgMTQuNSAyNi40IDIwLjggMzkuOC02LjMgMTMuNC0xMy4yIDI2LjgtMjAuNyAzOS45em0zMi4zLTEzYzUuNCAxMy40IDEwIDI2LjggMTMuOCAzOS44LTEzLjEgMy4yLTI2LjkgNS45LTQxLjIgOCA0LjktNy43IDkuOC0xNS42IDE0LjQtMjMuNyA0LjYtOCA4LjktMTYuMSAxMy0yNC4xek00MjEuMiA0MzBjLTkuMy05LjYtMTguNi0yMC4zLTI3LjgtMzIgOSAuNCAxOC4yLjcgMjcuNS43IDkuNCAwIDE4LjctLjIgMjcuOC0uNy05IDExLjctMTguMyAyMi40LTI3LjUgMzJ6bS03NC40LTU4LjljLTE0LjItMi4xLTI3LjktNC43LTQxLTcuOSAzLjctMTIuOSA4LjMtMjYuMiAxMy41LTM5LjUgNC4xIDggOC40IDE2IDEzLjEgMjQgNC43IDggOS41IDE1LjggMTQuNCAyMy40ek00MjAuNyAxNjNjOS4zIDkuNiAxOC42IDIwLjMgMjcuOCAzMi05LS40LTE4LjItLjctMjcuNS0uNy05LjQgMC0xOC43LjItMjcuOC43IDktMTEuNyAxOC4zLTIyLjQgMjcuNS0zMnptLTc0IDU4LjljLTQuOSA3LjctOS44IDE1LjYtMTQuNCAyMy43LTQuNiA4LTguOSAxNi0xMyAyNC01LjQtMTMuNC0xMC0yNi44LTEzLjgtMzkuOCAxMy4xLTMuMSAyNi45LTUuOCA0MS4yLTcuOXptLTkwLjUgMTI1LjJjLTM1LjQtMTUuMS01OC4zLTM0LjktNTguMy01MC42IDAtMTUuNyAyMi45LTM1LjYgNTguMy01MC42IDguNi0zLjcgMTgtNyAyNy43LTEwLjEgNS43IDE5LjYgMTMuMiA0MCAyMi41IDYwLjktOS4yIDIwLjgtMTYuNiA0MS4xLTIyLjIgNjAuNi05LjktMy4xLTE5LjMtNi41LTI4LTEwLjJ6TTMxMCA0OTBjLTEzLjYtNy44LTE5LjUtMzcuNS0xNC45LTc1LjcgMS4xLTkuNCAyLjktMTkuMyA1LjEtMjkuNCAxOS42IDQuOCA0MSA4LjUgNjMuNSAxMC45IDEzLjUgMTguNSAyNy41IDM1LjMgNDEuNiA1MC0zMi42IDMwLjMtNjMuMiA0Ni45LTg0IDQ2LjktNC41LS4xLTguMy0xLTExLjMtMi43em0yMzcuMi03Ni4yYzQuNyAzOC4yLTEuMSA2Ny45LTE0LjYgNzUuOC0zIDEuOC02LjkgMi42LTExLjUgMi42LTIwLjcgMC01MS40LTE2LjUtODQtNDYuNiAxNC0xNC43IDI4LTMxLjQgNDEuMy00OS45IDIyLjYtMi40IDQ0LTYuMSA2My42LTExIDIuMyAxMC4xIDQuMSAxOS44IDUuMiAyOS4xem0zOC41LTY2LjdjLTguNiAzLjctMTggNy0yNy43IDEwLjEtNS43LTE5LjYtMTMuMi00MC0yMi41LTYwLjkgOS4yLTIwLjggMTYuNi00MS4xIDIyLjItNjAuNiA5LjkgMy4xIDE5LjMgNi41IDI4LjEgMTAuMiAzNS40IDE1LjEgNTguMyAzNC45IDU4LjMgNTAuNi0uMSAxNS43LTIzIDM1LjYtNTguNCA1MC42ek0zMjAuOCA3OC40eiIvPgogICAgPGNpcmNsZSBjeD0iNDIwLjkiIGN5PSIyOTYuNSIgcj0iNDUuNyIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-redo: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIGhlaWdodD0iMjQiIHZpZXdCb3g9IjAgMCAyNCAyNCIgd2lkdGg9IjE2Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgICA8cGF0aCBkPSJNMCAwaDI0djI0SDB6IiBmaWxsPSJub25lIi8+PHBhdGggZD0iTTE4LjQgMTAuNkMxNi41NSA4Ljk5IDE0LjE1IDggMTEuNSA4Yy00LjY1IDAtOC41OCAzLjAzLTkuOTYgNy4yMkwzLjkgMTZjMS4wNS0zLjE5IDQuMDUtNS41IDcuNi01LjUgMS45NSAwIDMuNzMuNzIgNS4xMiAxLjg4TDEzIDE2aDlWN2wtMy42IDMuNnoiLz4KICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-refresh: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDE4IDE4Ij4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTkgMTMuNWMtMi40OSAwLTQuNS0yLjAxLTQuNS00LjVTNi41MSA0LjUgOSA0LjVjMS4yNCAwIDIuMzYuNTIgMy4xNyAxLjMzTDEwIDhoNVYzbC0xLjc2IDEuNzZDMTIuMTUgMy42OCAxMC42NiAzIDkgMyA1LjY5IDMgMy4wMSA1LjY5IDMuMDEgOVM1LjY5IDE1IDkgMTVjMi45NyAwIDUuNDMtMi4xNiA1LjktNWgtMS41MmMtLjQ2IDItMi4yNCAzLjUtNC4zOCAzLjV6Ii8+CiAgICA8L2c+Cjwvc3ZnPgo=);
  --jp-icon-regex: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KICA8ZyBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiM0MTQxNDEiPgogICAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiAgPC9nPgoKICA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiBmaWxsPSIjRkZGIj4KICAgIDxjaXJjbGUgY2xhc3M9InN0MiIgY3g9IjUuNSIgY3k9IjE0LjUiIHI9IjEuNSIvPgogICAgPHJlY3QgeD0iMTIiIHk9IjQiIGNsYXNzPSJzdDIiIHdpZHRoPSIxIiBoZWlnaHQ9IjgiLz4KICAgIDxyZWN0IHg9IjguNSIgeT0iNy41IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjg2NiAtMC41IDAuNSAwLjg2NiAtMi4zMjU1IDcuMzIxOSkiIGNsYXNzPSJzdDIiIHdpZHRoPSI4IiBoZWlnaHQ9IjEiLz4KICAgIDxyZWN0IHg9IjEyIiB5PSI0IiB0cmFuc2Zvcm09Im1hdHJpeCgwLjUgLTAuODY2IDAuODY2IDAuNSAtMC42Nzc5IDE0LjgyNTIpIiBjbGFzcz0ic3QyIiB3aWR0aD0iMSIgaGVpZ2h0PSI4Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-run: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTggNXYxNGwxMS03eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-running: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDUxMiA1MTIiPgogIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICA8cGF0aCBkPSJNMjU2IDhDMTE5IDggOCAxMTkgOCAyNTZzMTExIDI0OCAyNDggMjQ4IDI0OC0xMTEgMjQ4LTI0OFMzOTMgOCAyNTYgOHptOTYgMzI4YzAgOC44LTcuMiAxNi0xNiAxNkgxNzZjLTguOCAwLTE2LTcuMi0xNi0xNlYxNzZjMC04LjggNy4yLTE2IDE2LTE2aDE2MGM4LjggMCAxNiA3LjIgMTYgMTZ2MTYweiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-save: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTE3IDNINWMtMS4xMSAwLTIgLjktMiAydjE0YzAgMS4xLjg5IDIgMiAyaDE0YzEuMSAwIDItLjkgMi0yVjdsLTQtNHptLTUgMTZjLTEuNjYgMC0zLTEuMzQtMy0zczEuMzQtMyAzLTMgMyAxLjM0IDMgMy0xLjM0IDMtMyAzem0zLTEwSDVWNWgxMHY0eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-search: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMTggMTgiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjEsMTAuOWgtMC43bC0wLjItMC4yYzAuOC0wLjksMS4zLTIuMiwxLjMtMy41YzAtMy0yLjQtNS40LTUuNC01LjRTMS44LDQuMiwxLjgsNy4xczIuNCw1LjQsNS40LDUuNCBjMS4zLDAsMi41LTAuNSwzLjUtMS4zbDAuMiwwLjJ2MC43bDQuMSw0LjFsMS4yLTEuMkwxMi4xLDEwLjl6IE03LjEsMTAuOWMtMi4xLDAtMy43LTEuNy0zLjctMy43czEuNy0zLjcsMy43LTMuN3MzLjcsMS43LDMuNywzLjcgUzkuMiwxMC45LDcuMSwxMC45eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-settings: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIiBkPSJNMTkuNDMgMTIuOThjLjA0LS4zMi4wNy0uNjQuMDctLjk4cy0uMDMtLjY2LS4wNy0uOThsMi4xMS0xLjY1Yy4xOS0uMTUuMjQtLjQyLjEyLS42NGwtMi0zLjQ2Yy0uMTItLjIyLS4zOS0uMy0uNjEtLjIybC0yLjQ5IDFjLS41Mi0uNC0xLjA4LS43My0xLjY5LS45OGwtLjM4LTIuNjVBLjQ4OC40ODggMCAwMDE0IDJoLTRjLS4yNSAwLS40Ni4xOC0uNDkuNDJsLS4zOCAyLjY1Yy0uNjEuMjUtMS4xNy41OS0xLjY5Ljk4bC0yLjQ5LTFjLS4yMy0uMDktLjQ5IDAtLjYxLjIybC0yIDMuNDZjLS4xMy4yMi0uMDcuNDkuMTIuNjRsMi4xMSAxLjY1Yy0uMDQuMzItLjA3LjY1LS4wNy45OHMuMDMuNjYuMDcuOThsLTIuMTEgMS42NWMtLjE5LjE1LS4yNC40Mi0uMTIuNjRsMiAzLjQ2Yy4xMi4yMi4zOS4zLjYxLjIybDIuNDktMWMuNTIuNCAxLjA4LjczIDEuNjkuOThsLjM4IDIuNjVjLjAzLjI0LjI0LjQyLjQ5LjQyaDRjLjI1IDAgLjQ2LS4xOC40OS0uNDJsLjM4LTIuNjVjLjYxLS4yNSAxLjE3LS41OSAxLjY5LS45OGwyLjQ5IDFjLjIzLjA5LjQ5IDAgLjYxLS4yMmwyLTMuNDZjLjEyLS4yMi4wNy0uNDktLjEyLS42NGwtMi4xMS0xLjY1ek0xMiAxNS41Yy0xLjkzIDAtMy41LTEuNTctMy41LTMuNXMxLjU3LTMuNSAzLjUtMy41IDMuNSAxLjU3IDMuNSAzLjUtMS41NyAzLjUtMy41IDMuNXoiLz4KPC9zdmc+Cg==);
  --jp-icon-share: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTSAxOCAyIEMgMTYuMzU0OTkgMiAxNSAzLjM1NDk5MDQgMTUgNSBDIDE1IDUuMTkwOTUyOSAxNS4wMjE3OTEgNS4zNzcxMjI0IDE1LjA1NjY0MSA1LjU1ODU5MzggTCA3LjkyMTg3NSA5LjcyMDcwMzEgQyA3LjM5ODUzOTkgOS4yNzc4NTM5IDYuNzMyMDc3MSA5IDYgOSBDIDQuMzU0OTkwNCA5IDMgMTAuMzU0OTkgMyAxMiBDIDMgMTMuNjQ1MDEgNC4zNTQ5OTA0IDE1IDYgMTUgQyA2LjczMjA3NzEgMTUgNy4zOTg1Mzk5IDE0LjcyMjE0NiA3LjkyMTg3NSAxNC4yNzkyOTcgTCAxNS4wNTY2NDEgMTguNDM5NDUzIEMgMTUuMDIxNTU1IDE4LjYyMTUxNCAxNSAxOC44MDgzODYgMTUgMTkgQyAxNSAyMC42NDUwMSAxNi4zNTQ5OSAyMiAxOCAyMiBDIDE5LjY0NTAxIDIyIDIxIDIwLjY0NTAxIDIxIDE5IEMgMjEgMTcuMzU0OTkgMTkuNjQ1MDEgMTYgMTggMTYgQyAxNy4yNjc0OCAxNiAxNi42MDE1OTMgMTYuMjc5MzI4IDE2LjA3ODEyNSAxNi43MjI2NTYgTCA4Ljk0MzM1OTQgMTIuNTU4NTk0IEMgOC45NzgyMDk1IDEyLjM3NzEyMiA5IDEyLjE5MDk1MyA5IDEyIEMgOSAxMS44MDkwNDcgOC45NzgyMDk1IDExLjYyMjg3OCA4Ljk0MzM1OTQgMTEuNDQxNDA2IEwgMTYuMDc4MTI1IDcuMjc5Mjk2OSBDIDE2LjYwMTQ2IDcuNzIyMTQ2MSAxNy4yNjc5MjMgOCAxOCA4IEMgMTkuNjQ1MDEgOCAyMSA2LjY0NTAwOTYgMjEgNSBDIDIxIDMuMzU0OTkwNCAxOS42NDUwMSAyIDE4IDIgeiBNIDE4IDQgQyAxOC41NjQxMjkgNCAxOSA0LjQzNTg3MDYgMTkgNSBDIDE5IDUuNTY0MTI5NCAxOC41NjQxMjkgNiAxOCA2IEMgMTcuNDM1ODcxIDYgMTcgNS41NjQxMjk0IDE3IDUgQyAxNyA0LjQzNTg3MDYgMTcuNDM1ODcxIDQgMTggNCB6IE0gNiAxMSBDIDYuNTY0MTI5NCAxMSA3IDExLjQzNTg3MSA3IDEyIEMgNyAxMi41NjQxMjkgNi41NjQxMjk0IDEzIDYgMTMgQyA1LjQzNTg3MDYgMTMgNSAxMi41NjQxMjkgNSAxMiBDIDUgMTEuNDM1ODcxIDUuNDM1ODcwNiAxMSA2IDExIHogTSAxOCAxOCBDIDE4LjU2NDEyOSAxOCAxOSAxOC40MzU4NzEgMTkgMTkgQyAxOSAxOS41NjQxMjkgMTguNTY0MTI5IDIwIDE4IDIwIEMgMTcuNDM1ODcxIDIwIDE3IDE5LjU2NDEyOSAxNyAxOSBDIDE3IDE4LjQzNTg3MSAxNy40MzU4NzEgMTggMTggMTggeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-spreadsheet: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8cGF0aCBjbGFzcz0ianAtaWNvbi1jb250cmFzdDEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNENBRjUwIiBkPSJNMi4yIDIuMnYxNy42aDE3LjZWMi4ySDIuMnptMTUuNCA3LjdoLTUuNVY0LjRoNS41djUuNXpNOS45IDQuNHY1LjVINC40VjQuNGg1LjV6bS01LjUgNy43aDUuNXY1LjVINC40di01LjV6bTcuNyA1LjV2LTUuNWg1LjV2NS41aC01LjV6Ii8+Cjwvc3ZnPgo=);
  --jp-icon-stop: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik02IDZoMTJ2MTJINnoiLz4KICAgIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tab: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTIxIDNIM2MtMS4xIDAtMiAuOS0yIDJ2MTRjMCAxLjEuOSAyIDIgMmgxOGMxLjEgMCAyLS45IDItMlY1YzAtMS4xLS45LTItMi0yem0wIDE2SDNWNWgxMHY0aDh2MTB6Ii8+CiAgPC9nPgo8L3N2Zz4K);
  --jp-icon-table-rows: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMSw4SDNWNGgxOFY4eiBNMjEsMTBIM3Y0aDE4VjEweiBNMjEsMTZIM3Y0aDE4VjE2eiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-tag: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjgiIGhlaWdodD0iMjgiIHZpZXdCb3g9IjAgMCA0MyAyOCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KCTxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CgkJPHBhdGggZD0iTTI4LjgzMzIgMTIuMzM0TDMyLjk5OTggMTYuNTAwN0wzNy4xNjY1IDEyLjMzNEgyOC44MzMyWiIvPgoJCTxwYXRoIGQ9Ik0xNi4yMDk1IDIxLjYxMDRDMTUuNjg3MyAyMi4xMjk5IDE0Ljg0NDMgMjIuMTI5OSAxNC4zMjQ4IDIxLjYxMDRMNi45ODI5IDE0LjcyNDVDNi41NzI0IDE0LjMzOTQgNi4wODMxMyAxMy42MDk4IDYuMDQ3ODYgMTMuMDQ4MkM1Ljk1MzQ3IDExLjUyODggNi4wMjAwMiA4LjYxOTQ0IDYuMDY2MjEgNy4wNzY5NUM2LjA4MjgxIDYuNTE0NzcgNi41NTU0OCA2LjA0MzQ3IDcuMTE4MDQgNi4wMzA1NUM5LjA4ODYzIDUuOTg0NzMgMTMuMjYzOCA1LjkzNTc5IDEzLjY1MTggNi4zMjQyNUwyMS43MzY5IDEzLjYzOUMyMi4yNTYgMTQuMTU4NSAyMS43ODUxIDE1LjQ3MjQgMjEuMjYyIDE1Ljk5NDZMMTYuMjA5NSAyMS42MTA0Wk05Ljc3NTg1IDguMjY1QzkuMzM1NTEgNy44MjU2NiA4LjYyMzUxIDcuODI1NjYgOC4xODI4IDguMjY1QzcuNzQzNDYgOC43MDU3MSA3Ljc0MzQ2IDkuNDE3MzMgOC4xODI4IDkuODU2NjdDOC42MjM4MiAxMC4yOTY0IDkuMzM1ODIgMTAuMjk2NCA5Ljc3NTg1IDkuODU2NjdDMTAuMjE1NiA5LjQxNzMzIDEwLjIxNTYgOC43MDUzMyA5Ljc3NTg1IDguMjY1WiIvPgoJPC9nPgo8L3N2Zz4K);
  --jp-icon-terminal: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0IiA+CiAgICA8cmVjdCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1iYWNrZ3JvdW5kLWNvbG9yIGpwLWljb24tc2VsZWN0YWJsZSIgd2lkdGg9IjIwIiBoZWlnaHQ9IjIwIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSgyIDIpIiBmaWxsPSIjMzMzMzMzIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtdGVybWluYWwtaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUtaW52ZXJzZSIgZD0iTTUuMDU2NjQgOC43NjE3MkM1LjA1NjY0IDguNTk3NjYgNS4wMzEyNSA4LjQ1MzEyIDQuOTgwNDcgOC4zMjgxMkM0LjkzMzU5IDguMTk5MjIgNC44NTU0NyA4LjA4MjAzIDQuNzQ2MDkgNy45NzY1NkM0LjY0MDYyIDcuODcxMDkgNC41IDcuNzc1MzkgNC4zMjQyMiA3LjY4OTQ1QzQuMTUyMzQgNy41OTk2MSAzLjk0MzM2IDcuNTExNzIgMy42OTcyNyA3LjQyNTc4QzMuMzAyNzMgNy4yODUxNiAyLjk0MzM2IDcuMTM2NzIgMi42MTkxNCA2Ljk4MDQ3QzIuMjk0OTIgNi44MjQyMiAyLjAxNzU4IDYuNjQyNTggMS43ODcxMSA2LjQzNTU1QzEuNTYwNTUgNi4yMjg1MiAxLjM4NDc3IDUuOTg4MjggMS4yNTk3NyA1LjcxNDg0QzEuMTM0NzcgNS40Mzc1IDEuMDcyMjcgNS4xMDkzOCAxLjA3MjI3IDQuNzMwNDdDMS4wNzIyNyA0LjM5ODQ0IDEuMTI4OTEgNC4wOTU3IDEuMjQyMTkgMy44MjIyN0MxLjM1NTQ3IDMuNTQ0OTIgMS41MTU2MiAzLjMwNDY5IDEuNzIyNjYgMy4xMDE1NkMxLjkyOTY5IDIuODk4NDQgMi4xNzk2OSAyLjczNDM3IDIuNDcyNjYgMi42MDkzOEMyLjc2NTYyIDIuNDg0MzggMy4wOTE4IDIuNDA0MyAzLjQ1MTE3IDIuMzY5MTRWMS4xMDkzOEg0LjM4ODY3VjIuMzgwODZDNC43NDAyMyAyLjQyNzczIDUuMDU2NjQgMi41MjM0NCA1LjMzNzg5IDIuNjY3OTdDNS42MTkxNCAyLjgxMjUgNS44NTc0MiAzLjAwMTk1IDYuMDUyNzMgMy4yMzYzM0M2LjI1MTk1IDMuNDY2OCA2LjQwNDMgMy43NDAyMyA2LjUwOTc3IDQuMDU2NjRDNi42MTkxNCA0LjM2OTE0IDYuNjczODMgNC43MjA3IDYuNjczODMgNS4xMTEzM0g1LjA0NDkyQzUuMDQ0OTIgNC42Mzg2NyA0LjkzNzUgNC4yODEyNSA0LjcyMjY2IDQuMDM5MDZDNC41MDc4MSAzLjc5Mjk3IDQuMjE2OCAzLjY2OTkyIDMuODQ5NjEgMy42Njk5MkMzLjY1MDM5IDMuNjY5OTIgMy40NzY1NiAzLjY5NzI3IDMuMzI4MTIgMy43NTE5NUMzLjE4MzU5IDMuODAyNzMgMy4wNjQ0NSAzLjg3Njk1IDIuOTcwNyAzLjk3NDYxQzIuODc2OTUgNC4wNjgzNiAyLjgwNjY0IDQuMTc5NjkgMi43NTk3NyA0LjMwODU5QzIuNzE2OCA0LjQzNzUgMi42OTUzMSA0LjU3ODEyIDIuNjk1MzEgNC43MzA0N0MyLjY5NTMxIDQuODgyODEgMi43MTY4IDUuMDE5NTMgMi43NTk3NyA1LjE0MDYyQzIuODA2NjQgNS4yNTc4MSAyLjg4MjgxIDUuMzY3MTkgMi45ODgyOCA1LjQ2ODc1QzMuMDk3NjYgNS41NzAzMSAzLjI0MDIzIDUuNjY3OTcgMy40MTYwMiA1Ljc2MTcyQzMuNTkxOCA1Ljg1MTU2IDMuODEwNTUgNS45NDMzNiA0LjA3MjI3IDYuMDM3MTFDNC40NjY4IDYuMTg1NTUgNC44MjQyMiA2LjMzOTg0IDUuMTQ0NTMgNi41QzUuNDY0ODQgNi42NTYyNSA1LjczODI4IDYuODM5ODQgNS45NjQ4NCA3LjA1MDc4QzYuMTk1MzEgNy4yNTc4MSA2LjM3MTA5IDcuNSA2LjQ5MjE5IDcuNzc3MzRDNi42MTcxOSA4LjA1MDc4IDYuNjc5NjkgOC4zNzUgNi42Nzk2OSA4Ljc1QzYuNjc5NjkgOS4wOTM3NSA2LjYyMzA1IDkuNDA0MyA2LjUwOTc3IDkuNjgxNjRDNi4zOTY0OCA5Ljk1NTA4IDYuMjM0MzggMTAuMTkxNCA2LjAyMzQ0IDEwLjM5MDZDNS44MTI1IDEwLjU4OTggNS41NTg1OSAxMC43NSA1LjI2MTcyIDEwLjg3MTFDNC45NjQ4NCAxMC45ODgzIDQuNjMyODEgMTEuMDY0NSA0LjI2NTYyIDExLjA5OTZWMTIuMjQ4SDMuMzMzOThWMTEuMDk5NkMzLjAwMTk1IDExLjA2ODQgMi42Nzk2OSAxMC45OTYxIDIuMzY3MTkgMTAuODgyOEMyLjA1NDY5IDEwLjc2NTYgMS43NzczNCAxMC41OTc3IDEuNTM1MTYgMTAuMzc4OUMxLjI5Njg4IDEwLjE2MDIgMS4xMDU0NyA5Ljg4NDc3IDAuOTYwOTM4IDkuNTUyNzNDMC44MTY0MDYgOS4yMTY4IDAuNzQ0MTQxIDguODE0NDUgMC43NDQxNDEgOC4zNDU3SDIuMzc4OTFDMi4zNzg5MSA4LjYyNjk1IDIuNDE5OTIgOC44NjMyOCAyLjUwMTk1IDkuMDU0NjlDMi41ODM5OCA5LjI0MjE5IDIuNjg5NDUgOS4zOTI1OCAyLjgxODM2IDkuNTA1ODZDMi45NTExNyA5LjYxNTIzIDMuMTAxNTYgOS42OTMzNiAzLjI2OTUzIDkuNzQwMjNDMy40Mzc1IDkuNzg3MTEgMy42MDkzOCA5LjgxMDU1IDMuNzg1MTYgOS44MTA1NUM0LjIwMzEyIDkuODEwNTUgNC41MTk1MyA5LjcxMjg5IDQuNzM0MzggOS41MTc1OEM0Ljk0OTIyIDkuMzIyMjcgNS4wNTY2NCA5LjA3MDMxIDUuMDU2NjQgOC43NjE3MlpNMTMuNDE4IDEyLjI3MTVIOC4wNzQyMlYxMUgxMy40MThWMTIuMjcxNVoiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDMuOTUyNjQgNikiIGZpbGw9IndoaXRlIi8+Cjwvc3ZnPgo=);
  --jp-icon-text-editor: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8cGF0aCBjbGFzcz0ianAtdGV4dC1lZGl0b3ItaWNvbi1jb2xvciBqcC1pY29uLXNlbGVjdGFibGUiIGZpbGw9IiM2MTYxNjEiIGQ9Ik0xNSAxNUgzdjJoMTJ2LTJ6bTAtOEgzdjJoMTJWN3pNMyAxM2gxOHYtMkgzdjJ6bTAgOGgxOHYtMkgzdjJ6TTMgM3YyaDE4VjNIM3oiLz4KPC9zdmc+Cg==);
  --jp-icon-toc: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld0JveD0iMCAwIDI0IDI0Ij4KICA8ZyBjbGFzcz0ianAtaWNvbjMganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjNjE2MTYxIj4KICAgIDxwYXRoIGQ9Ik03LDVIMjFWN0g3VjVNNywxM1YxMUgyMVYxM0g3TTQsNC41QTEuNSwxLjUgMCAwLDEgNS41LDZBMS41LDEuNSAwIDAsMSA0LDcuNUExLjUsMS41IDAgMCwxIDIuNSw2QTEuNSwxLjUgMCAwLDEgNCw0LjVNNCwxMC41QTEuNSwxLjUgMCAwLDEgNS41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMy41QTEuNSwxLjUgMCAwLDEgMi41LDEyQTEuNSwxLjUgMCAwLDEgNCwxMC41TTcsMTlWMTdIMjFWMTlIN000LDE2LjVBMS41LDEuNSAwIDAsMSA1LjUsMThBMS41LDEuNSAwIDAsMSA0LDE5LjVBMS41LDEuNSAwIDAsMSAyLjUsMThBMS41LDEuNSAwIDAsMSA0LDE2LjVaIiAvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-tree-view: url(data:image/svg+xml;base64,PHN2ZyBoZWlnaHQ9IjI0IiB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxnIGNsYXNzPSJqcC1pY29uMyIgZmlsbD0iIzYxNjE2MSI+CiAgICAgICAgPHBhdGggZD0iTTAgMGgyNHYyNEgweiIgZmlsbD0ibm9uZSIvPgogICAgICAgIDxwYXRoIGQ9Ik0yMiAxMVYzaC03djNIOVYzSDJ2OGg3VjhoMnYxMGg0djNoN3YtOGgtN3YzaC0yVjhoMnYzeiIvPgogICAgPC9nPgo8L3N2Zz4K);
  --jp-icon-trusted: url(data:image/svg+xml;base64,PHN2ZyBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDI0IDI1Ij4KICAgIDxwYXRoIGNsYXNzPSJqcC1pY29uMiIgc3Ryb2tlPSIjMzMzMzMzIiBzdHJva2Utd2lkdGg9IjIiIHRyYW5zZm9ybT0idHJhbnNsYXRlKDIgMykiIGQ9Ik0xLjg2MDk0IDExLjQ0MDlDMC44MjY0NDggOC43NzAyNyAwLjg2Mzc3OSA2LjA1NzY0IDEuMjQ5MDcgNC4xOTkzMkMyLjQ4MjA2IDMuOTMzNDcgNC4wODA2OCAzLjQwMzQ3IDUuNjAxMDIgMi44NDQ5QzcuMjM1NDkgMi4yNDQ0IDguODU2NjYgMS41ODE1IDkuOTg3NiAxLjA5NTM5QzExLjA1OTcgMS41ODM0MSAxMi42MDk0IDIuMjQ0NCAxNC4yMTggMi44NDMzOUMxNS43NTAzIDMuNDEzOTQgMTcuMzk5NSAzLjk1MjU4IDE4Ljc1MzkgNC4yMTM4NUMxOS4xMzY0IDYuMDcxNzcgMTkuMTcwOSA4Ljc3NzIyIDE4LjEzOSAxMS40NDA5QzE3LjAzMDMgMTQuMzAzMiAxNC42NjY4IDE3LjE4NDQgOS45OTk5OSAxOC45MzU0QzUuMzMzMiAxNy4xODQ0IDIuOTY5NjggMTQuMzAzMiAxLjg2MDk0IDExLjQ0MDlaIi8+CiAgICA8cGF0aCBjbGFzcz0ianAtaWNvbjIiIGZpbGw9IiMzMzMzMzMiIHN0cm9rZT0iIzMzMzMzMyIgdHJhbnNmb3JtPSJ0cmFuc2xhdGUoOCA5Ljg2NzE5KSIgZD0iTTIuODYwMTUgNC44NjUzNUwwLjcyNjU0OSAyLjk5OTU5TDAgMy42MzA0NUwyLjg2MDE1IDYuMTMxNTdMOCAwLjYzMDg3Mkw3LjI3ODU3IDBMMi44NjAxNSA0Ljg2NTM1WiIvPgo8L3N2Zz4K);
  --jp-icon-undo: url(data:image/svg+xml;base64,PHN2ZyB2aWV3Qm94PSIwIDAgMjQgMjQiIHdpZHRoPSIxNiIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTEyLjUgOGMtMi42NSAwLTUuMDUuOTktNi45IDIuNkwyIDd2OWg5bC0zLjYyLTMuNjJjMS4zOS0xLjE2IDMuMTYtMS44OCA1LjEyLTEuODggMy41NCAwIDYuNTUgMi4zMSA3LjYgNS41bDIuMzctLjc4QzIxLjA4IDExLjAzIDE3LjE1IDggMTIuNSA4eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-user: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICA8ZyBjbGFzcz0ianAtaWNvbjMiIGZpbGw9IiM2MTYxNjEiPgogICAgPHBhdGggZD0iTTE2IDdhNCA0IDAgMTEtOCAwIDQgNCAwIDAxOCAwek0xMiAxNGE3IDcgMCAwMC03IDdoMTRhNyA3IDAgMDAtNy03eiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-users: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZlcnNpb249IjEuMSIgdmlld0JveD0iMCAwIDM2IDI0IiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPGcgY2xhc3M9ImpwLWljb24zIiB0cmFuc2Zvcm09Im1hdHJpeCgxLjczMjcgMCAwIDEuNzMyNyAtMy42MjgyIC4wOTk1NzcpIiBmaWxsPSIjNjE2MTYxIj4KICA8cGF0aCB0cmFuc2Zvcm09Im1hdHJpeCgxLjUsMCwwLDEuNSwwLC02KSIgZD0ibTEyLjE4NiA3LjUwOThjLTEuMDUzNSAwLTEuOTc1NyAwLjU2NjUtMi40Nzg1IDEuNDEwMiAwLjc1MDYxIDAuMzEyNzcgMS4zOTc0IDAuODI2NDggMS44NzMgMS40NzI3aDMuNDg2M2MwLTEuNTkyLTEuMjg4OS0yLjg4MjgtMi44ODA5LTIuODgyOHoiLz4KICA8cGF0aCBkPSJtMjAuNDY1IDIuMzg5NWEyLjE4ODUgMi4xODg1IDAgMCAxLTIuMTg4NCAyLjE4ODUgMi4xODg1IDIuMTg4NSAwIDAgMS0yLjE4ODUtMi4xODg1IDIuMTg4NSAyLjE4ODUgMCAwIDEgMi4xODg1LTIuMTg4NSAyLjE4ODUgMi4xODg1IDAgMCAxIDIuMTg4NCAyLjE4ODV6Ii8+CiAgPHBhdGggdHJhbnNmb3JtPSJtYXRyaXgoMS41LDAsMCwxLjUsMCwtNikiIGQ9Im0zLjU4OTggOC40MjE5Yy0xLjExMjYgMC0yLjAxMzcgMC45MDExMS0yLjAxMzcgMi4wMTM3aDIuODE0NWMwLjI2Nzk3LTAuMzczMDkgMC41OTA3LTAuNzA0MzUgMC45NTg5OC0wLjk3ODUyLTAuMzQ0MzMtMC42MTY4OC0xLjAwMzEtMS4wMzUyLTEuNzU5OC0xLjAzNTJ6Ii8+CiAgPHBhdGggZD0ibTYuOTE1NCA0LjYyM2ExLjUyOTQgMS41Mjk0IDAgMCAxLTEuNTI5NCAxLjUyOTQgMS41Mjk0IDEuNTI5NCAwIDAgMS0xLjUyOTQtMS41Mjk0IDEuNTI5NCAxLjUyOTQgMCAwIDEgMS41Mjk0LTEuNTI5NCAxLjUyOTQgMS41Mjk0IDAgMCAxIDEuNTI5NCAxLjUyOTR6Ii8+CiAgPHBhdGggZD0ibTYuMTM1IDEzLjUzNWMwLTMuMjM5MiAyLjYyNTktNS44NjUgNS44NjUtNS44NjUgMy4yMzkyIDAgNS44NjUgMi42MjU5IDUuODY1IDUuODY1eiIvPgogIDxjaXJjbGUgY3g9IjEyIiBjeT0iMy43Njg1IiByPSIyLjk2ODUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-vega: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbjEganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjMjEyMTIxIj4KICAgIDxwYXRoIGQ9Ik0xMC42IDUuNGwyLjItMy4ySDIuMnY3LjNsNC02LjZ6Ii8+CiAgICA8cGF0aCBkPSJNMTUuOCAyLjJsLTQuNCA2LjZMNyA2LjNsLTQuOCA4djUuNWgxNy42VjIuMmgtNHptLTcgMTUuNEg1LjV2LTQuNGgzLjN2NC40em00LjQgMEg5LjhWOS44aDMuNHY3Ljh6bTQuNCAwaC0zLjRWNi41aDMuNHYxMS4xeiIvPgogIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-word: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIwIDIwIj4KIDxnIGNsYXNzPSJqcC1pY29uMiIgZmlsbD0iIzQxNDE0MSI+CiAgPHJlY3QgeD0iMiIgeT0iMiIgd2lkdGg9IjE2IiBoZWlnaHQ9IjE2Ii8+CiA8L2c+CiA8ZyBjbGFzcz0ianAtaWNvbi1hY2NlbnQyIiB0cmFuc2Zvcm09InRyYW5zbGF0ZSguNDMgLjA0MDEpIiBmaWxsPSIjZmZmIj4KICA8cGF0aCBkPSJtNC4xNCA4Ljc2cTAuMDY4Mi0xLjg5IDIuNDItMS44OSAxLjE2IDAgMS42OCAwLjQyIDAuNTY3IDAuNDEgMC41NjcgMS4xNnYzLjQ3cTAgMC40NjIgMC41MTQgMC40NjIgMC4xMDMgMCAwLjItMC4wMjMxdjAuNzE0cS0wLjM5OSAwLjEwMy0wLjY1MSAwLjEwMy0wLjQ1MiAwLTAuNjkzLTAuMjItMC4yMzEtMC4yLTAuMjg0LTAuNjYyLTAuOTU2IDAuODcyLTIgMC44NzItMC45MDMgMC0xLjQ3LTAuNDcyLTAuNTI1LTAuNDcyLTAuNTI1LTEuMjYgMC0wLjI2MiAwLjA0NTItMC40NzIgMC4wNTY3LTAuMjIgMC4xMTYtMC4zNzggMC4wNjgyLTAuMTY4IDAuMjMxLTAuMzA0IDAuMTU4LTAuMTQ3IDAuMjYyLTAuMjQyIDAuMTE2LTAuMDkxNCAwLjM2OC0wLjE2OCAwLjI2Mi0wLjA5MTQgMC4zOTktMC4xMjYgMC4xMzYtMC4wNDUyIDAuNDcyLTAuMTAzIDAuMzM2LTAuMDU3OCAwLjUwNC0wLjA3OTggMC4xNTgtMC4wMjMxIDAuNTY3LTAuMDc5OCAwLjU1Ni0wLjA2ODIgMC43NzctMC4yMjEgMC4yMi0wLjE1MiAwLjIyLTAuNDQxdi0wLjI1MnEwLTAuNDMtMC4zNTctMC42NjItMC4zMzYtMC4yMzEtMC45NzYtMC4yMzEtMC42NjIgMC0wLjk5OCAwLjI2Mi0wLjMzNiAwLjI1Mi0wLjM5OSAwLjc5OHptMS44OSAzLjY4cTAuNzg4IDAgMS4yNi0wLjQxIDAuNTA0LTAuNDIgMC41MDQtMC45MDN2LTEuMDVxLTAuMjg0IDAuMTM2LTAuODYxIDAuMjMxLTAuNTY3IDAuMDkxNC0wLjk4NyAwLjE1OC0wLjQyIDAuMDY4Mi0wLjc2NiAwLjMyNi0wLjMzNiAwLjI1Mi0wLjMzNiAwLjcwNHQwLjMwNCAwLjcwNCAwLjg2MSAwLjI1MnoiIHN0cm9rZS13aWR0aD0iMS4wNSIvPgogIDxwYXRoIGQ9Im0xMCA0LjU2aDAuOTQ1djMuMTVxMC42NTEtMC45NzYgMS44OS0wLjk3NiAxLjE2IDAgMS44OSAwLjg0IDAuNjgyIDAuODQgMC42ODIgMi4zMSAwIDEuNDctMC43MDQgMi40Mi0wLjcwNCAwLjg4Mi0xLjg5IDAuODgyLTEuMjYgMC0xLjg5LTEuMDJ2MC43NjZoLTAuODV6bTIuNjIgMy4wNHEtMC43NDYgMC0xLjE2IDAuNjQtMC40NTIgMC42My0wLjQ1MiAxLjY4IDAgMS4wNSAwLjQ1MiAxLjY4dDEuMTYgMC42M3EwLjc3NyAwIDEuMjYtMC42MyAwLjQ5NC0wLjY0IDAuNDk0LTEuNjggMC0xLjA1LTAuNDcyLTEuNjgtMC40NjItMC42NC0xLjI2LTAuNjR6IiBzdHJva2Utd2lkdGg9IjEuMDUiLz4KICA8cGF0aCBkPSJtMi43MyAxNS44IDEzLjYgMC4wMDgxYzAuMDA2OSAwIDAtMi42IDAtMi42IDAtMC4wMDc4LTEuMTUgMC0xLjE1IDAtMC4wMDY5IDAtMC4wMDgzIDEuNS0wLjAwODMgMS41LTJlLTMgLTAuMDAxNC0xMS4zLTAuMDAxNC0xMS4zLTAuMDAxNGwtMC4wMDU5Mi0xLjVjMC0wLjAwNzgtMS4xNyAwLjAwMTMtMS4xNyAwLjAwMTN6IiBzdHJva2Utd2lkdGg9Ii45NzUiLz4KIDwvZz4KPC9zdmc+Cg==);
  --jp-icon-yaml: url(data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxNiIgdmlld0JveD0iMCAwIDIyIDIyIj4KICA8ZyBjbGFzcz0ianAtaWNvbi1jb250cmFzdDIganAtaWNvbi1zZWxlY3RhYmxlIiBmaWxsPSIjRDgxQjYwIj4KICAgIDxwYXRoIGQ9Ik03LjIgMTguNnYtNS40TDMgNS42aDMuM2wxLjQgMy4xYy4zLjkuNiAxLjYgMSAyLjUuMy0uOC42LTEuNiAxLTIuNWwxLjQtMy4xaDMuNGwtNC40IDcuNnY1LjVsLTIuOS0uMXoiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxNi41IiByPSIyLjEiLz4KICAgIDxjaXJjbGUgY2xhc3M9InN0MCIgY3g9IjE3LjYiIGN5PSIxMSIgcj0iMi4xIi8+CiAgPC9nPgo8L3N2Zz4K);
}

/* Icon CSS class declarations */

.jp-AddAboveIcon {
  background-image: var(--jp-icon-add-above);
}

.jp-AddBelowIcon {
  background-image: var(--jp-icon-add-below);
}

.jp-AddIcon {
  background-image: var(--jp-icon-add);
}

.jp-BellIcon {
  background-image: var(--jp-icon-bell);
}

.jp-BugDotIcon {
  background-image: var(--jp-icon-bug-dot);
}

.jp-BugIcon {
  background-image: var(--jp-icon-bug);
}

.jp-BuildIcon {
  background-image: var(--jp-icon-build);
}

.jp-CaretDownEmptyIcon {
  background-image: var(--jp-icon-caret-down-empty);
}

.jp-CaretDownEmptyThinIcon {
  background-image: var(--jp-icon-caret-down-empty-thin);
}

.jp-CaretDownIcon {
  background-image: var(--jp-icon-caret-down);
}

.jp-CaretLeftIcon {
  background-image: var(--jp-icon-caret-left);
}

.jp-CaretRightIcon {
  background-image: var(--jp-icon-caret-right);
}

.jp-CaretUpEmptyThinIcon {
  background-image: var(--jp-icon-caret-up-empty-thin);
}

.jp-CaretUpIcon {
  background-image: var(--jp-icon-caret-up);
}

.jp-CaseSensitiveIcon {
  background-image: var(--jp-icon-case-sensitive);
}

.jp-CheckIcon {
  background-image: var(--jp-icon-check);
}

.jp-CircleEmptyIcon {
  background-image: var(--jp-icon-circle-empty);
}

.jp-CircleIcon {
  background-image: var(--jp-icon-circle);
}

.jp-ClearIcon {
  background-image: var(--jp-icon-clear);
}

.jp-CloseIcon {
  background-image: var(--jp-icon-close);
}

.jp-CodeCheckIcon {
  background-image: var(--jp-icon-code-check);
}

.jp-CodeIcon {
  background-image: var(--jp-icon-code);
}

.jp-CollapseAllIcon {
  background-image: var(--jp-icon-collapse-all);
}

.jp-ConsoleIcon {
  background-image: var(--jp-icon-console);
}

.jp-CopyIcon {
  background-image: var(--jp-icon-copy);
}

.jp-CopyrightIcon {
  background-image: var(--jp-icon-copyright);
}

.jp-CutIcon {
  background-image: var(--jp-icon-cut);
}

.jp-DeleteIcon {
  background-image: var(--jp-icon-delete);
}

.jp-DownloadIcon {
  background-image: var(--jp-icon-download);
}

.jp-DuplicateIcon {
  background-image: var(--jp-icon-duplicate);
}

.jp-EditIcon {
  background-image: var(--jp-icon-edit);
}

.jp-EllipsesIcon {
  background-image: var(--jp-icon-ellipses);
}

.jp-ErrorIcon {
  background-image: var(--jp-icon-error);
}

.jp-ExpandAllIcon {
  background-image: var(--jp-icon-expand-all);
}

.jp-ExtensionIcon {
  background-image: var(--jp-icon-extension);
}

.jp-FastForwardIcon {
  background-image: var(--jp-icon-fast-forward);
}

.jp-FileIcon {
  background-image: var(--jp-icon-file);
}

.jp-FileUploadIcon {
  background-image: var(--jp-icon-file-upload);
}

.jp-FilterDotIcon {
  background-image: var(--jp-icon-filter-dot);
}

.jp-FilterIcon {
  background-image: var(--jp-icon-filter);
}

.jp-FilterListIcon {
  background-image: var(--jp-icon-filter-list);
}

.jp-FolderFavoriteIcon {
  background-image: var(--jp-icon-folder-favorite);
}

.jp-FolderIcon {
  background-image: var(--jp-icon-folder);
}

.jp-HomeIcon {
  background-image: var(--jp-icon-home);
}

.jp-Html5Icon {
  background-image: var(--jp-icon-html5);
}

.jp-ImageIcon {
  background-image: var(--jp-icon-image);
}

.jp-InfoIcon {
  background-image: var(--jp-icon-info);
}

.jp-InspectorIcon {
  background-image: var(--jp-icon-inspector);
}

.jp-JsonIcon {
  background-image: var(--jp-icon-json);
}

.jp-JuliaIcon {
  background-image: var(--jp-icon-julia);
}

.jp-JupyterFaviconIcon {
  background-image: var(--jp-icon-jupyter-favicon);
}

.jp-JupyterIcon {
  background-image: var(--jp-icon-jupyter);
}

.jp-JupyterlabWordmarkIcon {
  background-image: var(--jp-icon-jupyterlab-wordmark);
}

.jp-KernelIcon {
  background-image: var(--jp-icon-kernel);
}

.jp-KeyboardIcon {
  background-image: var(--jp-icon-keyboard);
}

.jp-LaunchIcon {
  background-image: var(--jp-icon-launch);
}

.jp-LauncherIcon {
  background-image: var(--jp-icon-launcher);
}

.jp-LineFormIcon {
  background-image: var(--jp-icon-line-form);
}

.jp-LinkIcon {
  background-image: var(--jp-icon-link);
}

.jp-ListIcon {
  background-image: var(--jp-icon-list);
}

.jp-MarkdownIcon {
  background-image: var(--jp-icon-markdown);
}

.jp-MoveDownIcon {
  background-image: var(--jp-icon-move-down);
}

.jp-MoveUpIcon {
  background-image: var(--jp-icon-move-up);
}

.jp-NewFolderIcon {
  background-image: var(--jp-icon-new-folder);
}

.jp-NotTrustedIcon {
  background-image: var(--jp-icon-not-trusted);
}

.jp-NotebookIcon {
  background-image: var(--jp-icon-notebook);
}

.jp-NumberingIcon {
  background-image: var(--jp-icon-numbering);
}

.jp-OfflineBoltIcon {
  background-image: var(--jp-icon-offline-bolt);
}

.jp-PaletteIcon {
  background-image: var(--jp-icon-palette);
}

.jp-PasteIcon {
  background-image: var(--jp-icon-paste);
}

.jp-PdfIcon {
  background-image: var(--jp-icon-pdf);
}

.jp-PythonIcon {
  background-image: var(--jp-icon-python);
}

.jp-RKernelIcon {
  background-image: var(--jp-icon-r-kernel);
}

.jp-ReactIcon {
  background-image: var(--jp-icon-react);
}

.jp-RedoIcon {
  background-image: var(--jp-icon-redo);
}

.jp-RefreshIcon {
  background-image: var(--jp-icon-refresh);
}

.jp-RegexIcon {
  background-image: var(--jp-icon-regex);
}

.jp-RunIcon {
  background-image: var(--jp-icon-run);
}

.jp-RunningIcon {
  background-image: var(--jp-icon-running);
}

.jp-SaveIcon {
  background-image: var(--jp-icon-save);
}

.jp-SearchIcon {
  background-image: var(--jp-icon-search);
}

.jp-SettingsIcon {
  background-image: var(--jp-icon-settings);
}

.jp-ShareIcon {
  background-image: var(--jp-icon-share);
}

.jp-SpreadsheetIcon {
  background-image: var(--jp-icon-spreadsheet);
}

.jp-StopIcon {
  background-image: var(--jp-icon-stop);
}

.jp-TabIcon {
  background-image: var(--jp-icon-tab);
}

.jp-TableRowsIcon {
  background-image: var(--jp-icon-table-rows);
}

.jp-TagIcon {
  background-image: var(--jp-icon-tag);
}

.jp-TerminalIcon {
  background-image: var(--jp-icon-terminal);
}

.jp-TextEditorIcon {
  background-image: var(--jp-icon-text-editor);
}

.jp-TocIcon {
  background-image: var(--jp-icon-toc);
}

.jp-TreeViewIcon {
  background-image: var(--jp-icon-tree-view);
}

.jp-TrustedIcon {
  background-image: var(--jp-icon-trusted);
}

.jp-UndoIcon {
  background-image: var(--jp-icon-undo);
}

.jp-UserIcon {
  background-image: var(--jp-icon-user);
}

.jp-UsersIcon {
  background-image: var(--jp-icon-users);
}

.jp-VegaIcon {
  background-image: var(--jp-icon-vega);
}

.jp-WordIcon {
  background-image: var(--jp-icon-word);
}

.jp-YamlIcon {
  background-image: var(--jp-icon-yaml);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * (DEPRECATED) Support for consuming icons as CSS background images
 */

.jp-Icon,
.jp-MaterialIcon {
  background-position: center;
  background-repeat: no-repeat;
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-cover {
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

/**
 * (DEPRECATED) Support for specific CSS icon sizes
 */

.jp-Icon-16 {
  background-size: 16px;
  min-width: 16px;
  min-height: 16px;
}

.jp-Icon-18 {
  background-size: 18px;
  min-width: 18px;
  min-height: 18px;
}

.jp-Icon-20 {
  background-size: 20px;
  min-width: 20px;
  min-height: 20px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.lm-TabBar .lm-TabBar-addButton {
  align-items: center;
  display: flex;
  padding: 4px;
  padding-bottom: 5px;
  margin-right: 1px;
  background-color: var(--jp-layout-color2);
}

.lm-TabBar .lm-TabBar-addButton:hover {
  background-color: var(--jp-layout-color1);
}

.lm-DockPanel-tabBar .lm-TabBar-tab {
  width: var(--jp-private-horizontal-tab-width);
}

.lm-DockPanel-tabBar .lm-TabBar-content {
  flex: unset;
}

.lm-DockPanel-tabBar[data-orientation='horizontal'] {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for icons as inline SVG HTMLElements
 */

/* recolor the primary elements of an icon */
.jp-icon0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-accent0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-accent1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-accent2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-accent3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-accent4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-accent0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-accent1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-accent2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-accent3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-accent4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-none[fill] {
  fill: none;
}

.jp-icon-none[stroke] {
  stroke: none;
}

/* brand icon colors. Same for light and dark */
.jp-icon-brand0[fill] {
  fill: var(--jp-brand-color0);
}

.jp-icon-brand1[fill] {
  fill: var(--jp-brand-color1);
}

.jp-icon-brand2[fill] {
  fill: var(--jp-brand-color2);
}

.jp-icon-brand3[fill] {
  fill: var(--jp-brand-color3);
}

.jp-icon-brand4[fill] {
  fill: var(--jp-brand-color4);
}

.jp-icon-brand0[stroke] {
  stroke: var(--jp-brand-color0);
}

.jp-icon-brand1[stroke] {
  stroke: var(--jp-brand-color1);
}

.jp-icon-brand2[stroke] {
  stroke: var(--jp-brand-color2);
}

.jp-icon-brand3[stroke] {
  stroke: var(--jp-brand-color3);
}

.jp-icon-brand4[stroke] {
  stroke: var(--jp-brand-color4);
}

/* warn icon colors. Same for light and dark */
.jp-icon-warn0[fill] {
  fill: var(--jp-warn-color0);
}

.jp-icon-warn1[fill] {
  fill: var(--jp-warn-color1);
}

.jp-icon-warn2[fill] {
  fill: var(--jp-warn-color2);
}

.jp-icon-warn3[fill] {
  fill: var(--jp-warn-color3);
}

.jp-icon-warn0[stroke] {
  stroke: var(--jp-warn-color0);
}

.jp-icon-warn1[stroke] {
  stroke: var(--jp-warn-color1);
}

.jp-icon-warn2[stroke] {
  stroke: var(--jp-warn-color2);
}

.jp-icon-warn3[stroke] {
  stroke: var(--jp-warn-color3);
}

/* icon colors that contrast well with each other and most backgrounds */
.jp-icon-contrast0[fill] {
  fill: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[fill] {
  fill: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[fill] {
  fill: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[fill] {
  fill: var(--jp-icon-contrast-color3);
}

.jp-icon-contrast0[stroke] {
  stroke: var(--jp-icon-contrast-color0);
}

.jp-icon-contrast1[stroke] {
  stroke: var(--jp-icon-contrast-color1);
}

.jp-icon-contrast2[stroke] {
  stroke: var(--jp-icon-contrast-color2);
}

.jp-icon-contrast3[stroke] {
  stroke: var(--jp-icon-contrast-color3);
}

.jp-icon-dot[fill] {
  fill: var(--jp-warn-color0);
}

.jp-jupyter-icon-color[fill] {
  fill: var(--jp-jupyter-icon-color, var(--jp-warn-color0));
}

.jp-notebook-icon-color[fill] {
  fill: var(--jp-notebook-icon-color, var(--jp-warn-color0));
}

.jp-json-icon-color[fill] {
  fill: var(--jp-json-icon-color, var(--jp-warn-color1));
}

.jp-console-icon-color[fill] {
  fill: var(--jp-console-icon-color, white);
}

.jp-console-icon-background-color[fill] {
  fill: var(--jp-console-icon-background-color, var(--jp-brand-color1));
}

.jp-terminal-icon-color[fill] {
  fill: var(--jp-terminal-icon-color, var(--jp-layout-color2));
}

.jp-terminal-icon-background-color[fill] {
  fill: var(
    --jp-terminal-icon-background-color,
    var(--jp-inverse-layout-color2)
  );
}

.jp-text-editor-icon-color[fill] {
  fill: var(--jp-text-editor-icon-color, var(--jp-inverse-layout-color3));
}

.jp-inspector-icon-color[fill] {
  fill: var(--jp-inspector-icon-color, var(--jp-inverse-layout-color3));
}

/* CSS for icons in selected filebrowser listing items */
.jp-DirListing-item.jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

.jp-DirListing-item.jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* stylelint-disable selector-max-class, selector-max-compound-selectors */

/**
* TODO: come up with non css-hack solution for showing the busy icon on top
*  of the close icon
* CSS for complex behavior of close icon of tabs in the main area tabbar
*/
.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon3[fill] {
  fill: none;
}

.lm-DockPanel-tabBar
  .lm-TabBar-tab.lm-mod-closable.jp-mod-dirty
  > .lm-TabBar-tabCloseIcon
  > :not(:hover)
  > .jp-icon-busy[fill] {
  fill: var(--jp-inverse-layout-color3);
}

/* stylelint-enable selector-max-class, selector-max-compound-selectors */

/* CSS for icons in status bar */
#jp-main-statusbar .jp-mod-selected .jp-icon-selectable[fill] {
  fill: #fff;
}

#jp-main-statusbar .jp-mod-selected .jp-icon-selectable-inverse[fill] {
  fill: var(--jp-brand-color1);
}

/* special handling for splash icon CSS. While the theme CSS reloads during
   splash, the splash icon can loose theming. To prevent that, we set a
   default for its color variable */
:root {
  --jp-warn-color0: var(--md-orange-700);
}

/* not sure what to do with this one, used in filebrowser listing */
.jp-DragIcon {
  margin-right: 4px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/**
 * Support for alt colors for icons as inline SVG HTMLElements
 */

/* alt recolor the primary elements of an icon */
.jp-icon-alt .jp-icon0[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-alt .jp-icon0[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-alt .jp-icon1[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-alt .jp-icon2[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-alt .jp-icon3[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-alt .jp-icon4[stroke] {
  stroke: var(--jp-layout-color4);
}

/* alt recolor the accent elements of an icon */
.jp-icon-alt .jp-icon-accent0[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-alt .jp-icon-accent0[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-alt .jp-icon-accent1[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-alt .jp-icon-accent2[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-alt .jp-icon-accent3[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-alt .jp-icon-accent4[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-icon-hoverShow:not(:hover) .jp-icon-hoverShow-content {
  display: none !important;
}

/**
 * Support for hover colors for icons as inline SVG HTMLElements
 */

/**
 * regular colors
 */

/* recolor the primary elements of an icon */
.jp-icon-hover :hover .jp-icon0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/* recolor the accent elements of an icon */
.jp-icon-hover :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* set the color of an icon to transparent */
.jp-icon-hover :hover .jp-icon-none-hover[fill] {
  fill: none;
}

.jp-icon-hover :hover .jp-icon-none-hover[stroke] {
  stroke: none;
}

/**
 * inverse colors
 */

/* inverse recolor the primary elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[fill] {
  fill: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[fill] {
  fill: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[fill] {
  fill: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[fill] {
  fill: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[fill] {
  fill: var(--jp-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon0-hover[stroke] {
  stroke: var(--jp-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon1-hover[stroke] {
  stroke: var(--jp-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon2-hover[stroke] {
  stroke: var(--jp-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon3-hover[stroke] {
  stroke: var(--jp-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon4-hover[stroke] {
  stroke: var(--jp-layout-color4);
}

/* inverse recolor the accent elements of an icon */
.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[fill] {
  fill: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[fill] {
  fill: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[fill] {
  fill: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[fill] {
  fill: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[fill] {
  fill: var(--jp-inverse-layout-color4);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent0-hover[stroke] {
  stroke: var(--jp-inverse-layout-color0);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent1-hover[stroke] {
  stroke: var(--jp-inverse-layout-color1);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent2-hover[stroke] {
  stroke: var(--jp-inverse-layout-color2);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent3-hover[stroke] {
  stroke: var(--jp-inverse-layout-color3);
}

.jp-icon-hover.jp-icon-alt :hover .jp-icon-accent4-hover[stroke] {
  stroke: var(--jp-inverse-layout-color4);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-IFrame {
  width: 100%;
  height: 100%;
}

.jp-IFrame > iframe {
  border: none;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-IFrame {
  position: relative;
}

body.lm-mod-override-cursor .jp-IFrame::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-HoverBox {
  position: fixed;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FormGroup-content fieldset {
  border: none;
  padding: 0;
  min-width: 0;
  width: 100%;
}

/* stylelint-disable selector-max-type */

.jp-FormGroup-content fieldset .jp-inputFieldWrapper input,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper select,
.jp-FormGroup-content fieldset .jp-inputFieldWrapper textarea {
  font-size: var(--jp-content-font-size2);
  border-color: var(--jp-input-border-color);
  border-style: solid;
  border-radius: var(--jp-border-radius);
  border-width: 1px;
  padding: 6px 8px;
  background: none;
  color: var(--jp-ui-font-color0);
  height: inherit;
}

.jp-FormGroup-content fieldset input[type='checkbox'] {
  position: relative;
  top: 2px;
  margin-left: 0;
}

.jp-FormGroup-content button.jp-mod-styled {
  cursor: pointer;
}

.jp-FormGroup-content .checkbox label {
  cursor: pointer;
  font-size: var(--jp-content-font-size1);
}

.jp-FormGroup-content .jp-root > fieldset > legend {
  display: none;
}

.jp-FormGroup-content .jp-root > fieldset > p {
  display: none;
}

/** copy of `input.jp-mod-styled:focus` style */
.jp-FormGroup-content fieldset input:focus,
.jp-FormGroup-content fieldset select:focus {
  -moz-outline-radius: unset;
  outline: var(--jp-border-width) solid var(--md-blue-500);
  outline-offset: -1px;
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-FormGroup-content fieldset input:hover:not(:focus),
.jp-FormGroup-content fieldset select:hover:not(:focus) {
  background-color: var(--jp-border-color2);
}

/* stylelint-enable selector-max-type */

.jp-FormGroup-content .checkbox .field-description {
  /* Disable default description field for checkbox:
   because other widgets do not have description fields,
   we add descriptions to each widget on the field level.
  */
  display: none;
}

.jp-FormGroup-content #root__description {
  display: none;
}

.jp-FormGroup-content .jp-modifiedIndicator {
  width: 5px;
  background-color: var(--jp-brand-color2);
  margin-top: 0;
  margin-left: calc(var(--jp-private-settingeditor-modifier-indent) * -1);
  flex-shrink: 0;
}

.jp-FormGroup-content .jp-modifiedIndicator.jp-errorIndicator {
  background-color: var(--jp-error-color0);
  margin-right: 0.5em;
}

/* RJSF ARRAY style */

.jp-arrayFieldWrapper legend {
  font-size: var(--jp-content-font-size2);
  color: var(--jp-ui-font-color0);
  flex-basis: 100%;
  padding: 4px 0;
  font-weight: var(--jp-content-heading-font-weight);
  border-bottom: 1px solid var(--jp-border-color2);
}

.jp-arrayFieldWrapper .field-description {
  padding: 4px 0;
  white-space: pre-wrap;
}

.jp-arrayFieldWrapper .array-item {
  width: 100%;
  border: 1px solid var(--jp-border-color2);
  border-radius: 4px;
  margin: 4px;
}

.jp-ArrayOperations {
  display: flex;
  margin-left: 8px;
}

.jp-ArrayOperationsButton {
  margin: 2px;
}

.jp-ArrayOperationsButton .jp-icon3[fill] {
  fill: var(--jp-ui-font-color0);
}

button.jp-ArrayOperationsButton.jp-mod-styled:disabled {
  cursor: not-allowed;
  opacity: 0.5;
}

/* RJSF form validation error */

.jp-FormGroup-content .validationErrors {
  color: var(--jp-error-color0);
}

/* Hide panel level error as duplicated the field level error */
.jp-FormGroup-content .panel.errors {
  display: none;
}

/* RJSF normal content (settings-editor) */

.jp-FormGroup-contentNormal {
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-FormGroup-contentItem {
  margin-left: 7px;
  color: var(--jp-ui-font-color0);
}

.jp-FormGroup-contentNormal .jp-FormGroup-description {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-default {
  flex-basis: 100%;
  padding: 4px 7px;
}

.jp-FormGroup-contentNormal .jp-FormGroup-fieldLabel {
  font-size: var(--jp-content-font-size1);
  font-weight: normal;
  min-width: 120px;
}

.jp-FormGroup-contentNormal fieldset:not(:first-child) {
  margin-left: 7px;
}

.jp-FormGroup-contentNormal .field-array-of-string .array-item {
  /* Display `jp-ArrayOperations` buttons side-by-side with content except
    for small screens where flex-wrap will place them one below the other.
  */
  display: flex;
  align-items: center;
  flex-wrap: wrap;
}

.jp-FormGroup-contentNormal .jp-objectFieldWrapper .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

/* RJSF compact content (metadata-form) */

.jp-FormGroup-content.jp-FormGroup-contentCompact {
  width: 100%;
}

.jp-FormGroup-contentCompact .form-group {
  display: flex;
  padding: 0.5em 0.2em 0.5em 0;
}

.jp-FormGroup-contentCompact
  .jp-FormGroup-compactTitle
  .jp-FormGroup-description {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color2);
}

.jp-FormGroup-contentCompact .jp-FormGroup-fieldLabel {
  padding-bottom: 0.3em;
}

.jp-FormGroup-contentCompact .jp-inputFieldWrapper .form-control {
  width: 100%;
  box-sizing: border-box;
}

.jp-FormGroup-contentCompact .jp-arrayFieldWrapper .jp-FormGroup-compactTitle {
  padding-bottom: 7px;
}

.jp-FormGroup-contentCompact
  .jp-objectFieldWrapper
  .jp-objectFieldWrapper
  .form-group {
  padding: 2px 8px 2px var(--jp-private-settingeditor-modifier-indent);
  margin-top: 2px;
}

.jp-FormGroup-contentCompact ul.error-detail {
  margin-block-start: 0.5em;
  margin-block-end: 0.5em;
  padding-inline-start: 1em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-SidePanel {
  display: flex;
  flex-direction: column;
  min-width: var(--jp-sidebar-min-width);
  overflow-y: auto;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);
  font-size: var(--jp-ui-font-size1);
}

.jp-SidePanel-header {
  flex: 0 0 auto;
  display: flex;
  border-bottom: var(--jp-border-width) solid var(--jp-border-color2);
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin: 0;
  padding: 2px;
  text-transform: uppercase;
}

.jp-SidePanel-toolbar {
  flex: 0 0 auto;
}

.jp-SidePanel-content {
  flex: 1 1 auto;
}

.jp-SidePanel-toolbar,
.jp-AccordionPanel-toolbar {
  height: var(--jp-private-toolbar-height);
}

.jp-SidePanel-toolbar.jp-Toolbar-micro {
  display: none;
}

.lm-AccordionPanel .jp-AccordionPanel-title {
  box-sizing: border-box;
  line-height: 25px;
  margin: 0;
  display: flex;
  align-items: center;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  font-size: var(--jp-ui-font-size0);
}

.jp-AccordionPanel-title {
  cursor: pointer;
  user-select: none;
  -moz-user-select: none;
  -webkit-user-select: none;
  text-transform: uppercase;
}

.lm-AccordionPanel[data-orientation='horizontal'] > .jp-AccordionPanel-title {
  /* Title is rotated for horizontal accordion panel using CSS */
  display: block;
  transform-origin: top left;
  transform: rotate(-90deg) translate(-100%);
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleLabel {
  user-select: none;
  text-overflow: ellipsis;
  white-space: nowrap;
  overflow: hidden;
}

.jp-AccordionPanel-title .lm-AccordionPanel-titleCollapser {
  transform: rotate(-90deg);
  margin: auto 0;
  height: 16px;
}

.jp-AccordionPanel-title.lm-mod-expanded .lm-AccordionPanel-titleCollapser {
  transform: rotate(0deg);
}

.lm-AccordionPanel .jp-AccordionPanel-toolbar {
  background: none;
  box-shadow: none;
  border: none;
  margin-left: auto;
}

.lm-AccordionPanel .lm-SplitPanel-handle:hover {
  background: var(--jp-layout-color3);
}

.jp-text-truncated {
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Spinner {
  position: absolute;
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 10;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-layout-color0);
  outline: none;
}

.jp-SpinnerContent {
  font-size: 10px;
  margin: 50px auto;
  text-indent: -9999em;
  width: 3em;
  height: 3em;
  border-radius: 50%;
  background: var(--jp-brand-color3);
  background: linear-gradient(
    to right,
    #f37626 10%,
    rgba(255, 255, 255, 0) 42%
  );
  position: relative;
  animation: load3 1s infinite linear, fadeIn 1s;
}

.jp-SpinnerContent::before {
  width: 50%;
  height: 50%;
  background: #f37626;
  border-radius: 100% 0 0;
  position: absolute;
  top: 0;
  left: 0;
  content: '';
}

.jp-SpinnerContent::after {
  background: var(--jp-layout-color0);
  width: 75%;
  height: 75%;
  border-radius: 50%;
  content: '';
  margin: auto;
  position: absolute;
  top: 0;
  left: 0;
  bottom: 0;
  right: 0;
}

@keyframes fadeIn {
  0% {
    opacity: 0;
  }

  100% {
    opacity: 1;
  }
}

@keyframes load3 {
  0% {
    transform: rotate(0deg);
  }

  100% {
    transform: rotate(360deg);
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

button.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: none;
  box-sizing: border-box;
  text-align: center;
  line-height: 32px;
  height: 32px;
  padding: 0 12px;
  letter-spacing: 0.8px;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input.jp-mod-styled {
  background: var(--jp-input-background);
  height: 28px;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color1);
  padding-left: 7px;
  padding-right: 7px;
  font-size: var(--jp-ui-font-size2);
  color: var(--jp-ui-font-color0);
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

input[type='checkbox'].jp-mod-styled {
  appearance: checkbox;
  -webkit-appearance: checkbox;
  -moz-appearance: checkbox;
  height: auto;
}

input.jp-mod-styled:focus {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-select-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  padding: 1px;
  background-color: var(--jp-layout-color1);
  box-sizing: border-box;
  margin-bottom: 12px;
}

.jp-select-wrapper:not(.multiple) {
  height: 28px;
}

.jp-select-wrapper.jp-mod-focused select.jp-mod-styled {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-input-active-background);
}

select.jp-mod-styled:hover {
  cursor: pointer;
  color: var(--jp-ui-font-color0);
  background-color: var(--jp-input-hover-background);
  box-shadow: inset 0 0 1px rgba(0, 0, 0, 0.5);
}

select.jp-mod-styled {
  flex: 1 1 auto;
  width: 100%;
  font-size: var(--jp-ui-font-size2);
  background: var(--jp-input-background);
  color: var(--jp-ui-font-color0);
  padding: 0 25px 0 8px;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
}

select.jp-mod-styled:not([multiple]) {
  height: 32px;
}

select.jp-mod-styled[multiple] {
  max-height: 200px;
  overflow-y: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-switch {
  display: flex;
  align-items: center;
  padding-left: 4px;
  padding-right: 4px;
  font-size: var(--jp-ui-font-size1);
  background-color: transparent;
  color: var(--jp-ui-font-color1);
  border: none;
  height: 20px;
}

.jp-switch:hover {
  background-color: var(--jp-layout-color2);
}

.jp-switch-label {
  margin-right: 5px;
  font-family: var(--jp-ui-font-family);
}

.jp-switch-track {
  cursor: pointer;
  background-color: var(--jp-switch-color, var(--jp-border-color1));
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 34px;
  height: 16px;
  width: 35px;
  position: relative;
}

.jp-switch-track::before {
  content: '';
  position: absolute;
  height: 10px;
  width: 10px;
  margin: 3px;
  left: 0;
  background-color: var(--jp-ui-inverse-font-color1);
  -webkit-transition: 0.4s;
  transition: 0.4s;
  border-radius: 50%;
}

.jp-switch[aria-checked='true'] .jp-switch-track {
  background-color: var(--jp-switch-true-position-color, var(--jp-warn-color0));
}

.jp-switch[aria-checked='true'] .jp-switch-track::before {
  /* track width (35) - margins (3 + 3) - thumb width (10) */
  left: 19px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toolbar-height: calc(
    28px + var(--jp-border-width)
  ); /* leave 28px for content */
}

.jp-Toolbar {
  color: var(--jp-ui-font-color1);
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: 2px;
  z-index: 8;
  overflow-x: hidden;
}

/* Toolbar items */

.jp-Toolbar > .jp-Toolbar-item.jp-Toolbar-spacer {
  flex-grow: 1;
  flex-shrink: 1;
}

.jp-Toolbar-item.jp-Toolbar-kernelStatus {
  display: inline-block;
  width: 32px;
  background-repeat: no-repeat;
  background-position: center;
  background-size: 16px;
}

.jp-Toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  display: flex;
  padding-left: 1px;
  padding-right: 1px;
  font-size: var(--jp-ui-font-size1);
  line-height: var(--jp-private-toolbar-height);
  height: 100%;
}

/* Toolbar buttons */

/* This is the div we use to wrap the react component into a Widget */
div.jp-ToolbarButton {
  color: transparent;
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0;
  margin: 0;
}

button.jp-ToolbarButtonComponent {
  background: var(--jp-layout-color1);
  border: none;
  box-sizing: border-box;
  outline: none;
  appearance: none;
  -webkit-appearance: none;
  -moz-appearance: none;
  padding: 0 6px;
  margin: 0;
  height: 24px;
  border-radius: var(--jp-border-radius);
  display: flex;
  align-items: center;
  text-align: center;
  font-size: 14px;
  min-width: unset;
  min-height: unset;
}

button.jp-ToolbarButtonComponent:disabled {
  opacity: 0.4;
}

button.jp-ToolbarButtonComponent > span {
  padding: 0;
  flex: 0 0 auto;
}

button.jp-ToolbarButtonComponent .jp-ToolbarButtonComponent-label {
  font-size: var(--jp-ui-font-size1);
  line-height: 100%;
  padding-left: 2px;
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar.jp-Toolbar-micro {
  padding: 0;
  min-height: 0;
}

#jp-main-dock-panel[data-mode='single-document']
  .jp-MainAreaWidget
  > .jp-Toolbar {
  border: none;
  box-shadow: none;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-WindowedPanel-outer {
  position: relative;
  overflow-y: auto;
}

.jp-WindowedPanel-inner {
  position: relative;
}

.jp-WindowedPanel-window {
  position: absolute;
  left: 0;
  right: 0;
  overflow: visible;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/* Sibling imports */

body {
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
}

/* Disable native link decoration styles everywhere outside of dialog boxes */
a {
  text-decoration: unset;
  color: unset;
}

a:hover {
  text-decoration: unset;
  color: unset;
}

/* Accessibility for links inside dialog box text */
.jp-Dialog-content a {
  text-decoration: revert;
  color: var(--jp-content-link-color);
}

.jp-Dialog-content a:hover {
  text-decoration: revert;
}

/* Styles for ui-components */
.jp-Button {
  color: var(--jp-ui-font-color2);
  border-radius: var(--jp-border-radius);
  padding: 0 12px;
  font-size: var(--jp-ui-font-size1);

  /* Copy from blueprint 3 */
  display: inline-flex;
  flex-direction: row;
  border: none;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  text-align: left;
  vertical-align: middle;
  min-height: 30px;
  min-width: 30px;
}

.jp-Button:disabled {
  cursor: not-allowed;
}

.jp-Button:empty {
  padding: 0 !important;
}

.jp-Button.jp-mod-small {
  min-height: 24px;
  min-width: 24px;
  font-size: 12px;
  padding: 0 7px;
}

/* Use our own theme for hover styles */
.jp-Button.jp-mod-minimal:hover {
  background-color: var(--jp-layout-color2);
}

.jp-Button.jp-mod-minimal {
  background: none;
}

.jp-InputGroup {
  display: block;
  position: relative;
}

.jp-InputGroup input {
  box-sizing: border-box;
  border: none;
  border-radius: 0;
  background-color: transparent;
  color: var(--jp-ui-font-color0);
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
  padding-bottom: 0;
  padding-top: 0;
  padding-left: 10px;
  padding-right: 28px;
  position: relative;
  width: 100%;
  -webkit-appearance: none;
  -moz-appearance: none;
  appearance: none;
  font-size: 14px;
  font-weight: 400;
  height: 30px;
  line-height: 30px;
  outline: none;
  vertical-align: middle;
}

.jp-InputGroup input:focus {
  box-shadow: inset 0 0 0 var(--jp-border-width)
      var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-InputGroup input:disabled {
  cursor: not-allowed;
  resize: block;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input:disabled ~ span {
  cursor: not-allowed;
  color: var(--jp-ui-font-color2);
}

.jp-InputGroup input::placeholder,
input::placeholder {
  color: var(--jp-ui-font-color2);
}

.jp-InputGroupAction {
  position: absolute;
  bottom: 1px;
  right: 0;
  padding: 6px;
}

.jp-HTMLSelect.jp-DefaultStyle select {
  background-color: initial;
  border: none;
  border-radius: 0;
  box-shadow: none;
  color: var(--jp-ui-font-color0);
  display: block;
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  height: 24px;
  line-height: 14px;
  padding: 0 25px 0 10px;
  text-align: left;
  -moz-appearance: none;
  -webkit-appearance: none;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color2);
  cursor: not-allowed;
  resize: block;
}

.jp-HTMLSelect.jp-DefaultStyle select:disabled ~ span {
  cursor: not-allowed;
}

/* Use our own theme for hover and option styles */
/* stylelint-disable-next-line selector-max-type */
.jp-HTMLSelect.jp-DefaultStyle select:hover,
.jp-HTMLSelect.jp-DefaultStyle select > option {
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color0);
}

select {
  box-sizing: border-box;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-StatusBar-Widget {
  display: flex;
  align-items: center;
  background: var(--jp-layout-color2);
  min-height: var(--jp-statusbar-height);
  justify-content: space-between;
  padding: 0 10px;
}

.jp-StatusBar-Left {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-StatusBar-Middle {
  display: flex;
  align-items: center;
}

.jp-StatusBar-Right {
  display: flex;
  align-items: center;
  flex-direction: row-reverse;
}

.jp-StatusBar-Item {
  max-height: var(--jp-statusbar-height);
  margin: 0 2px;
  height: var(--jp-statusbar-height);
  white-space: nowrap;
  text-overflow: ellipsis;
  color: var(--jp-ui-font-color1);
  padding: 0 6px;
}

.jp-mod-highlighted:hover {
  background-color: var(--jp-layout-color3);
}

.jp-mod-clicked {
  background-color: var(--jp-brand-color1);
}

.jp-mod-clicked:hover {
  background-color: var(--jp-brand-color0);
}

.jp-mod-clicked .jp-StatusBar-TextItem {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-StatusBar-HoverItem {
  box-shadow: '0px 4px 4px rgba(0, 0, 0, 0.25)';
}

.jp-StatusBar-TextItem {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  line-height: 24px;
  color: var(--jp-ui-font-color1);
}

.jp-StatusBar-GroupItem {
  display: flex;
  align-items: center;
  flex-direction: row;
}

.jp-Statusbar-ProgressCircle svg {
  display: block;
  margin: 0 auto;
  width: 16px;
  height: 24px;
  align-self: normal;
}

.jp-Statusbar-ProgressCircle path {
  fill: var(--jp-inverse-layout-color3);
}

.jp-Statusbar-ProgressBar-progress-bar {
  height: 10px;
  width: 100px;
  border: solid 0.25px var(--jp-brand-color2);
  border-radius: 3px;
  overflow: hidden;
  align-self: center;
}

.jp-Statusbar-ProgressBar-progress-bar > div {
  background-color: var(--jp-brand-color2);
  background-image: linear-gradient(
    -45deg,
    rgba(255, 255, 255, 0.2) 25%,
    transparent 25%,
    transparent 50%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.2) 75%,
    transparent 75%,
    transparent
  );
  background-size: 40px 40px;
  float: left;
  width: 0%;
  height: 100%;
  font-size: 12px;
  line-height: 14px;
  color: #fff;
  text-align: center;
  animation: jp-Statusbar-ExecutionTime-progress-bar 2s linear infinite;
}

.jp-Statusbar-ProgressBar-progress-bar p {
  color: var(--jp-ui-font-color1);
  font-family: var(--jp-ui-font-family);
  font-size: var(--jp-ui-font-size1);
  line-height: 10px;
  width: 100px;
}

@keyframes jp-Statusbar-ExecutionTime-progress-bar {
  0% {
    background-position: 0 0;
  }

  100% {
    background-position: 40px 40px;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-commandpalette-search-height: 28px;
}

/*-----------------------------------------------------------------------------
| Overall styles
|----------------------------------------------------------------------------*/

.lm-CommandPalette {
  padding-bottom: 0;
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Modal variant
|----------------------------------------------------------------------------*/

.jp-ModalCommandPalette {
  position: absolute;
  z-index: 10000;
  top: 38px;
  left: 30%;
  margin: 0;
  padding: 4px;
  width: 40%;
  box-shadow: var(--jp-elevation-z4);
  border-radius: 4px;
  background: var(--jp-layout-color0);
}

.jp-ModalCommandPalette .lm-CommandPalette {
  max-height: 40vh;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-close-icon::after {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-header {
  display: none;
}

.jp-ModalCommandPalette .lm-CommandPalette .lm-CommandPalette-item {
  margin-left: 4px;
  margin-right: 4px;
}

.jp-ModalCommandPalette
  .lm-CommandPalette
  .lm-CommandPalette-item.lm-mod-disabled {
  display: none;
}

/*-----------------------------------------------------------------------------
| Search
|----------------------------------------------------------------------------*/

.lm-CommandPalette-search {
  padding: 4px;
  background-color: var(--jp-layout-color1);
  z-index: 2;
}

.lm-CommandPalette-wrapper {
  overflow: overlay;
  padding: 0 9px;
  background-color: var(--jp-input-active-background);
  height: 30px;
  box-shadow: inset 0 0 0 var(--jp-border-width) var(--jp-input-border-color);
}

.lm-CommandPalette.lm-mod-focused .lm-CommandPalette-wrapper {
  box-shadow: inset 0 0 0 1px var(--jp-input-active-box-shadow-color),
    inset 0 0 0 3px var(--jp-input-active-box-shadow-color);
}

.jp-SearchIconGroup {
  color: white;
  background-color: var(--jp-brand-color1);
  position: absolute;
  top: 4px;
  right: 4px;
  padding: 5px 5px 1px;
}

.jp-SearchIconGroup svg {
  height: 20px;
  width: 20px;
}

.jp-SearchIconGroup .jp-icon3[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-input {
  background: transparent;
  width: calc(100% - 18px);
  float: left;
  border: none;
  outline: none;
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  line-height: var(--jp-private-commandpalette-search-height);
}

.lm-CommandPalette-input::-webkit-input-placeholder,
.lm-CommandPalette-input::-moz-placeholder,
.lm-CommandPalette-input:-ms-input-placeholder {
  color: var(--jp-ui-font-color2);
  font-size: var(--jp-ui-font-size1);
}

/*-----------------------------------------------------------------------------
| Results
|----------------------------------------------------------------------------*/

.lm-CommandPalette-header:first-child {
  margin-top: 0;
}

.lm-CommandPalette-header {
  border-bottom: solid var(--jp-border-width) var(--jp-border-color2);
  color: var(--jp-ui-font-color1);
  cursor: pointer;
  display: flex;
  font-size: var(--jp-ui-font-size0);
  font-weight: 600;
  letter-spacing: 1px;
  margin-top: 8px;
  padding: 8px 0 8px 12px;
  text-transform: uppercase;
}

.lm-CommandPalette-header.lm-mod-active {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-header > mark {
  background-color: transparent;
  font-weight: bold;
  color: var(--jp-ui-font-color1);
}

.lm-CommandPalette-item {
  padding: 4px 12px 4px 4px;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  font-weight: 400;
  display: flex;
}

.lm-CommandPalette-item.lm-mod-disabled {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item.lm-mod-active {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item.lm-mod-active .lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-inverse-font-color0);
}

.lm-CommandPalette-item.lm-mod-active .jp-icon-selectable[fill] {
  fill: var(--jp-layout-color0);
}

.lm-CommandPalette-item.lm-mod-active:hover:not(.lm-mod-disabled) {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.lm-CommandPalette-item:hover:not(.lm-mod-active):not(.lm-mod-disabled) {
  background: var(--jp-layout-color2);
}

.lm-CommandPalette-itemContent {
  overflow: hidden;
}

.lm-CommandPalette-itemLabel > mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.lm-CommandPalette-item.lm-mod-disabled mark {
  color: var(--jp-ui-font-color2);
}

.lm-CommandPalette-item .lm-CommandPalette-itemIcon {
  margin: 0 4px 0 0;
  position: relative;
  width: 16px;
  top: 2px;
  flex: 0 0 auto;
}

.lm-CommandPalette-item.lm-mod-disabled .lm-CommandPalette-itemIcon {
  opacity: 0.6;
}

.lm-CommandPalette-item .lm-CommandPalette-itemShortcut {
  flex: 0 0 auto;
}

.lm-CommandPalette-itemCaption {
  display: none;
}

.lm-CommandPalette-content {
  background-color: var(--jp-layout-color1);
}

.lm-CommandPalette-content:empty::after {
  content: 'No results';
  margin: auto;
  margin-top: 20px;
  width: 100px;
  display: block;
  font-size: var(--jp-ui-font-size2);
  font-family: var(--jp-ui-font-family);
  font-weight: lighter;
}

.lm-CommandPalette-emptyMessage {
  text-align: center;
  margin-top: 24px;
  line-height: 1.32;
  padding: 0 8px;
  color: var(--jp-content-font-color3);
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Dialog {
  position: absolute;
  z-index: 10000;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  margin: 0;
  padding: 0;
  width: 100%;
  height: 100%;
  background: var(--jp-dialog-background);
}

.jp-Dialog-content {
  display: flex;
  flex-direction: column;
  margin-left: auto;
  margin-right: auto;
  background: var(--jp-layout-color1);
  padding: 24px 24px 12px;
  min-width: 300px;
  min-height: 150px;
  max-width: 1000px;
  max-height: 500px;
  box-sizing: border-box;
  box-shadow: var(--jp-elevation-z20);
  word-wrap: break-word;
  border-radius: var(--jp-border-radius);

  /* This is needed so that all font sizing of children done in ems is
   * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color1);
  resize: both;
}

.jp-Dialog-content.jp-Dialog-content-small {
  max-width: 500px;
}

.jp-Dialog-button {
  overflow: visible;
}

button.jp-Dialog-button:focus {
  outline: 1px solid var(--jp-brand-color1);
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button:focus::-moz-focus-inner {
  border: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus,
button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline-offset: 4px;
  -moz-outline-radius: 0;
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-accept:focus {
  outline: 1px solid var(--jp-accept-color-normal, var(--jp-brand-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-warn:focus {
  outline: 1px solid var(--jp-warn-color-normal, var(--jp-error-color1));
}

button.jp-Dialog-button.jp-mod-styled.jp-mod-reject:focus {
  outline: 1px solid var(--jp-reject-color-normal, var(--md-grey-600));
}

button.jp-Dialog-close-button {
  padding: 0;
  height: 100%;
  min-width: unset;
  min-height: unset;
}

.jp-Dialog-header {
  display: flex;
  justify-content: space-between;
  flex: 0 0 auto;
  padding-bottom: 12px;
  font-size: var(--jp-ui-font-size3);
  font-weight: 400;
  color: var(--jp-ui-font-color1);
}

.jp-Dialog-body {
  display: flex;
  flex-direction: column;
  flex: 1 1 auto;
  font-size: var(--jp-ui-font-size1);
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  overflow: auto;
}

.jp-Dialog-footer {
  display: flex;
  flex-direction: row;
  justify-content: flex-end;
  align-items: center;
  flex: 0 0 auto;
  margin-left: -12px;
  margin-right: -12px;
  padding: 12px;
}

.jp-Dialog-checkbox {
  padding-right: 5px;
}

.jp-Dialog-checkbox > input:focus-visible {
  outline: 1px solid var(--jp-input-active-border-color);
  outline-offset: 1px;
}

.jp-Dialog-spacer {
  flex: 1 1 auto;
}

.jp-Dialog-title {
  overflow: hidden;
  white-space: nowrap;
  text-overflow: ellipsis;
}

.jp-Dialog-body > .jp-select-wrapper {
  width: 100%;
}

.jp-Dialog-body > button {
  padding: 0 16px;
}

.jp-Dialog-body > label {
  line-height: 1.4;
  color: var(--jp-ui-font-color0);
}

.jp-Dialog-button.jp-mod-styled:not(:last-child) {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Input-Boolean-Dialog {
  flex-direction: row-reverse;
  align-items: end;
  width: 100%;
}

.jp-Input-Boolean-Dialog > label {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MainAreaWidget > :focus {
  outline: none;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error {
  padding: 6px;
}

.jp-MainAreaWidget .jp-MainAreaWidget-error > pre {
  width: auto;
  padding: 10px;
  background: var(--jp-error-color3);
  border: var(--jp-border-width) solid var(--jp-error-color1);
  border-radius: var(--jp-border-radius);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  white-space: pre-wrap;
  word-wrap: break-word;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/**
 * google-material-color v1.2.6
 * https://github.com/danlevan/google-material-color
 */
:root {
  --md-red-50: #ffebee;
  --md-red-100: #ffcdd2;
  --md-red-200: #ef9a9a;
  --md-red-300: #e57373;
  --md-red-400: #ef5350;
  --md-red-500: #f44336;
  --md-red-600: #e53935;
  --md-red-700: #d32f2f;
  --md-red-800: #c62828;
  --md-red-900: #b71c1c;
  --md-red-A100: #ff8a80;
  --md-red-A200: #ff5252;
  --md-red-A400: #ff1744;
  --md-red-A700: #d50000;
  --md-pink-50: #fce4ec;
  --md-pink-100: #f8bbd0;
  --md-pink-200: #f48fb1;
  --md-pink-300: #f06292;
  --md-pink-400: #ec407a;
  --md-pink-500: #e91e63;
  --md-pink-600: #d81b60;
  --md-pink-700: #c2185b;
  --md-pink-800: #ad1457;
  --md-pink-900: #880e4f;
  --md-pink-A100: #ff80ab;
  --md-pink-A200: #ff4081;
  --md-pink-A400: #f50057;
  --md-pink-A700: #c51162;
  --md-purple-50: #f3e5f5;
  --md-purple-100: #e1bee7;
  --md-purple-200: #ce93d8;
  --md-purple-300: #ba68c8;
  --md-purple-400: #ab47bc;
  --md-purple-500: #9c27b0;
  --md-purple-600: #8e24aa;
  --md-purple-700: #7b1fa2;
  --md-purple-800: #6a1b9a;
  --md-purple-900: #4a148c;
  --md-purple-A100: #ea80fc;
  --md-purple-A200: #e040fb;
  --md-purple-A400: #d500f9;
  --md-purple-A700: #a0f;
  --md-deep-purple-50: #ede7f6;
  --md-deep-purple-100: #d1c4e9;
  --md-deep-purple-200: #b39ddb;
  --md-deep-purple-300: #9575cd;
  --md-deep-purple-400: #7e57c2;
  --md-deep-purple-500: #673ab7;
  --md-deep-purple-600: #5e35b1;
  --md-deep-purple-700: #512da8;
  --md-deep-purple-800: #4527a0;
  --md-deep-purple-900: #311b92;
  --md-deep-purple-A100: #b388ff;
  --md-deep-purple-A200: #7c4dff;
  --md-deep-purple-A400: #651fff;
  --md-deep-purple-A700: #6200ea;
  --md-indigo-50: #e8eaf6;
  --md-indigo-100: #c5cae9;
  --md-indigo-200: #9fa8da;
  --md-indigo-300: #7986cb;
  --md-indigo-400: #5c6bc0;
  --md-indigo-500: #3f51b5;
  --md-indigo-600: #3949ab;
  --md-indigo-700: #303f9f;
  --md-indigo-800: #283593;
  --md-indigo-900: #1a237e;
  --md-indigo-A100: #8c9eff;
  --md-indigo-A200: #536dfe;
  --md-indigo-A400: #3d5afe;
  --md-indigo-A700: #304ffe;
  --md-blue-50: #e3f2fd;
  --md-blue-100: #bbdefb;
  --md-blue-200: #90caf9;
  --md-blue-300: #64b5f6;
  --md-blue-400: #42a5f5;
  --md-blue-500: #2196f3;
  --md-blue-600: #1e88e5;
  --md-blue-700: #1976d2;
  --md-blue-800: #1565c0;
  --md-blue-900: #0d47a1;
  --md-blue-A100: #82b1ff;
  --md-blue-A200: #448aff;
  --md-blue-A400: #2979ff;
  --md-blue-A700: #2962ff;
  --md-light-blue-50: #e1f5fe;
  --md-light-blue-100: #b3e5fc;
  --md-light-blue-200: #81d4fa;
  --md-light-blue-300: #4fc3f7;
  --md-light-blue-400: #29b6f6;
  --md-light-blue-500: #03a9f4;
  --md-light-blue-600: #039be5;
  --md-light-blue-700: #0288d1;
  --md-light-blue-800: #0277bd;
  --md-light-blue-900: #01579b;
  --md-light-blue-A100: #80d8ff;
  --md-light-blue-A200: #40c4ff;
  --md-light-blue-A400: #00b0ff;
  --md-light-blue-A700: #0091ea;
  --md-cyan-50: #e0f7fa;
  --md-cyan-100: #b2ebf2;
  --md-cyan-200: #80deea;
  --md-cyan-300: #4dd0e1;
  --md-cyan-400: #26c6da;
  --md-cyan-500: #00bcd4;
  --md-cyan-600: #00acc1;
  --md-cyan-700: #0097a7;
  --md-cyan-800: #00838f;
  --md-cyan-900: #006064;
  --md-cyan-A100: #84ffff;
  --md-cyan-A200: #18ffff;
  --md-cyan-A400: #00e5ff;
  --md-cyan-A700: #00b8d4;
  --md-teal-50: #e0f2f1;
  --md-teal-100: #b2dfdb;
  --md-teal-200: #80cbc4;
  --md-teal-300: #4db6ac;
  --md-teal-400: #26a69a;
  --md-teal-500: #009688;
  --md-teal-600: #00897b;
  --md-teal-700: #00796b;
  --md-teal-800: #00695c;
  --md-teal-900: #004d40;
  --md-teal-A100: #a7ffeb;
  --md-teal-A200: #64ffda;
  --md-teal-A400: #1de9b6;
  --md-teal-A700: #00bfa5;
  --md-green-50: #e8f5e9;
  --md-green-100: #c8e6c9;
  --md-green-200: #a5d6a7;
  --md-green-300: #81c784;
  --md-green-400: #66bb6a;
  --md-green-500: #4caf50;
  --md-green-600: #43a047;
  --md-green-700: #388e3c;
  --md-green-800: #2e7d32;
  --md-green-900: #1b5e20;
  --md-green-A100: #b9f6ca;
  --md-green-A200: #69f0ae;
  --md-green-A400: #00e676;
  --md-green-A700: #00c853;
  --md-light-green-50: #f1f8e9;
  --md-light-green-100: #dcedc8;
  --md-light-green-200: #c5e1a5;
  --md-light-green-300: #aed581;
  --md-light-green-400: #9ccc65;
  --md-light-green-500: #8bc34a;
  --md-light-green-600: #7cb342;
  --md-light-green-700: #689f38;
  --md-light-green-800: #558b2f;
  --md-light-green-900: #33691e;
  --md-light-green-A100: #ccff90;
  --md-light-green-A200: #b2ff59;
  --md-light-green-A400: #76ff03;
  --md-light-green-A700: #64dd17;
  --md-lime-50: #f9fbe7;
  --md-lime-100: #f0f4c3;
  --md-lime-200: #e6ee9c;
  --md-lime-300: #dce775;
  --md-lime-400: #d4e157;
  --md-lime-500: #cddc39;
  --md-lime-600: #c0ca33;
  --md-lime-700: #afb42b;
  --md-lime-800: #9e9d24;
  --md-lime-900: #827717;
  --md-lime-A100: #f4ff81;
  --md-lime-A200: #eeff41;
  --md-lime-A400: #c6ff00;
  --md-lime-A700: #aeea00;
  --md-yellow-50: #fffde7;
  --md-yellow-100: #fff9c4;
  --md-yellow-200: #fff59d;
  --md-yellow-300: #fff176;
  --md-yellow-400: #ffee58;
  --md-yellow-500: #ffeb3b;
  --md-yellow-600: #fdd835;
  --md-yellow-700: #fbc02d;
  --md-yellow-800: #f9a825;
  --md-yellow-900: #f57f17;
  --md-yellow-A100: #ffff8d;
  --md-yellow-A200: #ff0;
  --md-yellow-A400: #ffea00;
  --md-yellow-A700: #ffd600;
  --md-amber-50: #fff8e1;
  --md-amber-100: #ffecb3;
  --md-amber-200: #ffe082;
  --md-amber-300: #ffd54f;
  --md-amber-400: #ffca28;
  --md-amber-500: #ffc107;
  --md-amber-600: #ffb300;
  --md-amber-700: #ffa000;
  --md-amber-800: #ff8f00;
  --md-amber-900: #ff6f00;
  --md-amber-A100: #ffe57f;
  --md-amber-A200: #ffd740;
  --md-amber-A400: #ffc400;
  --md-amber-A700: #ffab00;
  --md-orange-50: #fff3e0;
  --md-orange-100: #ffe0b2;
  --md-orange-200: #ffcc80;
  --md-orange-300: #ffb74d;
  --md-orange-400: #ffa726;
  --md-orange-500: #ff9800;
  --md-orange-600: #fb8c00;
  --md-orange-700: #f57c00;
  --md-orange-800: #ef6c00;
  --md-orange-900: #e65100;
  --md-orange-A100: #ffd180;
  --md-orange-A200: #ffab40;
  --md-orange-A400: #ff9100;
  --md-orange-A700: #ff6d00;
  --md-deep-orange-50: #fbe9e7;
  --md-deep-orange-100: #ffccbc;
  --md-deep-orange-200: #ffab91;
  --md-deep-orange-300: #ff8a65;
  --md-deep-orange-400: #ff7043;
  --md-deep-orange-500: #ff5722;
  --md-deep-orange-600: #f4511e;
  --md-deep-orange-700: #e64a19;
  --md-deep-orange-800: #d84315;
  --md-deep-orange-900: #bf360c;
  --md-deep-orange-A100: #ff9e80;
  --md-deep-orange-A200: #ff6e40;
  --md-deep-orange-A400: #ff3d00;
  --md-deep-orange-A700: #dd2c00;
  --md-brown-50: #efebe9;
  --md-brown-100: #d7ccc8;
  --md-brown-200: #bcaaa4;
  --md-brown-300: #a1887f;
  --md-brown-400: #8d6e63;
  --md-brown-500: #795548;
  --md-brown-600: #6d4c41;
  --md-brown-700: #5d4037;
  --md-brown-800: #4e342e;
  --md-brown-900: #3e2723;
  --md-grey-50: #fafafa;
  --md-grey-100: #f5f5f5;
  --md-grey-200: #eee;
  --md-grey-300: #e0e0e0;
  --md-grey-400: #bdbdbd;
  --md-grey-500: #9e9e9e;
  --md-grey-600: #757575;
  --md-grey-700: #616161;
  --md-grey-800: #424242;
  --md-grey-900: #212121;
  --md-blue-grey-50: #eceff1;
  --md-blue-grey-100: #cfd8dc;
  --md-blue-grey-200: #b0bec5;
  --md-blue-grey-300: #90a4ae;
  --md-blue-grey-400: #78909c;
  --md-blue-grey-500: #607d8b;
  --md-blue-grey-600: #546e7a;
  --md-blue-grey-700: #455a64;
  --md-blue-grey-800: #37474f;
  --md-blue-grey-900: #263238;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2017, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| RenderedText
|----------------------------------------------------------------------------*/

:root {
  /* This is the padding value to fill the gaps between lines containing spans with background color. */
  --jp-private-code-span-padding: calc(
    (var(--jp-code-line-height) - 1) * var(--jp-code-font-size) / 2
  );
}

.jp-RenderedText {
  text-align: left;
  padding-left: var(--jp-code-padding);
  line-height: var(--jp-code-line-height);
  font-family: var(--jp-code-font-family);
}

.jp-RenderedText pre,
.jp-RenderedJavaScript pre,
.jp-RenderedHTMLCommon pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
  border: none;
  margin: 0;
  padding: 0;
}

.jp-RenderedText pre a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedText pre a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* console foregrounds and backgrounds */
.jp-RenderedText pre .ansi-black-fg {
  color: #3e424d;
}

.jp-RenderedText pre .ansi-red-fg {
  color: #e75c58;
}

.jp-RenderedText pre .ansi-green-fg {
  color: #00a250;
}

.jp-RenderedText pre .ansi-yellow-fg {
  color: #ddb62b;
}

.jp-RenderedText pre .ansi-blue-fg {
  color: #208ffb;
}

.jp-RenderedText pre .ansi-magenta-fg {
  color: #d160c4;
}

.jp-RenderedText pre .ansi-cyan-fg {
  color: #60c6c8;
}

.jp-RenderedText pre .ansi-white-fg {
  color: #c5c1b4;
}

.jp-RenderedText pre .ansi-black-bg {
  background-color: #3e424d;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-bg {
  background-color: #e75c58;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-bg {
  background-color: #00a250;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-bg {
  background-color: #ddb62b;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-bg {
  background-color: #208ffb;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-bg {
  background-color: #d160c4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-bg {
  background-color: #60c6c8;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-bg {
  background-color: #c5c1b4;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-black-intense-fg {
  color: #282c36;
}

.jp-RenderedText pre .ansi-red-intense-fg {
  color: #b22b31;
}

.jp-RenderedText pre .ansi-green-intense-fg {
  color: #007427;
}

.jp-RenderedText pre .ansi-yellow-intense-fg {
  color: #b27d12;
}

.jp-RenderedText pre .ansi-blue-intense-fg {
  color: #0065ca;
}

.jp-RenderedText pre .ansi-magenta-intense-fg {
  color: #a03196;
}

.jp-RenderedText pre .ansi-cyan-intense-fg {
  color: #258f8f;
}

.jp-RenderedText pre .ansi-white-intense-fg {
  color: #a1a6b2;
}

.jp-RenderedText pre .ansi-black-intense-bg {
  background-color: #282c36;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-red-intense-bg {
  background-color: #b22b31;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-green-intense-bg {
  background-color: #007427;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-yellow-intense-bg {
  background-color: #b27d12;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-blue-intense-bg {
  background-color: #0065ca;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-magenta-intense-bg {
  background-color: #a03196;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-cyan-intense-bg {
  background-color: #258f8f;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-white-intense-bg {
  background-color: #a1a6b2;
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-default-inverse-fg {
  color: var(--jp-ui-inverse-font-color0);
}

.jp-RenderedText pre .ansi-default-inverse-bg {
  background-color: var(--jp-inverse-layout-color0);
  padding: var(--jp-private-code-span-padding) 0;
}

.jp-RenderedText pre .ansi-bold {
  font-weight: bold;
}

.jp-RenderedText pre .ansi-underline {
  text-decoration: underline;
}

.jp-RenderedText[data-mime-type='application/vnd.jupyter.stderr'] {
  background: var(--jp-rendermime-error-background);
  padding-top: var(--jp-code-padding);
}

/*-----------------------------------------------------------------------------
| RenderedLatex
|----------------------------------------------------------------------------*/

.jp-RenderedLatex {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);
}

/* Left-justify outputs.*/
.jp-OutputArea-output.jp-RenderedLatex {
  padding: var(--jp-code-padding);
  text-align: left;
}

/*-----------------------------------------------------------------------------
| RenderedHTML
|----------------------------------------------------------------------------*/

.jp-RenderedHTMLCommon {
  color: var(--jp-content-font-color1);
  font-family: var(--jp-content-font-family);
  font-size: var(--jp-content-font-size1);
  line-height: var(--jp-content-line-height);

  /* Give a bit more R padding on Markdown text to keep line lengths reasonable */
  padding-right: 20px;
}

.jp-RenderedHTMLCommon em {
  font-style: italic;
}

.jp-RenderedHTMLCommon strong {
  font-weight: bold;
}

.jp-RenderedHTMLCommon u {
  text-decoration: underline;
}

.jp-RenderedHTMLCommon a:link {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:hover {
  text-decoration: underline;
  color: var(--jp-content-link-color);
}

.jp-RenderedHTMLCommon a:visited {
  text-decoration: none;
  color: var(--jp-content-link-color);
}

/* Headings */

.jp-RenderedHTMLCommon h1,
.jp-RenderedHTMLCommon h2,
.jp-RenderedHTMLCommon h3,
.jp-RenderedHTMLCommon h4,
.jp-RenderedHTMLCommon h5,
.jp-RenderedHTMLCommon h6 {
  line-height: var(--jp-content-heading-line-height);
  font-weight: var(--jp-content-heading-font-weight);
  font-style: normal;
  margin: var(--jp-content-heading-margin-top) 0
    var(--jp-content-heading-margin-bottom) 0;
}

.jp-RenderedHTMLCommon h1:first-child,
.jp-RenderedHTMLCommon h2:first-child,
.jp-RenderedHTMLCommon h3:first-child,
.jp-RenderedHTMLCommon h4:first-child,
.jp-RenderedHTMLCommon h5:first-child,
.jp-RenderedHTMLCommon h6:first-child {
  margin-top: calc(0.5 * var(--jp-content-heading-margin-top));
}

.jp-RenderedHTMLCommon h1:last-child,
.jp-RenderedHTMLCommon h2:last-child,
.jp-RenderedHTMLCommon h3:last-child,
.jp-RenderedHTMLCommon h4:last-child,
.jp-RenderedHTMLCommon h5:last-child,
.jp-RenderedHTMLCommon h6:last-child {
  margin-bottom: calc(0.5 * var(--jp-content-heading-margin-bottom));
}

.jp-RenderedHTMLCommon h1 {
  font-size: var(--jp-content-font-size5);
}

.jp-RenderedHTMLCommon h2 {
  font-size: var(--jp-content-font-size4);
}

.jp-RenderedHTMLCommon h3 {
  font-size: var(--jp-content-font-size3);
}

.jp-RenderedHTMLCommon h4 {
  font-size: var(--jp-content-font-size2);
}

.jp-RenderedHTMLCommon h5 {
  font-size: var(--jp-content-font-size1);
}

.jp-RenderedHTMLCommon h6 {
  font-size: var(--jp-content-font-size0);
}

/* Lists */

/* stylelint-disable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon ul:not(.list-inline),
.jp-RenderedHTMLCommon ol:not(.list-inline) {
  padding-left: 2em;
}

.jp-RenderedHTMLCommon ul {
  list-style: disc;
}

.jp-RenderedHTMLCommon ul ul {
  list-style: square;
}

.jp-RenderedHTMLCommon ul ul ul {
  list-style: circle;
}

.jp-RenderedHTMLCommon ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol ol {
  list-style: upper-alpha;
}

.jp-RenderedHTMLCommon ol ol ol {
  list-style: lower-alpha;
}

.jp-RenderedHTMLCommon ol ol ol ol {
  list-style: lower-roman;
}

.jp-RenderedHTMLCommon ol ol ol ol ol {
  list-style: decimal;
}

.jp-RenderedHTMLCommon ol,
.jp-RenderedHTMLCommon ul {
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon ul ul,
.jp-RenderedHTMLCommon ul ol,
.jp-RenderedHTMLCommon ol ul,
.jp-RenderedHTMLCommon ol ol {
  margin-bottom: 0;
}

/* stylelint-enable selector-max-type, selector-max-compound-selectors */

.jp-RenderedHTMLCommon hr {
  color: var(--jp-border-color2);
  background-color: var(--jp-border-color1);
  margin-top: 1em;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon > pre {
  margin: 1.5em 2em;
}

.jp-RenderedHTMLCommon pre,
.jp-RenderedHTMLCommon code {
  border: 0;
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  line-height: var(--jp-code-line-height);
  padding: 0;
  white-space: pre-wrap;
}

.jp-RenderedHTMLCommon :not(pre) > code {
  background-color: var(--jp-layout-color2);
  padding: 1px 5px;
}

/* Tables */

.jp-RenderedHTMLCommon table {
  border-collapse: collapse;
  border-spacing: 0;
  border: none;
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  table-layout: fixed;
  margin-left: auto;
  margin-bottom: 1em;
  margin-right: auto;
}

.jp-RenderedHTMLCommon thead {
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  vertical-align: bottom;
}

.jp-RenderedHTMLCommon td,
.jp-RenderedHTMLCommon th,
.jp-RenderedHTMLCommon tr {
  vertical-align: middle;
  padding: 0.5em;
  line-height: normal;
  white-space: normal;
  max-width: none;
  border: none;
}

.jp-RenderedMarkdown.jp-RenderedHTMLCommon td,
.jp-RenderedMarkdown.jp-RenderedHTMLCommon th {
  max-width: none;
}

:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon td,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon th,
:not(.jp-RenderedMarkdown).jp-RenderedHTMLCommon tr {
  text-align: right;
}

.jp-RenderedHTMLCommon th {
  font-weight: bold;
}

.jp-RenderedHTMLCommon tbody tr:nth-child(odd) {
  background: var(--jp-layout-color0);
}

.jp-RenderedHTMLCommon tbody tr:nth-child(even) {
  background: var(--jp-rendermime-table-row-background);
}

.jp-RenderedHTMLCommon tbody tr:hover {
  background: var(--jp-rendermime-table-row-hover-background);
}

.jp-RenderedHTMLCommon p {
  text-align: left;
  margin: 0;
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon img {
  -moz-force-broken-image-icon: 1;
}

/* Restrict to direct children as other images could be nested in other content. */
.jp-RenderedHTMLCommon > img {
  display: block;
  margin-left: 0;
  margin-right: 0;
  margin-bottom: 1em;
}

/* Change color behind transparent images if they need it... */
[data-jp-theme-light='false'] .jp-RenderedImage img.jp-needs-light-background {
  background-color: var(--jp-inverse-layout-color1);
}

[data-jp-theme-light='true'] .jp-RenderedImage img.jp-needs-dark-background {
  background-color: var(--jp-inverse-layout-color1);
}

.jp-RenderedHTMLCommon img,
.jp-RenderedImage img,
.jp-RenderedHTMLCommon svg,
.jp-RenderedSVG svg {
  max-width: 100%;
  height: auto;
}

.jp-RenderedHTMLCommon img.jp-mod-unconfined,
.jp-RenderedImage img.jp-mod-unconfined,
.jp-RenderedHTMLCommon svg.jp-mod-unconfined,
.jp-RenderedSVG svg.jp-mod-unconfined {
  max-width: none;
}

.jp-RenderedHTMLCommon .alert {
  padding: var(--jp-notebook-padding);
  border: var(--jp-border-width) solid transparent;
  border-radius: var(--jp-border-radius);
  margin-bottom: 1em;
}

.jp-RenderedHTMLCommon .alert-info {
  color: var(--jp-info-color0);
  background-color: var(--jp-info-color3);
  border-color: var(--jp-info-color2);
}

.jp-RenderedHTMLCommon .alert-info hr {
  border-color: var(--jp-info-color3);
}

.jp-RenderedHTMLCommon .alert-info > p:last-child,
.jp-RenderedHTMLCommon .alert-info > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-warning {
  color: var(--jp-warn-color0);
  background-color: var(--jp-warn-color3);
  border-color: var(--jp-warn-color2);
}

.jp-RenderedHTMLCommon .alert-warning hr {
  border-color: var(--jp-warn-color3);
}

.jp-RenderedHTMLCommon .alert-warning > p:last-child,
.jp-RenderedHTMLCommon .alert-warning > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-success {
  color: var(--jp-success-color0);
  background-color: var(--jp-success-color3);
  border-color: var(--jp-success-color2);
}

.jp-RenderedHTMLCommon .alert-success hr {
  border-color: var(--jp-success-color3);
}

.jp-RenderedHTMLCommon .alert-success > p:last-child,
.jp-RenderedHTMLCommon .alert-success > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon .alert-danger {
  color: var(--jp-error-color0);
  background-color: var(--jp-error-color3);
  border-color: var(--jp-error-color2);
}

.jp-RenderedHTMLCommon .alert-danger hr {
  border-color: var(--jp-error-color3);
}

.jp-RenderedHTMLCommon .alert-danger > p:last-child,
.jp-RenderedHTMLCommon .alert-danger > ul:last-child {
  margin-bottom: 0;
}

.jp-RenderedHTMLCommon blockquote {
  margin: 1em 2em;
  padding: 0 1em;
  border-left: 5px solid var(--jp-border-color2);
}

a.jp-InternalAnchorLink {
  visibility: hidden;
  margin-left: 8px;
  color: var(--md-blue-800);
}

h1:hover .jp-InternalAnchorLink,
h2:hover .jp-InternalAnchorLink,
h3:hover .jp-InternalAnchorLink,
h4:hover .jp-InternalAnchorLink,
h5:hover .jp-InternalAnchorLink,
h6:hover .jp-InternalAnchorLink {
  visibility: visible;
}

.jp-RenderedHTMLCommon kbd {
  background-color: var(--jp-rendermime-table-row-background);
  border: 1px solid var(--jp-border-color0);
  border-bottom-color: var(--jp-border-color2);
  border-radius: 3px;
  box-shadow: inset 0 -1px 0 rgba(0, 0, 0, 0.25);
  display: inline-block;
  font-size: var(--jp-ui-font-size0);
  line-height: 1em;
  padding: 0.2em 0.5em;
}

/* Most direct children of .jp-RenderedHTMLCommon have a margin-bottom of 1.0.
 * At the bottom of cells this is a bit too much as there is also spacing
 * between cells. Going all the way to 0 gets too tight between markdown and
 * code cells.
 */
.jp-RenderedHTMLCommon > *:last-child {
  margin-bottom: 0.5em;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Copyright (c) 2014-2017, PhosphorJS Contributors
|
| Distributed under the terms of the BSD 3-Clause License.
|
| The full license is in the file LICENSE, distributed with this software.
|----------------------------------------------------------------------------*/

.lm-cursor-backdrop {
  position: fixed;
  width: 200px;
  height: 200px;
  margin-top: -100px;
  margin-left: -100px;
  will-change: transform;
  z-index: 100;
}

.lm-mod-drag-image {
  will-change: transform;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-lineFormSearch {
  padding: 4px 12px;
  background-color: var(--jp-layout-color2);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
  font-size: var(--jp-ui-font-size1);
}

.jp-lineFormCaption {
  font-size: var(--jp-ui-font-size0);
  line-height: var(--jp-ui-font-size1);
  margin-top: 4px;
  color: var(--jp-ui-font-color0);
}

.jp-baseLineForm {
  border: none;
  border-radius: 0;
  position: absolute;
  background-size: 16px;
  background-repeat: no-repeat;
  background-position: center;
  outline: none;
}

.jp-lineFormButtonContainer {
  top: 4px;
  right: 8px;
  height: 24px;
  padding: 0 12px;
  width: 12px;
}

.jp-lineFormButtonIcon {
  top: 0;
  right: 0;
  background-color: var(--jp-brand-color1);
  height: 100%;
  width: 100%;
  box-sizing: border-box;
  padding: 4px 6px;
}

.jp-lineFormButton {
  top: 0;
  right: 0;
  background-color: transparent;
  height: 100%;
  width: 100%;
  box-sizing: border-box;
}

.jp-lineFormWrapper {
  overflow: hidden;
  padding: 0 8px;
  border: 1px solid var(--jp-border-color0);
  background-color: var(--jp-input-active-background);
  height: 22px;
}

.jp-lineFormWrapperFocusWithin {
  border: var(--jp-border-width) solid var(--md-blue-500);
  box-shadow: inset 0 0 4px var(--md-blue-300);
}

.jp-lineFormInput {
  background: transparent;
  width: 200px;
  height: 100%;
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  line-height: 28px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) 2014-2016, Jupyter Development Team.
|
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-JSONEditor {
  display: flex;
  flex-direction: column;
  width: 100%;
}

.jp-JSONEditor-host {
  flex: 1 1 auto;
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  border-radius: 0;
  background: var(--jp-layout-color0);
  min-height: 50px;
  padding: 1px;
}

.jp-JSONEditor.jp-mod-error .jp-JSONEditor-host {
  border-color: red;
  outline-color: red;
}

.jp-JSONEditor-header {
  display: flex;
  flex: 1 0 auto;
  padding: 0 0 0 12px;
}

.jp-JSONEditor-header label {
  flex: 0 0 auto;
}

.jp-JSONEditor-commitButton {
  height: 16px;
  width: 16px;
  background-size: 18px;
  background-repeat: no-repeat;
  background-position: center;
}

.jp-JSONEditor-host.jp-mod-focused {
  background-color: var(--jp-input-active-background);
  border: 1px solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

.jp-Editor.jp-mod-dropTarget {
  border: var(--jp-border-width) solid var(--jp-input-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/
.jp-DocumentSearch-input {
  border: none;
  outline: none;
  color: var(--jp-ui-font-color0);
  font-size: var(--jp-ui-font-size1);
  background-color: var(--jp-layout-color0);
  font-family: var(--jp-ui-font-family);
  padding: 2px 1px;
  resize: none;
}

.jp-DocumentSearch-overlay {
  position: absolute;
  background-color: var(--jp-toolbar-background);
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  border-left: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  top: 0;
  right: 0;
  z-index: 7;
  min-width: 405px;
  padding: 2px;
  font-size: var(--jp-ui-font-size1);

  --jp-private-document-search-button-height: 20px;
}

.jp-DocumentSearch-overlay button {
  background-color: var(--jp-toolbar-background);
  outline: 0;
}

.jp-DocumentSearch-overlay button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-overlay button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-overlay-row {
  display: flex;
  align-items: center;
  margin-bottom: 2px;
}

.jp-DocumentSearch-button-content {
  display: inline-block;
  cursor: pointer;
  box-sizing: border-box;
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-button-content svg {
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-input-wrapper {
  border: var(--jp-border-width) solid var(--jp-border-color0);
  display: flex;
  background-color: var(--jp-layout-color0);
  margin: 2px;
}

.jp-DocumentSearch-input-wrapper:focus-within {
  border-color: var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper {
  all: initial;
  overflow: hidden;
  display: inline-block;
  border: none;
  box-sizing: border-box;
}

.jp-DocumentSearch-toggle-wrapper {
  width: 14px;
  height: 14px;
}

.jp-DocumentSearch-button-wrapper {
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
}

.jp-DocumentSearch-toggle-wrapper:focus,
.jp-DocumentSearch-button-wrapper:focus {
  outline: var(--jp-border-width) solid
    var(--jp-cell-editor-active-border-color);
  outline-offset: -1px;
}

.jp-DocumentSearch-toggle-wrapper,
.jp-DocumentSearch-button-wrapper,
.jp-DocumentSearch-button-content:focus {
  outline: none;
}

.jp-DocumentSearch-toggle-placeholder {
  width: 5px;
}

.jp-DocumentSearch-input-button::before {
  display: block;
  padding-top: 100%;
}

.jp-DocumentSearch-input-button-off {
  opacity: var(--jp-search-toggle-off-opacity);
}

.jp-DocumentSearch-input-button-off:hover {
  opacity: var(--jp-search-toggle-hover-opacity);
}

.jp-DocumentSearch-input-button-on {
  opacity: var(--jp-search-toggle-on-opacity);
}

.jp-DocumentSearch-index-counter {
  padding-left: 10px;
  padding-right: 10px;
  user-select: none;
  min-width: 35px;
  display: inline-block;
}

.jp-DocumentSearch-up-down-wrapper {
  display: inline-block;
  padding-right: 2px;
  margin-left: auto;
  white-space: nowrap;
}

.jp-DocumentSearch-spacer {
  margin-left: auto;
}

.jp-DocumentSearch-up-down-wrapper button {
  outline: 0;
  border: none;
  width: var(--jp-private-document-search-button-height);
  height: var(--jp-private-document-search-button-height);
  vertical-align: middle;
  margin: 1px 5px 2px;
}

.jp-DocumentSearch-up-down-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-up-down-button:active {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-filter-button {
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-filter-button:hover {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled {
  background-color: var(--jp-layout-color2);
}

.jp-DocumentSearch-filter-button-enabled:hover {
  background-color: var(--jp-layout-color3);
}

.jp-DocumentSearch-search-options {
  padding: 0 8px;
  margin-left: 3px;
  width: 100%;
  display: grid;
  justify-content: start;
  grid-template-columns: 1fr 1fr;
  align-items: center;
  justify-items: stretch;
}

.jp-DocumentSearch-search-filter-disabled {
  color: var(--jp-ui-font-color2);
}

.jp-DocumentSearch-search-filter {
  display: flex;
  align-items: center;
  user-select: none;
}

.jp-DocumentSearch-regex-error {
  color: var(--jp-error-color0);
}

.jp-DocumentSearch-replace-button-wrapper {
  overflow: hidden;
  display: inline-block;
  box-sizing: border-box;
  border: var(--jp-border-width) solid var(--jp-border-color0);
  margin: auto 2px;
  padding: 1px 4px;
  height: calc(var(--jp-private-document-search-button-height) + 2px);
}

.jp-DocumentSearch-replace-button-wrapper:focus {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
}

.jp-DocumentSearch-replace-button {
  display: inline-block;
  text-align: center;
  cursor: pointer;
  box-sizing: border-box;
  color: var(--jp-ui-font-color1);

  /* height - 2 * (padding of wrapper) */
  line-height: calc(var(--jp-private-document-search-button-height) - 2px);
  width: 100%;
  height: 100%;
}

.jp-DocumentSearch-replace-button:focus {
  outline: none;
}

.jp-DocumentSearch-replace-wrapper-class {
  margin-left: 14px;
  display: flex;
}

.jp-DocumentSearch-replace-toggle {
  border: none;
  background-color: var(--jp-toolbar-background);
  border-radius: var(--jp-border-radius);
}

.jp-DocumentSearch-replace-toggle:hover {
  background-color: var(--jp-layout-color2);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.cm-editor {
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  border: 0;
  border-radius: 0;
  height: auto;

  /* Changed to auto to autogrow */
}

.cm-editor pre {
  padding: 0 var(--jp-code-padding);
}

.jp-CodeMirrorEditor[data-type='inline'] .cm-dialog {
  background-color: var(--jp-layout-color0);
  color: var(--jp-content-font-color1);
}

.jp-CodeMirrorEditor {
  cursor: text;
}

/* When zoomed out 67% and 33% on a screen of 1440 width x 900 height */
@media screen and (min-width: 2138px) and (max-width: 4319px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width1) solid
      var(--jp-editor-cursor-color);
  }
}

/* When zoomed out less than 33% */
@media screen and (min-width: 4320px) {
  .jp-CodeMirrorEditor[data-type='inline'] .cm-cursor {
    border-left: var(--jp-code-cursor-width2) solid
      var(--jp-editor-cursor-color);
  }
}

.cm-editor.jp-mod-readOnly .cm-cursor {
  display: none;
}

.jp-CollaboratorCursor {
  border-left: 5px solid transparent;
  border-right: 5px solid transparent;
  border-top: none;
  border-bottom: 3px solid;
  background-clip: content-box;
  margin-left: -5px;
  margin-right: -5px;
}

.cm-searching,
.cm-searching span {
  /* `.cm-searching span`: we need to override syntax highlighting */
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.cm-searching::selection,
.cm-searching span::selection {
  background-color: var(--jp-search-unselected-match-background-color);
  color: var(--jp-search-unselected-match-color);
}

.jp-current-match > .cm-searching,
.jp-current-match > .cm-searching span,
.cm-searching > .jp-current-match,
.cm-searching > .jp-current-match span {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.jp-current-match > .cm-searching::selection,
.cm-searching > .jp-current-match::selection,
.jp-current-match > .cm-searching span::selection {
  background-color: var(--jp-search-selected-match-background-color);
  color: var(--jp-search-selected-match-color);
}

.cm-trailingspace {
  background-image: url(data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAFCAYAAAB4ka1VAAAAsElEQVQIHQGlAFr/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA7+r3zKmT0/+pk9P/7+r3zAAAAAAAAAAABAAAAAAAAAAA6OPzM+/q9wAAAAAA6OPzMwAAAAAAAAAAAgAAAAAAAAAAGR8NiRQaCgAZIA0AGR8NiQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAQyoYJ/SY80UAAAAASUVORK5CYII=);
  background-position: center left;
  background-repeat: repeat-x;
}

.jp-CollaboratorCursor-hover {
  position: absolute;
  z-index: 1;
  transform: translateX(-50%);
  color: white;
  border-radius: 3px;
  padding-left: 4px;
  padding-right: 4px;
  padding-top: 1px;
  padding-bottom: 1px;
  text-align: center;
  font-size: var(--jp-ui-font-size1);
  white-space: nowrap;
}

.jp-CodeMirror-ruler {
  border-left: 1px dashed var(--jp-border-color2);
}

/* Styles for shared cursors (remote cursor locations and selected ranges) */
.jp-CodeMirrorEditor .cm-ySelectionCaret {
  position: relative;
  border-left: 1px solid black;
  margin-left: -1px;
  margin-right: -1px;
  box-sizing: border-box;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret > .cm-ySelectionInfo {
  white-space: nowrap;
  position: absolute;
  top: -1.15em;
  padding-bottom: 0.05em;
  left: -1px;
  font-size: 0.95em;
  font-family: var(--jp-ui-font-family);
  font-weight: bold;
  line-height: normal;
  user-select: none;
  color: white;
  padding-left: 2px;
  padding-right: 2px;
  z-index: 101;
  transition: opacity 0.3s ease-in-out;
}

.jp-CodeMirrorEditor .cm-ySelectionInfo {
  transition-delay: 0.7s;
  opacity: 0;
}

.jp-CodeMirrorEditor .cm-ySelectionCaret:hover > .cm-ySelectionInfo {
  opacity: 1;
  transition-delay: 0s;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-MimeDocument {
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-filebrowser-button-height: 28px;
  --jp-private-filebrowser-button-width: 48px;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-FileBrowser .jp-SidePanel-content {
  display: flex;
  flex-direction: column;
}

.jp-FileBrowser-toolbar.jp-Toolbar {
  flex-wrap: wrap;
  row-gap: 12px;
  border-bottom: none;
  height: auto;
  margin: 8px 12px 0;
  box-shadow: none;
  padding: 0;
  justify-content: flex-start;
}

.jp-FileBrowser-Panel {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
}

.jp-BreadCrumbs {
  flex: 0 0 auto;
  margin: 8px 12px;
}

.jp-BreadCrumbs-item {
  margin: 0 2px;
  padding: 0 2px;
  border-radius: var(--jp-border-radius);
  cursor: pointer;
}

.jp-BreadCrumbs-item:hover {
  background-color: var(--jp-layout-color2);
}

.jp-BreadCrumbs-item:first-child {
  margin-left: 0;
}

.jp-BreadCrumbs-item.jp-mod-dropTarget {
  background-color: var(--jp-brand-color2);
  opacity: 0.7;
}

/*-----------------------------------------------------------------------------
| Buttons
|----------------------------------------------------------------------------*/

.jp-FileBrowser-toolbar > .jp-Toolbar-item {
  flex: 0 0 auto;
  padding-left: 0;
  padding-right: 2px;
  align-items: center;
  height: unset;
}

.jp-FileBrowser-toolbar > .jp-Toolbar-item .jp-ToolbarButtonComponent {
  width: 40px;
}

/*-----------------------------------------------------------------------------
| Other styles
|----------------------------------------------------------------------------*/

.jp-FileDialog.jp-mod-conflict input {
  color: var(--jp-error-color1);
}

.jp-FileDialog .jp-new-name-title {
  margin-top: 12px;
}

.jp-LastModified-hidden {
  display: none;
}

.jp-FileSize-hidden {
  display: none;
}

.jp-FileBrowser .lm-AccordionPanel > h3:first-child {
  display: none;
}

/*-----------------------------------------------------------------------------
| DirListing
|----------------------------------------------------------------------------*/

.jp-DirListing {
  flex: 1 1 auto;
  display: flex;
  flex-direction: column;
  outline: 0;
}

.jp-DirListing-header {
  flex: 0 0 auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  overflow: hidden;
  border-top: var(--jp-border-width) solid var(--jp-border-color2);
  border-bottom: var(--jp-border-width) solid var(--jp-border-color1);
  box-shadow: var(--jp-toolbar-box-shadow);
  z-index: 2;
}

.jp-DirListing-headerItem {
  padding: 4px 12px 2px;
  font-weight: 500;
}

.jp-DirListing-headerItem:hover {
  background: var(--jp-layout-color2);
}

.jp-DirListing-headerItem.jp-id-name {
  flex: 1 0 84px;
}

.jp-DirListing-headerItem.jp-id-modified {
  flex: 0 0 112px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-DirListing-headerItem.jp-id-filesize {
  flex: 0 0 75px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
}

.jp-id-narrow {
  display: none;
  flex: 0 0 5px;
  padding: 4px;
  border-left: var(--jp-border-width) solid var(--jp-border-color2);
  text-align: right;
  color: var(--jp-border-color2);
}

.jp-DirListing-narrow .jp-id-narrow {
  display: block;
}

.jp-DirListing-narrow .jp-id-modified,
.jp-DirListing-narrow .jp-DirListing-itemModified {
  display: none;
}

.jp-DirListing-headerItem.jp-mod-selected {
  font-weight: 600;
}

/* increase specificity to override bundled default */
.jp-DirListing-content {
  flex: 1 1 auto;
  margin: 0;
  padding: 0;
  list-style-type: none;
  overflow: auto;
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-content mark {
  color: var(--jp-ui-font-color0);
  background-color: transparent;
  font-weight: bold;
}

.jp-DirListing-content .jp-DirListing-item.jp-mod-selected mark {
  color: var(--jp-ui-inverse-font-color0);
}

/* Style the directory listing content when a user drops a file to upload */
.jp-DirListing.jp-mod-native-drop .jp-DirListing-content {
  outline: 5px dashed rgba(128, 128, 128, 0.5);
  outline-offset: -10px;
  cursor: copy;
}

.jp-DirListing-item {
  display: flex;
  flex-direction: row;
  align-items: center;
  padding: 4px 12px;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-DirListing-checkboxWrapper {
  /* Increases hit area of checkbox. */
  padding: 4px;
}

.jp-DirListing-header
  .jp-DirListing-checkboxWrapper
  + .jp-DirListing-headerItem {
  padding-left: 4px;
}

.jp-DirListing-content .jp-DirListing-checkboxWrapper {
  position: relative;
  left: -4px;
  margin: -4px 0 -4px -8px;
}

.jp-DirListing-checkboxWrapper.jp-mod-visible {
  visibility: visible;
}

/* For devices that support hovering, hide checkboxes until hovered, selected...
*/
@media (hover: hover) {
  .jp-DirListing-checkboxWrapper {
    visibility: hidden;
  }

  .jp-DirListing-item:hover .jp-DirListing-checkboxWrapper,
  .jp-DirListing-item.jp-mod-selected .jp-DirListing-checkboxWrapper {
    visibility: visible;
  }
}

.jp-DirListing-item[data-is-dot] {
  opacity: 75%;
}

.jp-DirListing-item.jp-mod-selected {
  color: var(--jp-ui-inverse-font-color1);
  background: var(--jp-brand-color1);
}

.jp-DirListing-item.jp-mod-dropTarget {
  background: var(--jp-brand-color3);
}

.jp-DirListing-item:hover:not(.jp-mod-selected) {
  background: var(--jp-layout-color2);
}

.jp-DirListing-itemIcon {
  flex: 0 0 20px;
  margin-right: 4px;
}

.jp-DirListing-itemText {
  flex: 1 0 64px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  user-select: none;
}

.jp-DirListing-itemText:focus {
  outline-width: 2px;
  outline-color: var(--jp-inverse-layout-color1);
  outline-style: solid;
  outline-offset: 1px;
}

.jp-DirListing-item.jp-mod-selected .jp-DirListing-itemText:focus {
  outline-color: var(--jp-layout-color1);
}

.jp-DirListing-itemModified {
  flex: 0 0 125px;
  text-align: right;
}

.jp-DirListing-itemFileSize {
  flex: 0 0 90px;
  text-align: right;
}

.jp-DirListing-editor {
  flex: 1 0 64px;
  outline: none;
  border: none;
  color: var(--jp-ui-font-color1);
  background-color: var(--jp-layout-color1);
}

.jp-DirListing-item.jp-mod-running .jp-DirListing-itemIcon::before {
  color: var(--jp-success-color1);
  content: '\25CF';
  font-size: 8px;
  position: absolute;
  left: -8px;
}

.jp-DirListing-item.jp-mod-running.jp-mod-selected
  .jp-DirListing-itemIcon::before {
  color: var(--jp-ui-inverse-font-color1);
}

.jp-DirListing-item.lm-mod-drag-image,
.jp-DirListing-item.jp-mod-selected.lm-mod-drag-image {
  font-size: var(--jp-ui-font-size1);
  padding-left: 4px;
  margin-left: 4px;
  width: 160px;
  background-color: var(--jp-ui-inverse-font-color2);
  box-shadow: var(--jp-elevation-z2);
  border-radius: 0;
  color: var(--jp-ui-font-color1);
  transform: translateX(-40%) translateY(-58%);
}

.jp-Document {
  min-width: 120px;
  min-height: 120px;
  outline: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Main OutputArea
| OutputArea has a list of Outputs
|----------------------------------------------------------------------------*/

.jp-OutputArea {
  overflow-y: auto;
}

.jp-OutputArea-child {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-OutputPrompt {
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-outprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
  opacity: var(--jp-cell-prompt-opacity);

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-OutputArea-prompt {
  display: table-cell;
  vertical-align: top;
}

.jp-OutputArea-output {
  display: table-cell;
  width: 100%;
  height: auto;
  overflow: auto;
  user-select: text;
  -moz-user-select: text;
  -webkit-user-select: text;
  -ms-user-select: text;
}

.jp-OutputArea .jp-RenderedText {
  padding-left: 1ch;
}

/**
 * Prompt overlay.
 */

.jp-OutputArea-promptOverlay {
  position: absolute;
  top: 0;
  width: var(--jp-cell-prompt-width);
  height: 100%;
  opacity: 0.5;
}

.jp-OutputArea-promptOverlay:hover {
  background: var(--jp-layout-color2);
  box-shadow: inset 0 0 1px var(--jp-inverse-layout-color0);
  cursor: zoom-out;
}

.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay:hover {
  cursor: zoom-in;
}

/**
 * Isolated output.
 */
.jp-OutputArea-output.jp-mod-isolated {
  width: 100%;
  display: block;
}

/*
When drag events occur, `lm-mod-override-cursor` is added to the body.
Because iframes steal all cursor events, the following two rules are necessary
to suppress pointer events while resize drags are occurring. There may be a
better solution to this problem.
*/
body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated {
  position: relative;
}

body.lm-mod-override-cursor .jp-OutputArea-output.jp-mod-isolated::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: transparent;
}

/* pre */

.jp-OutputArea-output pre {
  border: none;
  margin: 0;
  padding: 0;
  overflow-x: auto;
  overflow-y: auto;
  word-break: break-all;
  word-wrap: break-word;
  white-space: pre-wrap;
}

/* tables */

.jp-OutputArea-output.jp-RenderedHTMLCommon table {
  margin-left: 0;
  margin-right: 0;
}

/* description lists */

.jp-OutputArea-output dl,
.jp-OutputArea-output dt,
.jp-OutputArea-output dd {
  display: block;
}

.jp-OutputArea-output dl {
  width: 100%;
  overflow: hidden;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dt {
  font-weight: bold;
  float: left;
  width: 20%;
  padding: 0;
  margin: 0;
}

.jp-OutputArea-output dd {
  float: left;
  width: 80%;
  padding: 0;
  margin: 0;
}

.jp-TrimmedOutputs pre {
  background: var(--jp-layout-color3);
  font-size: calc(var(--jp-code-font-size) * 1.4);
  text-align: center;
  text-transform: uppercase;
}

/* Hide the gutter in case of
 *  - nested output areas (e.g. in the case of output widgets)
 *  - mirrored output areas
 */
.jp-OutputArea .jp-OutputArea .jp-OutputArea-prompt {
  display: none;
}

/* Hide empty lines in the output area, for instance due to cleared widgets */
.jp-OutputArea-prompt:empty {
  padding: 0;
  border: 0;
}

/*-----------------------------------------------------------------------------
| executeResult is added to any Output-result for the display of the object
| returned by a cell
|----------------------------------------------------------------------------*/

.jp-OutputArea-output.jp-OutputArea-executeResult {
  margin-left: 0;
  width: 100%;
}

/* Text output with the Out[] prompt needs a top padding to match the
 * alignment of the Out[] prompt itself.
 */
.jp-OutputArea-executeResult .jp-RenderedText.jp-OutputArea-output {
  padding-top: var(--jp-code-padding);
  border-top: var(--jp-border-width) solid transparent;
}

/*-----------------------------------------------------------------------------
| The Stdin output
|----------------------------------------------------------------------------*/

.jp-Stdin-prompt {
  color: var(--jp-content-font-color0);
  padding-right: var(--jp-code-padding);
  vertical-align: baseline;
  flex: 0 0 auto;
}

.jp-Stdin-input {
  font-family: var(--jp-code-font-family);
  font-size: inherit;
  color: inherit;
  background-color: inherit;
  width: 42%;
  min-width: 200px;

  /* make sure input baseline aligns with prompt */
  vertical-align: baseline;

  /* padding + margin = 0.5em between prompt and cursor */
  padding: 0 0.25em;
  margin: 0 0.25em;
  flex: 0 0 70%;
}

.jp-Stdin-input::placeholder {
  opacity: 0;
}

.jp-Stdin-input:focus {
  box-shadow: none;
}

.jp-Stdin-input:focus::placeholder {
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Output Area View
|----------------------------------------------------------------------------*/

.jp-LinkedOutputView .jp-OutputArea {
  height: 100%;
  display: block;
}

.jp-LinkedOutputView .jp-OutputArea-output:only-child {
  height: 100%;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

@media print {
  .jp-OutputArea-child {
    break-inside: avoid-page;
  }
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-OutputPrompt {
    display: table-row;
    text-align: left;
  }

  .jp-OutputArea-child .jp-OutputArea-output {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }
}

/* Trimmed outputs warning */
.jp-TrimmedOutputs > a {
  margin: 10px;
  text-decoration: none;
  cursor: pointer;
}

.jp-TrimmedOutputs > a:hover {
  text-decoration: none;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Table of Contents
|----------------------------------------------------------------------------*/

:root {
  --jp-private-toc-active-width: 4px;
}

.jp-TableOfContents {
  display: flex;
  flex-direction: column;
  background: var(--jp-layout-color1);
  color: var(--jp-ui-font-color1);
  font-size: var(--jp-ui-font-size1);
  height: 100%;
}

.jp-TableOfContents-placeholder {
  text-align: center;
}

.jp-TableOfContents-placeholderContent {
  color: var(--jp-content-font-color2);
  padding: 8px;
}

.jp-TableOfContents-placeholderContent > h3 {
  margin-bottom: var(--jp-content-heading-margin-bottom);
}

.jp-TableOfContents .jp-SidePanel-content {
  overflow-y: auto;
}

.jp-TableOfContents-tree {
  margin: 4px;
}

.jp-TableOfContents ol {
  list-style-type: none;
}

/* stylelint-disable-next-line selector-max-type */
.jp-TableOfContents li > ol {
  /* Align left border with triangle icon center */
  padding-left: 11px;
}

.jp-TableOfContents-content {
  /* left margin for the active heading indicator */
  margin: 0 0 0 var(--jp-private-toc-active-width);
  padding: 0;
  background-color: var(--jp-layout-color1);
}

.jp-tocItem {
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

.jp-tocItem-heading {
  display: flex;
  cursor: pointer;
}

.jp-tocItem-heading:hover {
  background-color: var(--jp-layout-color2);
}

.jp-tocItem-content {
  display: block;
  padding: 4px 0;
  white-space: nowrap;
  text-overflow: ellipsis;
  overflow-x: hidden;
}

.jp-tocItem-collapser {
  height: 20px;
  margin: 2px 2px 0;
  padding: 0;
  background: none;
  border: none;
  cursor: pointer;
}

.jp-tocItem-collapser:hover {
  background-color: var(--jp-layout-color3);
}

/* Active heading indicator */

.jp-tocItem-heading::before {
  content: ' ';
  background: transparent;
  width: var(--jp-private-toc-active-width);
  height: 24px;
  position: absolute;
  left: 0;
  border-radius: var(--jp-border-radius);
}

.jp-tocItem-heading.jp-tocItem-active::before {
  background-color: var(--jp-brand-color1);
}

.jp-tocItem-heading:hover.jp-tocItem-active::before {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

.jp-Collapser {
  flex: 0 0 var(--jp-cell-collapser-width);
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
  border-radius: var(--jp-border-radius);
  opacity: 1;
}

.jp-Collapser-child {
  display: block;
  width: 100%;
  box-sizing: border-box;

  /* height: 100% doesn't work because the height of its parent is computed from content */
  position: absolute;
  top: 0;
  bottom: 0;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Hiding collapsers in print mode.

Note: input and output wrappers have "display: block" propery in print mode.
*/

@media print {
  .jp-Collapser {
    display: none;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Header/Footer
|----------------------------------------------------------------------------*/

/* Hidden by zero height by default */
.jp-CellHeader,
.jp-CellFooter {
  height: 0;
  width: 100%;
  padding: 0;
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Input
|----------------------------------------------------------------------------*/

/* All input areas */
.jp-InputArea {
  display: table;
  table-layout: fixed;
  width: 100%;
  overflow: hidden;
}

.jp-InputArea-editor {
  display: table-cell;
  overflow: hidden;
  vertical-align: top;

  /* This is the non-active, default styling */
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  background: var(--jp-cell-editor-background);
}

.jp-InputPrompt {
  display: table-cell;
  vertical-align: top;
  width: var(--jp-cell-prompt-width);
  color: var(--jp-cell-inprompt-font-color);
  font-family: var(--jp-cell-prompt-font-family);
  padding: var(--jp-code-padding);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  opacity: var(--jp-cell-prompt-opacity);
  line-height: var(--jp-code-line-height);
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;

  /* Right align prompt text, don't wrap to handle large prompt numbers */
  text-align: right;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;

  /* Disable text selection */
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
}

/*-----------------------------------------------------------------------------
| Mobile
|----------------------------------------------------------------------------*/
@media only screen and (max-width: 760px) {
  .jp-InputArea-editor {
    display: table-row;
    margin-left: var(--jp-notebook-padding);
  }

  .jp-InputPrompt {
    display: table-row;
    text-align: left;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Placeholder {
  display: table;
  table-layout: fixed;
  width: 100%;
}

.jp-Placeholder-prompt {
  display: table-cell;
  box-sizing: border-box;
}

.jp-Placeholder-content {
  display: table-cell;
  padding: 4px 6px;
  border: 1px solid transparent;
  border-radius: 0;
  background: none;
  box-sizing: border-box;
  cursor: pointer;
}

.jp-Placeholder-contentContainer {
  display: flex;
}

.jp-Placeholder-content:hover,
.jp-InputPlaceholder > .jp-Placeholder-content:hover {
  border-color: var(--jp-layout-color3);
}

.jp-Placeholder-content .jp-MoreHorizIcon {
  width: 32px;
  height: 16px;
  border: 1px solid transparent;
  border-radius: var(--jp-border-radius);
}

.jp-Placeholder-content .jp-MoreHorizIcon:hover {
  border: 1px solid var(--jp-border-color1);
  box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.25);
  background-color: var(--jp-layout-color0);
}

.jp-PlaceholderText {
  white-space: nowrap;
  overflow-x: hidden;
  color: var(--jp-inverse-layout-color3);
  font-family: var(--jp-code-font-family);
}

.jp-InputPlaceholder > .jp-Placeholder-content {
  border-color: var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Private CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-private-cell-scrolling-output-offset: 5px;
}

/*-----------------------------------------------------------------------------
| Cell
|----------------------------------------------------------------------------*/

.jp-Cell {
  padding: var(--jp-cell-padding);
  margin: 0;
  border: none;
  outline: none;
  background: transparent;
}

/*-----------------------------------------------------------------------------
| Common input/output
|----------------------------------------------------------------------------*/

.jp-Cell-inputWrapper,
.jp-Cell-outputWrapper {
  display: flex;
  flex-direction: row;
  padding: 0;
  margin: 0;

  /* Added to reveal the box-shadow on the input and output collapsers. */
  overflow: visible;
}

/* Only input/output areas inside cells */
.jp-Cell-inputArea,
.jp-Cell-outputArea {
  flex: 1 1 auto;
}

/*-----------------------------------------------------------------------------
| Collapser
|----------------------------------------------------------------------------*/

/* Make the output collapser disappear when there is not output, but do so
 * in a manner that leaves it in the layout and preserves its width.
 */
.jp-Cell.jp-mod-noOutputs .jp-Cell-outputCollapser {
  border: none !important;
  background: transparent !important;
}

.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputCollapser {
  min-height: var(--jp-cell-collapser-min-height);
}

/*-----------------------------------------------------------------------------
| Output
|----------------------------------------------------------------------------*/

/* Put a space between input and output when there IS output */
.jp-Cell:not(.jp-mod-noOutputs) .jp-Cell-outputWrapper {
  margin-top: 5px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea {
  overflow-y: auto;
  max-height: 24em;
  margin-left: var(--jp-private-cell-scrolling-output-offset);
  resize: vertical;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea[style*='height'] {
  max-height: unset;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-Cell-outputArea::after {
  content: ' ';
  box-shadow: inset 0 0 6px 2px rgb(0 0 0 / 30%);
  width: 100%;
  height: 100%;
  position: sticky;
  bottom: 0;
  top: 0;
  margin-top: -50%;
  float: left;
  display: block;
  pointer-events: none;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-child {
  padding-top: 6px;
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-prompt {
  width: calc(
    var(--jp-cell-prompt-width) - var(--jp-private-cell-scrolling-output-offset)
  );
}

.jp-CodeCell.jp-mod-outputsScrolled .jp-OutputArea-promptOverlay {
  left: calc(-1 * var(--jp-private-cell-scrolling-output-offset));
}

/*-----------------------------------------------------------------------------
| CodeCell
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| MarkdownCell
|----------------------------------------------------------------------------*/

.jp-MarkdownOutput {
  display: table-cell;
  width: 100%;
  margin-top: 0;
  margin-bottom: 0;
  padding-left: var(--jp-code-padding);
}

.jp-MarkdownOutput.jp-RenderedHTMLCommon {
  overflow: auto;
}

/* collapseHeadingButton (show always if hiddenCellsButton is _not_ shown) */
.jp-collapseHeadingButton {
  display: flex;
  min-height: var(--jp-cell-collapser-min-height);
  font-size: var(--jp-code-font-size);
  position: absolute;
  background-color: transparent;
  background-size: 25px;
  background-repeat: no-repeat;
  background-position-x: center;
  background-position-y: top;
  background-image: var(--jp-icon-caret-down);
  right: 0;
  top: 0;
  bottom: 0;
}

.jp-collapseHeadingButton.jp-mod-collapsed {
  background-image: var(--jp-icon-caret-right);
}

/*
 set the container font size to match that of content
 so that the nested collapse buttons have the right size
*/
.jp-MarkdownCell .jp-InputPrompt {
  font-size: var(--jp-content-font-size1);
}

/*
  Align collapseHeadingButton with cell top header
  The font sizes are identical to the ones in packages/rendermime/style/base.css
*/
.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='1'] {
  font-size: var(--jp-content-font-size5);
  background-position-y: calc(0.3 * var(--jp-content-font-size5));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='2'] {
  font-size: var(--jp-content-font-size4);
  background-position-y: calc(0.3 * var(--jp-content-font-size4));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='3'] {
  font-size: var(--jp-content-font-size3);
  background-position-y: calc(0.3 * var(--jp-content-font-size3));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='4'] {
  font-size: var(--jp-content-font-size2);
  background-position-y: calc(0.3 * var(--jp-content-font-size2));
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='5'] {
  font-size: var(--jp-content-font-size1);
  background-position-y: top;
}

.jp-mod-rendered .jp-collapseHeadingButton[data-heading-level='6'] {
  font-size: var(--jp-content-font-size0);
  background-position-y: top;
}

/* collapseHeadingButton (show only on (hover,active) if hiddenCellsButton is shown) */
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-collapseHeadingButton {
  display: none;
}

.jp-Notebook.jp-mod-showHiddenCellsButton
  :is(.jp-MarkdownCell:hover, .jp-mod-active)
  .jp-collapseHeadingButton {
  display: flex;
}

/* showHiddenCellsButton (only show if jp-mod-showHiddenCellsButton is set, which
is a consequence of the showHiddenCellsButton option in Notebook Settings)*/
.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton {
  margin-left: calc(var(--jp-cell-prompt-width) + 2 * var(--jp-code-padding));
  margin-top: var(--jp-code-padding);
  border: 1px solid var(--jp-border-color2);
  background-color: var(--jp-border-color3) !important;
  color: var(--jp-content-font-color0) !important;
  display: flex;
}

.jp-Notebook.jp-mod-showHiddenCellsButton .jp-showHiddenCellsButton:hover {
  background-color: var(--jp-border-color2) !important;
}

.jp-showHiddenCellsButton {
  display: none;
}

/*-----------------------------------------------------------------------------
| Printing
|----------------------------------------------------------------------------*/

/*
Using block instead of flex to allow the use of the break-inside CSS property for
cell outputs.
*/

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

:root {
  --jp-notebook-toolbar-padding: 2px 5px 2px 2px;
}

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-NotebookPanel-toolbar {
  padding: var(--jp-notebook-toolbar-padding);

  /* disable paint containment from lumino 2.0 default strict CSS containment */
  contain: style size !important;
}

.jp-Toolbar-item.jp-Notebook-toolbarCellType .jp-select-wrapper.jp-mod-focused {
  border: none;
  box-shadow: none;
}

.jp-Notebook-toolbarCellTypeDropdown select {
  height: 24px;
  font-size: var(--jp-ui-font-size1);
  line-height: 14px;
  border-radius: 0;
  display: block;
}

.jp-Notebook-toolbarCellTypeDropdown span {
  top: 5px !important;
}

.jp-Toolbar-responsive-popup {
  position: absolute;
  height: fit-content;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: flex-end;
  border-bottom: var(--jp-border-width) solid var(--jp-toolbar-border-color);
  box-shadow: var(--jp-toolbar-box-shadow);
  background: var(--jp-toolbar-background);
  min-height: var(--jp-toolbar-micro-height);
  padding: var(--jp-notebook-toolbar-padding);
  z-index: 1;
  right: 0;
  top: 0;
}

.jp-Toolbar > .jp-Toolbar-responsive-opener {
  margin-left: auto;
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Variables
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------

/*-----------------------------------------------------------------------------
| Styles
|----------------------------------------------------------------------------*/

.jp-Notebook-ExecutionIndicator {
  position: relative;
  display: inline-block;
  height: 100%;
  z-index: 9997;
}

.jp-Notebook-ExecutionIndicator-tooltip {
  visibility: hidden;
  height: auto;
  width: max-content;
  width: -moz-max-content;
  background-color: var(--jp-layout-color2);
  color: var(--jp-ui-font-color1);
  text-align: justify;
  border-radius: 6px;
  padding: 0 5px;
  position: fixed;
  display: table;
}

.jp-Notebook-ExecutionIndicator-tooltip.up {
  transform: translateX(-50%) translateY(-100%) translateY(-32px);
}

.jp-Notebook-ExecutionIndicator-tooltip.down {
  transform: translateX(calc(-100% + 16px)) translateY(5px);
}

.jp-Notebook-ExecutionIndicator-tooltip.hidden {
  display: none;
}

.jp-Notebook-ExecutionIndicator:hover .jp-Notebook-ExecutionIndicator-tooltip {
  visibility: visible;
}

.jp-Notebook-ExecutionIndicator span {
  font-size: var(--jp-ui-font-size1);
  font-family: var(--jp-ui-font-family);
  color: var(--jp-ui-font-color1);
  line-height: 24px;
  display: block;
}

.jp-Notebook-ExecutionIndicator-progress-bar {
  display: flex;
  justify-content: center;
  height: 100%;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

/*
 * Execution indicator
 */
.jp-tocItem-content::after {
  content: '';

  /* Must be identical to form a circle */
  width: 12px;
  height: 12px;
  background: none;
  border: none;
  position: absolute;
  right: 0;
}

.jp-tocItem-content[data-running='0']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background: none;
}

.jp-tocItem-content[data-running='1']::after {
  border-radius: 50%;
  border: var(--jp-border-width) solid var(--jp-inverse-layout-color3);
  background-color: var(--jp-inverse-layout-color3);
}

.jp-tocItem-content[data-running='0'],
.jp-tocItem-content[data-running='1'] {
  margin-right: 12px;
}

/*
 * Copyright (c) Jupyter Development Team.
 * Distributed under the terms of the Modified BSD License.
 */

.jp-Notebook-footer {
  height: 27px;
  margin-left: calc(
    var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
      var(--jp-cell-padding)
  );
  width: calc(
    100% -
      (
        var(--jp-cell-prompt-width) + var(--jp-cell-collapser-width) +
          var(--jp-cell-padding) + var(--jp-cell-padding)
      )
  );
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  color: var(--jp-ui-font-color3);
  margin-top: 6px;
  background: none;
  cursor: pointer;
}

.jp-Notebook-footer:focus {
  border-color: var(--jp-cell-editor-active-border-color);
}

/* For devices that support hovering, hide footer until hover */
@media (hover: hover) {
  .jp-Notebook-footer {
    opacity: 0;
  }

  .jp-Notebook-footer:focus,
  .jp-Notebook-footer:hover {
    opacity: 1;
  }
}

/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| Imports
|----------------------------------------------------------------------------*/

/*-----------------------------------------------------------------------------
| CSS variables
|----------------------------------------------------------------------------*/

:root {
  --jp-side-by-side-output-size: 1fr;
  --jp-side-by-side-resized-cell: var(--jp-side-by-side-output-size);
  --jp-private-notebook-dragImage-width: 304px;
  --jp-private-notebook-dragImage-height: 36px;
  --jp-private-notebook-selected-color: var(--md-blue-400);
  --jp-private-notebook-active-color: var(--md-green-400);
}

/*-----------------------------------------------------------------------------
| Notebook
|----------------------------------------------------------------------------*/

/* stylelint-disable selector-max-class */

.jp-NotebookPanel {
  display: block;
  height: 100%;
}

.jp-NotebookPanel.jp-Document {
  min-width: 240px;
  min-height: 120px;
}

.jp-Notebook {
  padding: var(--jp-notebook-padding);
  outline: none;
  overflow: auto;
  background: var(--jp-layout-color0);
}

.jp-Notebook.jp-mod-scrollPastEnd::after {
  display: block;
  content: '';
  min-height: var(--jp-notebook-scroll-padding);
}

.jp-MainAreaWidget-ContainStrict .jp-Notebook * {
  contain: strict;
}

.jp-Notebook .jp-Cell {
  overflow: visible;
}

.jp-Notebook .jp-Cell .jp-InputPrompt {
  cursor: move;
}

/*-----------------------------------------------------------------------------
| Notebook state related styling
|
| The notebook and cells each have states, here are the possibilities:
|
| - Notebook
|   - Command
|   - Edit
| - Cell
|   - None
|   - Active (only one can be active)
|   - Selected (the cells actions are applied to)
|   - Multiselected (when multiple selected, the cursor)
|   - No outputs
|----------------------------------------------------------------------------*/

/* Command or edit modes */

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-InputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

.jp-Notebook .jp-Cell:not(.jp-mod-active) .jp-OutputPrompt {
  opacity: var(--jp-cell-prompt-not-active-opacity);
  color: var(--jp-cell-prompt-not-active-font-color);
}

/* cell is active */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser {
  background: var(--jp-brand-color1);
}

/* cell is dirty */
.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt {
  color: var(--jp-warn-color1);
}

.jp-Notebook .jp-Cell.jp-mod-dirty .jp-InputPrompt::before {
  color: var(--jp-warn-color1);
  content: '•';
}

.jp-Notebook .jp-Cell.jp-mod-active.jp-mod-dirty .jp-Collapser {
  background: var(--jp-warn-color1);
}

/* collapser is hovered */
.jp-Notebook .jp-Cell .jp-Collapser:hover {
  box-shadow: var(--jp-elevation-z2);
  background: var(--jp-brand-color1);
  opacity: var(--jp-cell-collapser-not-active-hover-opacity);
}

/* cell is active and collapser is hovered */
.jp-Notebook .jp-Cell.jp-mod-active .jp-Collapser:hover {
  background: var(--jp-brand-color0);
  opacity: 1;
}

/* Command mode */

.jp-Notebook.jp-mod-commandMode .jp-Cell.jp-mod-selected {
  background: var(--jp-notebook-multiselected-color);
}

.jp-Notebook.jp-mod-commandMode
  .jp-Cell.jp-mod-active.jp-mod-selected:not(.jp-mod-multiSelected) {
  background: transparent;
}

/* Edit mode */

.jp-Notebook.jp-mod-editMode .jp-Cell.jp-mod-active .jp-InputArea-editor {
  border: var(--jp-border-width) solid var(--jp-cell-editor-active-border-color);
  box-shadow: var(--jp-input-box-shadow);
  background-color: var(--jp-cell-editor-active-background);
}

/*-----------------------------------------------------------------------------
| Notebook drag and drop
|----------------------------------------------------------------------------*/

.jp-Notebook-cell.jp-mod-dropSource {
  opacity: 0.5;
}

.jp-Notebook-cell.jp-mod-dropTarget,
.jp-Notebook.jp-mod-commandMode
  .jp-Notebook-cell.jp-mod-active.jp-mod-selected.jp-mod-dropTarget {
  border-top-color: var(--jp-private-notebook-selected-color);
  border-top-style: solid;
  border-top-width: 2px;
}

.jp-dragImage {
  display: block;
  flex-direction: row;
  width: var(--jp-private-notebook-dragImage-width);
  height: var(--jp-private-notebook-dragImage-height);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background);
  overflow: visible;
}

.jp-dragImage-singlePrompt {
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

.jp-dragImage .jp-dragImage-content {
  flex: 1 1 auto;
  z-index: 2;
  font-size: var(--jp-code-font-size);
  font-family: var(--jp-code-font-family);
  line-height: var(--jp-code-line-height);
  padding: var(--jp-code-padding);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  background: var(--jp-cell-editor-background-color);
  color: var(--jp-content-font-color3);
  text-align: left;
  margin: 4px 4px 4px 0;
}

.jp-dragImage .jp-dragImage-prompt {
  flex: 0 0 auto;
  min-width: 36px;
  color: var(--jp-cell-inprompt-font-color);
  padding: var(--jp-code-padding);
  padding-left: 12px;
  font-family: var(--jp-cell-prompt-font-family);
  letter-spacing: var(--jp-cell-prompt-letter-spacing);
  line-height: 1.9;
  font-size: var(--jp-code-font-size);
  border: var(--jp-border-width) solid transparent;
}

.jp-dragImage-multipleBack {
  z-index: -1;
  position: absolute;
  height: 32px;
  width: 300px;
  top: 8px;
  left: 8px;
  background: var(--jp-layout-color2);
  border: var(--jp-border-width) solid var(--jp-input-border-color);
  box-shadow: 2px 2px 4px 0 rgba(0, 0, 0, 0.12);
}

/*-----------------------------------------------------------------------------
| Cell toolbar
|----------------------------------------------------------------------------*/

.jp-NotebookTools {
  display: block;
  min-width: var(--jp-sidebar-min-width);
  color: var(--jp-ui-font-color1);
  background: var(--jp-layout-color1);

  /* This is needed so that all font sizing of children done in ems is
    * relative to this base size */
  font-size: var(--jp-ui-font-size1);
  overflow: auto;
}

.jp-ActiveCellTool {
  padding: 12px 0;
  display: flex;
}

.jp-ActiveCellTool-Content {
  flex: 1 1 auto;
}

.jp-ActiveCellTool .jp-ActiveCellTool-CellContent {
  background: var(--jp-cell-editor-background);
  border: var(--jp-border-width) solid var(--jp-cell-editor-border-color);
  border-radius: 0;
  min-height: 29px;
}

.jp-ActiveCellTool .jp-InputPrompt {
  min-width: calc(var(--jp-cell-prompt-width) * 0.75);
}

.jp-ActiveCellTool-CellContent > pre {
  padding: 5px 4px;
  margin: 0;
  white-space: normal;
}

.jp-MetadataEditorTool {
  flex-direction: column;
  padding: 12px 0;
}

.jp-RankedPanel > :not(:first-child) {
  margin-top: 12px;
}

.jp-KeySelector select.jp-mod-styled {
  font-size: var(--jp-ui-font-size1);
  color: var(--jp-ui-font-color0);
  border: var(--jp-border-width) solid var(--jp-border-color1);
}

.jp-KeySelector label,
.jp-MetadataEditorTool label,
.jp-NumberSetter label {
  line-height: 1.4;
}

.jp-NotebookTools .jp-select-wrapper {
  margin-top: 4px;
  margin-bottom: 0;
}

.jp-NumberSetter input {
  width: 100%;
  margin-top: 4px;
}

.jp-NotebookTools .jp-Collapse {
  margin-top: 16px;
}

/*-----------------------------------------------------------------------------
| Presentation Mode (.jp-mod-presentationMode)
|----------------------------------------------------------------------------*/

.jp-mod-presentationMode .jp-Notebook {
  --jp-content-font-size1: var(--jp-content-presentation-font-size1);
  --jp-code-font-size: var(--jp-code-presentation-font-size);
}

.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-InputPrompt,
.jp-mod-presentationMode .jp-Notebook .jp-Cell .jp-OutputPrompt {
  flex: 0 0 110px;
}

/*-----------------------------------------------------------------------------
| Side-by-side Mode (.jp-mod-sideBySide)
|----------------------------------------------------------------------------*/
.jp-mod-sideBySide.jp-Notebook .jp-Notebook-cell {
  margin-top: 3em;
  margin-bottom: 3em;
  margin-left: 5%;
  margin-right: 5%;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell {
  display: grid;
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-output-size)
    );
  grid-template-rows: auto minmax(0, 1fr) auto;
  grid-template-areas:
    'header header header'
    'input handle output'
    'footer footer footer';
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell.jp-mod-resizedCell {
  grid-template-columns: minmax(0, 1fr) min-content minmax(
      0,
      var(--jp-side-by-side-resized-cell)
    );
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellHeader {
  grid-area: header;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-inputWrapper {
  grid-area: input;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-Cell-outputWrapper {
  /* overwrite the default margin (no vertical separation needed in side by side move */
  margin-top: 0;
  grid-area: output;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellFooter {
  grid-area: footer;
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle {
  grid-area: handle;
  user-select: none;
  display: block;
  height: 100%;
  cursor: ew-resize;
  padding: 0 var(--jp-cell-padding);
}

.jp-mod-sideBySide.jp-Notebook .jp-CodeCell .jp-CellResizeHandle::after {
  content: '';
  display: block;
  background: var(--jp-border-color2);
  height: 100%;
  width: 5px;
}

.jp-mod-sideBySide.jp-Notebook
  .jp-CodeCell.jp-mod-resizedCell
  .jp-CellResizeHandle::after {
  background: var(--jp-border-color0);
}

.jp-CellResizeHandle {
  display: none;
}

/*-----------------------------------------------------------------------------
| Placeholder
|----------------------------------------------------------------------------*/

.jp-Cell-Placeholder {
  padding-left: 55px;
}

.jp-Cell-Placeholder-wrapper {
  background: #fff;
  border: 1px solid;
  border-color: #e5e6e9 #dfe0e4 #d0d1d5;
  border-radius: 4px;
  -webkit-border-radius: 4px;
  margin: 10px 15px;
}

.jp-Cell-Placeholder-wrapper-inner {
  padding: 15px;
  position: relative;
}

.jp-Cell-Placeholder-wrapper-body {
  background-repeat: repeat;
  background-size: 50% auto;
}

.jp-Cell-Placeholder-wrapper-body div {
  background: #f6f7f8;
  background-image: -webkit-linear-gradient(
    left,
    #f6f7f8 0%,
    #edeef1 20%,
    #f6f7f8 40%,
    #f6f7f8 100%
  );
  background-repeat: no-repeat;
  background-size: 800px 104px;
  height: 104px;
  position: absolute;
  right: 15px;
  left: 15px;
  top: 15px;
}

div.jp-Cell-Placeholder-h1 {
  top: 20px;
  height: 20px;
  left: 15px;
  width: 150px;
}

div.jp-Cell-Placeholder-h2 {
  left: 15px;
  top: 50px;
  height: 10px;
  width: 100px;
}

div.jp-Cell-Placeholder-content-1,
div.jp-Cell-Placeholder-content-2,
div.jp-Cell-Placeholder-content-3 {
  left: 15px;
  right: 15px;
  height: 10px;
}

div.jp-Cell-Placeholder-content-1 {
  top: 100px;
}

div.jp-Cell-Placeholder-content-2 {
  top: 120px;
}

div.jp-Cell-Placeholder-content-3 {
  top: 140px;
}

</style>
<style type="text/css">
/*-----------------------------------------------------------------------------
| Copyright (c) Jupyter Development Team.
| Distributed under the terms of the Modified BSD License.
|----------------------------------------------------------------------------*/

/*
The following CSS variables define the main, public API for styling JupyterLab.
These variables should be used by all plugins wherever possible. In other
words, plugins should not define custom colors, sizes, etc unless absolutely
necessary. This enables users to change the visual theme of JupyterLab
by changing these variables.

Many variables appear in an ordered sequence (0,1,2,3). These sequences
are designed to work well together, so for example, `--jp-border-color1` should
be used with `--jp-layout-color1`. The numbers have the following meanings:

* 0: super-primary, reserved for special emphasis
* 1: primary, most important under normal situations
* 2: secondary, next most important under normal situations
* 3: tertiary, next most important under normal situations

Throughout JupyterLab, we are mostly following principles from Google's
Material Design when selecting colors. We are not, however, following
all of MD as it is not optimized for dense, information rich UIs.
*/

:root {
  /* Elevation
   *
   * We style box-shadows using Material Design's idea of elevation. These particular numbers are taken from here:
   *
   * https://github.com/material-components/material-components-web
   * https://material-components-web.appspot.com/elevation.html
   */

  --jp-shadow-base-lightness: 0;
  --jp-shadow-umbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.2
  );
  --jp-shadow-penumbra-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.14
  );
  --jp-shadow-ambient-color: rgba(
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    var(--jp-shadow-base-lightness),
    0.12
  );
  --jp-elevation-z0: none;
  --jp-elevation-z1: 0 2px 1px -1px var(--jp-shadow-umbra-color),
    0 1px 1px 0 var(--jp-shadow-penumbra-color),
    0 1px 3px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z2: 0 3px 1px -2px var(--jp-shadow-umbra-color),
    0 2px 2px 0 var(--jp-shadow-penumbra-color),
    0 1px 5px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z4: 0 2px 4px -1px var(--jp-shadow-umbra-color),
    0 4px 5px 0 var(--jp-shadow-penumbra-color),
    0 1px 10px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z6: 0 3px 5px -1px var(--jp-shadow-umbra-color),
    0 6px 10px 0 var(--jp-shadow-penumbra-color),
    0 1px 18px 0 var(--jp-shadow-ambient-color);
  --jp-elevation-z8: 0 5px 5px -3px var(--jp-shadow-umbra-color),
    0 8px 10px 1px var(--jp-shadow-penumbra-color),
    0 3px 14px 2px var(--jp-shadow-ambient-color);
  --jp-elevation-z12: 0 7px 8px -4px var(--jp-shadow-umbra-color),
    0 12px 17px 2px var(--jp-shadow-penumbra-color),
    0 5px 22px 4px var(--jp-shadow-ambient-color);
  --jp-elevation-z16: 0 8px 10px -5px var(--jp-shadow-umbra-color),
    0 16px 24px 2px var(--jp-shadow-penumbra-color),
    0 6px 30px 5px var(--jp-shadow-ambient-color);
  --jp-elevation-z20: 0 10px 13px -6px var(--jp-shadow-umbra-color),
    0 20px 31px 3px var(--jp-shadow-penumbra-color),
    0 8px 38px 7px var(--jp-shadow-ambient-color);
  --jp-elevation-z24: 0 11px 15px -7px var(--jp-shadow-umbra-color),
    0 24px 38px 3px var(--jp-shadow-penumbra-color),
    0 9px 46px 8px var(--jp-shadow-ambient-color);

  /* Borders
   *
   * The following variables, specify the visual styling of borders in JupyterLab.
   */

  --jp-border-width: 1px;
  --jp-border-color0: var(--md-grey-400);
  --jp-border-color1: var(--md-grey-400);
  --jp-border-color2: var(--md-grey-300);
  --jp-border-color3: var(--md-grey-200);
  --jp-inverse-border-color: var(--md-grey-600);
  --jp-border-radius: 2px;

  /* UI Fonts
   *
   * The UI font CSS variables are used for the typography all of the JupyterLab
   * user interface elements that are not directly user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-ui-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-ui-font-scale-factor: 1.2;
  --jp-ui-font-size0: 0.83333em;
  --jp-ui-font-size1: 13px; /* Base font size */
  --jp-ui-font-size2: 1.2em;
  --jp-ui-font-size3: 1.44em;
  --jp-ui-font-family: system-ui, -apple-system, blinkmacsystemfont, 'Segoe UI',
    helvetica, arial, sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji',
    'Segoe UI Symbol';

  /*
   * Use these font colors against the corresponding main layout colors.
   * In a light theme, these go from dark to light.
   */

  /* Defaults use Material Design specification */
  --jp-ui-font-color0: rgba(0, 0, 0, 1);
  --jp-ui-font-color1: rgba(0, 0, 0, 0.87);
  --jp-ui-font-color2: rgba(0, 0, 0, 0.54);
  --jp-ui-font-color3: rgba(0, 0, 0, 0.38);

  /*
   * Use these against the brand/accent/warn/error colors.
   * These will typically go from light to darker, in both a dark and light theme.
   */

  --jp-ui-inverse-font-color0: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color1: rgba(255, 255, 255, 1);
  --jp-ui-inverse-font-color2: rgba(255, 255, 255, 0.7);
  --jp-ui-inverse-font-color3: rgba(255, 255, 255, 0.5);

  /* Content Fonts
   *
   * Content font variables are used for typography of user generated content.
   *
   * The font sizing here is done assuming that the body font size of --jp-content-font-size1
   * is applied to a parent element. When children elements, such as headings, are sized
   * in em all things will be computed relative to that body size.
   */

  --jp-content-line-height: 1.6;
  --jp-content-font-scale-factor: 1.2;
  --jp-content-font-size0: 0.83333em;
  --jp-content-font-size1: 14px; /* Base font size */
  --jp-content-font-size2: 1.2em;
  --jp-content-font-size3: 1.44em;
  --jp-content-font-size4: 1.728em;
  --jp-content-font-size5: 2.0736em;

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-content-presentation-font-size1: 17px;
  --jp-content-heading-line-height: 1;
  --jp-content-heading-margin-top: 1.2em;
  --jp-content-heading-margin-bottom: 0.8em;
  --jp-content-heading-font-weight: 500;

  /* Defaults use Material Design specification */
  --jp-content-font-color0: rgba(0, 0, 0, 1);
  --jp-content-font-color1: rgba(0, 0, 0, 0.87);
  --jp-content-font-color2: rgba(0, 0, 0, 0.54);
  --jp-content-font-color3: rgba(0, 0, 0, 0.38);
  --jp-content-link-color: var(--md-blue-900);
  --jp-content-font-family: system-ui, -apple-system, blinkmacsystemfont,
    'Segoe UI', helvetica, arial, sans-serif, 'Apple Color Emoji',
    'Segoe UI Emoji', 'Segoe UI Symbol';

  /*
   * Code Fonts
   *
   * Code font variables are used for typography of code and other monospaces content.
   */

  --jp-code-font-size: 13px;
  --jp-code-line-height: 1.3077; /* 17px for 13px base */
  --jp-code-padding: 5px; /* 5px for 13px base, codemirror highlighting needs integer px value */
  --jp-code-font-family-default: menlo, consolas, 'DejaVu Sans Mono', monospace;
  --jp-code-font-family: var(--jp-code-font-family-default);

  /* This gives a magnification of about 125% in presentation mode over normal. */
  --jp-code-presentation-font-size: 16px;

  /* may need to tweak cursor width if you change font size */
  --jp-code-cursor-width0: 1.4px;
  --jp-code-cursor-width1: 2px;
  --jp-code-cursor-width2: 4px;

  /* Layout
   *
   * The following are the main layout colors use in JupyterLab. In a light
   * theme these would go from light to dark.
   */

  --jp-layout-color0: white;
  --jp-layout-color1: white;
  --jp-layout-color2: var(--md-grey-200);
  --jp-layout-color3: var(--md-grey-400);
  --jp-layout-color4: var(--md-grey-600);

  /* Inverse Layout
   *
   * The following are the inverse layout colors use in JupyterLab. In a light
   * theme these would go from dark to light.
   */

  --jp-inverse-layout-color0: #111;
  --jp-inverse-layout-color1: var(--md-grey-900);
  --jp-inverse-layout-color2: var(--md-grey-800);
  --jp-inverse-layout-color3: var(--md-grey-700);
  --jp-inverse-layout-color4: var(--md-grey-600);

  /* Brand/accent */

  --jp-brand-color0: var(--md-blue-900);
  --jp-brand-color1: var(--md-blue-700);
  --jp-brand-color2: var(--md-blue-300);
  --jp-brand-color3: var(--md-blue-100);
  --jp-brand-color4: var(--md-blue-50);
  --jp-accent-color0: var(--md-green-900);
  --jp-accent-color1: var(--md-green-700);
  --jp-accent-color2: var(--md-green-300);
  --jp-accent-color3: var(--md-green-100);

  /* State colors (warn, error, success, info) */

  --jp-warn-color0: var(--md-orange-900);
  --jp-warn-color1: var(--md-orange-700);
  --jp-warn-color2: var(--md-orange-300);
  --jp-warn-color3: var(--md-orange-100);
  --jp-error-color0: var(--md-red-900);
  --jp-error-color1: var(--md-red-700);
  --jp-error-color2: var(--md-red-300);
  --jp-error-color3: var(--md-red-100);
  --jp-success-color0: var(--md-green-900);
  --jp-success-color1: var(--md-green-700);
  --jp-success-color2: var(--md-green-300);
  --jp-success-color3: var(--md-green-100);
  --jp-info-color0: var(--md-cyan-900);
  --jp-info-color1: var(--md-cyan-700);
  --jp-info-color2: var(--md-cyan-300);
  --jp-info-color3: var(--md-cyan-100);

  /* Cell specific styles */

  --jp-cell-padding: 5px;
  --jp-cell-collapser-width: 8px;
  --jp-cell-collapser-min-height: 20px;
  --jp-cell-collapser-not-active-hover-opacity: 0.6;
  --jp-cell-editor-background: var(--md-grey-100);
  --jp-cell-editor-border-color: var(--md-grey-300);
  --jp-cell-editor-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-cell-editor-active-background: var(--jp-layout-color0);
  --jp-cell-editor-active-border-color: var(--jp-brand-color1);
  --jp-cell-prompt-width: 64px;
  --jp-cell-prompt-font-family: var(--jp-code-font-family-default);
  --jp-cell-prompt-letter-spacing: 0;
  --jp-cell-prompt-opacity: 1;
  --jp-cell-prompt-not-active-opacity: 0.5;
  --jp-cell-prompt-not-active-font-color: var(--md-grey-700);

  /* A custom blend of MD grey and blue 600
   * See https://meyerweb.com/eric/tools/color-blend/#546E7A:1E88E5:5:hex */
  --jp-cell-inprompt-font-color: #307fc1;

  /* A custom blend of MD grey and orange 600
   * https://meyerweb.com/eric/tools/color-blend/#546E7A:F4511E:5:hex */
  --jp-cell-outprompt-font-color: #bf5b3d;

  /* Notebook specific styles */

  --jp-notebook-padding: 10px;
  --jp-notebook-select-background: var(--jp-layout-color1);
  --jp-notebook-multiselected-color: var(--md-blue-50);

  /* The scroll padding is calculated to fill enough space at the bottom of the
  notebook to show one single-line cell (with appropriate padding) at the top
  when the notebook is scrolled all the way to the bottom. We also subtract one
  pixel so that no scrollbar appears if we have just one single-line cell in the
  notebook. This padding is to enable a 'scroll past end' feature in a notebook.
  */
  --jp-notebook-scroll-padding: calc(
    100% - var(--jp-code-font-size) * var(--jp-code-line-height) -
      var(--jp-code-padding) - var(--jp-cell-padding) - 1px
  );

  /* Rendermime styles */

  --jp-rendermime-error-background: #fdd;
  --jp-rendermime-table-row-background: var(--md-grey-100);
  --jp-rendermime-table-row-hover-background: var(--md-light-blue-50);

  /* Dialog specific styles */

  --jp-dialog-background: rgba(0, 0, 0, 0.25);

  /* Console specific styles */

  --jp-console-padding: 10px;

  /* Toolbar specific styles */

  --jp-toolbar-border-color: var(--jp-border-color1);
  --jp-toolbar-micro-height: 8px;
  --jp-toolbar-background: var(--jp-layout-color1);
  --jp-toolbar-box-shadow: 0 0 2px 0 rgba(0, 0, 0, 0.24);
  --jp-toolbar-header-margin: 4px 4px 0 4px;
  --jp-toolbar-active-background: var(--md-grey-300);

  /* Statusbar specific styles */

  --jp-statusbar-height: 24px;

  /* Input field styles */

  --jp-input-box-shadow: inset 0 0 2px var(--md-blue-300);
  --jp-input-active-background: var(--jp-layout-color1);
  --jp-input-hover-background: var(--jp-layout-color1);
  --jp-input-background: var(--md-grey-100);
  --jp-input-border-color: var(--jp-inverse-border-color);
  --jp-input-active-border-color: var(--jp-brand-color1);
  --jp-input-active-box-shadow-color: rgba(19, 124, 189, 0.3);

  /* General editor styles */

  --jp-editor-selected-background: #d9d9d9;
  --jp-editor-selected-focused-background: #d7d4f0;
  --jp-editor-cursor-color: var(--jp-ui-font-color0);

  /* Code mirror specific styles */

  --jp-mirror-editor-keyword-color: #008000;
  --jp-mirror-editor-atom-color: #88f;
  --jp-mirror-editor-number-color: #080;
  --jp-mirror-editor-def-color: #00f;
  --jp-mirror-editor-variable-color: var(--md-grey-900);
  --jp-mirror-editor-variable-2-color: rgb(0, 54, 109);
  --jp-mirror-editor-variable-3-color: #085;
  --jp-mirror-editor-punctuation-color: #05a;
  --jp-mirror-editor-property-color: #05a;
  --jp-mirror-editor-operator-color: #a2f;
  --jp-mirror-editor-comment-color: #408080;
  --jp-mirror-editor-string-color: #ba2121;
  --jp-mirror-editor-string-2-color: #708;
  --jp-mirror-editor-meta-color: #a2f;
  --jp-mirror-editor-qualifier-color: #555;
  --jp-mirror-editor-builtin-color: #008000;
  --jp-mirror-editor-bracket-color: #997;
  --jp-mirror-editor-tag-color: #170;
  --jp-mirror-editor-attribute-color: #00c;
  --jp-mirror-editor-header-color: blue;
  --jp-mirror-editor-quote-color: #090;
  --jp-mirror-editor-link-color: #00c;
  --jp-mirror-editor-error-color: #f00;
  --jp-mirror-editor-hr-color: #999;

  /*
    RTC user specific colors.
    These colors are used for the cursor, username in the editor,
    and the icon of the user.
  */

  --jp-collaborator-color1: #ffad8e;
  --jp-collaborator-color2: #dac83d;
  --jp-collaborator-color3: #72dd76;
  --jp-collaborator-color4: #00e4d0;
  --jp-collaborator-color5: #45d4ff;
  --jp-collaborator-color6: #e2b1ff;
  --jp-collaborator-color7: #ff9de6;

  /* Vega extension styles */

  --jp-vega-background: white;

  /* Sidebar-related styles */

  --jp-sidebar-min-width: 250px;

  /* Search-related styles */

  --jp-search-toggle-off-opacity: 0.5;
  --jp-search-toggle-hover-opacity: 0.8;
  --jp-search-toggle-on-opacity: 1;
  --jp-search-selected-match-background-color: rgb(245, 200, 0);
  --jp-search-selected-match-color: black;
  --jp-search-unselected-match-background-color: var(
    --jp-inverse-layout-color0
  );
  --jp-search-unselected-match-color: var(--jp-ui-inverse-font-color0);

  /* Icon colors that work well with light or dark backgrounds */
  --jp-icon-contrast-color0: var(--md-purple-600);
  --jp-icon-contrast-color1: var(--md-green-600);
  --jp-icon-contrast-color2: var(--md-pink-600);
  --jp-icon-contrast-color3: var(--md-blue-600);

  /* Button colors */
  --jp-accept-color-normal: var(--md-blue-700);
  --jp-accept-color-hover: var(--md-blue-800);
  --jp-accept-color-active: var(--md-blue-900);
  --jp-warn-color-normal: var(--md-red-700);
  --jp-warn-color-hover: var(--md-red-800);
  --jp-warn-color-active: var(--md-red-900);
  --jp-reject-color-normal: var(--md-grey-600);
  --jp-reject-color-hover: var(--md-grey-700);
  --jp-reject-color-active: var(--md-grey-800);

  /* File or activity icons and switch semantic variables */
  --jp-jupyter-icon-color: #f37626;
  --jp-notebook-icon-color: #f37626;
  --jp-json-icon-color: var(--md-orange-700);
  --jp-console-icon-background-color: var(--md-blue-700);
  --jp-console-icon-color: white;
  --jp-terminal-icon-background-color: var(--md-grey-800);
  --jp-terminal-icon-color: var(--md-grey-200);
  --jp-text-editor-icon-color: var(--md-grey-700);
  --jp-inspector-icon-color: var(--md-grey-700);
  --jp-switch-color: var(--md-grey-400);
  --jp-switch-true-position-color: var(--md-orange-900);
}
</style>
<style type="text/css">
/* Force rendering true colors when outputing to pdf */
* {
  -webkit-print-color-adjust: exact;
}

/* Misc */
a.anchor-link {
  display: none;
}

/* Input area styling */
.jp-InputArea {
  overflow: hidden;
}

.jp-InputArea-editor {
  overflow: hidden;
}

.cm-editor.cm-s-jupyter .highlight pre {
/* weird, but --jp-code-padding defined to be 5px but 4px horizontal padding is hardcoded for pre.cm-line */
  padding: var(--jp-code-padding) 4px;
  margin: 0;

  font-family: inherit;
  font-size: inherit;
  line-height: inherit;
  color: inherit;

}

.jp-OutputArea-output pre {
  line-height: inherit;
  font-family: inherit;
}

.jp-RenderedText pre {
  color: var(--jp-content-font-color1);
  font-size: var(--jp-code-font-size);
}

/* Hiding the collapser by default */
.jp-Collapser {
  display: none;
}

@page {
    margin: 0.5in; /* Margin for each printed piece of paper */
}

@media print {
  .jp-Cell-inputWrapper,
  .jp-Cell-outputWrapper {
    display: block;
  }
}
</style>
<!-- Load mathjax -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.7/latest.js?config=TeX-AMS_CHTML-full,Safe"> </script>
<!-- MathJax configuration -->
<script type="text/x-mathjax-config">
    init_mathjax = function() {
        if (window.MathJax) {
        // MathJax loaded
            MathJax.Hub.Config({
                TeX: {
                    equationNumbers: {
                    autoNumber: "AMS",
                    useLabelIds: true
                    }
                },
                tex2jax: {
                    inlineMath: [ ['$','$'], ["\\(","\\)"] ],
                    displayMath: [ ['$$','$$'], ["\\[","\\]"] ],
                    processEscapes: true,
                    processEnvironments: true
                },
                displayAlign: 'center',
                CommonHTML: {
                    linebreaks: {
                    automatic: true
                    }
                }
            });

            MathJax.Hub.Queue(["Typeset", MathJax.Hub]);
        }
    }
    init_mathjax();
    </script>
<!-- End of mathjax configuration --><script type="module">
  document.addEventListener("DOMContentLoaded", async () => {
    const diagrams = document.querySelectorAll(".jp-Mermaid > pre.mermaid");
    // do not load mermaidjs if not needed
    if (!diagrams.length) {
      return;
    }
    const mermaid = (await import("https://cdnjs.cloudflare.com/ajax/libs/mermaid/10.7.0/mermaid.esm.min.mjs")).default;
    const parser = new DOMParser();

    mermaid.initialize({
      maxTextSize: 100000,
      maxEdges: 100000,
      startOnLoad: false,
      fontFamily: window
        .getComputedStyle(document.body)
        .getPropertyValue("--jp-ui-font-family"),
      theme: document.querySelector("body[data-jp-theme-light='true']")
        ? "default"
        : "dark",
    });

    let _nextMermaidId = 0;

    function makeMermaidImage(svg) {
      const img = document.createElement("img");
      const doc = parser.parseFromString(svg, "image/svg+xml");
      const svgEl = doc.querySelector("svg");
      const { maxWidth } = svgEl?.style || {};
      const firstTitle = doc.querySelector("title");
      const firstDesc = doc.querySelector("desc");

      img.setAttribute("src", `data:image/svg+xml,${encodeURIComponent(svg)}`);
      if (maxWidth) {
        img.width = parseInt(maxWidth);
      }
      if (firstTitle) {
        img.setAttribute("alt", firstTitle.textContent);
      }
      if (firstDesc) {
        const caption = document.createElement("figcaption");
        caption.className = "sr-only";
        caption.textContent = firstDesc.textContent;
        return [img, caption];
      }
      return [img];
    }

    async function makeMermaidError(text) {
      let errorMessage = "";
      try {
        await mermaid.parse(text);
      } catch (err) {
        errorMessage = `${err}`;
      }

      const result = document.createElement("details");
      result.className = 'jp-RenderedMermaid-Details';
      const summary = document.createElement("summary");
      summary.className = 'jp-RenderedMermaid-Summary';
      const pre = document.createElement("pre");
      const code = document.createElement("code");
      code.innerText = text;
      pre.appendChild(code);
      summary.appendChild(pre);
      result.appendChild(summary);

      const warning = document.createElement("pre");
      warning.innerText = errorMessage;
      result.appendChild(warning);
      return [result];
    }

    async function renderOneMarmaid(src) {
      const id = `jp-mermaid-${_nextMermaidId++}`;
      const parent = src.parentNode;
      let raw = src.textContent.trim();
      const el = document.createElement("div");
      el.style.visibility = "hidden";
      document.body.appendChild(el);
      let results = null;
      let output = null;
      try {
        let { svg } = await mermaid.render(id, raw, el);
        svg = cleanMermaidSvg(svg);
        results = makeMermaidImage(svg);
        output = document.createElement("figure");
        results.map(output.appendChild, output);
      } catch (err) {
        parent.classList.add("jp-mod-warning");
        results = await makeMermaidError(raw);
        output = results[0];
      } finally {
        el.remove();
      }
      parent.classList.add("jp-RenderedMermaid");
      parent.appendChild(output);
    }


    /**
     * Post-process to ensure mermaid diagrams contain only valid SVG and XHTML.
     */
    function cleanMermaidSvg(svg) {
      return svg.replace(RE_VOID_ELEMENT, replaceVoidElement);
    }


    /**
     * A regular expression for all void elements, which may include attributes and
     * a slash.
     *
     * @see https://developer.mozilla.org/en-US/docs/Glossary/Void_element
     *
     * Of these, only `<br>` is generated by Mermaid in place of `\n`,
     * but _any_ "malformed" tag will break the SVG rendering entirely.
     */
    const RE_VOID_ELEMENT =
      /<\s*(area|base|br|col|embed|hr|img|input|link|meta|param|source|track|wbr)\s*([^>]*?)\s*>/gi;

    /**
     * Ensure a void element is closed with a slash, preserving any attributes.
     */
    function replaceVoidElement(match, tag, rest) {
      rest = rest.trim();
      if (!rest.endsWith('/')) {
        rest = `${rest} /`;
      }
      return `<${tag} ${rest}>`;
    }

    void Promise.all([...diagrams].map(renderOneMarmaid));
  });
</script>
<style>
  .jp-Mermaid:not(.jp-RenderedMermaid) {
    display: none;
  }

  .jp-RenderedMermaid {
    overflow: auto;
    display: flex;
  }

  .jp-RenderedMermaid.jp-mod-warning {
    width: auto;
    padding: 0.5em;
    margin-top: 0.5em;
    border: var(--jp-border-width) solid var(--jp-warn-color2);
    border-radius: var(--jp-border-radius);
    color: var(--jp-ui-font-color1);
    font-size: var(--jp-ui-font-size1);
    white-space: pre-wrap;
    word-wrap: break-word;
  }

  .jp-RenderedMermaid figure {
    margin: 0;
    overflow: auto;
    max-width: 100%;
  }

  .jp-RenderedMermaid img {
    max-width: 100%;
  }

  .jp-RenderedMermaid-Details > pre {
    margin-top: 1em;
  }

  .jp-RenderedMermaid-Summary {
    color: var(--jp-warn-color2);
  }

  .jp-RenderedMermaid:not(.jp-mod-warning) pre {
    display: none;
  }

  .jp-RenderedMermaid-Summary > pre {
    display: inline-block;
    white-space: normal;
  }
</style>
<!-- End of mermaid configuration --></head>
<body class="jp-Notebook" data-jp-theme-light="true" data-jp-theme-name="JupyterLab Light">
<main>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="1.-Consolidated-files-in-the-unique-DataFrame-and-show-the-total-files-extracted">1. Consolidated files in the unique DataFrame and show the total files extracted<a class="anchor-link" href="#1.-Consolidated-files-in-the-unique-DataFrame-and-show-the-total-files-extracted">¶</a></h2>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [2]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">os</span>
<span class="kn">import</span> <span class="nn">sys</span>
<span class="kn">import</span> <span class="nn">pandas</span> <span class="k">as</span> <span class="nn">pd</span>
<span class="kn">from</span> <span class="nn">etl.common.utils.common</span> <span class="kn">import</span> <span class="n">DefaultOutputFolder</span> <span class="k">as</span> <span class="nb">dir</span>

<span class="n">notebook_path</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">abspath</span><span class="p">(</span><span class="s2">"data_explorer.ipynb"</span><span class="p">))</span>
<span class="n">sys</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">path</span><span class="o">.</span><span class="n">dirname</span><span class="p">(</span><span class="n">notebook_path</span><span class="p">))</span>

<span class="c1">## Files from Default Folder</span>
<span class="n">files</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">listdir</span><span class="p">(</span><span class="nb">dir</span><span class="p">())</span>
<span class="n">dfs</span> <span class="o">=</span> <span class="p">[]</span>


<span class="k">if</span> <span class="ow">not</span> <span class="n">files</span><span class="p">:</span> <span class="nb">print</span><span class="p">(</span><span class="s2">"No files found in the output folder."</span><span class="p">)</span>

<span class="k">for</span> <span class="n">file</span> <span class="ow">in</span> <span class="n">files</span><span class="p">:</span>
    <span class="k">if</span> <span class="n">file</span><span class="o">.</span><span class="n">endswith</span><span class="p">(</span><span class="s2">".parquet"</span><span class="p">):</span>
        <span class="n">df</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">read_parquet</span><span class="p">(</span><span class="nb">dir</span><span class="p">()</span> <span class="o">+</span> <span class="n">file</span><span class="p">)</span>
        <span class="n">dfs</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">df</span><span class="p">)</span>
    
<span class="n">allFiles</span> <span class="o">=</span> <span class="n">pd</span><span class="o">.</span><span class="n">concat</span><span class="p">(</span><span class="n">dfs</span><span class="p">,</span> <span class="n">ignore_index</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="c1"># Ordering DataFrame by column name</span>
<span class="n">allFiles</span> <span class="o">=</span> <span class="n">allFiles</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="p">[</span><span class="s1">'extracted_at'</span><span class="p">],</span> <span class="n">ascending</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

<span class="c1"># count the rows in the all dataframe</span>
<span class="n">allFiles</span><span class="o">.</span><span class="n">shape</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span>
</pre></div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="1.1-Data-set-sample,-list-5-files">1.1 Data set sample, list 5 files<a class="anchor-link" href="#1.1-Data-set-sample,-list-5-files">¶</a></h2>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [4]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="n">allFiles</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[4]:</div>
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<style scoped="">
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>code</th>
<th>codein</th>
<th>name</th>
<th>high</th>
<th>low</th>
<th>varBid</th>
<th>pctChange</th>
<th>bid</th>
<th>ask</th>
<th>timestamp</th>
<th>create_date</th>
<th>symbol</th>
<th>extracted_at</th>
</tr>
</thead>
<tbody>
<tr>
<th>89</th>
<td>EUR</td>
<td>TTD</td>
<td>Euro/Dólar de Trinidad</td>
<td>7.289</td>
<td>7.288</td>
<td>0.001</td>
<td>0.01</td>
<td>7.139</td>
<td>7.439</td>
<td>1714135022</td>
<td>2024-04-26 09:37:02</td>
<td>EUR-TTD</td>
<td>2024-04-26 12:37:16</td>
</tr>
<tr>
<th>114</th>
<td>EUR</td>
<td>TWD</td>
<td>Euro/Dólar Taiuanês</td>
<td>35.022</td>
<td>34.889</td>
<td>0.003</td>
<td>0.01</td>
<td>34.944</td>
<td>34.945</td>
<td>1714135022</td>
<td>2024-04-26 09:37:02</td>
<td>EUR-TWD</td>
<td>2024-04-26 12:37:16</td>
</tr>
<tr>
<th>67</th>
<td>USD</td>
<td>BIF</td>
<td>Dólar Americano/Franco Burundinense</td>
<td>2874</td>
<td>2865.3</td>
<td>-8.7</td>
<td>-0.3</td>
<td>2839.22</td>
<td>2891.39</td>
<td>1714134877</td>
<td>2024-04-26 09:34:37</td>
<td>USD-BIF</td>
<td>2024-04-26 12:35:02</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="2.-Change-DataTypes-and-Reorder-columns">2. Change DataTypes and Reorder columns<a class="anchor-link" href="#2.-Change-DataTypes-and-Reorder-columns">¶</a></h2>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [5]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="c1"># Change data types</span>
<span class="n">df</span> <span class="o">=</span> <span class="n">allFiles</span><span class="o">.</span><span class="n">astype</span><span class="p">({</span><span class="s1">'ask'</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="s1">'bid'</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="s1">'varBid'</span><span class="p">:</span> <span class="nb">float</span><span class="p">,</span> <span class="s1">'pctChange'</span><span class="p">:</span> <span class="nb">float</span><span class="p">})</span>

<span class="c1"># Show the dataframe</span>
<span class="n">df</span><span class="o">.</span><span class="n">head</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[5]:</div>
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<style scoped="">
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>code</th>
<th>codein</th>
<th>name</th>
<th>high</th>
<th>low</th>
<th>varBid</th>
<th>pctChange</th>
<th>bid</th>
<th>ask</th>
<th>timestamp</th>
<th>create_date</th>
<th>symbol</th>
<th>extracted_at</th>
</tr>
</thead>
<tbody>
<tr>
<th>89</th>
<td>EUR</td>
<td>TTD</td>
<td>Euro/Dólar de Trinidad</td>
<td>7.289</td>
<td>7.288</td>
<td>0.001</td>
<td>0.01</td>
<td>7.139</td>
<td>7.439</td>
<td>1714135022</td>
<td>2024-04-26 09:37:02</td>
<td>EUR-TTD</td>
<td>2024-04-26 12:37:16</td>
</tr>
<tr>
<th>114</th>
<td>EUR</td>
<td>TWD</td>
<td>Euro/Dólar Taiuanês</td>
<td>35.022</td>
<td>34.889</td>
<td>0.003</td>
<td>0.01</td>
<td>34.944</td>
<td>34.945</td>
<td>1714135022</td>
<td>2024-04-26 09:37:02</td>
<td>EUR-TWD</td>
<td>2024-04-26 12:37:16</td>
</tr>
<tr>
<th>67</th>
<td>USD</td>
<td>BIF</td>
<td>Dólar Americano/Franco Burundinense</td>
<td>2874</td>
<td>2865.3</td>
<td>-8.700</td>
<td>-0.30</td>
<td>2839.220</td>
<td>2891.390</td>
<td>1714134877</td>
<td>2024-04-26 09:34:37</td>
<td>USD-BIF</td>
<td>2024-04-26 12:35:02</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="3.-Using-SQL-for-Data-Exploration">3. Using SQL for Data Exploration<a class="anchor-link" href="#3.-Using-SQL-for-Data-Exploration">¶</a></h2><pre><code>3.1 What is the currency with the highest ask value?</code></pre>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [6]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">pandasql</span> <span class="kn">import</span> <span class="n">sqldf</span>

<span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    SELECT symbol, name, max(ask) max_ask FROM df </span>
<span class="s2">    where code = 'BRL' </span>
<span class="s2">    group by symbol, name</span>
<span class="s2">    order by 3 desc limit 1</span>
<span class="s2">"""</span>

<span class="n">newDf</span> <span class="o">=</span> <span class="n">sqldf</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">locals</span><span class="p">())</span>

<span class="n">newDf</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[6]:</div>
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<style scoped="">
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>symbol</th>
<th>name</th>
<th>max_ask</th>
</tr>
</thead>
<tbody>
<tr>
<th>0</th>
<td>BRL-LBP</td>
<td>Real Brasileiro/Libra Libanesa</td>
<td>17206.94</td>
</tr>
</tbody>
</table>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<pre><code>3.1 Disponible Data</code></pre>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [7]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">from</span> <span class="nn">pandasql</span> <span class="kn">import</span> <span class="n">sqldf</span>

<span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    SELECT code, codein, name FROM df </span>
<span class="s2">    group by 1,2,3</span>
<span class="s2">"""</span>

<span class="n">newDf</span> <span class="o">=</span> <span class="n">sqldf</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">locals</span><span class="p">())</span>

<span class="n">newDf</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child jp-OutputArea-executeResult">
<div class="jp-OutputPrompt jp-OutputArea-prompt">Out[7]:</div>
<div class="jp-RenderedHTMLCommon jp-RenderedHTML jp-OutputArea-output jp-OutputArea-executeResult" data-mime-type="text/html" tabindex="0">
<div>
<style scoped="">
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
<thead>
<tr style="text-align: right;">
<th></th>
<th>code</th>
<th>codein</th>
<th>name</th>
</tr>
</thead>
<tbody>
<tr>
<th>0</th>
<td>AED</td>
<td>BRL</td>
<td>Dirham dos Emirados/Real Brasileiro</td>
</tr>
<tr>
<th>1</th>
<td>AED</td>
<td>EUR</td>
<td>Dirham dos Emirados/Euro</td>
</tr>
<tr>
<th>2</th>
<td>AFN</td>
<td>USD</td>
<td>Afghani do Afeganistão/Dólar Americano</td>
</tr>
<tr>
<th>3</th>
<td>ARS</td>
<td>EUR</td>
<td>Peso Argentino/Euro</td>
</tr>
<tr>
<th>4</th>
<td>AUD</td>
<td>EUR</td>
<td>Dólar Australiano/Euro</td>
</tr>
<tr>
<th>...</th>
<td>...</td>
<td>...</td>
<td>...</td>
</tr>
<tr>
<th>297</th>
<td>XAGG</td>
<td>USD</td>
<td>Prata/Dólar Americano</td>
</tr>
<tr>
<th>298</th>
<td>XBR</td>
<td>USD</td>
<td>Brent Spot/Dólar Americano</td>
</tr>
<tr>
<th>299</th>
<td>XRP</td>
<td>EUR</td>
<td>XRP/Euro</td>
</tr>
<tr>
<th>300</th>
<td>ZAR</td>
<td>EUR</td>
<td>Rand Sul-Africano/Euro</td>
</tr>
<tr>
<th>301</th>
<td>ZAR</td>
<td>USD</td>
<td>Rand Sul-Africano/Dólar Americano</td>
</tr>
</tbody>
</table>
<p>302 rows × 3 columns</p>
</div>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<h2 id="4.-Using-SQL-+-Matplotlib-for-Data-Viz">4. Using SQL + Matplotlib for Data Viz<a class="anchor-link" href="#4.-Using-SQL-+-Matplotlib-for-Data-Viz">¶</a></h2><pre><code>4.1 What is the TOP 10 Most Value Currency considering BRL?</code></pre>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [8]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    SELECT </span>
<span class="s2">        name</span>
<span class="s2">        ,round(avg(ask),2) AvgAsk</span>
<span class="s2">    FROM df </span>
<span class="s2">    where codein = 'BRL'</span>
<span class="s2">    and not code in ('BTC', 'ETH', 'LTC', 'DOGE')</span>
<span class="s2">    group by name</span>
<span class="s2">    order by avg(ask) desc limit 10</span>
<span class="s2">"""</span>

<span class="n">newDf</span> <span class="o">=</span> <span class="n">sqldf</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">locals</span><span class="p">())</span>
<span class="n">newDf</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">'AvgAsk'</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="n">AvgAskByCurrency</span> <span class="o">=</span> <span class="n">newDf</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span>
    <span class="n">kind</span><span class="o">=</span><span class="s1">'barh'</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s1">'name'</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">'AvgAsk'</span><span class="p">,</span> 
    <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> 
    <span class="n">legend</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> 
    <span class="n">color</span><span class="o">=</span><span class="s1">'blue'</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s1">'Top 10 Most Valuable Currencies by Ask Price'</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">'Ask Price'</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">'Symbol'</span><span class="p">)</span>


<span class="c1"># Adicionando rótulos aos dados</span>
<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">newDf</span><span class="p">[</span><span class="s1">'AvgAsk'</span><span class="p">]):</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">index</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">))</span>

<span class="c1"># Exibir o gráfico</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABbkAAANXCAYAAAAYXFJxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAACC80lEQVR4nOzdd5gW5dk34GvpS1l6D4IiXbBgRwUVxYZiVCxEQEFsiCViR8CKxoYaiLEAISgoimAD0YBRbCAWVGwIYkeRjrRlvj/8eF6XXWBBFCee53HMcbzPzD0z18wzS3x/e+81WUmSJAEAAAAAAClUZFsXAAAAAAAAW0rIDQAAAABAagm5AQAAAABILSE3AAAAAACpJeQGAAAAACC1hNwAAAAAAKSWkBsAAAAAgNQScgMAAAAAkFpCbgAAAAAAUkvIDQAA/G7169cvsrKyftVzDB06NLKysmLatGmbHNumTZto06bNr1rPH03Xrl2jXr16v+k569WrF0cdddRves5fas6cOZGVlRW33HLLNjn/5MmTIysrKyZPnrxNzg8AGyPkBgAgFbKysgq1/BYBzODBg+OEE06I7bbbLrKysqJr164bHLtw4cLo0aNHVK1aNcqUKRMHHnhgTJ8+vVDnadOmTWRlZUWDBg0K3D5x4sTMdY8ePXpLLmWTnn766ejXr98mx82bNy+KFSsWf/nLXzY4ZsmSJZGdnR1//vOft2KF/xsmT54cf/7zn6NGjRpRokSJqFatWrRv3z4ee+yxbV0aW8HMmTMjKysrSpUqFQsXLtwmNfz838kiRYpErVq14tBDDxVaA/A/odi2LgAAAApj+PDheT7/61//iokTJ+Zb36RJk1+9lptuuimWLFkSe+65Z3z99dcbHLd27do48sgj4+23347evXtHlSpVYtCgQdGmTZt44403Nhhe/1ypUqXik08+iddffz323HPPPNtGjBgRpUqVihUrVvzia9qQp59+Ov7+979vMuiuVq1aHHLIITF27NhYvnx5lC5dOt+Yxx57LFasWLHRIPyPqG/fvnHNNddEgwYN4swzz4y6devG/Pnz4+mnn47jjjsuRowYEaeccsq2LvNXc++998batWu3dRm/qn//+99Ro0aNWLBgQYwePTq6d+++Teo45JBDonPnzpEkScyePTsGDRoUBx10UDz11FNx+OGHb3TfAw44IH788ccoUaLEb1QtABSekBsAgFRYPxh99dVXY+LEidskMH3hhRcys7jLli27wXGjR4+Ol19+OR555JE4/vjjIyKiY8eO0bBhw+jbt288+OCDmzxX/fr1Y82aNfHQQw/lCblXrFgRY8aMiSOPPDIeffTRX35RW0GnTp1i/PjxMW7cuDjppJPybX/wwQejfPnyceSRR26D6n6fRo8eHddcc00cf/zx8eCDD0bx4sUz23r37h0TJkyI1atXb5VzbeiXD2vWrIm1a9dus/Dy59f8vyhJknjwwQfjlFNOidmzZ8eIESO2WcjdsGHDPP9mHnvssdGiRYu44447Nhhyr1ixIkqUKBFFihSJUqVK/ValAsBm0a4EAID/GcuWLYu//vWvUadOnShZsmQ0atQobrnllkiSJM+4rKys6NmzZ4wYMSIaNWoUpUqVipYtW8Z///vfQp2nbt26heoTPXr06KhevXqe9hxVq1aNjh07xtixY2PlypWFOt/JJ58co0aNyjPb9Yknnojly5dHx44dC9znzTffjMMPPzxycnKibNmycfDBB8err76aZ8zq1aujf//+0aBBgyhVqlRUrlw59ttvv5g4cWJE/NQr+e9//3tE5G11sCHHHntslClTpsDwft68efH888/H8ccfHyVLlowXX3wx0/KlZMmSUadOnbjwwgvjxx9/3Oi9WNeXeOjQofm2ZWVl5Zlx/tlnn8U555wTjRo1iuzs7KhcuXKccMIJMWfOnAKPvXz58jjzzDOjcuXKkZOTE507d44FCxZstJ6IiJUrV0bfvn1jxx13zFzLJZdcUqjvt0+fPlGpUqV44IEHCgx727Vrl+kdva53+Pr1F9QruU2bNrHTTjvFG2+8EQcccECULl06rrjiijx9ne+4446oX79+lCxZMt5///2IiPjggw/i+OOPj0qVKkWpUqVi9913j3HjxuU537o6pkyZEhdddFGmFc+xxx4b3333Xb5reOaZZ6J169ZRrly5yMnJiT322CPPM1JQT+61a9fGHXfcEc2aNYtSpUpF9erV48wzz8z3fUybNi3atWsXVapUiezs7Nh+++3j9NNP3+R9X+fZZ5+NXXbZJUqVKhVNmzbN0x7m008/jaysrLj99tvz7ffyyy9HVlZWPPTQQ5s8x5QpU2LOnDlx0kknxUknnRT//e9/44svvsg3bkuuJUmS6NGjR5QoUWKLWts0b948qlSpErNnz46I/3uWRo4cGVdddVXUrl07SpcuHYsXL95gT+7XXnstjjjiiKhYsWKUKVMmWrRoEQMHDswzpjDPFQD8EmZyAwDwPyFJkjj66KNj0qRJ0a1bt9hll11iwoQJ0bt37/jyyy/zBVUvvPBCjBo1Knr16hUlS5aMQYMGxWGHHRavv/567LTTTlulpjfffDN22223KFIk79ySPffcM/75z3/GRx99FM2bN9/kcU455ZTo169fTJ48OQ466KCI+GlW9MEHHxzVqlXLN/69996L/fffP3JycuKSSy6J4sWLxz333BNt2rSJF154Ifbaa6+I+OmljjfeeGN079499txzz1i8eHFMmzYtpk+fHoccckiceeaZ8dVXXxXYFqYgZcqUiWOOOSZGjx4dP/zwQ1SqVCmzbdSoUZGbmxudOnWKiIhHHnkkli9fHmeffXZUrlw5Xn/99bjrrrviiy++iEceeWST5yqMqVOnxssvvxwnnXRS/OlPf4o5c+bE4MGDo02bNvH+++/nm9Xcs2fPqFChQvTr1y8+/PDDGDx4cHz22WeZcK8ga9eujaOPPjpeeuml6NGjRzRp0iRmzJgRt99+e3z00Ufx+OOPb7C+jz/+OD744IM4/fTTo1y5clvlmn9u/vz5cfjhh8dJJ50Uf/nLX6J69eqZbUOGDIkVK1ZEjx49omTJklGpUqV47733olWrVlG7du247LLLokyZMvHwww9Hhw4d4tFHH41jjz02z/HPO++8qFixYvTt2zfmzJkTd9xxR/Ts2TNGjRqVGTN06NA4/fTTo1mzZnH55ZdHhQoV4s0334zx48dvtAXLmWeeGUOHDo3TTjstevXqFbNnz46777473nzzzZgyZUoUL1485s2bF4ceemhUrVo1LrvssqhQoULMmTOn0GHvxx9/HCeeeGKcddZZ0aVLlxgyZEiccMIJMX78+DjkkENihx12iFatWsWIESPiwgsvzLPviBEjoly5cnHMMcds8jwjRoyI+vXrxx577BE77bRTlC5dOh566KHo3bt3ZsyWXEtubm6cfvrpMWrUqMxfdWyuBQsWxIIFC2LHHXfMs/7aa6+NEiVKxMUXXxwrV67c4Cz/iRMnxlFHHRU1a9aM888/P2rUqBEzZ86MJ598Ms4///yIiM1+rgBgiyQAAJBC5557bvLz/5x9/PHHk4hIrrvuujzjjj/++CQrKyv55JNPMusiIomIZNq0aZl1n332WVKqVKnk2GOP3aw6ypQpk3Tp0mWD204//fR865966qkkIpLx48dv9NitW7dOmjVrliRJkuy+++5Jt27dkiRJkgULFiQlSpRIhg0blkyaNCmJiOSRRx7J7NehQ4ekRIkSyaxZszLrvvrqq6RcuXLJAQcckFm38847J0ceeeRGa1j/Pm/Kumu755578qzfe++9k9q1aye5ublJkiTJ8uXL8+174403JllZWclnn32WWde3b9885589e3YSEcmQIUPy7R8RSd++fTOfCzrHK6+8kkRE8q9//SuzbsiQIUlEJC1btkxWrVqVWX/zzTcnEZGMHTs2s65169ZJ69atM5+HDx+eFClSJHnxxRfznOcf//hHEhHJlClT8tWwztixY5OISG6//fYNjvm5dXXOnj07z/p1z8CkSZPy1BkRyT/+8Y88Y9fdv5ycnGTevHl5th188MFJ8+bNkxUrVmTWrV27Ntl3332TBg0a5Kujbdu2ydq1azPrL7zwwqRo0aLJwoULkyRJkoULFyblypVL9tprr+THH3/Mc66f79elS5ekbt26mc8vvvhiEhHJiBEj8uwzfvz4POvHjBmTREQyderUDd2yDapbt24SEcmjjz6aWbdo0aKkZs2aya677ppZd8899yQRkcycOTOzbtWqVUmVKlU2+HP/c6tWrUoqV66cXHnllZl1p5xySrLzzjvnGVeYa1n33f3tb39LVq9enZx44olJdnZ2MmHChEJc8U8/H926dUu+++67ZN68eclrr72WHHzwwUlEJLfeemuSJP/3LO2www75fn7Wf87WrFmTbL/99kndunWTBQsW5Bn78++3sM8VAPwS2pUAAPA/4emnn46iRYtGr1698qz/61//GkmSxDPPPJNn/T777BMtW7bMfN5uu+3imGOOiQkTJkRubu5WqenHH3+MkiVL5lu/rq/tplpz/Nwpp5wSjz32WKxatSpGjx4dRYsWLXAGZG5ubjz77LPRoUOH2GGHHTLra9asGaecckq89NJLsXjx4oiIqFChQrz33nvx8ccfb+6lbdC62ag/b0cxe/bsePXVV+Pkk0/OzGrPzs7ObF+2bFl8//33se+++0aSJPHmm29ulVp+fo7Vq1fH/PnzY8cdd4wKFSrE9OnT843v0aNHnpYhZ599dhQrViyefvrpDZ7jkUceiSZNmkTjxo3j+++/zyzrZtxPmjRpg/uu+x5+jVncERElS5aM0047rcBtxx13XFStWjXz+Ycffoj//Oc/0bFjx1iyZEnmOubPnx/t2rWLjz/+OL788ss8x+jRo0eeGe77779/5ObmxmeffRYRP83yXbJkSVx22WX5ejlvrO3NI488EuXLl49DDjkkzz1t2bJllC1bNnNPK1SoEBERTz755Bb1La9Vq1aen6F1LWrefPPN+OabbyLipx76pUqVihEjRmTGTZgwIb7//vtCvQ/gmWeeifnz58fJJ5+cWXfyySfH22+/He+9915m3eZcy6pVq+KEE06IJ598Mp5++uk49NBDC3W9ERH3339/VK1aNapVqxZ77bVXpuXMBRdckGdcly5d8vz8FOTNN9+M2bNnxwUXXJCpf5113++WPFcAsCWE3AAA/E/47LPPolatWvkCwyZNmmS2/1yDBg3yHaNhw4axfPnyAvsKb4ns7OwC+zKvWLEis72wTjrppFi0aFE888wzMWLEiDjqqKMKDEe/++67WL58eTRq1CjftiZNmsTatWvj888/j4iIa665JhYuXBgNGzaM5s2bR+/eveOdd94pdE0FKVasWJx44onx4osvZsKrdYH3ulYlERFz586Nrl27RqVKlaJs2bJRtWrVaN26dURELFq06BfVsM6PP/4YV199daZHe5UqVaJq1aqxcOHCAs+x/jNRtmzZqFmz5gZ7eEf81PLivffei6pVq+ZZGjZsGBE/taHYkJycnIiIWLJkyRZc3abVrl17g20mtt9++zyfP/nkk0iSJPr06ZPvWvr27RsR+a9lu+22y/O5YsWKERGZvtmzZs2KiNjs9j8ff/xxLFq0KKpVq5avlqVLl2bqaN26dRx33HHRv3//qFKlShxzzDExZMiQQve633HHHfOF7eu+t3XfeYUKFaJ9+/Z5fmkzYsSIqF27duYXGRvz73//O7bffvsoWbJkfPLJJ/HJJ59E/fr1o3Tp0nmC8825lhtvvDEef/zxGD16dLRp06ZQ17rOMcccExMnToznnnsuXnvttfj+++/j1ltvzddSaf3noyCF+X635LkCgC2hJzcAAPxKatasGV9//XW+9evW1apVa7OO1aZNm7j11ltjypQp8eijj/7i+g444ICYNWtWjB07Np599tm477774vbbb49//OMf0b179y0+7l/+8pe4++6746GHHoqLL744HnrooWjatGnssssuEfHTbPNDDjkkfvjhh7j00kujcePGUaZMmfjyyy+ja9eueV6wub4NzQAuaPb9eeedF0OGDIkLLrgg9tlnnyhfvnxkZWXFSSedtNFzbI61a9dG8+bN47bbbitwe506dTa4b+PGjSMiYsaMGYU61+Zce8TGf4my/rZ19+Piiy+Odu3aFbjP+n2bixYtWuC4ZL0XvW6utWvXRrVq1fKEwD+3bgZ6VlZWjB49Ol599dV44oknYsKECXH66afHrbfeGq+++mqULVv2F9WxTufOneORRx6Jl19+OZo3bx7jxo2Lc845J18wvL7FixfHE088EStWrCjwl2oPPvhgXH/99ZkXuhb2Wtq1axfjx4+Pm2++Odq0aZNvlvzG/OlPf4q2bdtuctzm/AJuY7bkuQKALSHkBgDgf0LdunXjueeeiyVLluSZ4fzBBx9ktv9cQS06PvrooyhdunSeNg6/xC677BIvvvhirF27Nk8g9tprr0Xp0qUzs0YL65RTTonu3btHhQoV4ogjjihwTNWqVaN06dLx4Ycf5tv2wQcfRJEiRfIEr5UqVYrTTjstTjvttFi6dGkccMAB0a9fv0zIvbG2Ehuy1157Rf369ePBBx+MQw45JN577724/vrrM9tnzJgRH330UQwbNiw6d+6cWT9x4sRNHnvdbOGFCxfmWb/+TP2IiNGjR0eXLl3i1ltvzaxbsWJFvn3X+fjjj+PAAw/MfF66dGl8/fXXG7zXERH169ePt99+Ow4++ODNvlcNGzaMRo0axdixY2PgwIGbDGU359o317rWNsWLFy9UCFoY9evXj4iId999d7OCzPr168dzzz0XrVq1KlTYuvfee8fee+8d119/fTz44IPRqVOnGDly5CZ/UbNulvHPv7ePPvooIiLq1auXWXfYYYdF1apVY8SIEbHXXnvF8uXL49RTT91kXY899lisWLEiBg8eHFWqVMmz7cMPP4yrrroqpkyZEvvtt99mXcvee+8dZ511Vhx11FFxwgknxJgxY6JYsd/+/7X/+fe7oWfm13iuAKAg2pUAAPA/4Ygjjojc3Ny4++6786y//fbbIysrKw4//PA861955ZU8fZk///zzGDt2bBx66KEbnKG6uY4//vj49ttv47HHHsus+/777+ORRx6J9u3bF9ive1PH69u3bwwaNGiDbSiKFi0ahx56aIwdOzZPm41vv/02Hnzwwdhvv/0ybTLmz5+fZ9+yZcvGjjvumKdFQpkyZSIif7C6KZ06dYo333wz+vbtG1lZWXHKKafkqTEi74zfJEli4MCBmzxuTk5OVKlSJf773//mWT9o0KB8Y4sWLZpvVvFdd921wZnP//znP/P0Qx48eHCsWbMm37Pzcx07dowvv/wy7r333nzbfvzxx1i2bNlGr6d///4xf/786N69e6xZsybf9meffTaefPLJiPi/UPHn156bmxv//Oc/N3qOwqhWrVq0adMm7rnnngL/+mBLWvgceuihUa5cubjxxhszLXrW2dhs744dO0Zubm5ce+21+batWbMm8ywuWLAg33HW/bVAYVqWfPXVVzFmzJjM58WLF8e//vWv2GWXXaJGjRqZ9cWKFYuTTz45Hn744Rg6dGg0b948WrRoscnj//vf/44ddtghzjrrrDj++OPzLBdffHGULVs2M1t9c6+lbdu2MXLkyBg/fnyceuqpW+0vEzbHbrvtFttvv33ccccd+f59WHctv8ZzBQAFMZMbAID/Ce3bt48DDzwwrrzyypgzZ07svPPO8eyzz8bYsWPjggsuyASE6+y0007Rrl276NWrV5QsWTITkvbv33+T53riiSfi7bffjoifXmj4zjvvxHXXXRcREUcffXQmADv++ONj7733jtNOOy3ef//9qFKlSgwaNChyc3MLdZ71lS9fPvr167fJcdddd11MnDgx9ttvvzjnnHOiWLFicc8998TKlSvj5ptvzoxr2rRptGnTJlq2bBmVKlWKadOmxejRo6Nnz56ZMeteztmrV69o165dFC1aNE466aRN1vCXv/wlrrnmmhg7dmy0atUqz8zYxo0bR/369ePiiy+OL7/8MnJycuLRRx/N9HLelO7du8eAAQOie/fusfvuu8d///vfzAzcnzvqqKNi+PDhUb58+WjatGm88sor8dxzz0XlypULPO6qVavi4IMPjo4dO8aHH34YgwYNiv322y+OPvroDdZy6qmnxsMPPxxnnXVWTJo0KVq1ahW5ubnxwQcfxMMPPxwTJkyI3XfffYP7n3jiiTFjxoy4/vrr480334yTTz456tatG/Pnz4/x48fH888/n+kH3axZs9h7773j8ssvjx9++CEqVaoUI0eOLDAc3xJ///vfY7/99ovmzZvHGWecETvssEN8++238corr8QXX3yReeYLKycnJ26//fbo3r177LHHHnHKKadExYoV4+23347ly5fHsGHDCtyvdevWceaZZ8aNN94Yb731Vhx66KFRvHjx+Pjjj+ORRx6JgQMHxvHHHx/Dhg2LQYMGxbHHHhv169ePJUuWxL333hs5OTkbnX2/TsOGDaNbt24xderUqF69ejzwwAPx7bffxpAhQ/KN7dy5c9x5550xadKkuOmmmzZ57K+++iomTZqU70W465QsWTLatWsXjzzySNx5551bdC0dOnSIIUOGROfOnSMnJyfuueeeTda1NRUpUiQGDx4c7du3j1122SVOO+20qFmzZnzwwQfx3nvvxYQJEyJi6z9XAFCgBAAAUujcc89N1v/P2SVLliQXXnhhUqtWraR48eJJgwYNkr/97W/J2rVr84yLiOTcc89N/v3vfycNGjRISpYsmey6667JpEmTCnXuLl26JBFR4DJkyJA8Y3/44YekW7duSeXKlZPSpUsnrVu3TqZOnVqo87Ru3Tpp1qzZRsdMmjQpiYjkkUceybN++vTpSbt27ZKyZcsmpUuXTg488MDk5ZdfzjPmuuuuS/bcc8+kQoUKSXZ2dtK4cePk+uuvT1atWpUZs2bNmuS8885LqlatmmRlZeW75xuzxx57JBGRDBo0KN+2999/P2nbtm1StmzZpEqVKskZZ5yRvP322/nuYd++ffOdc/ny5Um3bt2S8uXLJ+XKlUs6duyYzJs3L4mIpG/fvplxCxYsSE477bSkSpUqSdmyZZN27dolH3zwQVK3bt2kS5cumXFDhgxJIiJ54YUXkh49eiQVK1ZMypYtm3Tq1CmZP39+nnO3bt06ad26dZ51q1atSm666aakWbNmScmSJZOKFSsmLVu2TPr3758sWrSoUPfq+eefT4455pikWrVqSbFixZKqVasm7du3T8aOHZtn3KxZs5K2bdsmJUuWTKpXr55cccUVycSJE5OIyPP8bujZmT17dhIRyd/+9rcC65g1a1bSuXPnpEaNGknx4sWT2rVrJ0cddVQyevTofPdr/ed43bO4/s/RuHHjkn333TfJzs5OcnJykj333DN56KGHMtu7dOmS1K1bN18t//znP5OWLVsm2dnZSbly5ZLmzZsnl1xySfLVV18lSfLTM37y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/1iyZEmh9r/00kujVq1a0bZt21+50l/HHzrk7tq1a6YRe/HixaN69epxyCGHxAMPPBBr164tcJ/zzjsvOnToEF27dv1ti42Ihx56KIoWLRrnnnvub37u9Q0cODCGDh26rcso0GeffRbZ2dmxdOnSPE33ixYtGnXq1IkePXrEDz/88JvWtC5oXreUKFEidtxxx7juuusiSZJf9dx16tSJr7/+OnbaaactPsbUqVOjR48eW7EqAAAAALaWww8/PE444YRo0aJFtGvXLp5++ulYuHBhPPzww5vcd8CAATFy5MgYM2ZMlCpV6jeoduv7w/fkPuyww2LIkCGRm5sb3377bYwfPz7OP//8GD16dIwbNy6KFct7i+69995frZbVq1dH8eLFN7j9/vvvj0suuSTuueeeuPXWW7fJQ5ebmxtZWVlRvnz53/zchTV27Ng48MADo2zZshHxU9P95557LnJzc2PmzJlx+umnx6JFi2LUqFG/eW3PPfdcNGvWLFauXBkvvfRSdO/ePWrWrBndunUrcPyqVauiRIkSv+icRYsWLXQ/pg2pWrXqRrdv6tkFAAAA4LdToUKFaNiwYXzyyScbHXfLLbfEgAED4rnnnosWLVr8RtVtfX/omdwRESVLlowaNWpE7dq1Y7fddosrrrgixo4dG88880yemcpz586NY445JsqWLRs5OTnRsWPH+Pbbbzd43KlTp8YhhxwSVapUifLly0fr1q1j+vTpecZkZWXF4MGD4+ijj44yZcrE9ddfv8HjzZ49O15++eW47LLLomHDhvHYY4/l2T506NCoUKFCPPnkk9GoUaMoXbp0HH/88bF8+fIYNmxY1KtXLypWrBi9evWK3NzczH4rV66Miy++OGrXrh1lypSJvfbaKyZPnpzvuOPGjYumTZtGyZIlY+7cufnalaxduzZuvvnm2HHHHaNkyZKx3Xbb5bmeSy+9NBo2bBilS5eOHXbYIfr06ROrV6/ObF/X7mP48OFRr169KF++fJx00kl5/qRi5cqV0atXr6hWrVqUKlUq9ttvv5g6dWq+ezV27Ng4+uijM5/XNd2vXbt2tG3bNk444YSYOHFinn3uu+++aNKkSZQqVSoaN24cgwYNyrN9U/UXVuXKlaNGjRpRt27d6NSpU7Rq1SrPc7Huvl5//fVRq1ataNSoUUREDB8+PHbfffcoV65c1KhRI0455ZSYN29eZr8FCxZEp06domrVqpGdnR0NGjSIIUOGRET+diUFeemll2L//feP7OzsqFOnTvTq1SuWLVuW2b5+u5INPbuDBw+O+vXrR4kSJaJRo0YxfPjwzb5HAAAAAPwyS5cujVmzZkXNmjU3OObmm2+Oa6+9NsaPHx+77777b1jd1veHD7kLctBBB8XOO++cCZLXrl0bxxxzTPzwww/xwgsvxMSJE+PTTz+NE088cYPHWLJkSXTp0iVeeumlePXVV6NBgwZxxBFH5OuD069fvzj22GNjxowZcfrpp2/weEOGDIkjjzwyypcvH3/5y1/i/vvvzzdm+fLlceedd8bIkSNj/PjxMXny5Dj22GPj6aefjqeffjqGDx8e99xzT4wePTqzT8+ePeOVV16JkSNHxjvvvBMnnHBCHHbYYfHxxx/nOe5NN90U9913X7z33ntRrVq1fOe+/PLLY8CAAdGnT594//3348EHH4zq1atntpcrVy6GDh0a77//fgwcODDuvffeuP322/McY9asWfH444/Hk08+GU8++WS88MILMWDAgMz2Sy65JB599NEYNmxYTJ8+PXbcccdo165dntYjCxcujJdeeilPyP1zc+bMiQkTJuSZHT1ixIi4+uqr4/rrr4+ZM2fGDTfcEH369Ilhw4ZtVv2ba9q0afHGG2/EXnvtlWf9888/Hx9++GFMnDgxnnzyyYj4aab0tddeG2+//XY8/vjjMWfOnDwtc9bd92eeeSZmzpwZgwcPjipVqhSqjlmzZsVhhx0Wxx13XLzzzjsxatSoeOmll6Jnz54b3W/9Z3fMmDFx/vnnx1//+td4991348wzz4zTTjstJk2atMFjrFy5MhYvXpxnAQAAAGDzXHzxxfHCCy/EnDlz4uWXX45jjz02ihYtGieffHJERHTu3Dkuv/zyzPibbrop+vTpEw888EDUq1cvvvnmm/jmm29i6dKl2+oSfpnkD6xLly7JMcccU+C2E088MWnSpEmSJEny7LPPJkWLFk3mzp2b2f7ee+8lEZG8/vrrSZIkSd++fZOdd955g+fKzc1NypUrlzzxxBOZdRGRXHDBBZusMzc3N6lTp07y+OOPJ0mSJN99911SokSJ5NNPP82MGTJkSBIRySeffJJZd+aZZyalS5dOlixZklnXrl275Mwzz0ySJEk+++yzpGjRosmXX36Z53wHH3xwcvnll+c57ltvvZVnzM/v3eLFi5OSJUsm99577yavZZ2//e1vScuWLTOf+/btm5QuXTpZvHhxZl3v3r2TvfbaK0mSJFm6dGlSvHjxZMSIEZntq1atSmrVqpXcfPPNmXUjRoxIdt999zzHLVKkSFKmTJmkVKlSSUQkEZHcdtttmTH169dPHnzwwTz1XXvttck+++yzWfVv7PufPXt2EhFJdnZ2UqZMmaR48eJJRCQ9evTIM65Lly5J9erVk5UrV27wWEmSJFOnTk0iIvPdtm/fPjnttNM2eu4333wzSZIkmTRpUhIRyYIFC5IkSZJu3brlq+PFF19MihQpkvz4449JkiRJ3bp1k9tvvz2zvaBnd999903OOOOMPOtOOOGE5IgjjtjgdfTt2zfzneRdFiURicVisVgsFovFYrFYLBaLZRNLkvyUZdasWTMpUaJEUrt27eTEE0/MkxO2bt066dKlS+Zz3bp1k4Iymb59+24wx/mtLVq0KImIZNGiRZsc+4fvyb0hSZJEVlZWRETMnDkz6tSpE3Xq1Mlsb9q0aVSoUCFmzpwZe+yxR779v/3227jqqqti8uTJMW/evMjNzY3ly5fH3Llz84wrzJ8CTJw4MZYtWxZHHHFERERUqVIl84LMa6+9NjOudOnSUb9+/czn6tWrR7169TK9qdetW9fmYsaMGZGbmxsNGzbMc76VK1dG5cqVM59LlCix0Z48M2fOjJUrV8bBBx+8wTGjRo2KO++8M2bNmhVLly6NNWvWRE5OTp4x9erVi3LlymU+16xZM1PrrFmzYvXq1dGqVavM9uLFi8eee+4ZM2fOzKxbv1VJRESjRo1i3LhxsWLFivj3v/8db731Vpx33nkREbFs2bKYNWtWdOvWLc4444zMPmvWrMnTd7ww9RfGqFGjokmTJrF69ep4991347zzzouKFSvmmbHevHnzfH2433jjjejXr1+8/fbbsWDBgsyLUefOnRtNmzaNs88+O4477riYPn16HHroodGhQ4fYd999C1XT22+/He+8806MGDEisy5Jkli7dm3Mnj07mjRpUuB+6z+7M2fOzPdyylatWsXAgQM3eO7LL788LrroosznxYsX5/k5AwAAAGDTRo4cudHtP29PHPFTt4P/JULuDZg5c2Zsv/32W7x/ly5dYv78+TFw4MCoW7dulCxZMvbZZ59YtWpVnnFlypTZ5LHuv//++OGHHyI7Ozuzbu3atfHOO+9E//79o0iRn7rOrP/iv6ysrALXrQtIly5dGkWLFo033ngjihYtmmfcz4Px7OzsTOBfkJ/XVZBXXnklOnXqFP3794927dpF+fLlY+TIkXHrrbfmGbexWgtj1apVMX78+LjiiivyrC9RokTsuOOOEfHT22KPPPLI6N+/f1x77bWZP8G4995787UNWXdPClt/YdSpUydTS5MmTWLWrFnRp0+f6NevX+ZFous/E8uWLYt27dpFu3btYsSIEVG1atWYO3dutGvXLvM8HX744fHZZ5/F008/HRMnToyDDz44zj333Ljllls2WdPSpUvjzDPPjF69euXbtt12221wv8I8u5tSsmTJKFmy5C8+DgAAAAB/XELuAvznP/+JGTNmxIUXXhgRP4WRn3/+eXz++eeZWabvv/9+LFy4MJo2bVrgMaZMmRKDBg3KzL7+/PPP4/vvv9/sWubPnx9jx46NkSNHRrNmzTLrc3NzY7/99otnn302DjvssM0+bkTErrvuGrm5uTFv3rzYf//9t+gYERENGjSI7OzseP7556N79+75tr/88stRt27duPLKKzPrPvvss806x7qXGU6ZMiXq1q0bET/1qZ46dWpccMEFEfHTb6QqVqwYO++880aPddVVV8VBBx0UZ599dtSqVStq1aoVn376aXTq1KnA8Vuj/g0pWrRorFmzJlatWpUJudf3wQcfxPz582PAgAGZ52/atGn5xlWtWjW6dOkSXbp0if333z969+5dqJB7t912i/fffz8Tvm+pJk2axJQpU6JLly6ZdVOmTNngzwgAAAAAbA1/+JB75cqV8c0330Rubm58++23MX78+LjxxhvjqKOOis6dO0dERNu2baN58+bRqVOnuOOOO2LNmjVxzjnnROvWrTfYbqRBgwYxfPjw2H333WPx4sXRu3fvTc54Lsjw4cOjcuXK0bFjx3yzqY844oi4//77tzjkbtiwYXTq1Ck6d+4ct956a+y6667x3XffxfPPPx8tWrSII488slDHKVWqVFx66aVxySWXRIkSJaJVq1bx3XffxXvvvRfdunWLBg0axNy5c2PkyJGxxx57xFNPPRVjxozZrFrLlCkTZ599dvTu3TsqVaoU2223Xdx8882xfPny6NatW0REjBs3boMvnPy5ffbZJ1q0aBE33HBD3H333dG/f//o1atXlC9fPg477LBYuXJlTJs2LRYsWBAXXXTRVql/nfnz58c333wTa9asiRkzZsTAgQPjwAMP3Gjrk+222y5KlCgRd911V5x11lnx7rvv5mlTExFx9dVXR8uWLaNZs2axcuXKePLJJzfYZmR9l156aey9997Rs2fP6N69e5QpUybef//9mDhxYtx9992FvrbevXtHx44dY9ddd422bdvGE088EY899lg899xzhT4GAAAAAGyuItu6gG1t/PjxUbNmzahXr14cdthhMWnSpLjzzjtj7NixmXYVWVlZMXbs2KhYsWIccMAB0bZt29hhhx1i1KhRGzzu/fffHwsWLIjddtstTj311OjVq1dUq1Zts+t74IEH4thjjy2wXchxxx0X48aN26IZ4usMGTIkOnfuHH/961+jUaNG0aFDh5g6depG21QUpE+fPvHXv/41rr766mjSpEmceOKJmX7aRx99dFx44YXRs2fP2GWXXeLll1+OPn36bHatAwYMiOOOOy5OPfXU2G233eKTTz6JCRMmRMWKFSOi8CF3RMSFF14Y9913X3z++efRvXv3uO+++2LIkCHRvHnzaN26dQwdOjTTrmZr1R/x0y9M1j1vPXr0iCOOOGKjz1HETzO0hw4dGo888kg0bdo0BgwYkG+GdokSJeLyyy+PFi1axAEHHBBFixbdZC+mdVq0aBEvvPBCfPTRR7H//vvHrrvuGldffXXUqlVrs66tQ4cOMXDgwLjllluiWbNmcc8998SQIUOiTZs2m3UcAAAAANgcWUmSJNu6CPilpk+fHgcddFB89913+Xp7kx6LFy/+/y/8XBQRm/9iTwAAAIA/mv/VdHddTrRo0aKNdkGIMJOb/xFr1qyJu+66S8ANAAAAAH8wZnIDvxtmcgMAAABsnv/VdNdMbgAAAAAA/hCE3AAAAAAApJaQGwAAAACA1BJyAwAAAACQWkJuAAAAAABSS8gNAAAAAEBqCbkBAAAAAEgtITcAAAAAAKkl5AYAAAAAILWE3AAAAAAApJaQGwAAAACA1BJyAwAAAACQWkJuAAAAAABSS8gNAAAAAEBqCbkBAAAAAEgtITcAAAAAAKkl5AYAAAAAILWE3AAAAAAApJaQGwAAAACA1BJyAwAAAACQWkJuAAAAAABSS8gNAAAAAEBqCbkBAAAAAEgtITcA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hTtgVlZ8+umnv6go4I9p8eLFUb58+YhYFBE527ocAACALVK4pAWAjVmXEy1atChycjaeExV6Jvfs2bN/cWEAAAAAALA1/eKe3EmSRCEngwMAAAAAwFa1xSH3v/71r2jevHlkZ2dHdnZ2tGjRIoYPH741awMAAAAAgI0qdLuSn7vtttuiT58+0bNnz2jVqlVERLz00ktx1llnxffffx8XXnjhVi0SAAAAAAAKUugXT/7c9ttvH/3794/OnTvnWT9s2LDo16+f/t3AFvHiSQAA4H+Brq4Av9zmvHhyi9qVfP3117HvvvvmW7/vvvvG119/vSWHBAAAAACAzbZFIfeOO+4YDz/8cL71o0aNigYNGvziogAAAAAAoDC2qCd3//7948QTT4z//ve/mZ7cU6ZMieeff77A8BsAAAAAAH4NWzST+7jjjovXXnstqlSpEo8//ng8/vjjUaVKlXj99dfj2GOP3do1AgAAAABAgbboxZMAvwYvngQAAP4XSFoAfrnNefHkFrUriYjIzc2NMWPGxMyZMyMiomnTpnHMMcdEsWJbfEgAAAAAANgsW9Su5L333ouGDRtGly5dYsyYMTFmzJjo0qVLNGjQIN59992tXSMAAABAqgwePDhatGgROTk5kZOTE/vss08888wzG93njjvuiEaNGkV2dnbUqVMnLrzwwlixYkWeMV9++WX85S9/icqVK0d2dnY0b948pk2b9mteCsDv3hZNu+7evXs0a9Yspk2bFhUrVoyIiAULFkTXrl2jR48e8fLLL2/VIgEAAADS5E9/+lMMGDAgGjRoEEmSxLBhw+KYY46JN998M5o1a5Zv/IMPPhiXXXZZPPDAA7HvvvvGRx99FF27do2srKy47bbbIuKn7KVVq1Zx4IEHxjPPPBNVq1aNjz/+OJPNAPxRbVFP7uzs7Jg2bVq+f5Tffffd2GOPPeLHH3/cagUCfxx6cgMAAP8LNpS0VKpUKf72t79Ft27d8m3r2bNnzJw5M55//vnMur/+9a/x2muvxUsvvRQREZdddllMmTIlXnzxxV+lboDfk83pyb1F7UoaNmwY3377bb718+bNix133HFLDgkAAADwPyk3NzdGjhwZy5Yti3322afAMfvuu2+88cYb8frrr0dExKeffhpPP/10HHHEEZkx48aNi9133z1OOOGEqFatWuy6665x7733/ibXAPB7VuiQe/HixZnlxhtvjF69esXo0aPjiy++iC+++CJGjx4dF1xwQdx0002/Zr1b7JNPPokbbrjBLHMAAADgNzFjxowoW7ZslCxZMs4666wYM2ZMNG3atMCxp5xySlxzzTWx3377RfHixaN+/frRpk2buOKKKzJjPv300xg8eHA0aNAgJkyYEGeffXb06tUrhg0b9ltdEsDvUqFD7goVKkTFihWjYsWK0b59+3j//fejY8eOUbdu3ahbt2507Ngx3n333Wjfvv2vWe8WWbFiRRx//PFRq1atyM7Ozqzv169f7LLLLr9ZHfXq1Ys77rjjVz/P0KFDo0KFCr/6efg/v/WztDnmzJkTWVlZ8dZbb0VExOTJkyMrKysWLlxY6GP8Vs8uAADA/5JGjRrFW2+9Fa+99lqcffbZ0aVLl3j//fcLHDt58uS44YYbYtCgQTF9+vR47LHH4qmnnoprr702M2bt2rWx2267xQ033BC77rpr9OjRI84444z4xz/+8VtdEsDvUqFfPDlp0qRfs45C69q1a+Y3lMWKFYtKlSpFixYt4uSTT46uXbtGkSL5c/vzzjsvOnToEF27dv2Nq/11TJo0Kf72t7/Fa6+9Fj/++GPUq1cvDj/88Ljooouidu3aceKJJ+b5c6Y/ms8++ywaN24c3333Xdxyyy3Rv3//iIgoUqRI1KpVKw4//PAYMGBAVKpU6Terac6cObH99ttnPhcvXjy222676Nq1a1x55ZWRlZX1q527Tp068fXXX0eVKlW2+BhTp06NMmXKbMWqAAAA/veVKFEi09a1ZcuWMXXq1Bg4cGDcc889+cb26dMnTj311OjevXtERDRv3jyWLVsWPXr0iCuvvDKKFCkSNWvWzDcTvEmTJvHoo4/++hcD8DtW6JC7devWv2Ydm+Wwww6LIUOGRG5ubnz77bcxfvz4OP/882P06NExbty4KFYs72X9mv2pVq9eHcWLF//Vjr++e+65J84555zo0qVLPProo1GvXr2YO3du/Otf/4pbb701brvttsjOzs4zYz3tVq1aFSVKlCj0+LFjx8aBBx4YZcuWjYiIZs2axXPPPRe5ubkxc+bMOP3002PRokUxatSoX6vkDXruueeiWbNmsXLlynjppZeie/fuUbNmzQJfOhKx+ddekKJFi0aNGjV+0TGqVq260e2/9c8BAABAGq1duzZWrlxZ4Lbly5fnm7hXtGjRiIhI/v+bLFu1ahUffvhhnjEfffRR1K1b91eoFiA9tujFkxE/tQB5/fXX48knn4xx48blWX5tJUuWjBo1akTt2rVjt912iyuuuCLGjh0bzzzzTAwdOjQzbu7cuXHMMcdE2bJlIycnJzp27FjgCzPXmTp1ahxyyCFRpUqVKF++fLRu3TqmT5+eZ0xWVlYMHjw4jj766ChTpkxcf/31BR5r3rx50b59+8jOzo7tt98+RowYkW/MwoULo3v37lG1atXIycmJgw46KN5+++0N1vfFF19Er169olevXvHAAw9EmzZtol69enHAAQfEfffdF1dffXVE5G9Xsq6VxvDhw6NevXpRvnz5OOmkk2LJkiWZMUuWLIlOnTpFmTJlombNmnH77bdHmzZt4oILLsiMGT58eOy+++5Rrly5qFGjRpxyyikxb968zPZ1bTCeeuqpaNGiRZQqVSr23nvvePfdd/PV8nN33HFH1KtXL/O5a9eu0aFDh7j++uujVq1a0ahRo0Kdf52xY8fG0UcfnflcrFixzPPStm3bOOGEE2LixIl59rnvvvuiSZMmUapUqWjcuHEMGjQoz/ZLL700GjZsGKVLl44ddtgh+vTpE6tXr97AN7VhlStXjho1akTdunWjU6dO0apVqzzP2JZe+4IFC6JTp05RtWrVyM7OjgYNGsSQIUMiIn+7koK89NJLsf/++0d2dnbUqVMnevXqFcuWLctsX79dyYZ+DgYPHhz169ePEiVKRKNGjWL48OGbfY8AAAD+F1x++eXx3//+N+bMmRMzZsyIyy+/PCZPnhydOnWKiIjOnTvH5Zdfnhnfvn37GDx4cIwcOTJmz54dEydOjD59+kT79u0zYfeFF14Yr776atxwww3xySefxIMPPhj//Oc/49xzz90m1wjwe1Homdw/N378+OjcuXN8//33+bZlZWVFbm7uLy5scx100EGx8847x2OPPRbdu3ePtWvXZgLuF154IdasWRPnnntunHjiiTF58uQCj7FkyZLo0qVL3HXXXZEkSdx6661xxBFHxMcffxzlypXLjOvXr18MGDAg7rjjjnyzxtfp2rVrfPXVVzFp0qQoXrx49OrVK18ge8IJJ0R2dnY888wzUb58+bjnnnvi4IMPjo8++qjAVhqPPPJIrFq1Ki655JICz7mxPtyzZs2Kxx9/PJ588slYsGBBdOzYMQYMGJAJJy+66KKYMmVKjBs3LqpXrx5XX311TJ8+PU8gvXr16rj22mujUaNGMW/evLjooouia9eu8fTTT+c5V+/evWPgwIFRo0aNuOKKK6J9+/bx0UcfbdZM3+effz5ycnLyhNGFOf/ChQvjpZde2mC4OmfOnJgwYUKe2dEjRoyIq6++Ou6+++7Ydddd480334wzzjgjypQpE126dImIiHLlysXQoUOjVq1aMWPGjDjjjDOiXLlyG/wuCmPatGnxxhtvROfOnX/xtffp0yfef//9eOaZZ6JKlSrxySefFPolq7NmzYrDDjssrrvuunjggQfiu+++i549e0bPnj0zQXlB1v85GDNmTJx//vlxxx13RNu2bePJJ5+M0047Lf70pz/FgQceWOAxVq5cmWcWw+LFiwtVMwAAwO/dvHnzonPnzvH1119H+fLlo0WLFjFhwoQ45JBDIuKniXk/n7l91VVXRVZWVlx11VXx5ZdfRtWqVaN9+/Z5JtftscceMWbMmLj88svjmmuuie233z7uuOOOTHAO8IeVbIEdd9wxOeecc5JvvvlmS3b/Rbp06ZIcc8wxBW478cQTkyZNmiRJkiTPPvtsUrRo0WTu3LmZ7e+9914SEcnrr7+eJEmS9O3bN9l55503eK7c3NykXLlyyRNPPJFZFxHJBRdcsNEaP/zwwzznSZIkmTlzZhIRye23354kSZK8+OKLSU5OTrJixYo8+9avXz+55557Cjzu2WefneTk5Gz03EmSJEOGDEnKly+f+dy3b9+kdOnSyeLFizPrevfuney1115JkiTJ4sWLk+LFiyePPPJIZvvChQuT0qVLJ+eff/4GzzN16tQkIpIlS5YkSZIkkyZNSiIiGTlyZGbM/Pnzk+zs7GTUqFGZWta/57fffntSt27dzOcuXbok1atXT1auXLnR61z//EmSJCNGjEh23333PNdepEiRpEyZMkmpUqWSiEgiIrntttsyY+rXr588+OCDeY597bXXJvvss88Gz/23v/0tadmyZZ7zbOxZmj17dhIRSXZ2dlKmTJmkePHiSUQkPXr0yDNuS6+9ffv2yWmnnbbRc7/55ptJkvzf97RgwYIkSZKkW7du+ep48cUXkyJFiiQ//vhjkiRJUrdu3cyzmyQF/xzsu+++yRlnnJFn3QknnJAcccQRG7yOvn37Zr6TvMuiJCKxWCwWi8VisVgsllQuAPxyixYtSiIiWbRo0SbHblG7km+//TYuuuiiqF69+i+I17e+JEkyL/CbOXNm1KlTJ+rUqZPZ3rRp06hQoULMnDmzwP2//fbbOOOMM6JBgwZRvnz5yMnJiaVLl8bcuXPzjNt99903WsfMmTOjWLFi0bJly8y6xo0b55lp/fbbb8fSpUujcuXKUbZs2cwye/bsmDVr1iavb3PVq1cvz2z0mjVrZmaWf/rpp7F69erYc889M9vLly+faZWxzhtvvBHt27eP7bbbLsqVK5fp077+/dlnn30y/3elSpWiUaNGG7znG9K8efN8vagLc/71W5VE/N/brKdOnRqXXnpptGvXLs4777yIiFi2bFnMmjUrunXrlud7uO666/J8D6NGjYpWrVpFjRo1omzZsnHVVVflu+7CGDVqVLz11lvx9ttvx8MPPxxjx46Nyy677Bdf+9lnnx0jR46MXXbZJS655JJ4+eWXC13T22+/HUOHDs1z/e3atYu1a9fG7NmzN7jf+j8HM2fOjFatWuVZ16pVq41+95dffnksWrQos3z++eeFrhsAAAAAIrawXcnxxx8fkydPjvr162/ten6RmTNnxvbbb7/F+3fp0iXmz58fAwcOjLp160bJkiVjn332iVWrVuUZV6ZMmV9aaixdujRq1qxZYOuUDbUdadiwYSxatCi+/vrrqFmz5madb/1WIVlZWbF27dpC779s2bJo165dtGvXLkaMGBFVq1aNuXPnRrt27fLdn40pUqRIJEmSZ11Bva3Xv8eFOf+qVati/PjxccUVV+TZ9+dvsx4wYEAceeSR0b9//7j22mtj6dKlEfHTy0n32muvPPut63n2yiuvRKdOnaJ///7Rrl27KF++fIwcOTJuvfXWQl/3OnXq1MnU0qRJk5g1a1b06dMn+vXrF6VKldriaz/88MPjs88+i6effjomTpwYBx98cJx77rlxyy23bLKmpUuXxplnnhm9evXKt2277bbb4H5b4+egZMmSUbJkyV98HAAAAAD+uLYo5L777rvjhBNOiBdffDGaN2+eL0AtKCz7tf3nP/+JGTNmxIUXXhgRPwWIn3/+eXz++eeZ2dzvv/9+LFy4MJo2bVrgMaZMmRKDBg2KI444IiIiPv/88wL7jm9K48aNY82aNfHGG2/EHnvsERERH374YSxcuDAzZrfddotvvvkmihUrluelixtz/PHHx2WXXRY333xz3H777fm2L1y4cKN9uTdkhx12iOLFi8fUqVMzoeaiRYvio48+igMOOCAiIj744IOYP39+DBgwIHM/p02bVuDxXn311cxxFixYEB999FE0adIkIiKqVq0a33zzTZ5Z6Rt7IeI6hTn/5MmTo2LFirHzzjtv9FhXXXVVHHTQQXH22WdHrVq1olatWvHpp59usIfZyy+/HHXr1o0rr7wys+6zzz7bZM2FUbRo0VizZk2sWrUqE3Kvr7D3vmrVqtGlS5fo0qVL7L///tG7d+9Chdy77bZbvP/++5nwfUs1adIkpkyZkuljHvHTz9SGft4AAAAAYGvYopD7oYceimeffTZKlSoVkydPztNCIysr61cPuVeuXBnffPNN5Obmxrfffhvjx4+PG2+8MY466qjMS/zatm0bzZs3j06dOsUdd9wRa9asiXPOOSdat269wXYjDRo0iOHDh8fuu+8eixcvjt69e0d2dvZm19eoUaM47LDD4swzz4zBgwdHsWLF4oILLshzrLZt28Y+++wTHTp0iJtvvjkaNmwYX331VTz11FNx7LHHFlhjnTp14vbbb4+ePXvG4sWLo3PnzlGvXr344osv4l//+leULVt2i2YXlytXLrp06RK9e/eOSpUqRbVq1aJv375RpEiRzHe73XbbRYkSJeKuu+6Ks846K95999249tprCzzeNddcE5UrV47q1avHlVdeGVWqVIkOHTpERESbNm3iu+++i5tvvjmOP/74GD9+fDzzzDORk5Oz0RoLc/5x48bla1VSkH322SdatGgRN9xwQ9x9993Rv3//6NWrV5QvXz4OO+ywWLlyZUybNi0WLFgQF110UTRo0CDmzp0bI0eOjD322COeeuqpGDNmTCHubH7z58+Pb775JtasWRMzZsyIgQMHxoEHHrjR6y/MtV999dXRsmXLaNasWaxcuTKefPLJzC8WNuXSSy+NvffeO3r27Bndu3ePMmXKxPvvvx8TJ06Mu+++u9DX1rt37+jYsWPsuuuu0bZt23jiiSfisccei+eee67QxwAAAACAzbVFPbmvvPLK6N+/fyxatCjmzJkTs2fPziyffvrp1q4xn/Hjx0fNmjWjXr16cdhhh8WkSZPizjvvjLFjx2ZaTGRlZcXYsWOjYsWKccABB0Tbtm1jhx12iFGjRm3wuPfff38sWLAgdttttzj11FOjV69eUa1atS2qcciQIVGrVq1o3bp1/PnPf44ePXrkOVZWVlY8/fTTccABB8Rpp50WDRs2jJNOOik+++yzjfY6P+ecc+LZZ5+NL7/8Mo499tho3LhxdO/ePXJycuLiiy/eolojIm677bbYZ5994qijjoq2bdtGq1atokmTJpnZxVWrVo2hQ4fGI488Ek2bNo0BAwZscJbwgAED4vzzz4+WLVvGN998E0888USmx3STJk1i0KBB8fe//z123nnneP311wtVd2HOX9iQOyLiwgsvjPvuuy8+//zz6N69e9x3330xZMiQaN68ebRu3TqGDh2aaX1z9NFHx4UXXhg9e/aMXXbZJV5++eXo06dPoc6zvrZt22ae3R49esQRRxyx0WeysNdeokSJuPzyy6NFixZxwAEHRNGiRWPkyJGFqqlFixbxwgsvxEcffRT7779/7LrrrnH11VdHrVq1NuvaOnToEAMHDoxbbrklmjVrFvfcc08MGTIk2rRps1nHAQAAAIDNkZWs3yC5ECpVqhRTp0793fXkZutZtmxZ1K5dO2699dbo1q1bofaZPHlyHHjggbFgwYItapvyS0yfPj0OOuig+O677/K1zyE9Fi9eHOXLl4+IRRGx8dn9AAAAv1ebn7QAsL51OdGiRYs22QVii2Zyd+nSZZOzT0mXN998Mx566KGYNWtWTJ8+PdOf+phjjtnGlRXOmjVr4q677hJwAwAAAMAfzBb15M7NzY2bb745JkyYEC1atMgXLN52221bpTh+W7fcckt8+OGHUaJEiWjZsmW8+OKLUaVKlW1dVqHsueeeseeee27rMgAAAACA39gWtSs58MADN3zArKz4z3/+84uKAv6YtCsBAAD+F2hXAvDLbU67ki2ayT1p0qQtKgwAAAAAALamLerJPWTIkPjxxx+3di0AAAAAALBZtijkvuyyy6J69erRrVu3ePnll7d2TQAAAAAAUChbFHJ/+eWXMWzYsPj++++jTZs20bhx47jpppvim2++2dr1AQAAAADABm1RyF2sWLE49thjY+zYsfH555/HGWecESNGjIjtttsujj766Bg7dmysXbt2a9cKAAAAAAB5bFHI/XPVq1eP/fbbL/bZZ58oUqRIzJgxI7p06RL169ePyZMnb4USAQAAAACgYFsccn/77bdxyy23RLNmzaJNmzaxePHiePLJJ2P27Nnx5ZdfRseOHaNLly5bs1YAAAAAAMgjK0mSZHN3at++fUyYMCEaNmwY3bt3j86dO0elSpXyjJk3b17UqFFD2xKg0BYvXhzly5ePiEURkbOtywEAANgim5+0ALC+dTnRokWLIidn4zlRsS05QbVq1eKFF16IffbZZ4NjqlatGrNnz96SwwMAAAAAQKFsVruSV155JZ588sm4//77MwH3v/71r9h+++2jWrVq0aNHj1i5cmVERGRlZUXdunW3fsUAAAAAAPD/bVbIfc0118R7772X+Txjxozo1q1btG3bNi677LJ44okn4sYbb9zqRQIAAAAAQEE2K+R+66234uCDD858HjlyZOy1115x7733xkUXXRR33nlnPPzww1u9SAAAAAAAKMhmhdwLFiyI6tWrZz6/8MILcfjhh2c+77HHHvH5559vveoAAAAAAGAjNivkrl69euZlkqtWrYrp06fH3nvvndm+ZMmSKF68+NatEAAAAAAANmCzQu4jjjgiLrvssnjxxRfj8ssvj9KlS8f++++f2f7OO+9E/fr1t3qRAAAAAABQkGKbM/jaa6+NP//5z9G6desoW7ZsDBs2LEqUKJHZ/sADD8Shhx661YsEAAAAAICCZCVJkmzuTosWLYqyZctG0aJF86z/4YcfomzZsnmCb4DCWrx4cZQvXz4iFkVEzrYuBwAAYItsftICwPrW5USLFi2KnJyN50SbNZN7nZ9CqPwqVaq0JYcDAAAAAIAtslk9uQEAAAAA4PdEyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqVVsWxcAsL5FiyJycrZ1FQAAAACkgZncAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqSXkBgAAAAAgtYTcAAAAAACklpAbAAAAAIDUEnIDAAAAAJBaQm4AAAAAAFJLyA0AAAAAQGoJuQEAAAAASC0hNwAAAAAAqVVsWxcAsL7y5bd1BQCFlyTbugIAAIA/NjO5AQAAAABILSE3AAAAAACpJeQGAAAAACC1hNwAAAAAAKSWkBsAAAAAgNQScgMAAAAAkFpCbgAAAAAAUkvIDQAAAABAagm5AQAAAABILSE3AAAAAACpJeQGAAAAACC1hNwAAAAAAKSWkBsAAAAAgNQScgMAAAAAkFpCbgAAAAAAUkvIDQAAAABAagm5AQAAAABILSE3AAAAAACpJeQGAAAAACC1hNwAAAAAAKSWkBsAAAAAgNQScgMAAAAAkFpCbgAAAAAAUkvIDQAAAABAagm5AQAAAABILSE3AAAAAACpJeQGAAAAACC1hNwAAAAAAKSWkBsAAAAAgNQScgMAAAAAkFpCbgAAAAAAUkvIDQAAAABAagm5AQAAAABILSE3AAAAAACpJeQGAAAAACC1hNwAAAAAAKSWkBsAAAAAgNQScgMAAAAAkFpCbgAAAAAAUkvIDQAAAABAagm5AQAAAABILSE3AAAAAACpJeQGAAAAACC1hNwAAAAAAKSWkBsAAAAAgNQScgMAAAAAkFpCbgAAAAAAUkvIDQAAAABAagm5AQAAAABILSE3AAAAAACpJeQGAAAAACC1hNwAAAAAAKSWkBsAAAAAgNQScgMAAAAAkFpCbgCAreC///1vtG/fPmrVqhVZWVnx+OOPF3rfKVOmRLFixWKXXXbJs/7GG2+MPfbYI8qVKxfVqlWLDh06xIcffrh1CwcAAEg5ITcAwFawbNmy2HnnnePvf//7Zu23cOHC6Ny5cxx88MH5tr3wwgtx7rnnxquvvhoTJ06M1atXx6GHHhrLli3bWmUDAACkXlaSJMm2LgIgImLx4sVRvnz5iFgUETnbuhyAQinov6SysrJizJgx0aFDh03uf9JJJ0WDBg2iaNGi8fjjj8dbb721wbHfffddVKtWLV544YU44IADtrxoAACA37l1OdGiRYsiJ2fjOZGZ3AAA28iQIUPi008/jb59+xZq/KJFiyIiolKlSr9mWQAAAKlSbFsXAADwR/Txxx/HZZddFi+++GIUK7bp/yRbu3ZtXHDBBdGqVavYaaedfoMKAQAA0iE1M7kL8wKnrl27FurPgreVoUOHRoUKFbZ1GZtt8uTJkZWVFQsXLvxVjr+5L+f6vWrTpk1ccMEF27qMAq3/7PXr1y/fy802Zs6cOZGVlbXRP6EHoPByc3PjlFNOif79+0fDhg0Ltc+5554b7777bowcOfJXrg4AACBdtmnI3bVr18jKyoqsrKwoXrx4VK9ePQ455JB44IEHYu3atXnGfv3113H44Ydvo0rTYejQoZn7+fOlVKlSv+i4++67b3z99df/v1dyOgwbNiz222+/iPgpfP75vWjYsGHceOON8Vu3o1//+ylbtmy0bNkyHnvssV/93CeeeGJ89NFHW7x/nTp14uuvvzZzEGArWbJkSUybNi169uwZxYoVi2LFisU111wTb7/9dhQrViz+85//5Bnfs2fPePLJJ2PSpEnxpz/9aRtVDQAA8Pu0zduVHHbYYTFkyJDIzc2Nb7/9NsaPHx/nn39+jB49OsaNG5f5890aNWps9DirV6/+Lcr93cvJyYkPP/wwz7qsrKxfdMwSJUps9P7n5uZGVlZWFCny+/nDgLFjx8bRRx+d+XzGGWfENddcEytXroz//Oc/0aNHj6hQoUKcffbZv2ldP/9+lixZEkOGDImOHTvGe++9F40aNSpwn1WrVkWJEiV+0Xmzs7MjOzt7i/cvWrToRp+BJEkiNze3UH9uD8BP/3swY8aMPOsGDRoU//nPf2L06NGx/fbbR8RP/76ed955MWbMmJg8eXJmPQAAAP9nm6eSJUuWjBo1akTt2rVjt912iyuuuCLGjh0bzzzzTAwdOjQz7uctLda1Thg1alS0bt06SpUqFSNGjMiMveWWW6JmzZpRuXLlOPfcc/ME4MOHD4/dd989ypUrFzVq1IhTTjkl5s2bl9m+rjXHhAkTYtddd43s7Ow46KCDYt68efHMM89EkyZNIicnJ0455ZRYvnz5Rq9t6NChsd1220Xp0qXj2GOPjfnz5+cbM3jw4Khfv36UKFEiGjVqFMOHD89sS5Ik+vXrF9ttt12ULFkyatWqFb169droObOysqJGjRp5lurVq2e2t2nTJs4777y44IILomLFilG9evW49957Y9myZXHaaadFuXLlYscdd4xnnnkm3z1Z165kXeuLcePGRdOmTaNkyZIxd+7cmDp1ahxyyCFRpUqVKF++fLRu3TqmT5+ep76PP/44DjjggChVqlQ0bdo0Jk6cmO8aZsyYEQcddFBkZ2dH5cqVo0ePHrF06dI89ey5555RpkyZqFChQrRq1So+++yzzPYVK1bEs88+myfkLl26dNSoUSPq1q0bp512WrRo0SLPuVeuXBkXX3xx1K5dO8qUKRN77bVXTJ48ObN9/vz5cfLJJ0ft2rWjdOnS0bx583jooYc2+l1s6vtp0KBBXHfddVGkSJF45513MmPq1asX1157bXTu3DlycnKiR48eERFx6aWXRsOGDaN06dKxww47RJ8+ffI822+//XYceOCBUa5cucjJyYmWLVvGtGnTIqJwrXLuu+++aNKkSZQqVSoaN24cgwYNymxbv13JumfimWeeiZYtW0bJkiXjpZdeipUrV0avXr2iWrVqUapUqdhvv/1i6tSpGzznypUrY/HixXkWgLRaunRpvPXWW5l/K2fPnh1vvfVWzJ07NyIiLr/88ujcuXNERBQpUiR22mmnPMu6fzt32mmnKFOmTET81KLk3//+dzz44INRrly5+Oabb+Kbb76JH3/8cZtcIwAAwO/RNg+5C3LQQQfFzjvvvMk2Dpdddlmcf/75MXPmzGjXrl1EREyaNClmzZoVkyZNimHDhsXQoUPzhOWrV6+Oa6+9Nt5+++14/PHHY86cOdG1a9d8x+7Xr1/cfffd8fLLL8fnn38eHTt2jDvuuCMefPDBeOqpp+LZZ5+Nu+66a4O1vfbaa9GtW7fo2bNnvPXWW3HggQfGddddl2fMmDFj4vzzz4+//vWv8e6778aZZ54Zp512WkyaNCkiIh599NG4/fbb45577omPP/44Hn/88WjevHkh7+KGDRs2LKpUqRKvv/56nHfeeXH22WfHCSecEPvuu29Mnz49Dj300Dj11FM3GuIvX748brrpprjvvvvivffei2rVqsWSJUuiS5cu8dJLL8Wrr74aDRo0iCOOOCKWLFkSET+9MOvPf/5zlChRIl577bX4xz/+EZdeemme4y5btizatWsXFStWjKlTp8YjjzwSzz33XPTs2TMiItasWRMdOnSI1q1bxzvvvBOvvPJK9OjRI89s9eeffz5q164djRs3zld3kiTx4osvxgcffJBndnTPnj3jlVdeiZEjR8Y777wTJ5xwQhx22GHx8ccfR8RPwXnLli3jqaeeinfffTd69OgRp556arz++utb/D3k5ubGsGHDIiJit912y7PtlltuiZ133jnefPPN6NOnT0RElCtXLoYOHRrvv/9+DBw4MO699964/fbbM/t06tQp/vSnP8XUqVPjjTfeiMsuuyyKFy9eqFpGjBgRV199dVx//fUxc+bMuOGGG6JPnz6Z+jbksssuiwEDBsTMmTOjRYsWcckll8Sj/6+9ew+2qrzvB/w5HAWRy1EMImfkokHAGwiiiCZKlQSVoLTehqKQRK0xeEHUto5GMKYRo2bAkjpqCDQxBmkUrxEEo9goVsBi1aJGaoJJEBUpeNCAHNbvD3+ceuSqwW5W+jwza4b9rne967vX3kvls1/fdffd+ed//uc8++yz6dKlSwYOHJh33nlnk8dfd911qampadg6dOiwTfUC7Ijmz5+fXr16pVevXkmS0aNHp1evXrn66quTfLj02obAe1vdcsstWblyZfr375/27ds3bHfdddd2rx8AAKC0igoaMWJEcfLJJ29y3xlnnFHsv//+Da+TFNOnTy+Koihee+21Ikkxfvz4jcbr1KlTsW7duoa20047rTjjjDM2W8O8efOKJMW7775bFEVRPPbYY0WSYvbs2Q19rrvuuiJJsXjx4oa28847rxg4cOBmxx06dGhx4oknbvSeampqGl4feeSRxbnnntuoz2mnndZw3E033VR07dq1WLt27WbP81GTJ08ukhQtWrRotB1//PENfY455pjiC1/4QsPrdevWFS1atCjOOuushralS5cWSYq5c+cWRfE/12TFihWNzrNw4cIt1lNfX1+0atWqeOCBB4qiKIqZM2cWO+20U/H73/++oc/DDz/c6LO97bbbit13372oq6tr6PPQQw8VTZo0Kd54441i+fLlRZLi8ccf3+x5zz333OKyyy5r9J533nnnokWLFsXOO+9cJCl22WWX4sknnyyKoih++9vfFtXV1Y3qKoqiOO6444orrrhis+cZNGhQcemllzY6z8UXX7zZ/h//fJo0aVI0a9asmDx5cqN+nTp1KoYMGbLZcTa44YYbikMPPbThdatWrYopU6Zs9twf/e6NGTOm6NmzZ8Prz3/+88Wdd97Z6Jhrr7226NevX1EU/3PP/fu//3tRFP/znbj33nsb+tfV1RU777xz8dOf/rShbe3atUVtbW3xve99b5N1/fGPfyxWrlzZsL3++utFkiJZWSSFzWazlWIDAABg+1u5cmWRpFi5cuVW++6wC+gWRbHVtaT79OmzUduBBx6Y6urqhtft27dvtOblggULMnbs2Dz33HNZsWJFwwMulyxZkgMOOKChX48ePRr+3K5du4YlIj7atqVZvIsWLcpf/uVfNmrr169fZsyY0ajPhqUoNjjqqKMyYcKEJMlpp52W8ePHZ999983xxx+fE088MYMHD97iusetWrXaaImQj6/F/NH3Vl1dnT322KPRDPENy5t8dBmXj2vatGmjcZJk2bJlueqqq/L444/nzTffTH19fd57772GWWuLFi1Khw4dUltb2+iafNSiRYvSs2fPhv9Ne8M1Wb9+fV5++eUcffTR+epXv5qBAwfmS1/6UgYMGJDTTz897du3T/Lh9+aBBx7ItGnTGo07bNiwXHnllVmxYkXGjBmTI488MkceeWSSD5dHqa+vT9euXRsds2bNmuyxxx5JPpx1/d3vfjfTpk3L73//+6xduzZr1qzJrrvuutlrtCkf/Xzee++9zJ49O9/4xjeyxx57ZPDgwQ39NvXdvuuuu3LzzTdn8eLFqaury7p169K6deuG/aNHj84555yTn/zkJxkwYEBOO+20fP7zn99qTatXr87ixYtz9tln59xzz21oX7du3VYfNvrROhcvXpwPPvggRx11VEPbzjvvnMMPPzyLFi3a5PHNmjVLs2bNtlojAAAAAGzODhtyL1q0aKsPV/poELrBx5dnqKqqagiyNyyFMXDgwPz0pz9N27Zts2TJkgwcODBr167d7DhVVVVbHPez0qFDh7z88suZPXt2Zs2alW9+85u54YYbMmfOnM0uQ9GkSZN06dJli+Nu6r18/P0m2eL7a968+UY/QowYMSLLly/PhAkT0qlTpzRr1iz9+vXb6Nr+qSZPnpyLLrooM2bMyF133ZWrrroqs2bNyhFHHJFnnnkm69atawiwN6ipqWm4LtOmTUuXLl1yxBFHZMCAAamrq0t1dXUWLFjQ6AeSJGnZsmWS5IYbbsiECRMyfvz4HHzwwWnRokVGjRr1id/bxz+fHj165JFHHsn111/fKOT++Hd77ty5GTZsWK655poMHDgwNTU1mTp1am666aaGPmPHjs1f//Vf56GHHsrDDz+cMWPGZOrUqRv92PJxG9Y7v/3229O3b99G+z5+PT5uU/cgAAAAAPxv2iHX5P7lL3+Z559/Pqeccsp2Hfell17K8uXLM27cuHzxi19M9+7dtzhb+U+x//7759/+7d8atT399NMb9XnyyScbtT355JONZpQ3b948gwcPzs0335zHH388c+fObTQzfUfy5JNP5qKLLsqJJ56YAw88MM2aNcvbb7/dsH///ffP66+/nqVLlza0beqaPPfcc1m9enWjcZs0aZJu3bo1tPXq1StXXHFFnnrqqRx00EG58847kyT33XdfBg0atMVwtmXLlrn44otz2WWXpSiK9OrVK/X19XnzzTfTpUuXRttee+3VUMPJJ5+cM888Mz179sy+++6bV1555U+7YP9fdXX1Vh8g9tRTT6VTp0658sor06dPn+y3336NHra5QdeuXXPJJZfkkUceyV/91V9l8uTJWz1/u3btUltbm//6r//a6P1v7Yemj9rwANWPfqc/+OCDzJs3r9F3GgAAAAC2p4rP5F6zZk3eeOON1NfXZ9myZZkxY0auu+66fOUrX8nw4cO367k6duyYpk2b5h//8R/zjW98Iy+88EKuvfba7XqODS666KIcddRRufHGG3PyySdn5syZjZYqSZLLL788p59+enr16pUBAwbkgQceyD333JPZs2cnSaZMmZL6+vr07ds3u+66a+644440b948nTp12ux5i6LIG2+8sVH7nnvumSZNPtvfNPbbb7/85Cc/SZ8+fbJq1apcfvnljZZKGTBgQLp27ZoRI0bkhhtuyKpVq3LllVc2GmPYsGEZM2ZMRowYkbFjx+att97KhRdemLPOOivt2rXLa6+9lttuuy0nnXRSamtr8/LLL+fXv/51w3fl/vvvz7e//e2t1nreeefl2muvzd13351TTz01w4YNy/Dhw3PTTTelV69eeeutt/Loo4+mR48eGTRoUPbbb7/8/Oc/z1NPPZXdd9893//+97Ns2bJPHN5+9PN5//33M2vWrMycObPhoWRburZLlizJ1KlTc9hhh+Whhx7K9OnTG/a///77ufzyy3Pqqadmn332ye9+97vMmzdvm38ouuaaa3LRRRelpqYmxx9/fNasWZP58+dnxYoVGT169DaN0aJFi5x//vm5/PLL06ZNm3Ts2DHf+9738t577+Xss8/epjEAAAAA4JOq+EzuGTNmpH379uncuXOOP/74PPbYY7n55ptz3333bXWphE+qbdu2mTJlSv7lX/4lBxxwQMaNG5cbb7xxu55jgyOOOCK33357JkyYkJ49e+aRRx7JVVdd1ajPkCFDMmHChNx444058MADc+utt2by5Mnp379/kmS33XbL7bffnqOOOio9evTI7Nmz88ADDzSsE70pq1atSvv27TfaPqsZ6x81adKkrFixIr17985ZZ52Viy66KHvuuWfD/iZNmmT69Ol5//33c/jhh+ecc87JP/zDPzQaY9ddd83MmTPzzjvv5LDDDsupp56a4447LhMnTmzY/9JLL+WUU05J165d8zd/8zcZOXJkzjvvvCxevDivvvpqBg4cuNVa27Rpk+HDh2fs2LFZv359Jk+enOHDh+fSSy9Nt27dMmTIkMybNy8dO3ZMklx11VXp3bt3Bg4cmP79+2evvfbKkCFDPvE1+ujns//+++emm27Kt7/97Y3C/o876aSTcskll+SCCy7IIYcckqeeeirf+ta3GvZXV1dn+fLlGT58eLp27ZrTTz89J5xwQq655pptquucc87JD3/4w0yePDkHH3xwjjnmmEyZMuUTzeROknHjxuWUU07JWWedld69e+fVV1/NzJkzs/vuu3+icQAAAABgW1UVRVFUugjYHr7//e9n9uzZ+cUvflHpUviUVq1a9f8fdrkySeutdQfYIfgvKQAAgO1vQ060cuXKtG695Zyo4jO5YXvZe++9c8UVV1S6DAAAAADgf1HF1+SG7eX000+vdAkAAAAAwP8yM7kBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKa6dKFwDwcStXJq1bV7oKAAAAAMrATG4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACU1k6VLgBgg6IokiSrVq2qcCUAAAAAVNKGfGhDXrQlQm5gh7F8+fIkSYcOHSpcCQAAAAA7gnfffTc1NTVb7CPkBnYYbdq0SZIsWbJkq//wArZu1apV6dChQ15//fW0bt260uVA6bmnYPtyT8H2436C7cs9tWMoiiLvvvtuamtrt9pXyA3sMJo0+fAxATU1Nf4lAttR69at3VOwHbmnYPtyT8H2436C7cs9VXnbOgnSgycBAAAAACgtITcAAAAAAKUl5AZ2GM2aNcuYMWPSrFmzSpcCfxbcU7B9uadg+3JPwfbjfoLtyz1VPlVFURSVLgIAAAAAAD4NM7kBAAAAACgtITcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQG9gh/OAHP0jnzp2zyy67pG/fvnnmmWcqXRKU1hNPPJHBgwentrY2VVVVuffeeytdEpTWddddl8MOOyytWrXKnnvumSFDhuTll1+udFlQWrfcckt69OiR1q1bp3Xr1unXr18efvjhSpcFfzbGjRuXqqqqjBo1qtKlQCmNHTs2VVVVjbbu3btXuiy2gZAbqLi77roro0ePzpgxY/Lss8+mZ8+eGThwYN58881KlwaltHr16vTs2TM/+MEPKl0KlN6cOXMycuTIPP3005k1a1Y++OCDfPnLX87q1asrXRqU0t57751x48ZlwYIFmT9/fo499ticfPLJefHFFytdGpTevHnzcuutt6ZHjx6VLgVK7cADD8zSpUsbtl/96leVLoltUFUURVHpIoD/2/r27ZvDDjssEydOTJKsX78+HTp0yIUXXpi///u/r3B1UG5VVVWZPn16hgwZUulS4M/CW2+9lT333DNz5szJ0UcfXely4M9CmzZtcsMNN+Tss8+udClQWnV1dendu3f+6Z/+Kd/5zndyyCGHZPz48ZUuC0pn7Nixuffee7Nw4cJKl8InZCY3UFFr167NggULMmDAgIa2Jk2aZMCAAZk7d24FKwOAja1cuTLJh6Ec8Kepr6/P1KlTs3r16vTr16/S5UCpjRw5MoMGDWr09yrg0/n1r3+d2tra7Lvvvhk2bFiWLFlS6ZLYBjtVugDg/7a333479fX1adeuXaP2du3a5aWXXqpQVQCwsfXr12fUqFE56qijctBBB1W6HCit559/Pv369csf//jHtGzZMtOnT88BBxxQ6bKgtKZOnZpnn3028+bNq3QpUHp9+/bNlClT0q1btyxdujTXXHNNvvjFL+aFF15Iq1atKl0eWyDkBgCAbTBy5Mi88MIL1mWEP1G3bt2ycOHCrFy5Mj//+c8zYsSIzJkzR9ANn8Lrr7+eiy++OLNmzcouu+xS6XKg9E444YSGP/fo0SN9+/ZNp06dMm3aNMtq7eCE3EBFfe5zn0t1dXWWLVvWqH3ZsmXZa6+9KlQVADR2wQUX5MEHH8wTTzyRvffeu9LlQKk1bdo0Xbp0SZIceuihmTdvXiZMmJBbb721wpVB+SxYsCBvvvlmevfu3dBWX1+fJ554IhMnTsyaNWtSXV1dwQqh3Hbbbbd07do1r776aqVLYSusyQ1UVNOmTXPooYfm0UcfbWhbv359Hn30UWszAlBxRVHkggsuyPTp0/PLX/4y++yzT6VLgj8769evz5o1aypdBpTScccdl+effz4LFy5s2Pr06ZNhw4Zl4cKFAm74E9XV1WXx4sVp3759pUthK8zkBipu9OjRGTFiRPr06ZPDDz8848ePz+rVq/O1r32t0qVBKdXV1TWaafDaa69l4cKFadOmTTp27FjByqB8Ro4cmTvvvDP33XdfWrVqlTfeeCNJUlNTk+bNm1e4OiifK664IieccEI6duyYd999N3feeWcef/zxzJw5s9KlQSm1atVqo+dEtGjRInvssYfnR8CncNlll2Xw4MHp1KlT/vCHP2TMmDGprq7O0KFDK10aWyHkBirujDPOyFtvvZWrr746b7zxRg455JDMmDFjo4dRAttm/vz5+Yu/+IuG16NHj06SjBgxIlOmTKlQVVBOt9xyS5Kkf//+jdonT56cr371q//7BUHJvfnmmxk+fHiWLl2ampqa9OjRIzNnzsyXvvSlSpcGAPnd736XoUOHZvny5Wnbtm2+8IUv5Omnn07btm0rXRpbUVUURVHpIgAAAAAA4NOwJjcAAAAAAKUl5AYAAAAAoLSE3AAAAAAAlJaQGwAAAACA0hJyAwAAAABQWkJuAAAAAABKS8gNAAAAAEBpCbkBAAAAACgtITcAAMBn5De/+U2qqqqycOHCz/xc/fv3z6hRoz7z8wAA7GiE3AAAAFsxd+7cVFdXZ9CgQZ/5ucaOHZuqqqpUVVVlp512SufOnXPJJZekrq5ui8fdc889ufbaaz/z+gAAdjRCbgAAgK2YNGlSLrzwwjzxxBP5wx/+8Jmf78ADD8zSpUvzm9/8Jtdff31uu+22XHrppZvsu3bt2iRJmzZt0qpVq8+8NgCAHY2QGwAAYAvq6upy11135fzzz8+gQYMyZcqURvtXrFiRYcOGpW3btmnevHn222+/TJ48eZNj1dfX5+tf/3q6d++eJUuWbPacO+20U/baa6/svffeOeOMMzJs2LDcf//9ST6c6X3IIYfkhz/8YfbZZ5/ssssuSTZermTNmjX5u7/7u3To0CHNmjVLly5dMmnSpIb9L7zwQk444YS0bNky7dq1y1lnnZW33377U14lAIDKEXIDAABswbRp09K9e/d069YtZ555Zn70ox+lKIqG/d/61rfyn//5n3n44YezaNGi3HLLLfnc5z630Thr1qzJaaedloULF+Zf//Vf07Fjx22uoXnz5g0ztpPk1Vdfzd1335177rlns+t9Dx8+PD/72c9y8803Z9GiRbn11lvTsmXLJMl///d/59hjj02vXr0yf/78zJgxI8uWLcvpp5++zTUBAOwodqp0AQAAADuySZMm5cwzz0ySHH/88Vm5cmXmzJmT/v37J0mWLFmSXr16pU+fPkmSzp07bzRGXV1dBg0alDVr1uSxxx5LTU3NNp9/wYIFufPOO3Psscc2tK1duzY//vGP07Zt200e88orr2TatGmZNWtWBgwYkCTZd999G/ZPnDgxvXr1yne/+92Gth/96Efp0KFDXnnllXTt2nWb6wMAqDQzuQEAADbj5ZdfzjPPPJOhQ4cm+XAZkTPOOKPRsh/nn39+pk6dmkMOOSR/+7d/m6eeemqjcYYOHZrVq1fnkUce2aaA+/nnn0/Lli3TvHnzHH744enXr18mTpzYsL9Tp06bDbiTZOHChamurs4xxxyzyf3PPfdcHnvssbRs2bJh6969e5Jk8eLFW60PAGBHYiY3AADAZkyaNCnr1q1LbW1tQ1tRFGnWrFkmTpyYmpqanHDCCfntb3+bX/ziF5k1a1aOO+64jBw5MjfeeGPDMSeeeGLuuOOOzJ07t9GM7M3p1q1b7r///uy0006pra1N06ZNG+1v0aLFFo9v3rz5FvfX1dVl8ODBuf766zfa1759+63WBwCwIzGTGwAAYBPWrVuXH//4x7npppuycOHChu25555LbW1tfvaznzX0bdu2bUaMGJE77rgj48ePz2233dZorPPPPz/jxo3LSSedlDlz5mz13E2bNk2XLl3SuXPnjQLubXHwwQdn/fr1mz1X79698+KLL6Zz587p0qVLo21rAToAwI5GyA0AALAJDz74YFasWJGzzz47Bx10UKPtlFNOaViy5Oqrr859992XV199NS+++GIefPDB7L///huNd+GFF+Y73/lOvvKVr+RXv/rVZ1p7586dM2LEiHz961/Pvffem9deey2PP/54pk2bliQZOXJk3nnnnQwdOjTz5s3L4sWLM3PmzHzta19LfX39Z1obAMD2JuQGAADYhEmTJmXAgAGbXEP7lFNOyfz58/Mf//Efadq0aa644or06NEjRx99dKqrqzN16tRNjjlq1Khcc801OfHEEze5dvf2dMstt+TUU0/NN7/5zXTv3j3nnntuVq9enSSpra3Nk08+mfr6+nz5y1/OwQcfnFGjRmW33XZLkyb+mggAlEtVURRFpYsAAAAAAIBPw0/0AAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBa/w9AOTIYxo0+3wAAAABJRU5ErkJggg=="/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>4.2 What is the TOP 10 locations BRL has + value?</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [9]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    SELECT </span>
<span class="s2">        name</span>
<span class="s2">        ,round(avg(ask),2) AvgAsk</span>
<span class="s2">    FROM df </span>
<span class="s2">    where codein = 'BRL'</span>
<span class="s2">    and not code in ('BTC', 'ETH', 'LTC')</span>
<span class="s2">    group by name</span>
<span class="s2">    order by avg(ask) limit 10</span>
<span class="s2">"""</span>

<span class="n">newDf</span> <span class="o">=</span> <span class="n">sqldf</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">locals</span><span class="p">())</span>
<span class="n">newDf</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">'AvgAsk'</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="n">AvgAskByCurrency</span> <span class="o">=</span> <span class="n">newDf</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span>
    <span class="n">kind</span><span class="o">=</span><span class="s1">'barh'</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s1">'name'</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">'AvgAsk'</span><span class="p">,</span> 
    <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> 
    <span class="n">legend</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> 
    <span class="n">color</span><span class="o">=</span><span class="s1">'blue'</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s1">'Top 10 Most Valuable Currencies by Ask Price'</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">'Ask Price'</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">'Symbol'</span><span class="p">)</span>


<span class="c1"># Adicionando rótulos aos dados</span>
<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">newDf</span><span class="p">[</span><span class="s1">'AvgAsk'</span><span class="p">]):</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">index</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">))</span>

<span class="c1"># Exibir o gráfico</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,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XLlymjRpksOYtDxXAAD8HczkBgAAwL+CMUbNmjXT+vXr1bVrV1WoUEGrVq3S4MGD9euvvyYLqjZu3Ki5c+cqIiJCbm5umjx5sho1aqStW7eqbNmyD6SmXbt2qVKlSnJycpxbUq1aNX388cc6fPiwgoKC7nueDh06aPjw4dqwYYOeeOIJSX/Niq5fv75y586dbPz+/fv1+OOPy8fHRy+//LKyZMmiqVOnKiQkRBs3blT16tUl/fVSxzFjxqhbt26qVq2a4uPjtX37du3cuVMNGjRQz5499dtvv6XYFiYlXl5eat68uebPn68///xTOXLksO+bO3euEhIS1LFjR0nSvHnzdPXqVfXq1Us5c+bU1q1b9f777+uXX37RvHnz7nuttNi2bZu2bNmiZ555Ro899piOHz+uKVOmKCQkRAcOHEg2q7lv377Kli2bhg8frkOHDmnKlCk6ceKEPdxLSWJiopo1a6Zvv/1WPXr0UGBgoPbu3asJEybo8OHDWrRoUar1HTlyRAcPHtTzzz8vb2/vB3LPdzp//ryefPJJPfPMM3r22WeVJ08e+76oqChdv35dPXr0kJubm3LkyKH9+/erdu3aKlCggIYMGSIvLy99+eWXatGihb766iu1bNnS4fz9+vVT9uzZFRkZqePHj2vixInq27ev5s6dax8zY8YMPf/88ypTpoyGDh2qbNmyadeuXVq5cuU9W7D07NlTM2bMUJcuXRQREaFjx47pgw8+0K5du7R582ZlyZJF586dU8OGDeXn56chQ4YoW7ZsOn78eJrD3iNHjqhdu3Z64YUXFB4erqioKLVp00YrV65UgwYNVLRoUdWuXVvR0dF68cUXHY6Njo6Wt7e3mjdvft/rREdHq1ixYqpatarKli0rT09PffHFFxo8eLB9TEbuJSEhQc8//7zmzp1r/1sd6XXhwgVduHBBxYsXd9g+atQoubq6atCgQbpx40aqs/zXrFmjJk2aKF++fOrfv7/y5s2r2NhYLV26VP3795ekdD9XAABkiAEAAAAsqE+fPubO/5xdtGiRkWTeeOMNh3GtW7c2NpvN/PTTT/Ztkowks337dvu2EydOGHd3d9OyZct01eHl5WXCw8NT3ff8888n275s2TIjyaxcufKe5w4ODjZlypQxxhhTpUoV07VrV2OMMRcuXDCurq5m5syZZv369UaSmTdvnv24Fi1aGFdXV3P06FH7tt9++814e3ubunXr2reVL1/ePPXUU/es4e7P+X6S7m3q1KkO22vUqGEKFChgEhISjDHGXL16NdmxY8aMMTabzZw4ccK+LTIy0uH6x44dM5JMVFRUsuMlmcjISPt6Stf47rvvjCTz2Wef2bdFRUUZSaZy5crm5s2b9u1vv/22kWRiYmLs24KDg01wcLB9fdasWcbJycls2rTJ4TofffSRkWQ2b96crIYkMTExRpKZMGFCqmPulFTnsWPHHLYnPQPr1693qFOS+eijjxzGJn1+Pj4+5ty5cw776tevb4KCgsz169ft2xITE02tWrVMQEBAsjpCQ0NNYmKiffuLL75onJ2dzcWLF40xxly8eNF4e3ub6tWrm2vXrjlc687jwsPDjb+/v31906ZNRpKJjo52OGblypUO2xcuXGgkmW3btqX2kaXK39/fSDJfffWVfVtcXJzJly+fqVixon3b1KlTjSQTGxtr33bz5k2TK1euVH/u73Tz5k2TM2dO8+qrr9q3dejQwZQvX95hXFruJem7e+edd8ytW7dMu3btjIeHh1m1alUa7vivn4+uXbua33//3Zw7d8788MMPpn79+kaSGT9+vDHm/56lokWLJvv5ufs5u337tilSpIjx9/c3Fy5ccBh75/eb1ucKAIC/g3YlAAAA+FdYvny5nJ2dFRER4bD9pZdekjFGK1ascNhes2ZNVa5c2b5eqFAhNW/eXKtWrVJCQsIDqenatWtyc3NLtj2pr+39WnPcqUOHDlqwYIFu3ryp+fPny9nZOcUZkAkJCVq9erVatGihokWL2rfny5dPHTp00Lfffqv4+HhJUrZs2bR//34dOXIkvbeWqqTZqHe2ozh27Ji+//57tW/f3j6r3cPDw77/ypUr+uOPP1SrVi0ZY7Rr164HUsud17h165bOnz+v4sWLK1u2bNq5c2ey8T169HBoGdKrVy+5uLho+fLlqV5j3rx5CgwMVKlSpfTHH3/Yl6QZ9+vXr0/12KTv4WHM4pYkNzc3denSJcV9rVq1kp+fn339zz//1Ndff622bdvq0qVL9vs4f/68wsLCdOTIEf36668O5+jRo4fDDPfHH39cCQkJOnHihKS/ZvleunRJQ4YMSdbL+V5tb+bNmydfX181aNDA4TOtXLmysmbNav9Ms2XLJklaunRphvqW58+f3+Fn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QrLzJP1tgbS0LPntt9+0cOFC+3p8fLw+++wzVahQQXnz5rVvd3FxUfv27fXll19qxowZCgoKUrly5e57/s8//1xFixbVCy+8oNatWzssgwYNUtasWe2z1dN7L6GhoZozZ45Wrlyp55577oH9zYT0qFSpkooUKaKJEycm+/Mh6V4exnMFAEBKmMkNAACAf4WmTZuqXr16evXVV3X8+HGVL19eq1evVkxMjAYMGGAPCJOULVtWYWFhioiIkJubmz0kHTFixH2vtWTJEu3Zs0fSXy80/PHHH/XGG29Ikpo1a2YPwFq3bq0aNWqoS5cuOnDggHLlyqXJkycrISEhTde5m6+vr4YPH37fcW+88YbWrFmjOnXqqHfv3nJxcdHUqVN148YNvf322/ZxpUuXVkhIiCpXrqwcOXJo+/btmj9/vvr27Wsfk/RyzoiICIWFhcnZ2VnPPPPMfWt49tlnNXLkSMXExKh27doOM2NLlSqlYsWKadCgQfr111/l4+Ojr776yt7L+X66deumsWPHqlu3bqpSpYq++eYb+wzcOzVp0kSzZs2Sr6+vSpcure+++05r165Vzpw5UzzvzZs3Vb9+fbVt21aHDh3S5MmTVadOHTVr1izVWp577jl9+eWXeuGFF7R+/XrVrl1bCQkJOnjwoL788kutWrVKVapUSfX4du3aae/evRo9erR27dql9u3by9/fX+fPn9fKlSu1bt06ez/oMmXKqEaNGho6dKj+/PNP5ciRQ3PmzEkxHM+IDz/8UHXq1FFQUJC6d++uokWL6uzZs/ruu+/0yy+/2J/5tPLx8dGECRPUrVs3Va1aVR06dFD27Nm1Z88eXb16VTNnzkzxuODgYPXs2VNjxozR7t271bBhQ2XJkkVHjhzRvHnzNGnSJLVu3VozZ87U5MmT1bJlSxUrVkyXLl3StGnT5OPjc8/Z90lKlCihrl27atu2bcqTJ4+mT5+us2fPKioqKtnYTp066b333tP69ev11ltv3ffcv/32m9avX5/sRbhJ3NzcFBYWpnnz5um9997L0L20aNFCUVFR6tSpk3x8fDR16tT71vUgOTk5acqUKWratKkqVKigLl26KF++fDp48KD279+vVatWSXrwzxUAACkyAAAAgAX16dPH3P2fs5cuXTIvvviiyZ8/v8mSJYsJCAgw77zzjklMTHQYJ8n06dPHfP75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3EyZMiXPPvts+vXrlzfeeGOHHn/ppZemuro6/fv3f58nfX98pCP3aaedVr8Q+6677po2bdrkc5/7XG6++eZs3Lhxi48577zzMmTIkJx22mkf7LBJfvazn6WysjKjR4/+wJ/7nSZNmpTp06eXe4wtev7559O0adPU1NQ0WHS/srIy7dq1y1lnnZXXXnvtA51pU2jetFVVVaVTp0751re+lVKp9L4+d7t27fLiiy/mk5/85Hu+xsKFC3PWWWftxKkAAAAA2FmOO+64nHLKKenRo0cGDBiQu+++O6+//npuv/327T524sSJmTFjRu688840adLkA5h25/vIr8k9cODATJs2LXV1dVm1alXmzp2br371q/n5z3+e2bNnp1Gjhj+iG2+88X2b5a233squu+661eNTp07NJZdckhtuuCHXXnttWV50dXV1qaioSMuWLT/w595Rs2bNymc/+9k0b948yduL7t93332pq6vLsmXLcsYZZ2TNmjWZOXPmBz7bfffdl+7du6e2tjYLFizImWeembZt22bUqFFbPH/9+vWpqqr6p56zsrJyh9dj2prWrVtv8/j2XrsAAAAAfHD22GOPdO7cOcuXL9/meddcc00mTpyY++67Lz169PiAptv5PtJ3cidJ48aNs++++2a//fZLr1698o1vfCOzZs3KPffc0+BO5ZUrV+bEE09M8+bNs/vuu+fUU0/NqlWrtnrdhQsX5nOf+1z23nvvtGzZMkceeWQef/zxBudUVFRkypQpOeGEE9KsWbN8+9vf3ur1nn322TzyyCP5+te/ns6dO+eOO+5ocHz69OnZY489MmfOnHTp0iW77bZbvvCFL+TNN9/Mj3/843Ts2DGtWrXK+eefn7q6uvrH1dbW5mtf+1r222+/NGvWLH369MmDDz642XVnz56dAw88MI0bN87KlSs3W65k48aNufrqq9OpU6c0btw47du3b/D9XHrppencuXN222237L///hk3blzeeuut+uOblvu45ZZb0rFjx7Rs2TL//u//3uBXKmpra3P++ednn332SZMmTfKZz3wmCxcu3OxnNWvWrJxwwgn1X29adH+//fZL//79c8opp2TevHkNHnPTTTelW7duadKkSbp27Zof/vCHDY5vb/4dtddee2XfffdNhw4dMnz48Bx++OENXhebfq7f/va3U11dnS5duiRJbrnllvTu3TstWrTIvvvum//4j//Iyy+/XP+41atXZ/jw4WndunWaNm2aAw44INOmTUuy+XIlW7JgwYL069cvTZs2Tbt27XL++edn3bp19cffuVzJ1l67U6ZMySc+8YlUVVWlS5cuueWWW971zwgAAACAf05NTU1WrFiRtm3bbvWcq6++OldccUXmzp2b3r17f4DT7Xwf+ci9JUcffXQOPvjg+pC8cePGnHjiiXnttdcyf/78zJs3L3/6058ydOjQrV7jjTfeyMiRI7NgwYL89re/zQEHHJBBgwZttg7OhAkTctJJJ2Xp0qU544wztnq9adOmZfDgwWnZsmW++MUvZurUqZud8+abb+b666/PjBkzMnfu3Dz44IM56aSTcvfdd+fuu+/OLbfckhtuuCE///nP6x9z7rnn5tFHH82MGTPy5JNP5pRTTsnAgQPzxz/+scF1r7rqqtx00015+umns88++2z23GPHjs3EiRMzbty4PPPMM7ntttvSpk2b+uMtWrTI9OnT88wzz2TSpEm58cYb873vfa/BNVasWJG77rorc+bMyZw5czJ//vxMnDix/vgll1ySX/ziF/nxj3+cxx9/PJ06dcqAAQMaLD3y+uuvZ8GCBQ0i9z967rnncu+99za4O/rWW2/NZZddlm9/+9tZtmxZrrzyyowbNy4//vGP39X879aiRYuyePHi9OnTp8H++++/P7///e8zb968zJkzJ8nbd0pfccUVeeKJJ3LXXXflueeea7Bkzqaf+z333JNly5ZlypQp2XvvvXdojhUrVmTgwIE5+eST8+STT2bmzJlZsGBBzj333G0+7p2v3TvvvDNf/epXc9FFF+Wpp57K2WefndNPPz0PPPDAVq9RW1ubtWvXNtgAAAAAeHe+9rWvZf78+XnuuefyyCOP5KSTTkplZWWGDRuWJBkxYkTGjh1bf/5VV12VcePG5eabb07Hjh3z0ksv5aWXXkpNTU25voV/TukjbOTIkaUTTzxxi8eGDh1a6tatW6lUKpV+9atflSorK0srV66sP/7000+XkpQee+yxUqlUKo0fP7508MEHb/W56urqSi1atCj98pe/rN+XpDRmzJjtzllXV1dq165d6a677iqVSqXSK6+8Uqqqqir96U9/qj9n2rRppSSl5cuX1+87++yzS7vttlvpjTfeqN83YMCA0tlnn10qlUql559/vlRZWVn685//3OD5jjnmmNLYsWMbXHfJkiUNzvnHn93atWtLjRs3Lt14443b/V42+e53v1s69NBD678eP358abfddiutXbu2ft/FF19c6tOnT6lUKpVqampKu+66a+nWW2+tP75+/fpSdXV16eqrr67fd+utt5Z69+7d4Lq77LJLqVmzZqUmTZqUkpSSlP7rv/6r/pxPfOITpdtuu63BfFdccUWpb9++72r+bf35P/vss6UkpaZNm5aaNWtW2nXXXUtJSmeddVaD80aOHFlq06ZNqba2dqvXKpVKpYULF5aS1P/ZHn/88aXTTz99m8/9v//7v6VSqVR64IEHSklKq1evLpVKpdKoUaM2m+M3v/lNaZdddin97W9/K5VKpVKHDh1K3/ve9+qPb+m1++lPf7r05S9/ucG+U045pTRo0KCtfh/jx4+v/zNpuK0pJSWbzWaz2Ww2m81ms9lsNtt2tlLp7ZbZtm3bUlVVVWm//fYrDR06tEEnPPLII0sjR46s/7pDhw6lLTWZ8ePHb7XjfNDWrFlTSlJas2bNds/9yK/JvTWlUikVFRVJkmXLlqVdu3Zp165d/fEDDzwwe+yxR5YtW5bDDjtss8evWrUq3/zmN/Pggw/m5ZdfTl1dXd58882sXLmywXk78qsA8+bNy7p16zJo0KAkyd57713/AZlXXHFF/Xm77bZbPvGJT9R/3aZNm3Ts2LF+bepN+zYtc7F06dLU1dWlc+fODZ6vtrY2e+21V/3XVVVV21yTZ9myZamtrc0xxxyz1XNmzpyZ66+/PitWrEhNTU02bNiQ3XffvcE5HTt2TIsWLeq/btu2bf2sK1asyFtvvZXDDz+8/viuu+6aT33qU1m2bFn9vncuVZIkXbp0yezZs/P3v/89P/3pT7NkyZKcd955SZJ169ZlxYoVGTVqVL785S/XP2bDhg0N1h3fkfl3xMyZM9OtW7e89dZbeeqpp3LeeeelVatWDe5YP+iggzZbh3vx4sWZMGFCnnjiiaxevbr+g1FXrlyZAw88MOecc05OPvnkPP744zn22GMzZMiQfPrTn96hmZ544ok8+eSTufXWW+v3lUqlbNy4Mc8++2y6deu2xce987W7bNmyzT6c8vDDD8+kSZO2+txjx47NhRdeWP/12rVrG7zPAAAAANi+GTNmbPP4Py5PnLy92sG/EpF7K5YtW5aPf/zj7/nxI0eOzKuvvppJkyalQ4cOady4cfr27Zv169c3OK9Zs2bbvdbUqVPz2muvpWnTpvX7Nm7cmCeffDKXX355dtnl7VVn3vnBfxUVFVvctymQ1tTUpLKyMosXL05lZWWD8/4xjDdt2rQ++G/JP861JY8++miGDx+eyy+/PAMGDEjLli0zY8aMXHvttQ3O29asO2L9+vWZO3duvvGNbzTYX1VVlU6dOiV5+9NiBw8enMsvvzxXXHFF/a9g3HjjjZstG7LpZ7Kj8++Idu3a1c/SrVu3rFixIuPGjcuECRPqP0j0na+JdevWZcCAARkwYEBuvfXWtG7dOitXrsyAAQPqX0/HHXdcnn/++dx9992ZN29ejjnmmIwePTrXXHPNdmeqqanJ2WefnfPPP3+zY+3bt9/q43bktbs9jRs3TuPGjf/p6wAAAADw0SVyb8Gvf/3rLF26NBdccEGSt2PkCy+8kBdeeKH+LtNnnnkmr7/+eg488MAtXuPhhx/OD3/4w/q7r1944YX89a9/fdezvPrqq5k1a1ZmzJiR7t271++vq6vLZz7zmfzqV7/KwIED3/V1k6Rnz56pq6vLyy+/nH79+r2nayTJAQcckKZNm+b+++/PmWeeudnxRx55JB06dMj/+3//r37f888//66eY9OHGT788MPp0KFDkrfXqV64cGHGjBmT5O2/kWrVqlUOPvjgbV7rm9/8Zo4++uicc845qa6uTnV1df70pz9l+PDhWzx/Z8y/NZWVldmwYUPWr19fH7nf6Xe/+11effXVTJw4sf71t2jRos3Oa926dUaOHJmRI0emX79+ufjii3cocvfq1SvPPPNMfXx/r7p165aHH344I0eOrN/38MMPb/U9AgAAAAA7w0c+ctfW1uall15KXV1dVq1alblz5+Y73/lOPv/5z2fEiBFJkv79++eggw7K8OHDc91112XDhg35yle+kiOPPHKry40ccMABueWWW9K7d++sXbs2F1988XbveN6SW265JXvttVdOPfXUze6mHjRoUKZOnfqeI3fnzp0zfPjwjBgxItdee2169uyZV155Jffff3969OiRwYMH79B1mjRpkksvvTSXXHJJqqqqcvjhh+eVV17J008/nVGjRuWAAw7IypUrM2PGjBx22GH5n//5n9x5553vatZmzZrlnHPOycUXX5w999wz7du3z9VX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dVe5R4LC+s53vpPDDjssLVq0yD777JMhQ4bk97//fbnHgsKaMmVKevTokd133z277757+vbtm3vuuafcY8G/jIkTJ6aioiJjxowp9yhQSBMmTEhFRUWDrWvXruUeix0gcgNlN3PmzFx44YUZP358Hn/88Rx88MEZMGBAXn755XKPBoW0bt26HHzwwfnBD35Q7lGg8ObPn5/Ro0fnt7/9bebNm5e33norxx57bNatW1fu0aCQPvaxj2XixIlZvHhxFi1alKOPPjonnnhinn766XKPBoW3cOHC3HDDDenRo0e5R4FC6969e1588cX6bcGCBeUeiR1QUSqVSuUeAvho69OnTw477LBMnjw5SbJx48a0a9cu5513Xr7+9a+XeTootoqKitx5550ZMmRIuUeBfwmvvPJK9tlnn8yfPz9HHHFEuceBfwl77rlnvvvd72bUqFHlHgUKq6amJr169coPf/jDfOtb38ohhxyS6667rtxjQeFMmDAhd911V5YsWVLuUXiX3MkNlNX69euzePHi9O/fv37fLrvskv79++fRRx8t42QAsLk1a9YkeTvKAf+curq6zJgxI+vWrUvfvn3LPQ4U2ujRozN48OAG/18FvDd//OMfU11dnf333z/Dhw/PypUryz0SO6BRuQcAPtr++te/pq6uLm3atGmwv02bNvnd735XpqkAYHMbN27MmDFjcvjhh+eTn/xkuceBwlq6dGn69u2bv//972nevHnuvPPOHHjggeUeCwprxowZefzxx7Nw4cJyjwKF16dPn0yfPj1dunTJiy++mMsvvzz9+vXLU089lRYtWpR7PLZB5AYAgB0wevToPPXUU9ZlhH9Sly5dsmTJkqxZsyY///nPM3LkyMyfP1/ohvfghRdeyFe/+tXMmzcvTZo0Kfc4UHjHHXdc/T/36NEjffr0SYcOHXL77bdbVutDTuQGymrvvfdOZWVlVq1a1WD/qlWrsu+++5ZpKgBo6Nxzz82cOXPy0EMP5WMf+1i5x4FCq6qqSqdOnZIkhx56aBYuXJhJkyblhhtuKPNkUDyLFy/Oyy+/nF69etXvq6ury0MPPZTJkyentrY2lZWVZZwQim2PPfZI586ds3z58nKPwnZYkxsoq6qqqhx66KG5//776/dt3Lgx999/v7UZASi7UqmUc889N3feeWd+/etf5+Mf/3i5R4J/ORs3bkxtbW25x4BCOuaYY7J06dIsWbKkfuvdu3eGDx+eJUuWCNzwT6qpqcmKFSvStm3bco/CdriTGyi7Cy+8MCNHjkzv3r3zqU99Ktddd13WrVuX008/vdyjQSHV1NQ0uNPg2WefzZIlS7Lnnnumffv2ZZwMimf06NG57bbbMmvWrLRo0SIvvfRSkqRly5Zp2rRpmaeD4hk7dmyOO+64tG/fPm+88UZuu+22PPjgg7n33nvLPRoUUosWLTb7nIhmzZplr7328vkR8B587Wtfy/HHH58OHTrkL3/5S8aPH5/KysoMGzas3KOxHSI3UHZDhw7NK6+8kssuuywvvfRSDjnkkMydO3ezD6MEdsyiRYvy2c9+tv7rCy+8MEkycuTITJ8+vUxTQTFNmTIlSXLUUUc12D9t2rScdtppH/xAUHAvv/xyRowYkRdffDEtW7ZMjx49cu+99+Zzn/tcuUcDgPzf//1fhg0blldffTWtW7fOZz7zmfz2t79N69atyz0a21FRKpVK5R4CAAAAAADeC2tyAwAAAABQWCI3AAAAAACFJXIDAAAAAFBYIjcAAAAAAIUlcgMAAAAAUFgiNwAAAAAAhSVyAwAAAABQWCI3AAAAAACFJXIDAAC8T5577rlUVFRkyZIl7/tzHXXUURkzZsz7/jwAAB82IjcAAMB2PProo6msrMzgwYPf9+eaMGFCKioqUlFRkUaNGqVjx4654IILUlNTs83H3XHHHbniiive9/kAAD5sRG4AAIDtmDp1as4777w89NBD+ctf/vK+P1/37t3z4osv5rnnnstVV12VH/3oR7nooou2eO769euTJHvuuWdatGjxvs8GAPBhI3IDAABsQ01NTWbOnJlzzjkngwcPzvTp0xscX716dYYPH57WrVunadOmOeCAAzJt2rQtXquuri5nnHFGunbtmpUrV271ORs1apR99903H/vYxzJ06NAMHz48s2fPTvL2nd6HHHJIbrrppnz84x9PkyZNkmy+XEltbW0uvfTStGvXLo0bN06nTp0yderU+uNPPfVUjjvuuDRv3jxt2rTJl770pfz1r399jz8lAIDyEbkBAAC24fbbb0/Xrl3TpUuXfPGLX8zNN9+cUqlUf3zcuHF55plncs8992TZsmWZMmVK9t57782uU1tbm1NOOSVLlizJb37zm7Rv336HZ2jatGn9HdtJsnz58vziF7/IHXfcsdX1vkeMGJGf/exnuf7667Ns2bLccMMNad68eZLk9ddfz9FHH52ePXtm0aJFmTt3blatWpVTTz11h2cCAPiwaFTuAQAAAD7Mpk6dmi9+8YtJkoEDB2bNmjWZP39+jjrqqCTJypUr07Nnz/Tu3TtJ0rFjx82uUVNTk8GDB6e2tjYPPPBAWrZsucPPv3jx4tx22205+uij6/etX78+P/nJT9K6destPuYPf/hDbr/99sybNy/9+/dPkuy///71xydPnpyePXvmyiuvrN938803p127dvnDH/6Qzp077/B8AADl5k5uAACArfj973+fxx57LMOGDUvy9jIiQ4cObbDsxznnnJMZM2bkkEMOySWXXJJHHnlks+sMGzYs69aty69+9asdCtxLly5N8+bN07Rp03zqU59K3759M3ny5PrjHTp02GrgTpIlS5aksrIyRx555BaPP/HEE3nggQfSvHnz+q1r165JkhUrVmx3PgCADxN3cgMAAGzF1KlTs2HDhlRXV9fvK5VKady4cSZPnpyWLVvmuOOOy/PPP5+777478+bNyzHHHJPRo0fnmmuuqX/MoEGD8tOf/jSPPvpogzuyt6ZLly6ZPXt2GjVqlOrq6lRVVTU43qxZs20+vmnTpts8XlNTk+OPPz5XXXXVZsfatm273fkAAD5M3MkNAACwBRs2bMhPfvKTXHvttVmyZEn99sQTT6S6ujo/+9nP6s9t3bp1Ro4cmZ/+9Ke57rrr8qMf/ajBtc4555xMnDgxJ5xwQubPn7/d566qqkqnTp3SsWPHzQL3jjjooIOycePGrT5Xr1698vTTT6djx47p1KlTg217AR0A4MNG5AYAANiCOXPmZPXq1Rk1alQ++clPNthOPvnk+iVLLrvsssyaNSvLly/P008/nTlz5qRbt26bXe+8887Lt771rXz+85/PggUL3tfZO3bsmJEjR+aMM87IXXfdlWeffTYPPvhgbr/99iTJ6NGj89prr2XYsGFZuHBhVqxYkXvvvTenn3566urq3tfZAAB2NpEbAABgC6ZOnZr+/ftvcQ3tk08+OYsWLcqTTz6ZqqqqjB07Nj169MgRRxyRysrKzJgxY4vXHDNmTC6//PIMGjRoi2t370xTpkzJF77whXzlK19J165d8+Uvfznr1q1LklRXV+fhhx9OXV1djj322Bx00EEZM2ZM9thjj+yyi/9NBACKpaJUKpXKPQQAAAAAALwX/ooeAAAAAIDCErkBAAAAACgskRsAAAAAgMISuQEAAAAAKCyRGwAAAACAwhK5AQAAAAAoLJEbAAAAAIDCErkBAAAAACgskRsAAAAAgMISuQEAAAAAKCyRGwAAAACAwvr/AGFwzm11M+7HAAAAAElFTkSuQmCC"/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>4.3 What the top 10 like BRL in value?</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [10]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    SELECT </span>
<span class="s2">        name</span>
<span class="s2">        ,round(avg(ask),2) AvgAsk</span>
<span class="s2">    FROM df </span>
<span class="s2">    where codein = 'BRL'</span>
<span class="s2">    and not code in ('BTC', 'ETH', 'LTC', 'DOGE')</span>
<span class="s2">    and ask &gt;=1</span>
<span class="s2">    group by name</span>
<span class="s2">    order by avg(ask) desc limit 5</span>
<span class="s2">"""</span>

<span class="n">newDf</span> <span class="o">=</span> <span class="n">sqldf</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">locals</span><span class="p">())</span>
<span class="n">newDf</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">'AvgAsk'</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="n">AvgAskByCurrency</span> <span class="o">=</span> <span class="n">newDf</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span>
    <span class="n">kind</span><span class="o">=</span><span class="s1">'barh'</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s1">'name'</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">'AvgAsk'</span><span class="p">,</span> 
    <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> 
    <span class="n">legend</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> 
    <span class="n">color</span><span class="o">=</span><span class="s1">'blue'</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s1">'Top 10 Most Valuable Currencies by Ask Price'</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">'Ask Price'</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">'Symbol'</span><span class="p">)</span>


<span class="c1"># Adicionando rótulos aos dados</span>
<span class="k">for</span> <span class="n">index</span><span class="p">,</span> <span class="n">value</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">newDf</span><span class="p">[</span><span class="s1">'AvgAsk'</span><span class="p">]):</span>
    <span class="n">plt</span><span class="o">.</span><span class="n">text</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">index</span><span class="p">,</span> <span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">))</span>

<span class="c1"># Exibir o gráfico</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABbkAAANXCAYAAAAYXFJxAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAACC8ElEQVR4nOzdZ7QW5dk24HPTO4J0g6gIiAbsFRVUFBuWRLFFwIgYo2KJJho1oMZoLFFTNEYTMAZFxYIVRAPGLtZYsCGWGFsQARsozPfDj/26pW0QxUmOY61ZK8/MPTPXzDOb1/fc976moiiKIgAAAAAAUEI1VnQBAAAAAACwrITcAAAAAACUlpAbAAAAAIDSEnIDAAAAAFBaQm4AAAAAAEpLyA0AAAAAQGkJuQEAAAAAKC0hNwAAAAAApSXkBgAAAACgtITcAADAt9awYcNSUVHxtZ5jxIgRqaioyCOPPLLEsb169UqvXr2+1nr+1wwcODCrrbbaN3rO1VZbLbvuuus3es6v6pVXXklFRUXOPffcFXL+iRMnpqKiIhMnTlwh5weAxRFyAwBQChUVFdVavokA5uKLL87ee++dVVddNRUVFRk4cOAix77//vsZPHhwWrZsmYYNG2abbbbJY489Vq3z9OrVKxUVFenUqdNCt48fP77yukePHr0sl7JEt912W4YNG7bEce+8805q1aqVH/zgB4scM2vWrNSvXz/f+973lmOF/x0mTpyY733ve2nTpk3q1KmTVq1apW/fvrn++utXdGksB5MnT05FRUXq1auX999/f4XU8MV/J2vUqJF27dplhx12EFoD8F+h1oouAAAAquOKK66o8vmvf/1rxo8fv8D6rl27fu21/PrXv86sWbOyySab5M0331zkuHnz5mWXXXbJk08+meOPPz4tWrTIRRddlF69euXRRx9dZHj9RfXq1ctLL72Uhx9+OJtsskmVbSNHjky9evXyySeffOVrWpTbbrstf/jDH5YYdLdq1Srbb799xowZk48++igNGjRYYMz111+fTz75ZLFB+P+ioUOH5rTTTkunTp1y6KGHpkOHDpk2bVpuu+22fP/738/IkSOz//77r+gyvzaXXnpp5s2bt6LL+Fr97W9/S5s2bTJ9+vSMHj06gwYNWiF1bL/99unfv3+KosjUqVNz0UUXZdttt82tt96anXbaabH7br311vn4449Tp06db6haAKg+ITcAAKXw5WD0wQcfzPjx41dIYHr33XdXzuJu1KjRIseNHj06999/f6699trstddeSZJ+/fqlc+fOGTp0aK688solnqtjx4757LPPctVVV1UJuT/55JPccMMN2WWXXXLdddd99YtaDg444ICMHTs2N910U/bdd98Ftl955ZVp2rRpdtlllxVQ3bfT6NGjc9ppp2WvvfbKlVdemdq1a1duO/744zNu3Lh8+umny+Vci/rlw2effZZ58+atsPDyi9f836goilx55ZXZf//9M3Xq1IwcOXKFhdydO3eu8m/mnnvume7du+eCCy5YZMj9ySefpE6dOqlRo0bq1av3TZUKAEtFuxIAAP5rfPjhh/nJT36S9u3bp27duunSpUvOPffcFEVRZVxFRUWOOOKIjBw5Ml26dEm9evWy4YYb5h//+Ee1ztOhQ4dq9YkePXp0WrduXaU9R8uWLdOvX7+MGTMms2fPrtb59ttvv1x99dVVZrvefPPN+eijj9KvX7+F7vP4449np512SpMmTdKoUaNst912efDBB6uM+fTTT3PqqaemU6dOqVevXlZeeeVsueWWGT9+fJLPeyX/4Q9/SFK11cGi7LnnnmnYsOFCw/t33nknd911V/baa6/UrVs399xzT2XLl7p166Z9+/Y55phj8vHHHy/2XszvSzxixIgFtlVUVFSZcf7qq6/mxz/+cbp06ZL69etn5ZVXzt57751XXnllocf+6KOPcuihh2bllVdOkyZN0r9//0yfPn2x9STJ7NmzM3To0Ky55pqV1/LTn/60Wt/vKaeckubNm+cvf/nLQsPePn36VPaOnt87/Mv1L6xXcq9evfLd7343jz76aLbeeus0aNAgP//5z6v0db7gggvSsWPH1K1bN88++2yS5Lnnnstee+2V5s2bp169etloo41y0003VTnf/Druu+++HHvssZWtePbcc8+8++67C1zD7bffnp49e6Zx48Zp0qRJNt544yrPyMJ6cs+bNy8XXHBB1llnndSrVy+tW7fOoYceusD38cgjj6RPnz5p0aJF6tevn9VXXz0//OEPl3jf57vjjjuy3nrrpV69ell77bWrtId5+eWXU1FRkfPPP3+B/e6///5UVFTkqquuWuI57rvvvrzyyivZd999s+++++Yf//hH/vWvfy0wblmupSiKDB48OHXq1Fmm1jbdunVLixYtMnXq1CT/9yyNGjUqJ598clZZZZU0aNAgM2fOXGRP7oceeig777xzmjVrloYNG6Z79+658MILq4ypznMFAF+FmdwAAPxXKIoiu+22WyZMmJCDDz446623XsaNG5fjjz8+b7zxxgJB1d13352rr746Q4YMSd26dXPRRRdlxx13zMMPP5zvfve7y6Wmxx9/PBtssEFq1Kg6t2STTTbJn/70p7zwwgvp1q3bEo+z//77Z9iwYZk4cWK23XbbJJ/Pit5uu+3SqlWrBcY/88wz2WqrrdKkSZP89Kc/Te3atXPJJZekV69eufvuu7Ppppsm+fyljmeeeWYGDRqUTTbZJDNnzswjjzySxx57LNtvv30OPfTQ/Pvf/15oW5iFadiwYXbfffeMHj067733Xpo3b1657eqrr87cuXNzwAEHJEmuvfbafPTRRznssMOy8sor5+GHH87vfve7/Otf/8q11167xHNVx6RJk3L//fdn3333zXe+85288sorufjii9OrV688++yzC8xqPuKII7LSSitl2LBhef7553PxxRfn1VdfrQz3FmbevHnZbbfdcu+992bw4MHp2rVrnnrqqZx//vl54YUXcuONNy6yvhdffDHPPfdcfvjDH6Zx48bL5Zq/aNq0adlpp52y77775gc/+EFat25duW348OH55JNPMnjw4NStWzfNmzfPM888kx49emSVVVbJCSeckIYNG+aaa67JHnvskeuuuy577rlnleMfeeSRadasWYYOHZpXXnklF1xwQY444ohcffXVlWNGjBiRH/7wh1lnnXVy4oknZqWVVsrjjz+esWPHLrYFy6GHHpoRI0bkoIMOypAhQzJ16tT8/ve/z+OPP5777rsvtWvXzjvvvJMddtghLVu2zAknnJCVVlopr7zySrXD3hdffDH77LNPfvSjH2XAgAEZPnx49t5774wdOzbbb7991lhjjfTo0SMjR47MMcccU2XfkSNHpnHjxtl9992XeJ6RI0emY8eO2XjjjfPd7343DRo0yFVXXZXjjz++csyyXMvcuXPzwx/+MFdffXXlX3UsrenTp2f69OlZc801q6w//fTTU6dOnRx33HGZPXv2Imf5jx8/Prvuumvatm2bo446Km3atMnkyZNzyy235KijjkqSpX6uAGCZFAAAUEKHH3548cX/nL3xxhuLJMUvf/nLKuP22muvoqKionjppZcq1yUpkhSPPPJI5bpXX321qFevXrHnnnsuVR0NGzYsBgwYsMhtP/zhDxdYf+uttxZJirFjxy722D179izWWWedoiiKYqONNioOPvjgoiiKYvr06UWdOnWKyy+/vJgwYUKRpLj22msr99tjjz2KOnXqFFOmTKlc9+9//7to3LhxsfXWW1euW3fddYtddtllsTV8+T4vyfxru+SSS6qs32yzzYpVVlmlmDt3blEURfHRRx8tsO+ZZ55ZVFRUFK+++mrluqFDh1Y5/9SpU4skxfDhwxfYP0kxdOjQys8LO8cDDzxQJCn++te/Vq4bPnx4kaTYcMMNizlz5lSuP/vss4skxZgxYyrX9ezZs+jZs2fl5yuuuKKoUaNGcc8991Q5zx//+MciSXHfffctUMN8Y8aMKZIU559//iLHfNH8OqdOnVpl/fxnYMKECVXqTFL88Y9/rDJ2/v1r0qRJ8c4771TZtt122xXdunUrPvnkk8p18+bNK7bYYouiU6dOC9TRu3fvYt68eZXrjznmmKJmzZrF+++/XxRFUbz//vtF48aNi0033bT4+OOPq5zri/sNGDCg6NChQ+Xne+65p0hSjBw5sso+Y8eOrbL+hhtuKJIUkyZNWtQtW6QOHToUSYrrrruuct2MGTOKtm3bFuuvv37luksuuaRIUkyePLly3Zw5c4oWLVos8uf+i+bMmVOsvPLKxUknnVS5bv/99y/WXXfdKuOqcy3zv7tzzjmn+PTTT4t99tmnqF+/fjFu3LhqXPHnPx8HH3xw8e677xbvvPNO8dBDDxXbbbddkaQ477zziqL4v2dpjTXWWODn58vP2WeffVasvvrqRYcOHYrp06dXGfvF77e6zxUAfBXalQAA8F/htttuS82aNTNkyJAq63/yk5+kKIrcfvvtVdZvvvnm2XDDDSs/r7rqqtl9990zbty4zJ07d7nU9PHHH6du3boLrJ/f13ZJrTm+aP/998/111+fOXPmZPTo0alZs+ZCZ0DOnTs3d9xxR/bYY4+sscYalevbtm2b/fffP/fee29mzpyZJFlppZXyzDPP5MUXX1zaS1uk+bNRv9iOYurUqXnwwQez3377Vc5qr1+/fuX2Dz/8MP/5z3+yxRZbpCiKPP7448ulli+e49NPP820adOy5pprZqWVVspjjz22wPjBgwdXaRly2GGHpVatWrntttsWeY5rr702Xbt2zVprrZX//Oc/lcv8GfcTJkxY5L7zv4evYxZ3ktStWzcHHXTQQrd9//vfT8uWLSs/v/fee/n73/+efv36ZdasWZXXMW3atPTp0ycvvvhi3njjjSrHGDx4cJUZ7ltttVXmzp2bV199Ncnns3xnzZqVE044YYFezotre3PttdemadOm2X777avc0w033DCNGjWqvKcrrbRSkuSWW25Zpr7l7dq1q/IzNL9FzeOPP5633noryec99OvVq5eRI0dWjhs3blz+85//VOt9ALfffnumTZuW/fbbr3LdfvvtlyeffDLPPPNM5bqluZY5c+Zk7733zi233JLbbrstO+ywQ7WuN0n+/Oc/p2XLlmnVqlU23XTTypYzRx99dJVxAwYMqPLzszCPP/54pk6dmqOPPrqy/vnmf7/L8lwBwLIQcgMA8F/h1VdfTbt27RYIDLt27Vq5/Ys6deq0wDE6d+6cjz76aKF9hZdF/fr1F9qX+ZNPPqncXl377rtvZsyYkdtvvz0jR47MrrvuutBw9N13381HH32ULl26LLCta9eumTdvXl5//fUkyWmnnZb3338/nTt3Trdu3XL88cfnn//8Z7VrWphatWpln332yT333FMZXs0PvOe3KkmS1157LQMHDkzz5s3TqFGjtGzZMj179kySzJgx4yvVMN/HH3+cX/ziF5U92lu0aJGWLVvm/fffX+g5vvxMNGrUKG3btl1kD+/k85YXzzzzTFq2bFll6dy5c5LP21AsSpMmTZIks2bNWoarW7JVVlllkW0mVl999SqfX3rppRRFkVNOOWWBaxk6dGiSBa9l1VVXrfK5WbNmSVLZN3vKlClJstTtf1588cXMmDEjrVq1WqCWDz74oLKOnj175vvf/35OPfXUtGjRIrvvvnuGDx9e7V73a6655gJh+/zvbf53vtJKK6Vv375VfmkzcuTIrLLKKpW/yFicv/3tb1l99dVTt27dvPTSS3nppZfSsWPHNGjQoEpwvjTXcuaZZ+bGG2/M6NGj06tXr2pd63y77757xo8fnzvvvDMPPfRQ/vOf/+S8885boKXSl5+PhanO97sszxUALAs9uQEA4GvStm3bvPnmmwusn7+uXbt2S3WsXr165bzzzst9992X66677ivXt/XWW2fKlCkZM2ZM7rjjjlx22WU5//zz88c//jGDBg1a5uP+4Ac/yO9///tcddVVOe6443LVVVdl7bXXznrrrZfk89nm22+/fd5777387Gc/y1prrZWGDRvmjTfeyMCBA6u8YPPLFjUDeGGz74888sgMHz48Rx99dDbffPM0bdo0FRUV2XfffRd7jqUxb968dOvWLb/5zW8Wur19+/aL3HettdZKkjz11FPVOtfSXHuy+F+ifHnb/Ptx3HHHpU+fPgvd58t9m2vWrLnQccWXXvS6tObNm5dWrVpVCYG/aP4M9IqKiowePToPPvhgbr755owbNy4//OEPc9555+XBBx9Mo0aNvlId8/Xv3z/XXntt7r///nTr1i033XRTfvzjHy8QDH/ZzJkzc/PNN+eTTz5Z6C/VrrzyypxxxhmVL3St7rX06dMnY8eOzdlnn51evXotMEt+cb7zne+kd+/eSxy3NL+AW5xlea4AYFkIuQEA+K/QoUOH3HnnnZk1a1aVGc7PPfdc5fYvWliLjhdeeCENGjSo0sbhq1hvvfVyzz33ZN68eVUCsYceeigNGjSonDVaXfvvv38GDRqUlVZaKTvvvPNCx7Rs2TINGjTI888/v8C25557LjVq1KgSvDZv3jwHHXRQDjrooHzwwQfZeuutM2zYsMqQe3FtJRZl0003TceOHXPllVdm++23zzPPPJMzzjijcvtTTz2VF154IZdffnn69+9fuX78+PFLPPb82cLvv/9+lfVfnqmfJKNHj86AAQNy3nnnVa775JNPFth3vhdffDHbbLNN5ecPPvggb7755iLvdZJ07NgxTz75ZLbbbrulvledO3dOly5dMmbMmFx44YVLDGWX5tqX1vzWNrVr165WCFodHTt2TJI8/fTTSxVkduzYMXfeeWd69OhRrbB1s802y2abbZYzzjgjV155ZQ444ICMGjVqib+omT/L+Ivf2wsvvJAkWW211SrX7bjjjmnZsmVGjhyZTTfdNB999FEOPPDAJdZ1/fXX55NPPsnFF1+cFi1aVNn2/PPP5+STT859992XLbfccqmuZbPNNsuPfvSj7Lrrrtl7771zww03pFatb/7/tf/i97uoZ+breK4AYGG0KwEA4L/CzjvvnLlz5+b3v/99lfXnn39+KioqstNOO1VZ/8ADD1Tpy/z6669nzJgx2WGHHRY5Q3Vp7bXXXnn77bdz/fXXV677z3/+k2uvvTZ9+/ZdaL/uJR1v6NChueiiixbZhqJmzZrZYYcdMmbMmCptNt5+++1ceeWV2XLLLSvbZEybNq3Kvo0aNcqaa65ZpUVCw4YNkywYrC7JAQcckMcffzxDhw5NRUVF9t9//yo1JlVn/BZFkQsvvHCJx23SpElatGiRf/zjH1XWX3TRRQuMrVmz5gKzin/3u98tcubzn/70pyr9kC+++OJ89tlnCzw7X9SvX7+88cYbufTSSxfY9vHHH+fDDz9c7PWceuqpmTZtWgYNGpTPPvtsge133HFHbrnlliT/Fyp+8drnzp2bP/3pT4s9R3W0atUqvXr1yiWXXLLQvz5YlhY+O+ywQxo3bpwzzzyzskXPfIub7d2vX7/MnTs3p59++gLbPvvss8pncfr06QscZ/5fC1SnZcm///3v3HDDDZWfZ86cmb/+9a9Zb7310qZNm8r1tWrVyn777ZdrrrkmI0aMSLdu3dK9e/clHv9vf/tb1lhjjfzoRz/KXnvtVWU57rjj0qhRo8rZ6kt7Lb17986oUaMyduzYHHjggcvtLxOWxgYbbJDVV189F1xwwQL/Psy/lq/juQKAhTGTGwCA/wp9+/bNNttsk5NOOimvvPJK1l133dxxxx0ZM2ZMjj766MqAcL7vfve76dOnT4YMGZK6detWhqSnnnrqEs91880358knn0zy+QsN//nPf+aXv/xlkmS33XarDMD22muvbLbZZjnooIPy7LPPpkWLFrnooosyd+7cap3ny5o2bZphw4Ytcdwvf/nLjB8/PltuuWV+/OMfp1atWrnkkksye/bsnH322ZXj1l577fTq1SsbbrhhmjdvnkceeSSjR4/OEUccUTlm/ss5hwwZkj59+qRmzZrZd999l1jDD37wg5x22mkZM2ZMevToUWVm7FprrZWOHTvmuOOOyxtvvJEmTZrkuuuuq+zlvCSDBg3KWWedlUGDBmWjjTbKP/7xj8oZuF+066675oorrkjTpk2z9tpr54EHHsidd96ZlVdeeaHHnTNnTrbbbrv069cvzz//fC666KJsueWW2W233RZZy4EHHphrrrkmP/rRjzJhwoT06NEjc+fOzXPPPZdrrrkm48aNy0YbbbTI/ffZZ5889dRTOeOMM/L4449nv/32S4cOHTJt2rSMHTs2d911V2U/6HXWWSebbbZZTjzxxLz33ntp3rx5Ro0atdBwfFn84Q9/yJZbbplu3brlkEMOyRprrJG33347DzzwQP71r39VPvPV1aRJk5x//vkZNGhQNt544+y///5p1qxZnnzyyXz00Ue5/PLLF7pfz549c+ihh+bMM8/ME088kR122CG1a9fOiy++mGuvvTYXXnhh9tprr1x++eW56KKLsueee6Zjx46ZNWtWLr300jRp0mSxs+/n69y5cw4++OBMmjQprVu3zl/+8pe8/fbbGT58+AJj+/fvn9/+9reZMGFCfv3rXy/x2P/+978zYcKEBV6EO1/dunXTp0+fXHvttfntb3+7TNeyxx57ZPjw4enfv3+aNGmSSy65ZIl1LU81atTIxRdfnL59+2a99dbLQQcdlLZt2+a5557LM888k3HjxiVZ/s8VACxUAQAAJXT44YcXX/7P2VmzZhXHHHNM0a5du6J27dpFp06dinPOOaeYN29elXFJisMPP7z429/+VnTq1KmoW7dusf766xcTJkyo1rkHDBhQJFnoMnz48Cpj33vvveLggw8uVl555aJBgwZFz549i0mTJlXrPD179izWWWedxY6ZMGFCkaS49tprq6x/7LHHij59+hSNGjUqGjRoUGyzzTbF/fffX2XML3/5y2KTTTYpVlpppaJ+/frFWmutVZxxxhnFnDlzKsd89tlnxZFHHlm0bNmyqKioWOCeL87GG29cJCkuuuiiBbY9++yzRe/evYtGjRoVLVq0KA455JDiySefXOAeDh06dIFzfvTRR8XBBx9cNG3atGjcuHHRr1+/4p133imSFEOHDq0cN3369OKggw4qWrRoUTRq1Kjo06dP8dxzzxUdOnQoBgwYUDlu+PDhRZLi7rvvLgYPHlw0a9asaNSoUXHAAQcU06ZNq3Lunj17Fj179qyybs6cOcWvf/3rYp111inq1q1bNGvWrNhwww2LU089tZgxY0a17tVdd91V7L777kWrVq2KWrVqFS1btiz69u1bjBkzpsq4KVOmFL179y7q1q1btG7duvj5z39ejB8/vkhS5fld1LMzderUIklxzjnnLLSOKVOmFP379y/atGlT1K5du1hllVWKXXfdtRg9evQC9+vLz/H8Z/HLP0c33XRTscUWWxT169cvmjRpUmyyySbFVVddVbl9wIABRYcOHRao5U9/+lOx4YYbFvXr1y8aN25cdOvWrfjpT39a/Pvf/y6K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AgAAlENpZnJX5wVOAwcOrNafBa8oI0aMyEorrbSiy1hqEydOTEVFRd5///2v5fhL+3Kub6tevXrl6KOPXtFlLNSXn71hw4Yt8HKzxXnllVdSUVGx2D+hB6D65s6dm/333z+nnnpqOnfuXK19Dj/88Dz99NMZNWrU11wdAABAuazQkHvgwIGpqKhIRUVFateundatW2f77bfPX/7yl8ybN6/K2DfffDM77bTTCqq0HEaMGFF5P7+41KtX7ysdd4sttsibb775/3sll8Pll1+eLbfcMsnn4fMX70Xnzp1z5pln5ptuR//l76dRo0bZcMMNc/3113/t595nn33ywgsvLPP+7du3z5tvvmnmIMByMmvWrDzyyCM54ogjUqtWrdSqVSunnXZannzyydSqVSt///vfq4w/4ogjcsstt2TChAn5zne+s4KqBgAA+HZa4e1KdtxxxwwfPjxz587N22+/nbFjx+aoo47K6NGjc9NNN1X++W6bNm0We5xPP/30myj3W69JkyZ5/vnnq6yrqKj4SsesU6fOYu//3LlzU1FRkRo1vj1/GDBmzJjstttulZ8POeSQnHbaaZk9e3b+/ve/Z/DgwVlppZVy2GGHfaN1ffH7mTVrVoYPH55+/frlmWeeSZcuXRa6z5w5c1KnTp2vdN769eunfv36y7x/zZo1F/sMFEWRuXPnVuvP7QH4/P8ePPXUU1XWXXTRRfn73/+e0aNHZ/XVV0/y+b+vRx55ZG644YZMnDixcj0AAAD/Z4WnknXr1k2bNm2yyiqrZIMNNsjPf/7zjBkzJrfffntGjBhROe6LLS3mt064+uqr07Nnz9SrVy8jR46sHHvuueembdu2WXnllXP44YdXCcCvuOKKbLTRRmncuHHatGmT/fffP++8807l9vmtOcaNG5f1118/9evXz7bbbpt33nknt99+e7p27ZomTZpk//33z0cffbTYaxsxYkRWXXXVNGjQIHvuuWemTZu2wJiLL744HTt2TJ06ddKlS5dcccUVlduKosiwYcOy6qqrpm7dumnXrl2GDBmy2HNWVFSkTZs2VZbWrVtXbu/Vq1eOPPLIHH300WnWrFlat26dSy+9NB9++GEOOuigNG7cOGuuuWZuv/32Be7J/HYl81tf3HTTTVl77bVTt27dvPbaa5k0aVK23377tGjRIk2bNk3Pnj3z2GOPVanvxRdfzNZbb5169epl7bXXzvjx4xe4hqeeeirbbrtt6tevn5VXXjmDBw/OBx98UKWeTTbZJA0bNsxKK62UHj165NVXX63c/sknn+SOO+6oEnI3aNAgbdq0SYcOHXLQQQele/fuVc49e/bsHHfccVlllVXSsGHDbLrpppk4cWLl9mnTpmW//fbLKquskgYNGqRbt2656qqrFvtdLOn76dSpU375y1+mRo0a+ec//1k5ZrXVVsvpp5+e/v37p0mTJhk8eHCS5Gc/+1k6d+6cBg0aZI011sgpp5xS5dl+8skns80226Rx48Zp0qRJNtxwwzzyyCNJqtcq57LLLkvXrl1Tr169rLXWWrnooosqt325Xcn8Z+L222/PhhtumLp16+bee+/N7NmzM2TIkLRq1Sr16tXLlltumUmTJi3ynLNnz87MmTOrLABl9cEHH+SJJ56o/Ldy6tSpeeKJJ/Laa68lSU488cT0798/SVKjRo1897vfrbLM/7fzu9/9bho2bJjk8xYlf/vb33LllVemcePGeeutt/LWW2/l448/XiHXCAAA8G20wkPuhdl2222z7rrrLrGNwwknnJCjjjoqkydPTp8+fZIkEyZMyJQpUzJhwoRcfvnlGTFiRJWw/NNPP83pp5+eJ598MjfeeGNeeeWVDBw4cIFjDxs2LL///e9z//335/XXX0+/fv1ywQUX5Morr8ytt96aO+64I7/73e8WWdtDDz2Ugw8+OEcccUSeeOKJbLPNNvnlL39ZZcwNN9yQo446Kj/5yU/y9NNP59BDD81BBx2UCRMmJEmuu+66nH/++bnkkkvy4osv5sYbb0y3bt2qeRcX7fLLL0+LFi3y8MMP58gjj8xhhx2WvffeO1tssUUee+yx7LDDDjnwwAMXG+J/9NFH+fWvf53LLrsszzzzTFq1apVZs2ZlwIABuffee/Pggw+mU6dO2XnnnTNr1qwkn78w63vf+17q1KmThx56KH/84x/zs5/9rMpxP/zww/Tp0yfNmjXLpEmTcu211+bOO+/MEUcckST57LPPsscee6Rnz5755z//mQceeCCDBw+uMlv9rrvuyiqrrJK11lprgbqLosg999yT5557rsrs6COOOCIPPPBARo0alX/+85/Ze++9s+OOO+bFF19M8nlwvuGGG+bWW2/N008/ncGDB+fAAw/Mww8/vMzfw9y5c3P55ZcnSTbYYIMq284999ysu+66efzxx3PKKackSRo3bpwRI0bk2WefzYUXXphLL700559/fuU+BxxwQL7zne9k0qRJefTRR3PCCSekdu3a1apl5MiR+cUvfpEzzjgjkydPzq9+9auccsoplfUtygknnJCzzjorkydPTvfu3fPTn/401113XS6//PI89thjWXPNNdOnT5+89957C93/zDPPTNOmTSuX9u3bV6tegG+jRx55JOuvv37WX3/9JMmxxx6b9ddfP7/4xS+SfN56bX7gXV0XX3xxZsyYkV69eqVt27aVy9VXX73c6wcAACitYgUaMGBAsfvuuy902z777FN07dq18nOS4oYbbiiKoiimTp1aJCkuuOCCBY7XoUOH4rPPPqtct/feexf77LPPImuYNGlSkaSYNWtWURRFMWHChCJJceedd1aOOfPMM4skxZQpUyrXHXrooUWfPn0Wedz99tuv2HnnnRe4pqZNm1Z+3mKLLYpDDjmkypi99967cr/zzjuv6Ny5czFnzpxFnueLhg8fXiQpGjZsWGXZcccdK8f07Nmz2HLLLSs/f/bZZ0XDhg2LAw88sHLdm2++WSQpHnjggaIo/u+eTJ8+vcp5nnjiicXWM3fu3KJx48bFzTffXBRFUYwbN66oVatW8cYbb1SOuf3226t8t3/605+KZs2aFR988EHlmFtvvbWoUaNG8dZbbxXTpk0rkhQTJ05c5HkPOeSQ4rjjjqtyzbVr1y4aNmxY1K5du0hS1KtXr7jvvvuKoiiKV199tahZs2aVuoqiKLbbbrvixBNPXOR5dtlll+InP/lJlfMcddRRixz/5e+nRo0aRd26dYvhw4dXGdehQ4dijz32WORx5jvnnHOKDTfcsPJz48aNixEjRizy3F989oYOHVqsu+66lZ87duxYXHnllVX2Of3004vNN9+8KIr/+5l7/PHHi6L4v2fixhtvrBz/wQcfFLVr1y5GjhxZuW7OnDlFu3btirPPPnuhdX3yySfFjBkzKpfXX3+9SFIkM4qksFgsllIsAAAALH8zZswokhQzZsxY4thvbQPdoiiW2Et6o402WmDdOuusk5o1a1Z+btu2bZWel48++miGDRuWJ598MtOnT698weVrr72Wtddeu3Jc9+7dK/9369atK1tEfHHd4mbxTp48OXvuuWeVdZtvvnnGjh1bZcz8VhTz9ejRIxdeeGGSZO+9984FF1yQNdZYIzvuuGN23nnn9O3bd7F9jxs3brxAi5Av92L+4rXVrFkzK6+8cpUZ4vPbm3yxjcuX1alTp8pxkuTtt9/OySefnIkTJ+add97J3Llz89FHH1XOWps8eXLat2+fdu3aVbknXzR58uSsu+66lX+mPf+ezJs3L88//3y23nrrDBw4MH369Mn222+f3r17p1+/fmnbtm2Sz5+bm2++Oddcc02V4x5wwAE56aSTMn369AwdOjRbbLFFtthiiySft0eZO3duOnfuXGWf2bNnZ+WVV07y+azrX/3qV7nmmmvyxhtvZM6cOZk9e3YaNGiwyHu0MF/8fj766KPceeed+dGPfpSVV145ffv2rRy3sGf76quvzm9/+9tMmTIlH3zwQT777LM0adKkcvuxxx6bQYMG5Yorrkjv3r2z9957p2PHjkus6cMPP8yUKVNy8MEH55BDDqlc/9lnny3xZaNfrHPKlCn59NNP06NHj8p1tWvXziabbJLJkycvdP+6deumbt26S6wRAAAAABblWxtyT548eYkvV/piEDrfl9szVFRUVAbZ81th9OnTJyNHjkzLli3z2muvpU+fPpkzZ84ij1NRUbHY435d2rdvn+effz533nlnxo8fnx//+Mc555xzcvfddy+yDUWNGjWy5pprLva4C7uWL19vksVeX/369Rf4JcSAAQMybdq0XHjhhenQoUPq1q2bzTfffIF7+1UNHz48Q4YMydixY3P11Vfn5JNPzvjx47PZZpvl4YcfzmeffVYZYM/XtGnTyvtyzTXXZM0118xmm22W3r1754MPPkjNmjXz6KOPVvkFSZI0atQoSXLOOefkwgsvzAUXXJBu3bqlYcOGOfroo5f62r78/XTv3j133HFHfv3rX1cJub/8bD/wwAM54IADcuqpp6ZPnz5p2rRpRo0alfPOO69yzLBhw7L//vvn1ltvze23356hQ4dm1KhRC/yy5cvm9zu/9NJLs+mmm1bZ9uX78WUL+xkEAAAAgG/St7In99///vc89dRT+f73v79cj/vcc89l2rRpOeuss7LVVltlrbXWWuxs5a+ia9eueeihh6qse/DBBxcYc99991VZd99991WZUV6/fv307ds3v/3tbzNx4sQ88MADVWamf5vcd999GTJkSHbeeeess846qVu3bv7zn/9Ubu/atWtef/31vPnmm5XrFnZPnnzyyXz44YdVjlujRo106dKlct3666+fE088Mffff3+++93v5sorr0ySjBkzJrvssstiw9lGjRrlqKOOynHHHZeiKLL++utn7ty5eeedd7LmmmtWWdq0aVNZw+67754f/OAHWXfddbPGGmvkhRde+Go37P+rWbPmEl8gdv/996dDhw456aSTstFGG6VTp05VXrY5X+fOnXPMMcfkjjvuyPe+970MHz58iedv3bp12rVrl5dffnmB61/SL5q+aP4LVL/4TH/66aeZNGlSlWcaAAAAAJanFT6Te/bs2Xnrrbcyd+7cvP322xk7dmzOPPPM7Lrrrunfv/9yPdeqq66aOnXq5He/+11+9KMf5emnn87pp5++XM8x35AhQ9KjR4+ce+652X333TNu3LgqrUqS5Pjjj0+/fv2y/vrrp3fv3rn55ptz/fXX584770ySjBgxInPnzs2mm26aBg0a5G9/+1vq16+fDh06LPK8RVHkrbfeWmB9q1atUqPG1/s7jU6dOuWKK67IRhttlJkzZ+b444+v0iqld+/e6dy5cwYMGJBzzjknM2fOzEknnVTlGAcccECGDh2aAQMGZNiwYXn33Xdz5JFH5sADD0zr1q0zderU/OlPf8puu+2Wdu3a5fnnn8+LL75Y+azcdNNNOe2005ZY66GHHprTTz891113Xfbaa68ccMAB6d+/f84777ysv/76effdd3PXXXele/fu2WWXXdKpU6eMHj06999/f5o1a5bf/OY3efvtt5c6vP3i9/Pxxx9n/PjxGTduXOVLyRZ3b1977bWMGjUqG2+8cW699dbccMMNlds//vjjHH/88dlrr72y+uqr51//+lcmTZpU7V8UnXrqqRkyZEiaNm2aHXfcMbNnz84jjzyS6dOn59hjj63WMRo2bJjDDjssxx9/fJo3b55VV101Z599dj766KMcfPDB1ToGAAAAACytFT6Te+zYsWnbtm1WW2217LjjjpkwYUJ++9vfZsyYMUtslbC0WrZsmREjRuTaa6/N2muvnbPOOivnnnvucj3HfJtttlkuvfTSXHjhhVl33XVzxx135OSTT64yZo899siFF16Yc889N+uss04uueSSDB8+PL169UqSrLTSSrn00kvTo0ePdO/ePXfeeWduvvnmyj7RCzNz5sy0bdt2geXrmrH+RX/+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5aIAAAAAAKA6lqkn96mnnpp99tkn//jHPyp7ct9333256667Fhp+AwAAAADA12GZZnJ///vfz0MPPZQWLVrkxhtvzI033pgWLVrk4Ycfzp577rm8awQAAAAAgIVaphdPAnwdvHgSAAD4byBpAfjqlubFk8vUriRJ5s6dmxtuuCGTJ09Okqy99trZfffdU6vWMh8SAAAAAACWyjK1K3nmmWfSuXPnDBgwIDfccENuuOGGDBgwIJ06dcrTTz+9vGsEAAAAKJWLL7443bt3T5MmTdKkSZNsvvnmuf322xe7zwUXXJAuXbqkfv36ad++fY455ph88sknVca88cYb+cEPfpCVV1459evXT7du3fLII498nZcC8K23TNOuBw0alHXWWSePPPJImjVrliSZPn16Bg4cmMGDB+f+++9frkUCAAAAlMl3vvOdnHXWWenUqVOKosjll1+e3XffPY8//njWWWedBcZfeeWVOeGEE/KXv/wlW2yxRV544YUMHDgwFRUV+c1vfpPk8+ylR48e2WabbXL77benZcuWefHFFyuzGYD/VcvUk7t+/fp55JFHFvhH+emnn87GG2+cjz/+eLkVCPzv0JMbAAD4b7CopKV58+Y555xzcvDBBy+w7YgjjsjkyZNz1113Va77yU9+koceeij33ntvkuSEE07Ifffdl3vuuedrqRvg22RpenIvU7uSzp075+23315g/TvvvJM111xzWQ4JAAAA8F9p7ty5GTVqVD788MNsvvnmCx2zxRZb5NFHH83DDz+cJHn55Zdz2223Zeedd64cc9NNN2WjjTbK3nvvnVatWmX99dfPpZde+o1cA8C3WbVD7pkzZ1YuZ555ZoYMGZLRo0fnX//6V/71r39l9OjROfroo/PrX//666x3mb300kv51a9+ZZY5AAAA8I146qmn0qhRo9StWzc/+tGPcsMNN2Tttdde6Nj9998/p512WrbccsvUrl07HTt2TK9evfLzn/+8cszLL7+ciy++OJ06dcq4ceNy2GGHZciQIbn88su/qUsC+Faqdsi90korpVmzZmnWrFn69u2bZ599Nv369UuHDh3SoUOH9OvXL08//XT69u37dda7TD755JPstddeadeuXerXr1+5ftiwYVlvvfW+sTpWW221XHDBBV/7eUaMGJGVVlrpaz8P/+ebfpaWxiuvvJKKioo88cQTSZKJEyemoqIi77//frWP8U09uwAAAP9NunTpkieeeCIPPfRQDjvssAwYMCDPPvvsQsdOnDgxv/rVr3LRRRflsccey/XXX59bb701p59+euWYefPmZYMNNsivfvWrrL/++hk8eHAOOeSQ/PGPf/ymLgngW6naL56cMGHC11lHtQ0cOLDyN5S1atVK8+bN07179+y3334ZOHBgatRYMLc/8sgjs8cee2TgwIHfcLVfjwkTJuScc87JQw89lI8//jirrbZadtpppxx77LFZZZVVss8++1T5c6b/Na+++mrWWmutvPvuuzn33HNz6qmnJklq1KiRdu3aZaeddspZZ52V5s2bf2M1vfLKK1l99dUrP9euXTurrrpqBg4cmJNOOikVFRVf27nbt2+fN998My1atFjmY0yaNCkNGzZcjlUBAAD896tTp05lW9cNN9wwkyZNyoUXXphLLrlkgbGnnHJKDjzwwAwaNChJ0q1bt3z44YcZPHhwTjrppNSoUSNt27ZdYCZ4165dc9111339FwPwLVbtkLtnz55fZx1LZccdd8zw4cMzd+7cvP322xk7dmyOOuqojB49OjfddFNq1ap6WV9nf6pPP/00tWvX/tqO/2WXXHJJfvzjH2fAgAG57rrrstpqq+W1117LX//615x33nn5zW9+k/r161eZsV52c+bMSZ06dao9fsyYMdlmm23SqFGjJMk666yTO++8M3Pnzs3kyZPzwx/+MDNmzMjVV1/9dZW8SHfeeWfWWWedzJ49O/fee28GDRqUtm3bLvSlI8nSX/vC1KxZM23atPlKx2jZsuVit3/TPwcAAABlNG/evMyePXuh2z766KMFJu7VrFkzSVL8/zdZ9ujRI88//3yVMS+88EI6dOjwNVQLUB7L9OLJ5PMWIA8//HBuueWW3HTTTVWWr1vdunXTpk2brLLKKtlggw3y85//PGPGjMntt9+eESNGVI577bXXsvvuu6dRo0Zp0qRJ+vXrt9AXZs43adKkbL/99mnRokWaNm2anj175rHHHqsypqKiIhdffHF22223NGzYMGecccZCj/XOO++kb9++qV+/flZfffWMHDlygTHvv/9+Bg0alJYtW6ZJkybZdttt8+STTy6yvn/9618ZMmRIhgwZkr/85S/p1atXVltttWy99da57LLL8otf/CLJgu1K5rfSuOKKK7LaaquladOm2XfffTNr1qzKMbNmzcoBBxyQhg0bpm3btjn//PPTq1evHH300ZVjrrjiimy00UZp3Lhx2rRpk/333z/vvPNO5fb5bTBuvfXWdO/ePfXq1ctmm22Wp59+eoFavuiCCy7IaqutVvl54MCB2WOPPXLGGWekXbt26dKlS7XOP9+YMWOy2267VX6uVatW5fPSu3fv7L333hk/fnyVfS677LJ07do19erVy1prrZWLLrqoyvaf/exn6dy5cxo0aJA11lgjp5xySj799NNFfFOLtvLKK6dNmzbp0KFDDjjggPTo0aPKM7as1z59+vQccMABadmyZerXr59OnTpl+PDhSRZsV7Iw9957b7baaqvUr18/7du3z5AhQ/Lhhx9Wbv9yu5JF/RxcfPHF6dixY+rUqZMuXbrkiiuuWOp7BAAA8N/gxBNPzD/+8Y+88soreeqpp3LiiSdm4sSJOeCAA5Ik/fv3z4knnlg5vm/fvrn44oszatSoTJ06NePHj88pp5ySvn37VobdxxxzTB588MH86le/yksvvZQrr7wyf/rTn3L44YevkGsE+Lao9kzuLxo7dmz69++f//znPwtsq6ioyNy5c79yYUtr2223zbrrrpvrr78+gwYNyrx58yoD7rvvvjufffZZDj/88Oyzzz6ZOHHiQo8xa9asDBgwIL/73e9SFEXOO++87LzzznnxxRfTuHHjynHDhg3LWWedlQsuuGCBWePzDRw4MP/+978zYcKE1K5dO0OGDFkgkN17771Tv3793H777WnatGkuueSSbLfddnnhhRcW2krj2muvzZw5c/LTn/50oedcXB/uKVOm5MYbb8wtt9yS6dOnp1+/fjnrrLMqw8ljjz029913X2666aa0bt06v/jFL/LYY49VCaQ//fTTnH766enSpUveeeedHHvssRk4cGBuu+22Kuc6/vjjc+GFF6ZNmzb5+c9/nr59++aFF15Yqpm+d911V5o0aVIljK7O+d9///3ce++9iwxXX3nllYwbN67K7OiRI0fmF7/4RX7/+99n/fXXz+OPP55DDjkkDRs2zIABA5IkjRs3zogRI9KuXbs89dRTOeSQQ9K4ceNFfhfV8cgjj+TRRx9N//79v/K1n3LKKXn22Wdz++23p0WLFnnppZeq/ZLVKVOmZMcdd8wvf/nL/OUvf8m7776bI444IkcccURlUL4wX/45uOGGG3LUUUflggsuSO/evXPLLbfkoIMOyne+851ss802Cz3G7Nmzq8ximDlzZrVqBgAA+LZ755130r9//7z55ptp2rRpunfvnnHjxmX77bdP8vnEvC/O3D755JNTUVGRk08+OW+88UZatmyZvn37Vplct/HGG+eGG27IiSeemNNOOy2rr756LrjggsrgHOB/VrEM1lxzzeLHP/5x8dZbby3L7l/JgAEDit13332h2/bZZ5+ia9euRVEUxR133FHUrFmzeO211yq3P/PMM0WS4uGHHy6KoiiGDh1arLvuuos819y5c4vGjRsXN998c+W6JMXRRx+92Bqff/75KucpiqKYPHlykaQ4//zzi6Ioinvuuado0qRJ8cknn1TZt2PHjsUll1yy0OMedthhRZMmTRZ77qIoiuHDhxdNmzat/Dx06NCiQYMGxcyZMyvXHX/88cWmm25aFEVRzJw5s6hdu3Zx7bXXVm5///33iwYNGhRHHXXUIs8zadKkIkkxa9asoiiKYsKECUWSYtSoUZVjpk2bVtSvX7+4+uqrK2v58j0///zziw4dOlR+HjBgQNG6deti9uzZi73OL5+/KIpi5MiRxUYbbVTl2mvUqFE0bNiwqFevXpGkSFL85je/qRzTsWPH4sorr6xy7NNPP73YfPPNF3nuc845p9hwww2rnGdxz9LUqVOLJEX9+vWLhg0bFrVr1y6SFIMHD64yblmvvW/fvsVBBx202HM//vjjRVH83/c0ffr0oiiK4uCDD16gjnvuuaeoUaNG8fHHHxdFURQdOnSofHaLYuE/B1tssUVxyCGHVFm39957FzvvvPMir2Po0KGV30nVZUaRFBaLxWKxWCwWi8VSygWAr27GjBlFkmLGjBlLHLtM7UrefvvtHHvssWnduvVXiNeXv6IoKl/gN3ny5LRv3z7t27ev3L722mtnpZVWyuTJkxe6/9tvv51DDjkknTp1StOmTdOkSZN88MEHee2116qM22ijjRZbx+TJk1OrVq1suOGGlevWWmutKjOtn3zyyXzwwQdZeeWV06hRo8pl6tSpmTJlyhKvb2mtttpqVWajt23btnJm+csvv5xPP/00m2yySeX2pk2bVrbKmO/RRx9N3759s+qqq6Zx48aVfdq/fH8233zzyv/dvHnzdOnSZZH3fFG6deu2QC/q6pz/y61Kkv97m/WkSZPys5/9LH369MmRRx6ZJPnwww8zZcqUHHzwwVW+h1/+8pdVvoerr746PXr0SJs2bdKoUaOcfPLJC1x3dVx99dV54okn8uSTT+aaa67JmDFjcsIJJ3zlaz/ssMMyatSorLfeevnpT3+a+++/v9o1PfnkkxkxYkSV6+/Tp0/mzZuXqVOnLnK/L/8cTJ48OT169KiyrkePHov97k888cTMmDGjcnn99derXTcAAAAAJMvYrmSvvfbKxIkT07Fjx+Vdz1cyefLkrL766su8/4ABAzJt2rRceOGF6dChQ+rWrZvNN988c+bMqTKuYcOGX7XUfPDBB2nbtu1CW6csqu1I586dM2PGjLz55ptp27btUp3vy61CKioqMm/evGrv/+GHH6ZPnz7p06dPRo4cmZYtW+a1115Lnz59Frg/i1OjRo0URVFl3cJ6W3/5Hlfn/HPmzMnYsWPz85//vMq+X3yb9VlnnZVddtklp556ak4//fR88MEHST5/Oemmm25aZb/5Pc8eeOCBHHDAATn11FPTp0+fNG3aNKNGjcp5551X7euer3379pW1dO3aNVOmTMkpp5ySYcOGpV69est87TvttFNeffXV3HbbbRk/fny22267HH744Tn33HOXWNMHH3yQQw89NEOGDFlg26qrrrrI/ZbHz0HdunVTt27dr3wcAAAAAP53LVPI/fvf/z5777137rnnnnTr1m2BAHVhYdnX7e9//3ueeuqpHHPMMUk+DxBff/31vP7665WzuZ999tm8//77WXvttRd6jPvuuy8XXXRRdt555yTJ66+/vtC+40uy1lpr5bPPPsujjz6ajTfeOEny/PPP5/33368cs8EGG+Stt95KrVq1qrx0cXH22muvnHDCCTn77LNz/vnnL7D9/fffX2xf7kVZY401Urt27UyaNKky1JwxY0ZeeOGFbL311kmS5557LtOmTctZZ51VeT8feeSRhR7vwQcfrDzO9OnT88ILL6Rr165JkpYtW+att96qMit9cS9EnK865584cWKaNWuWddddd7HHOvnkk7PtttvmsMMOS7t27dKuXbu8/PLLi+xhdv/996dDhw456aSTKte9+uqrS6y5OmrWrJnPPvssc+bMqQy5v6y6975ly5YZMGBABgwYkK222irHH398tULuDTbYIM8++2xl+L6sunbtmvvuu6+yj3ny+c/Uon7eAAAAAGB5WKaQ+6qrrsodd9yRevXqZeLEiVVaaFRUVHztIffs2bPz1ltvZe7cuXn77bczduzYnHnmmdl1110rX+LXu3fvdOvWLQcccEAuuOCCfPbZZ/nxj3+cnj17LrLdSKdOnXLFFVdko402ysyZM3P88cenfv36S11fly5dsuOOO+bQQw/NxRdfnFq1auXoo4+ucqzevXtn8803zx577JGzzz47nTt3zr///e/ceuut2XPPPRdaY/v27XP++efniCOOyMyZM9O/f/+sttpq+de//pW//vWvadSo0TLNLm7cuHEGDBiQ448/Ps2bN0+rVq0ydOjQ1KhRo/K7XXXVVVOnTp387ne/y49+9KM8/fTTOf300xd6vNNOOy0rr7xyWrdunZNOOiktWrTIHnvskSTp1atX3n333Zx99tnZa6+9Mnbs2Nx+++1p0qTJYmuszvlvuummBVqVLMzmm2+e7t2751e/+lV+//vf59RTT82QIUPStGnT7Ljjjpk9e3YeeeSRTJ8+Pccee2w6deqU1157LaNGjcrGG2+cW2+9NTfccEM17uyCpk2blrfeeiufffZZnnrqqVx44YXZZpttFnv91bn2X/ziF9lwww2zzjrrZPbs2bnlllsqf7GwJD/72c+y2Wab5YgjjsigQYPSsGHDPPvssxk/fnx+//vfV/vajj/++PTr1y/rr79+evfunZtvvjnXX3997rzzzmofAwAAAACW1jL15D7ppJNy6qmnZsaMGXnllVcyderUyuXll19e3jUuYOzYsWnbtm1WW2217LjjjpkwYUJ++9vfZsyYMZUtJioqKjJmzJg0a9YsW2+9dXr37p011lgjV1999SKP++c//znTp0/PBhtskAMPPDBDhgxJq1atlqnG4cOHp127dunZs2e+973vZfDgwVWOVVFRkdtuuy1bb711DjrooHTu3Dn77rtvXn311cX2Ov/xj3+cO+64I2+88Ub23HPPrLXWWhk0aFCaNGmS4447bplqTZLf/OY32XzzzbPrrrumd+/e6dGjR7p27Vo5u7hly5YZMWJErr322qy99to566yzFjlL+KyzzspRRx2VDTfcMG+99VZuvvnmyh7TXbt2zUUXXZQ//OEPWXfddfPwww9Xq+7qnL+6IXeSHHPMMbnsssvy+uuvZ9CgQbnssssyfPjwdOvWLT179syIESMqW9/stttuOeaYY3LEEUdkvfXWy/33359TTjmlWuf5st69e1c+u4MHD87OO++82Geyutdep06dnHjiienevXu23nrr1KxZM6NGjapWTd27d8/dd9+dF154IVtttVXWX3/9/OIXv0i7du2W6tr22GOPXHjhhTn33HOzzjrr5JJLLsnw4cPTq1evpToOAAAAACyNiuLLDZKroXnz5pk0adK3ric3y8+HH36YVVZZJeedd14OPvjgau0zceLEbLPNNpk+ffoytU35Kh577LFsu+22effddxdon0N5zJw5M02bNk0yI8niZ/cDAAB8Wy190gLAl83PiWbMmLHELhDLNJN7wIABS5x9Srk8/vjjueqqqzJlypQ89thjlf2pd9999xVcWfV89tln+d3vfifgBgAAAID/McvUk3vu3Lk5++yzM27cuHTv3n2BYPE3v/nNcimOb9a5556b559/PnXq1MmGG26Ye+65Jy1atFjRZVXLJptskk022WRFlwEAAAAAfMOWqV3JNttss+gDVlTk73//+1cqCvjfpF0JAADw30C7EoCvbmnalSzTTO4JEyYsU2EAAAAAALA8LVNP7uHDh+fjjz9e3rUAAAAAAMBSWaaQ+4QTTkjr1q1z8MEH5/7771/eNQEAAAAAQLUsU8j9xhtv5PLLL89//vOf9OrVK2uttVZ+/etf56233lre9QEAAAAAwCItU8hdq1at7LnnnhkzZkxef/31HHLIIRk5cmRWXXXV7LbbbhkzZkzmzZu3vGsFAAAAAIAqlink/qLWrVtnyy23zOabb54aNWrkqaeeyoABA9KxY8dMnDhxOZQIAAAAAAALt8wh99tvv51zzz0366yzTnr16pWZM2fmlltuydSpU/PGG2+kX79+GTBgwPKsFQAAAAAAqqgoiqJY2p369u2bcePGpXPnzhk0aFD69++f5s2bVxnzzjvvpE2bNtqWANU2c+bMNG3aNMmMJE1WdDkAAADLZOmTFgC+bH5ONGPGjDRpsvicqNaynKBVq1a5++67s/nmmy9yTMuWLTN16tRlOTwAAAAAAFTLUrUreeCBB3LLLbfkz3/+c2XA/de//jWrr756WrVqlcGDB2f27NlJkoqKinTo0GH5VwwAAAAAAP/fUoXcp512Wp555pnKz0899VQOPvjg9O7dOyeccEJuvvnmnHnmmcu9SAAAAAAAWJilCrmf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1KlTJ2uuuWZ++ctfpiiKr/Xc7du3z5tvvpnvfve7y3yMSZMmZfDgwcuxKgAAAACWl5122il77713unfvnj59+uS2227L+++/n2uuuWaJ+5511lkZNWpUbrjhhtSrV+8bqHb5+5/vyb3jjjtm+PDhmTt3bt5+++2MHTs2Rx11VEaPHp2bbroptWpVvUWXXnrp11bLp59+mtq1ay9y+5///Of89Kc/zSWXXJLzzjtvhTx0c+fOTUVFRZo2bfqNn7u6xowZk2222SaNGjVK8nnT/TvvvDNz587N5MmT88Mf/jAzZszI1Vdf/Y3Xduedd2adddbJ7Nmzc++992bQoEFp27ZtDj744IWOnzNnTurUqfOVzlmzZs1q92NalJYtWy52+5KeXQAAAAC+OSuttFI6d+6cl156abHjzj333Jx11lm58847071792+ouuXvf3omd5LUrVs3bdq0ySqrrJINNtggP//5zzNmzJjcfvvtVWYqv/baa9l9993TqFGjNGnSJP369cvbb7+9yONOmjQp22+/fVq0aJGmTZumZ8+eeeyxx6qMqaioyMUXX5zddtstDRs2zBlnnLHI402dOjX3339/TjjhhHTu3DnXX399le0jRozISiutlFtuuSVdunRJgwYNstdee+Wjjz7K5ZdfntVWWy3NmjXLkCFDMnfu3Mr9Zs+eneOOOy6rrLJKGjZsmE033TQTJ05c4Lg33XRT1l577dStWzevvfbaAu1K5s2bl7PPPjtrrrlm6tatm1VXXbXK9fzsZz9L586d06BBg6yxxho55ZRT8umnn1Zun9/u44orrshqq62Wpk2bZt99963yJxWzZ8/OkCFD0qpVq9SrVy9bbrllJk2atMC9GjNmTHbbbbfKz/Ob7q+yyirp3bt39t5774wfP77KPpdddlm6du2aevXqZa211spFF11UZfuS6q+ulVdeOW3atEmHDh1ywAEHpEePHlWei/n39Ywzzki7du3SpUuXJMkVV1yRjTbaKI0bN06bNm2y//7755133qncb/r06TnggAPSsmXL1K9fP506dcrw4cOTLNiuZGHuvffebLXVVqlfv37at2+fIUOG5MMPP6zc/uV2JYt6di+++OJ07NgxderUSZcuXXLFFVcs9T0CAAAA4Kv54IMPMmXKlLRt23aRY84+++ycfvrpGTt2bDbaaKNvsLrl738+5F6YbbfdNuuuu25lkDxv3rzsvvvuee+993L33Xdn/Pjxefnll7PPPvss8hizZs3KgAEDcu+99+bBBx9Mp06dsvPOOy/QB2fYsGHZc88989RTT+WHP/zhIo83fPjw7LLLLmnatGl+8IMf5M9//vMCYz766KP89re/zahRozJ27NhMnDgxe+65Z2677bbcdtttueKKK3LJJZdk9OjRlfscccQReeCBBzJq1Kj885//zN57750dd9wxL774YpXj/vrXv85ll12WZ555Jq1atVrg3CeeeGLOOuusnHLKKXn22Wdz5ZVXpnXr1pXbGzdunBEjRuTZZ5/NhRdemEsvvTTnn39+lWNMmTIlN954Y2655Zbccsstufv/tXfvQVrVh/3438vqIiLgDY1buWhQRCMKXigxXiJUFGJihkaGIbI1aCxBDWrU0gaQITWYaCuGxDERMYkasI232HihRjFeMgJ2FZRoJSq0EUWC4JJmkeX8/vDnM1m5G/w+HH29Zj4zPuec55z37j4Hh/d++Jw5czJlypTK/ssuuyw///nP8+Mf/zhPP/10evTokUGDBrVaeuStt97KY4891qrk/nOvvPJKHnjggVazo2+99dZMmDAh//zP/5xFixblyiuvzPjx4/PjH/94m/Jvq3nz5mX+/Pnp169fq+0PPfRQXnjhhcyePTv33ntvkndnSk+ePDnPPPNM7rrrrrzyyiutlsx57/t+3333ZdGiRbn++uuz9957b1WOxYsX59RTT83QoUPz7LPPZtasWXnsscdy/vnnb/Z97//s3nnnnfn617+eSy65JAsXLsx5552Xs88+Ow8//PAmz9Hc3JzVq1e3GgAAAABsm2984xuZM2dOXnnllTzxxBP54he/mNra2gwfPjxJMnLkyIwbN65y/FVXXZXx48fnpptuSvfu3bNs2bIsW7YsTU1N1foS/jLFx1hDQ0PxhS98YaP7hg0bVvTq1asoiqJ48MEHi9ra2mLJkiWV/c8991yRpHjqqaeKoiiKiRMnFkccccQmr9XS0lJ06NCh+MUvflHZlqQYO3bsFnO2tLQUXbp0Ke66666iKIpi+fLlRV1dXfG73/2ucsyMGTOKJMVLL71U2XbeeecVu+66a/H2229Xtg0aNKg477zziqIoildffbWora0t/vd//7fV9QYMGFCMGzeu1XkbGxtbHfPn37vVq1cXbdu2LX70ox9t8Wt5z3e/+93iqKOOqryeOHFiseuuuxarV6+ubLv00kuLfv36FUVRFE1NTcXOO+9c3HrrrZX9a9euLerr64vvfOc7lW233nprcfTRR7c6b5s2bYr27dsXu+yyS5GkSFL8y7/8S+WYT37yk8Vtt93WKt/kyZOL/v37b1P+zf38X3755SJJ0a5du6J9+/bFzjvvXCQpvvrVr7Y6rqGhodh3332L5ubmTZ6rKIpi7ty5RZLKz/b0008vzj777M1e+7/+67+KoiiKhx9+uEhSrFy5siiKohg1atQGOX79618Xbdq0Kf7v//6vKIqi6NatW/Gv//qvlf0b++x++tOfLs4999xW2770pS8VgwcP3uTXMXHixMrPpPVYVSSFYRiGYRiGYRiGYRiGsYVRFO92mfvtt19RV1dX/NVf/VUxbNiwVj3hiSeeWDQ0NFRed+vWrdhYJzNx4sRN9jj/r61atapIUqxatWqLx37s1+TelKIoUlNTkyRZtGhRunTpki5dulT2H3roodl9992zaNGiHHPMMRu8//XXX883v/nNPPLII3njjTfS0tKSP/7xj1myZEmr47bmnwLMnj07a9asyeDBg5Mke++9d+UBmZMnT64ct+uuu+aTn/xk5fW+++6b7t27V9amfm/be8tcLFiwIC0tLTn44INbXa+5uTl77bVX5XVdXd1m1+RZtGhRmpubM2DAgE0eM2vWrFx33XVZvHhxmpqasm7dunTs2LHVMd27d0+HDh0qr/fbb79K1sWLF+edd97JcccdV9m/884759hjj82iRYsq296/VEmS9OzZM/fcc0/+9Kc/5ZZbbkljY2MuuOCCJMmaNWuyePHijBo1Kueee27lPevWrWu17vjW5N8as2bNSq9evfLOO+9k4cKFueCCC7LHHnu0mrF++OGHb7AO9/z583PFFVfkmWeeycqVKysPRl2yZEkOPfTQjB49OkOHDs3TTz+dU045JWeccUY+/elPb1WmZ555Js8++2xuvfXWyraiKLJ+/fq8/PLL6dWr10bf9/7P7qJFizZ4OOVxxx2XqVOnbvLa48aNy8UXX1x5vXr16lb3GQAAAABbNnPmzM3u//PliZN3Vzv4KFFyb8KiRYtywAEHfOD3NzQ0ZMWKFZk6dWq6deuWtm3bpn///lm7dm2r49q3b7/Fc02fPj1/+MMf0q5du8q29evX59lnn82kSZPSps27q868/8F/NTU1G932XkHa1NSU2trazJ8/P7W1ta2O+/NivF27dpXCf2P+PNfGPPnkkxkxYkQmTZqUQYMGpVOnTpk5c2auueaaVsdtLuvWWLt2be6///784z/+Y6vtdXV16dGjR5J3nxY7ZMiQTJo0KZMnT678E4wf/ehHGywb8t73ZGvzb40uXbpUsvTq1SuLFy/O+PHjc8UVV1QeJPr+z8SaNWsyaNCgDBo0KLfeems6d+6cJUuWZNCgQZXP02mnnZZXX301v/zlLzN79uwMGDAgY8aMydVXX73FTE1NTTnvvPNy4YUXbrCva9eum3zf1nx2t6Rt27Zp27btX3weAAAAAD6+lNwb8atf/SoLFizIRRddlOTdMnLp0qVZunRpZZbp888/n7feeiuHHnroRs/x+OOP5wc/+EFl9vXSpUvz5ptvbnOWFStW5O67787MmTNz2GGHVba3tLTkM5/5TB588MGceuqp23zeJOnTp09aWlryxhtv5Pjjj/9A50iSgw46KO3atctDDz2Uc845Z4P9TzzxRLp165Z/+qd/qmx79dVXt+ka7z3M8PHHH0+3bt2SvLtO9dy5czN27Ngk7/5Gao899sgRRxyx2XN985vfzMknn5zRo0envr4+9fX1+d3vfpcRI0Zs9PjtkX9Tamtrs27duqxdu7ZScr/fb3/726xYsSJTpkypfP7mzZu3wXGdO3dOQ0NDGhoacvzxx+fSSy/dqpK7b9++ef755yvl+wfVq1evPP7442loaKhse/zxxzd5jwAAAADA9vCxL7mbm5uzbNmytLS05PXXX8/999+fb3/72/nc5z6XkSNHJkkGDhyYww8/PCNGjMi1116bdevW5Wtf+1pOPPHETS43ctBBB+WnP/1pjj766KxevTqXXnrpFmc8b8xPf/rT7LXXXjnzzDM3mE09ePDgTJ8+/QOX3AcffHBGjBiRkSNH5pprrkmfPn2yfPnyPPTQQ+ndu3eGDBmyVefZZZddcvnll+eyyy5LXV1djjvuuCxfvjzPPfdcRo0alYMOOihLlizJzJkzc8wxx+Q//uM/cuedd25T1vbt22f06NG59NJLs+eee6Zr1675zne+kz/+8Y8ZNWpUkuSee+7Z5AMn/1z//v3Tu3fvXHnllZk2bVomTZqUCy+8MJ06dcqpp56a5ubmzJs3LytXrszFF1+8XfK/Z8WKFVm2bFnWrVuXBQsWZOrUqfnsZz+72aVPunbtmrq6unzve9/L3//932fhwoWtlqlJkgkTJuSoo47KYYcdlubm5tx7772bXGbk/S6//PL89V//dc4///ycc845ad++fZ5//vnMnj0706ZN2+qv7dJLL82ZZ56ZPn36ZODAgfnFL36RO+64I//5n/+51ecAAAAAgG3VptoBqu3+++/Pfvvtl+7du+fUU0/Nww8/nOuuuy533313ZbmKmpqa3H333dljjz1ywgknZODAgTnwwAMza9asTZ53+vTpWblyZfr27ZuzzjorF154YfbZZ59tznfTTTfli1/84kaXCxk6dGjuueeeDzRD/D0zZszIyJEjc8kll6Rnz54544wzMnfu3M0uU7Ex48ePzyWXXJIJEyakV69eGTZsWGU97c9//vO56KKLcv755+fII4/ME088kfHjx29z1ilTpmTo0KE566yz0rdv37z00kt54IEHssceeyTZ+pI7SS666KLceOONWbp0ac4555zceOONmTFjRg4//PCceOKJufnmmyvL1Wyv/Mm7vzB57/P21a9+NYMHD97s5yh5d4b2zTffnH/7t3/LoYcemilTpmwwQ7uuri7jxo1L7969c8IJJ6S2tnaLazG9p3fv3pkzZ05efPHFHH/88enTp08mTJiQ+vr6bfrazjjjjEydOjVXX311DjvssNxwww2ZMWNGTjrppG06DwAAAABsi5qiKIpqh4C/1NNPP52TTz45y5cv32Btb8pj9erV//8DP1cl2fYHewIAAAB83HxU2933eqJVq1ZtdhWExExuPiLWrVuX733vewpuAAAAAPiYMZMb2GGYyQ0AAACwbT6q7a6Z3AAAAAAAfCwouQEAAAAAKC0lNwAAAAAApaXkBgAAAACgtJTcAAAAAACUlpIbAAAAAIDSUnIDAAAAAFBaSm4AAAAAAEpLyQ0AAAAAQGkpuQEAAAAAKC0lNwAAAAAApaXkBgAAAACgtJTcAAAAAACUlpIbAAAAAIDSUnIDAAAAAFBaSm4AAAAAAEpLyQ0AAAAAQGkpuQEAAAAAKC0lNwAAAAAApaXkBgAAAACgtJTcAAAAAACUlpIbAAAAAIDSUnIDAAAAAFBaSm4AAAAAAEpLyQ0AAAAAQGkpuQEAAAAAKC0lNwAAAAAApaXkBgAA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2dlll12qHQdK77TTTqv8d+/evdOvX79069Ytt99+u2W1dnBKbqCq9t5779TW1ub1119vtf3111/PJz7xiSqlAoDWzj///Nx777159NFHs//++1c7DpRaXV1devTokSQ56qijMnfu3EydOjU33HBDlZNB+cyfPz9vvPFG+vbtW9nW0tKSRx99NNOmTUtzc3Nqa2urmBDKbffdd8/BBx+cl156qdpR2AJrcgNVVVdXl6OOOioPPfRQZdv69evz0EMPWZsRgKoriiLnn39+7rzzzvzqV7/KAQccUO1I8JGzfv36NDc3VzsGlNKAAQOyYMGCNDY2VsbRRx+dESNGpLGxUcENf6GmpqYsXrw4++23X7WjsAVmcgNVd/HFF6ehoSFHH310jj322Fx77bVZs2ZNzj777GpHg1JqampqNdPg5ZdfTmNjY/bcc8907dq1ismgfMaMGZPbbrstd999dzp06JBly5YlSTp16pR27dpVOR2Uz7hx43Laaaela9euefvtt3PbbbflkUceyQMPPFDtaFBKHTp02OA5Ee3bt89ee+3l+RHwAXzjG9/I6aefnm7duuX3v/99Jk6cmNra2gwfPrza0dgCJTdQdcOGDcvy5cszYcKELFu2LEceeWTuv//+DR5GCWydefPm5bOf/Wzl9cUXX5wkaWhoyM0331ylVFBO119/fZLkpJNOarV9xowZ+bu/+7v/94Gg5N54442MHDkyr732Wjp16pTevXvngQceyN/8zd9UOxoA5H/+538yfPjwrFixIp07d85nPvOZ/OY3v0nnzp2rHY0tqCmKoqh2CAAAAAAA+CCsyQ0AAAAAQGkpuQEAAAAAKC0lNwAAAAAApaXkBgAAAACgtJTcAAAAAACUlpIbAAAAAIDSUnIDAAAAAFBaSm4AAAAAAEpLyQ0AAPAheeWVV1JTU5PGxsYP/VonnXRSxo4d+6FfBwBgR6PkBgAA2IInn3wytbW1GTJkyId+rSuuuCI1NTWpqanJTjvtlO7du+eiiy5KU1PTZt93xx13ZPLkyR96PgCAHY2SGwAAYAumT5+eCy64II8++mh+//vff+jXO+yww/Laa6/llVdeyVVXXZUf/vCHueSSSzZ67Nq1a5Mke+65Zzp06PChZwMA2NEouQEAADajqakps2bNyujRozNkyJDcfPPNrfavXLkyI0aMSOfOndOuXbscdNBBmTFjxkbP1dLSkq985Ss55JBDsmTJkk1ec6eddsonPvGJ7L///hk2bFhGjBiRe+65J8m7M72PPPLI3HjjjTnggAOyyy67JNlwuZLm5uZcfvnl6dKlS9q2bZsePXpk+vTplf0LFy7Maaedlt122y377rtvzjrrrLz55psf8LsEAFA9Sm4AAIDNuP3223PIIYekZ8+e+fKXv5ybbropRVFU9o8fPz7PP/987rvvvixatCjXX3999t577w3O09zcnC996UtpbGzMr3/963Tt2nWrM7Rr164yYztJXnrppfz85z/PHXfcscn1vkeOHJmf/exnue6667Jo0aLccMMN2W233ZIkb731Vk4++eT06dMn8+bNy/3335/XX389Z5555lZnAgDYUexU7QAAAAA7sunTp+fLX/5ykuTUU0/NqlWrMmfOnJx00klJkiVLlqRPnz45+uijkyTdu3ff4BxNTU0ZMmRImpub8/DDD6dTp05bff358+fntttuy8knn1zZtnbt2vzkJz9J586dN/qeF198Mbfffntmz56dgQMHJkkOPPDAyv5p06alT58+ufLKKyvbbrrppnTp0iUvvvhiDj744K3OBwBQbWZyAwAAbMILL7yQp556KsOHD0/y7jIiw4YNa7Xsx+jRozNz5swceeSRueyyy/LEE09scJ7hw4dnzZo1efDBB7eq4F6wYEF22223tGvXLscee2z69++fadOmVfZ369ZtkwV3kjQ2Nqa2tjYnnnjiRvc/88wzefjhh7PbbrtVxiGHHJIkWbx48RbzAQDsSMzkBgAA2ITp06dn3bp1qa+vr2wriiJt27bNtGnT0qlTp5x22ml59dVX88tf/jKzZ8/OgAEDMmbMmFx99dWV9wwePDi33HJLnnzyyVYzsjelZ8+eueeee7LTTjulvr4+dXV1rfa3b99+s+9v167dZvc3NTXl9NNPz1VXXbXBvv3222+L+QAAdiRmcgMAAGzEunXr8pOf/CTXXHNNGhsbK+OZZ55JfX19fvazn1WO7dy5cxoaGnLLLbfk2muvzQ9/+MNW5xo9enSmTJmSz3/+85kzZ84Wr11XV5cePXqke/fuGxTcW+Pwww/P+vXrN3mtvn375rnnnkv37t3To0ePVmNLBToAwI5GyQ0AALAR9957b1auXJlRo0blU5/6VKsxdOjQypIlEyZMyN13352XXnopzz33XO6999706tVrg/NdcMEF+da3vpXPfe5zeeyxxz7U7N27d09DQ0O+8pWv5K677srLL7+cRx55JLfffnuSZMyYMfnDH/6Q4cOHZ+7cuVm8eHEeeOCBnH322WlpaflQswEAbG9KbgAAgI2YPn16Bg4cuNE1tIcOHZp58+bl2WefTV1dXcaNG5fevXvnhBNOSG1tbWbOnLnRc44dOzaTJk3K4MGDN7p29/Z0/fXX52//9m/zta99LYccckjOPffcrFmzJklSX1+fxx9/PC0tLTnllFNy+OGHZ+zYsdl9993Tpo2/JgIA5VJTFEVR7RAAAAAAAPBB+BU9AAAAAAClpeQGAAAAAKC0lNwAAAAAAJSWkhsAAAAAgNJScgMAAAAAUFpKbgAAAAAASkvJDQAAAABAaSm5AQAAAAAoLSU3AAAAAAClpeQGAAAAAKC0lNwAAAAAAJTW/wfPRDIY5cbbSAAAAABJRU5ErkJggg=="/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>4.4 Average Ask By Day</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [11]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="c1">## Query to get the average ASK and BID by day</span>
<span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    SELECT </span>
<span class="s2">        create_date DT_REF</span>
<span class="s2">        ,round(avg(ask),2) AvgAsk</span>
<span class="s2">        ,round(avg(bid),2) Avgbid</span>
<span class="s2">    FROM df </span>
<span class="s2">    where not code in ('BTC', 'ETH', 'LTC', 'DOGE')</span>
<span class="s2">    group by 1</span>
<span class="s2">    order by 1 </span>
<span class="s2">"""</span>

<span class="n">newDf</span> <span class="o">=</span> <span class="n">sqldf</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">locals</span><span class="p">())</span>
<span class="n">newDf</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">'DT_REF'</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="n">cht</span> <span class="o">=</span> <span class="n">newDf</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span>
    <span class="n">kind</span><span class="o">=</span><span class="s1">'line'</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s1">'DT_REF'</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">'AvgAsk'</span><span class="p">,</span>
    <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> 
    <span class="n">legend</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> 
    <span class="n">color</span><span class="o">=</span><span class="s1">'blue'</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s1">'Average ASK tendence by Day'</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">'Date'</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">'AvgAsk'</span><span class="p">)</span>

<span class="c1">#exibir o grafico</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABOcAAANXCAYAAAB+DztKAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAAC++klEQVR4nOzdd5xcdbk/8Gc3lZaEliYxhA4SqtcYkCZIKIJRrvSiRLEEpV1AFDXAvaIgTaWIIigGKQq5iAiEIoiJAoHQBBQMcIEEVCALAdL2/P6Y39mdybaZ3dnsnDPv9+u1r505c2bmO0v0zPmc5/l+G5IkSQIAAAAAWOka+3oAAAAAAFCvhHMAAAAA0EeEcwAAAADQR4RzAAAAANBHhHMAAAAA0EeEcwAAAADQR4RzAAAAANBHhHMAAAAA0EeEcwAAAADQR4RzAADUtF133TV23XXXvh5Gj62//vrx8Y9/vK+HAQDUGOEcALDSXHLJJdHQ0BATJkzo66HUrOXLl8fo0aOjoaEhfv/733e43/333x977713vO9974vBgwfH+9///thvv/3immuuKdmvoaEhjj322DbP/853vhMNDQ1x9NFHR3Nzc4fv853vfCdmzJjR7c/DyvX8889HQ0NDy8+AAQNinXXWiR122CG+/vWvx4svvtjXQwQAViCcAwBWmunTp8f6668fDzzwQDz77LN9PZyadPfdd8f8+fNj/fXXj+nTp7e7zw033BA777xzvPrqq3HcccfFD3/4wzj88MPjjTfeiJ/85Cddvsd3v/vd+MY3vhFHHXVU/PSnP43Gxo6/EgrnsumQQw6Jq6++Oq644or45je/GRtssEFceOGFsfnmm8e1117b18MDAIr07+sBAAD1Yd68eTFr1qy48cYb4wtf+EJMnz49vv3tb6/UMTQ3N8eSJUti8ODBK/V9K/HLX/4ytttuuzjqqKPi61//eixatChWW221kn2mTZsWW2yxRfz5z3+OgQMHljz22muvdfr65557bpx22mlx5JFHxs9+9rNOgzmya7vttovDDz+8ZNsLL7wQe+65Zxx11FGx+eabx9Zbb91HowMAivk2BgCsFNOnT48111wz9t133/jP//zPkqqwpUuXxlprrRWf/exn2zyvqakpBg8eHP/1X//Vsm3x4sXx7W9/OzbaaKMYNGhQjBkzJk455ZRYvHhxyXPTls7p06fHBz7wgRg0aFDcdtttERHx/e9/P3bYYYdYe+21Y5VVVontt98+fv3rX7d5/3fffTe++tWvxjrrrBNrrLFG7L///vHyyy9HQ0NDTJs2rWTfl19+OY4++ugYMWJEDBo0KD7wgQ/Ez372s7L/Ru+++27cdNNNcfDBB8eBBx4Y7777bvzv//5vm/2ee+65+I//+I82wVxExPDhwzt8/fPPPz9OOeWUOPzww+PKK6/sMphraGiIRYsWxc9//vOWNsnPfOYzFX3eP/zhD9HQ0BDXX399/M///E+st956MXjw4Nh9993brZ68/PLLY8MNN4xVVlklPvShD8Uf//jHdsdW6b+BGTNmxJZbbtkyzvTfQbGXX345pkyZEqNHj45BgwbFuHHj4ktf+lIsWbKkZZ8333wzjj/++BgzZkwMGjQoNtpoo/je977XaWvwiu64447YZpttYvDgwbHFFlvEjTfe2PLYP/7xj2hoaIgLLrigzfNmzZoVDQ0N8atf/ars9yo2duzYuOqqq2LJkiVxzjnntGx//fXX47/+679i/Pjxsfrqq8eQIUNi7733jkcffbRln7fffjtWW221OO6449q87ksvvRT9+vWLs88+u1vjAoC6lwAArASbbbZZMmXKlCRJkuS+++5LIiJ54IEHWh4/+uijk2HDhiWLFy8ued7Pf/7zJCKSBx98MEmSJFm+fHmy5557Jquuumpy/PHHJz/+8Y+TY489Nunfv3/yiU98ouS5EZFsvvnmybrrrpucccYZycUXX5w88sgjSZIkyXrrrZd8+ctfTn70ox8l559/fvKhD30oiYjklltuKXmNAw88MImI5Igjjkguvvji5MADD0y23nrrJCKSb3/72y37LViwIFlvvfWSMWPGJGeeeWZy6aWXJvvvv38SEckFF1xQ1t/o2muvTRoaGpIXX3wxSZIk+ehHP5rss88+bfbbZJNNkjFjxiT/93//1+VrRkQyderU5MILL0wiIjn00EOTZcuWlTWeq6++Ohk0aFCy0047JVdffXVy9dVXJ7Nmzaro895zzz1JRCTbbrttsv322ycXXHBBMm3atGTVVVdNPvShD5W8309/+tMkIpIddtgh+cEPfpAcf/zxybBhw5INNtgg2WWXXVr2q/TfwNZbb52MGjUqOeuss5ILL7ww2WCDDZJVV101+de//tWy38svv5yMHj265TUvu+yy5Jvf/Gay+eabJ2+88UaSJEmyaNGiZKuttkrWXnvt5Otf/3py2WWXJUceeWTS0NCQHHfccV3+PceOHZtssskmybBhw5Kvfe1ryfnnn5+MHz8+aWxsTO64446W/Xbcccdk++23b/P8L3/5y8kaa6yRLFq0qMP3mDdvXhIRybnnntvhPhtuuGGy7rrrttx/8MEHkw033DD52te+lvz4xz9OzjzzzOR973tfMnTo0OTll19u2e+www5LRowY0ebfzznnnJM0NDQkL7zwQpd/AwCgLeEcANDrHnrooSQikpkzZyZJkiTNzc3JeuutVxJo3H777UlEJL/97W9LnrvPPvskG2ywQcv9q6++OmlsbEz++Mc/lux32WWXJRGR/OlPf2rZFhFJY2Nj8uSTT7YZ0zvvvFNyf8mSJcmWW26ZfPSjH23ZNmfOnCQikuOPP75k38985jNtwrkpU6Yko0aNKgl8kiRJDj744GTo0KFt3q89H//4x5Mdd9yx5f7ll1+e9O/fP3nttddK9rviiiuSiEgGDhyY7Lbbbsk3v/nN5I9//GOyfPnyNq8ZEcnYsWOTiEgOOeSQsoO51GqrrZYcddRRbbaX+3nTcG7zzTcvCV4vuuiiJCKSxx9/PEmSwt9/+PDhyTbbbFOy3+WXX55EREk4V+m/gYEDBybPPvtsy7ZHH300iYjkhz/8Ycu2I488MmlsbGwJgYs1NzcnSZIkZ511VrLaaqslf/vb30oe/9rXvpb069evJVTtSPrf4Te/+U3LtoULFyajRo1Ktt1225ZtP/7xj5OISJ566qmWbUuWLEnWWWeddv9bFCsnnPvEJz6RRESycOHCJEmS5L333mvzb2fevHnJoEGDkjPPPLNlW/q/0d///vcl+2611VYl/30AgMpoawUAet306dNjxIgRsdtuu0VEodXwoIMOimuvvTaWL18eEREf/ehHY5111onrrruu5XlvvPFGzJw5Mw466KCWbTfccENsvvnmsdlmm8W//vWvlp+PfvSjERFxzz33lLz3LrvsEltssUWbMa2yyiol77Nw4cLYaaed4uGHH27ZnrY+fvnLXy557le+8pWS+0mSxG9+85vYb7/9IkmSknFNmjQpFi5cWPK67fn3v/8dt99+exxyyCEt2w444ICWltBiRx99dNx2222x6667xv333x9nnXVW7LTTTrHxxhvHrFmz2rz2q6++GhER48aNi379+nU6jnJ05/N+9rOfLWnD3WmnnSKi0MYZEfHQQw/Fa6+9Fl/84hdL9vvMZz4TQ4cOLXmtSv8N7LHHHrHhhhu23N9qq61iyJAhLe/d3NwcM2bMiP322y8++MEPtvm8DQ0NLe+70047xZprrlnyvnvssUcsX7487rvvvi7/dqNHj45PfvKTLfeHDBkSRx55ZDzyyCOxYMGCiIg48MADY/DgwSWt37fffnv861//ajOPXHesvvrqERHx1ltvRUTEoEGDWlqcly9fHv/+979j9dVXj0033bTkv+Mee+wRo0ePLhnXE088EY899lhVxgUA9cqCEABAr1q+fHlce+21sdtuu8W8efNatk+YMCHOO++8uOuuu2LPPfeM/v37xwEHHBDXXHNNLF68OAYNGhQ33nhjLF26tCSc+/vf/x5PPfVUrLvuuu2+34oLIowbN67d/W655Zb47//+75g7d27JPGVpEBNRmEC/sbGxzWtstNFGJff/+c9/xptvvhmXX355XH755WWNa0XXXXddLF26NLbddtuSudgmTJgQ06dPj6lTp5bsP2nSpJg0aVK88847MWfOnLjuuuvisssui49//OPx9NNPl8w9d9RRR8Urr7wS3/nOd2KdddaJE044odOxdKU7n/f9739/yf0111wzIgrBaEThbx0RsfHGG5fsN2DAgNhggw1KtlX6b2DF907fP33vf/7zn9HU1BRbbrllu69X/L6PPfZY2e/bno022qjk31hExCabbBIREc8//3yMHDkyhg0bFvvtt19cc801cdZZZ0VEIeB+3/ve1xJA9sTbb78dERFrrLFGRBTCyYsuuiguueSSmDdvXktgHhGx9tprt9xubGyMww47LC699NJ45513YtVVV43p06fH4MGD49Of/nSPxwUA9Uo4BwD0qrvvvjvmz58f1157bVx77bVtHp8+fXrsueeeERFx8MEHx49//OP4/e9/H5MnT47rr78+Nttss5JVJZubm2P8+PFx/vnnt/t+Y8aMKblfXCGX+uMf/xj7779/7LzzznHJJZfEqFGjYsCAAXHllVfGNddcU/FnTBcDOPzww+Ooo45qd5+tttqq09dIq5F23HHHdh//xz/+0SakiohYddVVY6eddoqddtop1llnnTjjjDPi97//fck4+vfvH9dff33stddecdJJJ8WwYcPaXXyjXN35vB1V7CVJ0q33r+TfQLXeu7m5OT72sY/FKaec0u7jachWDUceeWTccMMNMWvWrBg/fnzcfPPN8eUvf7kqq+s+8cQTMXz48BgyZEhERHznO9+Jb37zm3H00UfHWWedFWuttVY0NjbG8ccf32ahiyOPPDLOPffcmDFjRhxyyCFxzTXXxMc//vE21Y0AQPmEcwBAr5o+fXoMHz48Lr744jaP3XjjjXHTTTfFZZddFqusskrsvPPOMWrUqLjuuuviIx/5SNx9993xjW98o+Q5G264YTz66KOx++67t6lAKtdvfvObGDx4cNx+++0xaNCglu1XXnllyX5jx46N5ubmmDdvXklF14qrjK677rqxxhprxPLly2OPPfaoeDzz5s2LWbNmxbHHHhu77LJLyWPNzc1xxBFHxDXXXBOnn356p6+TtmTOnz+/zWODBw+Om2++OXbbbbf4/Oc/H8OGDStpr+xIe3/jnn7e9owdOzYiCtVpxdVhS5cujXnz5pUEtNX4N1Bs3XXXjSFDhsQTTzzR6X4bbrhhvP322z36zM8++2wkSVIy7r/97W8REbH++uu3bNtrr71i3XXXjenTp8eECRPinXfeiSOOOKLb75uaPXt2PPfccyVtqL/+9a9jt912iyuuuKJk3zfffDPWWWedkm1bbrllbLvttjF9+vRYb7314sUXX4wf/vCHPR4XANQzc84BAL3m3XffjRtvvDE+/vGPx3/+53+2+Tn22GPjrbfeiptvvjkiCm1z//mf/xm//e1v4+qrr45ly5aVtLRGFObjevnll+MnP/lJu++3aNGiLsfVr1+/aGhoKGnfe/7552PGjBkl+02aNCkiIi655JKS7SuGEf369YsDDjggfvOb37Qb8Pzzn//sdDxp1dwpp5zS5m904IEHxi677FIyz9ddd93V7uvceuutERGx6aabtvv4kCFD4rbbbouNNtooDjnkkA5fp9hqq60Wb775Zsm2nn7e9nzwgx+MddddNy677LJYsmRJy/arrrqqzftX499AscbGxpg8eXL89re/jYceeqjN42mF3YEHHhizZ8+O22+/vc0+b775ZixbtqzL93rllVfipptuarnf1NQUv/jFL2KbbbaJkSNHtmzv379/HHLIIXH99dfHVVddFePHj++y+rIrL7zwQnzmM5+JgQMHxsknn9yyvV+/fm2qCG+44YZ4+eWX232dI444Iu6444648MILY+2114699967R+MCgHqncg4A6DU333xzvPXWW7H//vu3+/iHP/zhluqgNIQ76KCD4oc//GF8+9vfjvHjx8fmm29e8pwjjjgirr/++vjiF78Y99xzT+y4446xfPnyePrpp+P666+P22+/vd1J/Yvtu+++cf7558dee+0Vhx56aLz22mtx8cUXx0YbbRSPPfZYy37bb799HHDAAXHhhRfGv//97/jwhz8c9957b0ulU3H103e/+9245557YsKECfH5z38+tthii3j99dfj4YcfjjvvvDNef/31Dsczffr02Gabbdq0Y6b233//+MpXvhIPP/xwbLfddvGJT3wixo0bF/vtt19suOGGsWjRorjzzjvjt7/9bfzHf/xH7Lfffh2+17rrrhszZ86MHXfcMSZPnhx33XVXfOhDH+pw/+233z7uvPPOOP/882P06NExbty4mDBhQo8+b3sGDBgQ//3f/x1f+MIX4qMf/WgcdNBBMW/evLjyyivbtPNW49/Air7zne/EHXfcEbvsskscc8wxsfnmm8f8+fPjhhtuiPvvvz+GDRsWJ598ctx8883x8Y9/PD7zmc/E9ttvH4sWLYrHH388fv3rX8fzzz/fptJsRZtssklMmTIlHnzwwRgxYkT87Gc/i1dffbVN1WZEoYX0Bz/4Qdxzzz3xve99r6LP8/DDD8cvf/nLaG5ujjfffDMefPDB+M1vfhMNDQ1x9dVXlwR9H//4x+PMM8+Mz372s7HDDjvE448/HtOnT2+3jToi4tBDD41TTjklbrrppvjSl74UAwYMqGhsAMAK+mydWAAg9/bbb79k8ODByaJFizrc5zOf+UwyYMCA5F//+leSJEnS3NycjBkzJomI5L//+7/bfc6SJUuS733ve8kHPvCBZNCgQcmaa66ZbL/99skZZ5yRLFy4sGW/iEimTp3a7mtcccUVycYbb5wMGjQo2WyzzZIrr7wy+fa3v52s+PVo0aJFydSpU5O11lorWX311ZPJkycnzzzzTBIRyXe/+92SfV999dVk6tSpyZgxY5IBAwYkI0eOTHbffffk8ssv7/Dzz5kzJ4mI5Jvf/GaH+zz//PNJRCQnnHBCkiRJ8qtf/So5+OCDkw033DBZZZVVksGDBydbbLFF8o1vfCNpamoqeW5H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0sfbc/bZZ8fQoUNbfsaMGdOzDwsAZSoO4rS1AgBAtvVpW2tXDj744Jbb48ePj6222io23HDD+MMf/hC77757H44s4rTTTosTTzyx5X5TU5OADoCVojiI09YKAADZVtOVcyvaYIMNYp111olnn302IiJGjhwZr732Wsk+y5Yti9dff71lnrqRI0fGq6++WrJPer+rfTqa6y6iMBfekCFDSn4AYGUorpzT1goAANmWqXDupZdein//+98xatSoiIiYOHFivPnmmzFnzpyWfe6+++5obm6OCRMmtOxz3333xdKlS1v2mTlzZmy66aax5pprtuxz1113lbzXzJkzY+LEib39kQCgYsVVctpaAQAg2/o0nHv77bdj7ty5MXfu3IiImDdvXsydOzdefPHFePvtt+Pkk0+OP//5z/H888/HXXfdFZ/4xCdio402ikmTJkVExOabbx577bVXfP7zn48HHngg/vSnP8Wxxx4bBx98cIwePToiIg499NAYOHBgTJkyJZ588sm47rrr4qKLLippST3uuOPitttui/POOy+efvrpmDZtWjz00ENx7LHHrvS/CQB0RTgHAAD50afh3EMPPRTbbrttbLvtthERceKJJ8a2224b3/rWt6Jfv37x2GOPxf777x+bbLJJTJkyJbbffvv44x//GIPSHp6ImD59emy22Wax++67xz777BMf+chH4vLLL295fOjQoXHHHXfEvHnzYvvtt4+TTjopvvWtb8UxxxzTss8OO+wQ11xzTVx++eWx9dZbx69//euYMWNGbLnllivvjwEAZSpuYR0woO02AAAgOxqSJEn6ehB50NTUFEOHDo2FCxeafw6AXvXyyxHrrRfRv3/EdddFHHBAxEc+EvHHP/b1yAAAgFS5WVGm5pwDAFpbWPv3L/wUbwMAALJFOAcAGZO2sPbrV/gp3gYAAGSLcA4AMkblHAAA5IdwDgAyRjgHAAD5IZwDgIzR1goAAPkhnAOAjFE5BwAA+SGcA4CMEc4BAEB+COcAIGO0tQIAQH4I5wAgY1TOAQBAfgjnACBjhHMAAJAfwjkAyBhtrQAAkB/COQDIGJVzAACQH8I5AMgY4RwAAOSHcA4AMqa9tlbhHAAAZJNwDgAypr3KOXPOAQBANgnnACBjtLUCAEB+COcAIGPaa2tNkojm5r4bEwAA0D3COQDImPYq5yK0tgIAQBYJ5wAgYzoK57S2AgBA9gjnACBjhHMAAJAfwjkAyJj25pwr3g4AAGSHcA4AMqa4cq44nFM5BwAA2SOcA4CMKQ7nGhsLP8XbAQCA7BDOAUDGFLe1Fv/W1goAANkjnAOAjCmunCv+rXIOAACyRzgHABkjnAMAgPwQzgFAxmhrBQCA/BDOAUDGqJwDAID8EM4BQMYI5wAAID+EcwCQMdpaAQAgP4RzAJAxKucAACA/hHMAkDHCOQAAyA/hHABkjLZWAADID+EcAGSMyjkAAMgP4RwAZIxwDgAA8kM4BwAZ01Fbq3AOAACyRzgHABnTUeWcOecAACB7hHMAkDHaWgEAID+EcwCQMdpaAQAgP4RzAJAx2loBACA/hHMAkDHaWgEAID+EcwCQMdpaAQAgP4RzAJAx2loBACA/hHMAkDHaWgEAID+EcwCQMcI5AADID+EcAGRMR3POaWsFAIDsEc4BQMaonAMAgPwQzgFAxgjnAAAgP4RzAJAx2loBACA/hHMAkDEq5wAAID+EcwCQMcI5AADID+EcAGSMtlYAAMgP4RwAZIzKOQAAyA/hHABkjHAOAADyQzgHABmjrRUAAPJDOAcAGaNyDgAA8kM4BwAZI5wDAID8EM4BQMZoawUAgPwQzgFAxqicAwCA/BDOAUDGCOcAACA/hHMAkDEdtbUK5wAAIHuEcwCQIUnSceWcOecAACB7hHMAkCHNza23tbUCAED2CecAIEOKq+O0tQIAQPYJ5wAgQ4oDOG2tAACQfcI5AMiQzsI5lXMAAJA9wjkAyBDhHAAA5ItwDgAypLM557S1AgBA9gjnACBD0uq4xsaIhobCbZVzAACQXcI5AMiQNIBLA7ni28I5AADIHuEcAGRI2rqatrIW39bWCgAA2SOcA4AMUTkHAAD5IpwDgAwRzgEAQL4I5wAgQ7S1AgBAvgjnACBDVM4BAEC+COcAIEOEcwAAkC/COQDIEG2tAACQL8I5AMgQlXMAAJAvwjkAyBDhHAAA5ItwDgAyRFsrAADki3AOADJE5RwAAOSLcA4AMkQ4BwAA+SKcA4AM6aytVTgHAADZI5wDgAzprHLOnHMAAJA9wjkAyBBtrQAAkC/COQDIkK5Wa02SlT8mAACg+4RzAJAhnVXORUQ0N6/c8QAAAD0jnAOADOkqnNPaCgAA2SKcA4AMaa+tVTgHAADZJZwDgAxpr3KuOKizYisAAGRLn4Zz9913X+y3334xevToaGhoiBkzZrQ8tnTp0jj11FNj/Pjxsdpqq8Xo0aPjyCOPjFdeeaXkNdZff/1oaGgo+fnud79bss9jjz0WO+20UwwePDjGjBkT55xzTpux3HDDDbHZZpvF4MGDY/z48XHrrbf2ymcGgJ7Q1goAAPnSp+HcokWLYuutt46LL764zWPvvPNOPPzww/HNb34zHn744bjxxhvjmWeeif3337/NvmeeeWbMnz+/5ecrX/lKy2NNTU2x5557xtixY2POnDlx7rnnxrRp0+Lyyy9v2WfWrFlxyCGHxJQpU+KRRx6JyZMnx+TJk+OJJ57onQ8OAN3UXjjX2Nj2cQAAIBv6d71L79l7771j7733bvexoUOHxsyZM0u2/ehHP4oPfehD8eKLL8b73//+lu1rrLFGjBw5st3XmT59eixZsiR+9rOfxcCBA+MDH/hAzJ07N84///w45phjIiLioosuir322itOPvnkiIg466yzYubMmfGjH/0oLrvssmp8VACoivbmnGtoKNxfvlxbKwAAZE2m5pxbuHBhNDQ0xLBhw0q2f/e734211147tt122zj33HNjWVHZwOzZs2PnnXeOgQMHtmybNGlSPPPMM/HGG2+07LPHHnuUvOakSZNi9uzZHY5l8eLF0dTUVPIDAL2tvcq54vsq5wAAIFv6tHKuEu+9916ceuqpccghh8SQIUNatn/1q1+N7bbbLtZaa62YNWtWnHbaaTF//vw4//zzIyJiwYIFMW7cuJLXGjFiRMtja665ZixYsKBlW/E+CxYs6HA8Z599dpxxxhnV+ngAUJbOwrnFi4VzAACQNZkI55YuXRoHHnhgJEkSl156acljJ554YsvtrbbaKgYOHBhf+MIX4uyzz45Bgwb12phOO+20kvduamqKMWPG9Nr7AUBE+22txfe1tQIAQLbUfDiXBnMvvPBC3H333SVVc+2ZMGFCLFu2LJ5//vnYdNNNY+TIkfHqq6+W7JPeT+ep62ifjuaxi4gYNGhQr4Z/ANAeba0AAJAvNT3nXBrM/f3vf48777wz1l577S6fM3fu3GhsbIzhw4dHRMTEiRPjvvvui6VLl7bsM3PmzNh0001jzTXXbNnnrrvuKnmdmTNnxsSJE6v4aQCg54RzAACQL31aOff222/Hs88+23J/3rx5MXfu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zY0ePTpOOumk+K//+q+IiFi4cGGMGDEirrrqqjj44IPjqaeeii222CIefPDB+OAHPxgREbfddlvss88+8dJLL8Xo0aPj0ksvjW984xuxYMGCGDhwYEREfO1rX4sZM2bE008/HRERBx10UCxatChuueWWlvF8+MMfjm222SYuu+yyssbf1NQUQ4cOjYULF8aQIUOq9WcBgBYjRkS89lrEY49FjB/f9vHTT4/4n/+J+OpXIy66aOWPDwAAaFVuVlSzc87NmzcvFixYEHvssUfLtqFDh8aECRNi9uzZERExe/bsGDZsWEswFxGxxx57RGNjY/zlL39p2WfnnXduCeYiIiZNmhTPPPNMvPHGGy37FL9Puk/6Pu1ZvHhxNDU1lfwAQG8qt61V5RwAAGRHzYZzCxYsiIiIESNGlGwfMWJEy2MLFiyI4cOHlzzev3//WGuttUr2ae81it+jo33Sx9tz9tlnx9ChQ1t+xowZU+lHBICKlNvWas45AADIjpoN52rdaaedFgsXLmz5+b//+7++HhIAOWfOOQAAyJ+aDedGjhwZERGvvvpqyfZXX3215bGRI0fGa6+9VvL4smXL4vXXXy/Zp73XKH6PjvZJH2/PoEGDYsiQISU/ANCbtLUCAED+1Gw4N27cuBg5cmTcddddLduampriL3/5S0ycODEiIiZOnBhvvvlmzJkzp2Wfu+++O5qbm2PChAkt+9x3332xdOnSln1mzpwZm266aay55pot+xS/T7pP+j4AUAu0tQIAQP70aTj39ttvx9y5c2Pu3LkRUVgEYu7cufHiiy9GQ0NDHH/88fHf//3fcfPNN8fjjz8eRx55ZIwePbplRdfNN9889tprr/j85z8fDzzwQPzpT3+KY489Ng4++OAYPXp0REQceuihMXDgwJgyZUo8+eSTcd1118VFF10UJ554Yss4jjvuuLjtttvivPPOi6effjqmTZsWDz30UBx77LEr+08CAB3S1goAAPnTwdf7leOhhx6K3XbbreV+GpgdddRRcdVVV8Upp5wSixYtimOOOSbefPPN+MhHPhK33XZbDB48uOU506dPj2OPPTZ23333aGxsjAMOOCB+8IMftDw+dOjQuOOOO2Lq1Kmx/fbbxzrrrBPf+ta34phjjmnZZ4cddohrrrkmTj/99Pj6178eG2+8ccyYMSO23HLLlfBXAICuNTe33tbWCgAA+dGQJEnS14PIg6amphg6dGgsXLjQ/HMAVN2SJRGDBhVuv/FGxLBhbff58Y8jvvjFiE9+MuLGG1fq8AAAgBWUmxXV7JxzAECr4mo4ba0AAJAfwjkAyIDiRR46amsVzgEAQPYI5wAgA8qpnEtDO6u1AgBAdgjnACADisM5lXMAAJAfwjkAyIC0Gq6xsfDTHuEcAABkj3AOADIgDdw6qporfkxbKwAAZIdwDgAyIA3nOppvrvgxlXMAAJAdwjkAyADhHAAA5JNwDgAyIG1V1dYKAAD5IpwDgAxQOQcAAPkknAOADBDOAQBAPgnnACADtLUCAEA+CecAIANUzgEAQD4J5wAgA4RzAACQT8I5AMgAba0AAJBPwjkAyACVcwAAkE/COQDIAOEcAADkk3AOADKgkrZW4RwAAGSHcA4AMqCSyjlzzgEAQHYI5wAgA7S1AgBAPgnnACADtLUCAEA+CecAIAMqbWtNkt4fEwAA0HPCOaBmPfBAxB//2NejgNpQSTgXEdHc3LvjAQAAqqOTr/gAfae5OWLPPSPeey/i3/+OWG21vh4R9K1K2lojCmFeZ/sCAAC1QeUcUJPeey9i4cKIxYsLv6HeVVo5Z8VWAADIBuEcUJMWL27/NtSrSsM5i0IAAEA2COeAmlQcyL33Xt+NA2pFWgknnAMAgHypOJxramrq8LFnn322R4MBSBUHcirnoDVs62weucaio7q2VgAAyIaKw7l99903FrdzpvzMM8/ErrvuWo0xAaicgxWU09ba0NAa3qmcAwCAbKg4nFt99dXjk5/8ZCwr+tb/1FNPxa677hoHHHBAVQcH1C+Vc1CqnLbW4seFcwAAkA0Vh3M33nhjLFy4MA477LBIkiSeeOKJ2HXXXeOQQw6Jiy66qDfGCNQhlXNQqpy21uLHtbUCAEA2VBzOrbLKKvG73/0unnnmmTjwwANj9913jyOPPDLOP//83hgfUKes1gqlymlrLX5c5RwAAGRDF1/xC1ZcBKKxsTGuu+66+NjHPhYHHHBAfPOb32zZZ8iQIdUfJVB3tLVCKeEcAADkU1nh3LBhw6KhoaHN9iRJ4rLLLosf//jHkSRJNDQ0xHJ9NEAVaGuFUunhVVsrAADkS1nh3D333NPb4wAooa0VSqmcAwCAfCornNtll116exwAJYqr5VTOgXAOAADyquIFIW677ba4//77W+5ffPHFsc0228Shhx4ab7zxRlUHB9QvlXNQSlsrAADkU8Xh3Mknn9yy+MPjjz8eJ554Yuyzzz4xb968OPHEE6s+QKA+qZyDUirnAAAgn8pqay02b9682GKLLSIi4je/+U3st99+8Z3vfCcefvjh2Geffao+QKA+qZyDUsI5AADIp4or5wYOHBjvvPNORETceeedseeee0ZExFprrdVSUQfQU1ZrhVKVtrUK5wAAIBsqrpz7yEc+EieeeGLsuOOO8cADD8R1110XERF/+9vfYr311qv6AIH6VBzIqZyDyivnzDkHAADZUHHl3I9+9KPo379//PrXv45LL7003ve+90VExO9///vYa6+9qj5AoD6pnINS2loBACCfKq6ce//73x+33HJLm+0XXHBBvP7661UZFIA556CUtlYAAMiniivn2nPHHXfEQQcd1FJFB9BTVmuFUtpaAQAgn7odzr3wwgvx7W9/O9Zff/349Kc/HQ0NDfGLX/yimmMD6pjKOSilrRUAAPKporbWJUuWxI033hg//elP409/+lPsscce8dJLL8UjjzwS48eP760xAnVI5RyU0tYKAAD5VHbl3Fe+8pUYPXp0XHTRRfHJT34yXnrppfjtb38bDQ0N0a+rMwWACqmcg1LaWgEAIJ/Krpy79NJL49RTT42vfe1rscYaa/TmmACEc7ACba0AAJBPZVfOXX311fHAAw/EqFGj4qCDDopbbrkllrssD/QSba1Qqty2VuEcAABkS9nh3CGHHBIzZ86Mxx9/PDbbbLOYOnVqjBw5Mpqbm+Ovf/1rb44RqEMq56BUuZVzaXjn+hkAAGRDxau1jhs3Ls4444x4/vnn45e//GUccMABcfjhh8d6660XX/3qV3tjjEAdKg7kVM6BtlYAAMirilZrLdbQ0BCTJk2KSZMmxeuvvx6/+MUv4sorr6zm2IA6VhzIqZyD1ko44RwAAORLxZVz7VlrrbXi+OOPj0cffbQaLwegcg5WkIZtXc05p60VAACypeLKuRNPPLHd7Q0NDTF48ODYaKON4hOf+ESstdZaPR4cUL9UzkEpba0AAJBPFYdzjzzySDz88MOxfPny2HTTTSMi4m9/+1v069cvNttss7jkkkvipJNOivvvvz+22GKLqg8YqA8q56CUcA4AAPKp4rbWT3ziE7HHHnvEK6+8EnPmzIk5c+bESy+9FB/72MfikEMOiZdffjl23nnnOOGEE3pjvECdKA7nli6NaG7uu7FALUjbVLW1AgBAvlQczp177rlx1llnxZAhQ1q2DR06NKZNmxbnnHNOrLrqqvGtb30r5syZU9WBAvVlxWo5ra3UO5VzAACQTxWHcwsXLozXXnutzfZ//vOf0dTUFBERw4YNiyVLlvR8dEDdWjGME85R74RzAACQT91qaz366KPjpptuipdeeileeumluOmmm2LKlCkxefLkiIh44IEHYpNNNqn2WIE6sWxZ2zZW885R77S1AgBAPlW8IMSPf/zjOOGEE+Lggw+OZf//snz//v3jqKOOigsuuCAiIjbbbLP46U9/Wt2RAnWjvSBO5Rz1TuUcAADkU8Xh3Oqrrx4/+clP4oILLoh//OMfERGxwQYbxOqrr96yzzbbbFO1AQL1pziIW331iLffFs6BcA4AAPKp4rbWX/7yl/HOO+/E6quvHltttVVstdVWJcEcQE+llXP9+0estlrpNqhXlba1CucAACAbKg7nTjjhhBg+fHgceuihceutt8Zyk9oAVZZWyQ0aVPgp3gb1qtLKOYdnAADIhorDufnz58e1114bDQ0NceCBB8aoUaNi6tSpMWvWrN4YH1CHisO5wYMLt1XOUe+0tQIAQD5VHM71798/Pv7xj8f06dPjtddeiwsuuCCef/752G233WLDDTfsjTECdSYN4gYPVjkHKW2tAACQTxUvCFFs1VVXjUmTJsUbb7wRL7zwQjz11FPVGhdQx1TOQVvaWgEAIJ8qrpyLiHjnnXdi+vTpsc8++8T73ve+uPDCC+OTn/xkPPnkk9UeH1CHzDkHbWlrBQCAfKo4nDv44INj+PDhccIJJ8QGG2wQf/jDH+LZZ5+Ns846K5Y5EwCqoLitVeUcRCRJRHNz4ba2VgAAyJeK21r79esX119/fUyaNCn69esXb731Vlx++eVxxRVXxEMPPWT1VqDHVM5BqeJDq7ZWAADIl4rDuenTp0dExH333RdXXHFF/OY3v4nRo0fHpz71qfjRj35U9QEC9ae9BSFUzlHPiqvgtLUCAEC+VBTOLViwIK666qq44ooroqmpKQ488MBYvHhxzJgxI7bYYoveGiNQZ9pbEELlHPWsuAquq7ZW4RwAAGRL2XPO7bfffrHpppvGo48+GhdeeGG88sor8cMf/rA3xwbUqfbaWlXOUc8qqZxLwzttrQAAkA1lV879/ve/j69+9avxpS99KTbeeOPeHBNQ59pbEELlHPVMWysAAORX2ZVz999/f7z11lux/fbbx4QJE+JHP/pR/Otf/+rNsQF1SuUclCqugmvs4sgtnAMAgGwpO5z78Ic/HD/5yU9i/vz58YUvfCGuvfbaGD16dDQ3N8fMmTPjrbfe6s1xAnXEnHNQKg3a+vWLaGjofF9trQAAkC1lh3Op1VZbLY4++ui4//774/HHH4+TTjopvvvd78bw4cNj//33740xAnWmvdVahXPUszSc66qltXgflXMAAJANFYdzxTbddNM455xz4qWXXopf/epX1RoTUOfaq5zT1ko9S6vghHMAAJA/PQrnUv369YvJkyfHzTffXI2XA+qcyjkoVdzW2hVtrQAAkC1VCecAqknlHJTS1goAAPklnANqTnurtaqco54J5wAAIL+Ec0DNKW5rVTkHrS2q2loBACB/hHNAzVE5B6VUzgEAQH4J54Ca0144p3KOeiacAwCA/BLOATWnvbZWlXPUs+60tQrnAAAgG4RzQM1ROQelulM5Z845AADIBuEcUHNUzkEpba0AAJBfwjmg5qicg1LaWgEAIL+Ec0DNKQ7nVM6BtlYAAMgz4RxQc4rbWtPKOeEc9UxbKwAA5JdwDqg57VXOvfdeRJL03ZigL2lrBQCA/BLOATWnvTnnIiKWLu2b8UBf09YKAAD5VfPh3Prrrx8NDQ1tfqZOnRoREbvuumubx774xS+WvMaLL74Y++67b6y66qoxfPjwOPnkk2PZCiUFf/jDH2K77baLQYMGxUYbbRRXXXXVyvqIwAraW621eDvUm+6Ec83NhR8AAKC2lfE1v289+OCDsbzo8v8TTzwRH/vYx+LTn/50y7bPf/7zceaZZ7bcX3XVVVtuL1++PPbdd98YOXJkzJo1K+bPnx9HHnlkDBgwIL7zne9ERMS8efNi3333jS9+8Ysxffr0uOuuu+Jzn/tcjBo1KiZNmrQSPiWQSpLSyrmBA1sfM+8c9ao7ba3p8xpr/jIcAADUt5oP59Zdd92S+9/97ndjww03jF122aVl26qrrhojR45s9/l33HFH/PWvf40777wzRowYEdtss02cddZZceqpp8a0adNi4MCBcdlll8W4cePivPPOi4iIzTffPO6///644IILhHOwki1Z0np78OBCsDBwYGG7yjnqVXcq5yIK4dyAAb0zJgAAoDoydT19yZIl8ctf/jKOPvroaGhoaNk+ffr0WGeddWLLLbeM0047Ld55552Wx2bPnh3jx4+PESNGtGybNGlSNDU1xZNPPtmyzx577FHyXpMmTYrZs2d3OJbFixdHU1NTyQ/Qc8XVcel8c1Zspd51N5yzKAQAANS+mq+cKzZjxox488034zOf+UzLtkMPPTTGjh0bo0ePjsceeyxOPfXUeOaZZ+LGG2+MiIgFCxaUBHMR0XJ/wYIFne7T1NQU7777bqyyyiptxnL22WfHGWecUc2PB0RpAJe2tA4eHPHWWyrnqF9pW6twDgAA8idT4dwVV1wRe++9d4wePbpl2zHHHNNye/z48TFq1KjYfffd47nnnosNN9yw18Zy2mmnxYknnthyv6mpKcaMGdNr7wf1Ig3gBg5snStL5Rz1Lg3ZujPnHAAAUNsyE8698MILceedd7ZUxHVkwoQJERHx7LPPxoYbbhgjR46MBx54oGSfV199NSKiZZ66kSNHtmwr3mfIkCHtVs1FRAwaNCgGpYkBUDXFi0Gk0tsq56hXlbS1NjZGNDQUFldROQcAALUvM3POXXnllTF8+PDYd999O91v7ty5ERExatSoiIiYOHFiPP744/Haa6+17DNz5swYMmRIbLHFFi373HXXXSWvM3PmzJg4cWIVPwFQjvbCucGDSx+DelNJW2vxfsI5AACofZkI55qbm+PKK6+Mo446KvoXnZk899xzcdZZZ8WcOXPi+eefj5tvvjmOPPLI2HnnnWOrrbaKiIg999wztthiizjiiCPi0Ucfjdtvvz1OP/30mDp1akvl2xe/+MX4xz/+Eaeccko8/fTTcckll8T1118fJ5xwQp98XqhnaXVcGshFqJyDStpai/fT1goAALUvE+HcnXfeGS+++GIcffTRJdsHDhwYd955Z+y5556x2WabxUknnRQHHHBA/Pa3v23Zp1+/fnHLLbdEv379YuLEiXH44YfHkUceGWeeeWbLPuPGjYvf/e53MXPmzNh6663jvPPOi5/+9KcxadKklfYZgQKVc9BWJW2txfupnAMAgNqXiTnn9txzz0iSpM32MWPGxL333tvl88eOHRu33nprp/vsuuuu8cgjj3R7jEB1pAGcyjlopa0VAADyKxOVc0D9SAM4lXPQSlsr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pSt/TAC1QDhHt6ico9rKaWtVOUc90tYKQF60N8dw8W3f8YB6JZyjW1TOUW3ltLWqnKMepZVvwjkAsq69c4ji734u8gP1SjhHt3RWObdsmZJ0KldJW6urqtSTNFyrdM45ba0A1Jr2ziEaGiwKASCco1s6C+eKH4dyVdLWqnKOeqKtFYC8aK+ttfi+C7BAvarpcG7atGnR0NBQ8rPZZpu1PP7ee+/F1KlTY+21147VV189DjjggHj11VdLXuPFF1+MfffdN1ZdddUYPnx4nHzyybFshTOVP/zhD7HddtvFoEGDYqONNoqrrrpqZXy8TGsvnBs4sHDlK0JrK5Xr6MtaseK21iTp/TFBLdDWCkBetHcOUXzfBX6gXtV0OBcR8YEPfCDmz5/f8nP//fe3PHbCCSfEb3/727jhhhvi3nvvjVdeeSU+9alPtTy+fPny2HfffWPJkiUxa9as+PnPfx5XXXVVfOtb32rZZ968ebHvvvvGbrvtFnPnzo3jjz8+Pve5z8Xtt9++Uj9n1nRUkm5RCLqrksq5iIglS3p3PFArtLUCkBfCOYD2VXgdfuXr379/jBw5ss32hQsXxhVXXBHXXHNNfPSjH42IiCuvvDI233zz+POf/xwf/vCH44477oi//vWvceedd8aIESNim222ibPOOitOPfXUmDZtWgwcODAuu+yyGDduXJx33nkREbH55pvH/fffHxdccEFMmjRppX7WLOnswLpokco5KlfJghARhUq7zoI8yAttrQDkwbJlrcekjsI5ba1Avar5yrm///3vMXr06Nhggw3isMMOixdffDEiIubMmRNLly6NPfbYo2XfzTbbLN7//vfH7NmzIyJi9uzZMX78+BgxYkTLPpMmTYqmpqZ48sknW/Ypfo10n/Q1OrJ48eJoamoq+aknHYVzKuforkoWhIgw7xz1Q1srAHlQHLx1NOeccwigXtV0ODdhwoS46qqr4rbbbotLL7005s2bFzvttFO89dZbsWDBghg4cGAMGzas5DkjRoyIBQsWRETEggULSoK59PH0sc72aWpqinc7OTqcffbZMXTo0JafMWPG9PTjZkpXJekq56hEkpTX1trQUJjbMMKVVeqHtlYA8qD41EpbK0Cpmm5r3XvvvVtub7XVVjFhwoQYO3ZsXH/99bHKiv+PvpKddtppceKJJ7bcb2pqqquArqvKOeEc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TktrRMTYsRGrr14I5v72t+qNKy+Ec3SqWuFcuijEyphzrqHBvHO1rpptrSrnyKP0arVwDoAsSi+aVmPOORdge9e770bMnVu4vcMOEdtsU7ht3jlW1JPFICIK5+laWzsmnKNTWayci2gN58w7V5uq2daqco480tYKQJapnGvr8ccj9tkn4sEH+3okpR55pPC9Y/jwQmXTttu2bodiPVkMImVRiI5V4Zo8eVYrlXOVhnMWhaht1WxrVTlHHmlrBSDLhHNtnX9+xO9/X1gZ9fHHIwYO7OsRFaQtrR/+cKGyabvtCvdVzrGinlbORaic64zKOTpVjZWWip+/MhaEKN5fW2ttUjkHndPWCkCWaWtt649/LPz+298ifvCDvh1LsXQxiAkTCr/Tyrm5cyOSpE+GRA16992I558v3FY51zuEc3SqryvnutvWmrXKuddei2hu7utRrDwq56BzvdHWKpwDYGVROVdq/vxCxVzqzDMjFizou/EUK66ci4jYYotCVd+bb7aGMfDss4WwdtiwQgt0d6WVc//4R8SiRVUZWm4I5+hUtcO5Sirn3nmn9UpZnivnZsyIGDEi4txz+3okK081F4RQOUce9UZbqznnAFhZhHOl7r+/8Hv8+IgPfjDirbcivv71vh1TRCE0fPHFQjvrf/xHYdvAga0BitZWUsXzzTU0dP911l23cO4bEfHXv/Z8XHkinKNTfbkgRBqs9e8fscYalb1flirnfvnLwu/p0/t2HCtTNdtaVc6RR9paAciy9ByiGm2teQjn0pbWXXZpbWm98sq+XxwibWn9wAdKz7fSeecsCpENSRLx8su9+x7pfHM9aWlNpeGv1tZSwjk61ZdtrcXzzVWazmelcq65OeKeewq3H3+80N5aD6rZ1qpyjjzS1gpAllVj3ur0uXn4jpeGczvtFDFxYsThhxfuH3dc387rtmJLayqdd07lXDZccknEeutFXHpp771HNRaDSKXzzlkUopRwjk7VQuVcpfPNFT+n1ivnHn20NEBMg7q8q2Zbq8o58khbKwBZVs221vfey/bCBAsXRjz2WOH2Rz5S+P2970WstlrE7Nl92z2z4mIQqTScUzmXDWkn1ve/33vzmBe3tfaUyrn2CefoVK1UzlUqK5Vzd9/d+f286o3VWpcvVxlEfmhrBSDLqhnORWS7em727EJgssEGEaNHF7aNHh3x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QkKCdpmEhIRC34u5OivHZGraZ2XGNlKybdmUtWvXioiICOHq6ioefPBBsWXLFoPXld9yS9tycfYjo0eP1u6bAgMDxRNPPCGOHDli8N7FaSMrVqwQTZo00Z5Ptm7dWqxbt87iOqhM2EYqTxsRQiYWREdHCzc3N9GgQQMxbdo0gwuXxsda5upifDx28eJF8cwzzwhvb28RGBgohg4dWmEu8jgIUQVH6yYiIiIiIiIiIioHeLdWIiIiIiIiIiIiO2FwjoiIiIiIiIiIyE4YnCMiIiIiIiIiIrITBueIiIiIiIiIiIjshME5IiIiIiIiIiIiO2FwjoiIiIiIiIiIyE4YnCMiIiIiIiIiIrITBueIiIiIiIiIiIjshME5IiIiIiIiIiIiO2FwjoiIiIgKGTp0KBwcHODg4AAXFxcEBgaia9eu+Oyzz6DRaFSXs2LFCvj7+5deRYmIiIgqOAbniIiIiMikHj16ICMjA2lpadi2bRs6d+6MUaNGoWfPnsjPz7d39YiIiIgqBQbniIiIiMgkNzc31K5dG8HBwWjRogVef/11bNy4Edu2bcOKFSsAAPPnz8fDDz8MLy8vhISEYPjw4cjOzgYAJCUlITY2Frdu3dJm4U2ZMgUAkJOTg3HjxiE4OBheXl6Ijo5GUlKSfT4oERERkR0xOEdEREREqj322GOIiopCYmIiAMDR0RGLFy9GamoqPv/8c+zatQvjx48HALRt2xYLFy6Er68vMjIykJGRgXHjxgEARowYgQMHDmDNmjU4evQonnvuOfTo0QNnz56122cjIiIisgcHIYSwdyWIiIiIqHwZOnQoMjMz8e233xZ6rX///jh69ChOnDhR6LX169cjLi4O//zzDwA55tzo0aORmZmpXeavv/5CgwYN8NdffyEoKEg7v0uXLmjdujWmT59u889DREREVF4527sCRERERFSxCCHg4OAAAPjxxx8xY8YMnDp1Crdv30Z+fj7u37+Pu3fvwtPT0+T/Hzt2DAUFBYiIiDCYn5OTgxo1apR6/YmIiIjKEwbniIiIiMgqJ0+eRP369ZGWloaePXvilVdewbRp01C9enXs27cPw4YNQ25urtngXHZ2NpycnJCcnAwnJyeD17y9vcviIxARERGVGwzOEREREZFqu3btwrFjxzBmzBgkJydDo9Fg3rx5cHSUQxmvXbvWYHlXV1cUFBQYzGvevDkKCgpw9epVtG/fvszqTkRERFQeMThHRERERCbl5OTg8uXLKCgowJUrV7B9+3bMmDEDPXv2RExMDI4fP468vDwsWbIETz31FH7++WcsW7bMoIywsDBkZ2dj586diIqKgqenJyIiIjBw4EDExMRg3rx5aN68Oa5du4adO3eiadOmePLJJ+30iYmIiIjKHu/WSkREREQmbd++HXXq1EFYWBh69OiB3bt3Y/Hixdi4cSOcnJwQFRWF+fPnY9asWXjooYewevVqzJgxw6CMtm3bIi4uDv369UOtWrUwe/ZsAMDy5csRExOD//3vf4iMjESfPn1w+PBh1KtXzx4flYiIiMhueLdWIiIiIiIiIiIiO2HmHBERERERERERkZ0wOEdERERERERERGQnDM4RERERERERERHZCYNzREREREREREREdsLgHBERERERERERkZ0wOEdERERERERERGQnDM4RERERERERERHZCYNzREREREREREREdsLgHBERERERERERkZ0wOEdERERERERERGQnDM4RERERERERERHZyf8BTwMURqWFqyYAAAAASUVORK5CYII="/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
<p>4.5 Average Bid By Day</p>
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [12]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span><span class="kn">import</span> <span class="nn">matplotlib.pyplot</span> <span class="k">as</span> <span class="nn">plt</span>

<span class="n">query</span> <span class="o">=</span> <span class="s2">"""</span>
<span class="s2">    SELECT </span>
<span class="s2">        create_date DT_REF</span>
<span class="s2">        ,round(avg(ask),2) AvgAsk</span>
<span class="s2">        ,round(avg(bid),2) Avgbid</span>
<span class="s2">    FROM df </span>
<span class="s2">    where not code in ('BTC', 'ETH', 'LTC', 'DOGE')</span>
<span class="s2">    group by 1</span>
<span class="s2">    order by 1 </span>
<span class="s2">"""</span>

<span class="n">newDf</span> <span class="o">=</span> <span class="n">sqldf</span><span class="p">(</span><span class="n">query</span><span class="p">,</span> <span class="nb">locals</span><span class="p">())</span>
<span class="n">newDf</span><span class="o">.</span><span class="n">sort_values</span><span class="p">(</span><span class="n">by</span><span class="o">=</span><span class="s1">'DT_REF'</span><span class="p">,</span> <span class="n">ascending</span><span class="o">=</span><span class="kc">True</span><span class="p">,</span> <span class="n">inplace</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>

<span class="n">cht</span> <span class="o">=</span> <span class="n">newDf</span><span class="o">.</span><span class="n">plot</span><span class="p">(</span>
    <span class="n">kind</span><span class="o">=</span><span class="s1">'line'</span><span class="p">,</span> <span class="n">x</span><span class="o">=</span><span class="s1">'DT_REF'</span><span class="p">,</span> <span class="n">y</span><span class="o">=</span><span class="s1">'Avgbid'</span><span class="p">,</span>
    <span class="n">figsize</span><span class="o">=</span><span class="p">(</span><span class="mi">15</span><span class="p">,</span> <span class="mi">10</span><span class="p">),</span> 
    <span class="n">legend</span><span class="o">=</span><span class="kc">False</span><span class="p">,</span> 
    <span class="n">color</span><span class="o">=</span><span class="s1">'blue'</span><span class="p">,</span> <span class="n">title</span><span class="o">=</span><span class="s1">'Average BID tendence by Day'</span><span class="p">,</span> <span class="n">xlabel</span><span class="o">=</span><span class="s1">'Date'</span><span class="p">,</span> <span class="n">ylabel</span><span class="o">=</span><span class="s1">'Avgbid'</span><span class="p">)</span>

<span class="c1">#exibir o grafico</span>
<span class="n">plt</span><span class="o">.</span><span class="n">show</span><span class="p">()</span>
</pre></div>
</div>
</div>
</div>
</div>
<div class="jp-Cell-outputWrapper">
<div class="jp-Collapser jp-OutputCollapser jp-Cell-outputCollapser">
</div>
<div class="jp-OutputArea jp-Cell-outputArea">
<div class="jp-OutputArea-child">
<div class="jp-OutputPrompt jp-OutputArea-prompt"></div>
<div class="jp-RenderedImage jp-OutputArea-output" tabindex="0">
<img alt="No description has been provided for this image" class="" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABOcAAANXCAYAAAB+DztKAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjguNCwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy8fJSN1AAAACXBIWXMAAA9hAAAPYQGoP6dpAADDLUlEQVR4nOzdd5icZbk/8Hs3FQgJoSQhhxhCMfTqT4hIE0wCEcwRpEpRFDgGqSJyDgeDqDQBo1JEQY4SDuVQBEQwFCkSBAKhClICHJWACCTUtJ3fH3Pe3Zlsm5md+s7nc1177ezMOzPPhvBmnu9738/TkslkMgEAAAAAVF1rrQcAAAAAAM1KOAcAAAAANSKcAwAAAIAaEc4BAAAAQI0I5wAAAACgRoRzAAAAAFAjwjkAAAAAqBHhHAAAAADUiHAOAAAAAGpEOAcAQF26/PLLo6WlJV5++eVaD6VPpk+fHi0tLfHmm2/WeigAQB0SzgEAVXfhhRdGS0tLbLPNNrUeSt1Ze+21o6Wlpf1r8ODBsf7668eJJ54Yb731Vt6xXYU+hx56aN7zhwwZEuuss07svffecd1110VbW1tB47j11ltj+vTp5fzVqLCddtqp/b97a2trDB06NMaPHx8HHXRQzJo1q9bDAwC60b/WAwAAms/MmTNj7bXXjoceeiheeOGFWG+99Wo9pLqyxRZbxAknnBARER999FHMmTMnfvSjH8U999wTDz30UK/PHzRoUPziF7+IiIgPP/wwXnnllbj55ptj7733jp122il+85vfxNChQ3t8jVtvvTUuuOACAV2DWWutteKMM86IiIj3338/Xnjhhbj++uvjiiuuiH322SeuuOKKGDBgQI1HCQDkEs4BAFU1b968eOCBB+L666+PI444ImbOnBnf+c53qjqGtra2WLx4cQwePLiq71uof/mXf4kvfelL7T9/9atfjSFDhsQPf/jDeP7552P99dfv8fn9+/fPe35ExPe+970488wz4+STT46vfe1rcfXVV1dk7NTWsGHDOv23P/PMM+Poo4+OCy+8MNZee+0466yzajQ6AKAr2loBgKqaOXNmDB8+PKZMmRJ77713zJw5s/2xJUuWxKqrrhpf/vKXOz1v4cKFMXjw4PjmN7/Zft+iRYviO9/5Tqy33noxaNCgGDNmTHzrW9+KRYsW5T23paUljjrqqJg5c2ZsvPHGMWjQoLjtttsiIuKHP/xhfOpTn4rVVlstVlhhhdh6663jf/7nfzq9/4cffhhHH310rL766rHyyivHnnvuGX/729+ipaWlU3XZ3/72t/jKV74SI0eOjEGDBsXGG28cl112WV/+2GLUqFERkQ3eSvXtb387Jk6cGNdee2385S9/6fa4Qw89NC644IKIiLwW2URbW1v86Ec/io033jgGDx4cI0eOjCOOOCLefvvtvNdZe+2143Of+1zcf//98clPfjIGDx4c66yzTvzqV7/q9J5PP/10fOYzn4kVVlgh1lprrfje977XbQvu7373u9h+++1jpZVWipVXXjmmTJkSTz/9dKffYciQIfG3v/0tpk6dGkOGDIk11lgjvvnNb8ayZcvyjm1ra4sZM2bEpptuGoMHD4411lgjJk+eHI888kjecVdccUVsvfXWscIKK8Sqq64a++23X/zv//5vt3+Oy3vzzTdjn332iaFDh8Zqq60WxxxzTHz00Uftj++4446x+eabd/nc8ePHx6RJkwp+r1z9+vWLH//4x7HRRhvFT3/601iwYEH7Y7/85S/jM5/5TIwYMSIGDRoUG220UVx00UV5zz/kkENi9dVXjyVLlnR67YkTJ8b48eNLGhcAkCWcAwCqaubMmfGFL3whBg4cGPvvv388//zz8fDDD0dExIABA+Jf//Vf48Ybb4zFixfnPe/GG2+MRYsWxX777RcR2UBlzz33jB/+8Iexxx57xE9+8pOYOnVqnH/++bHvvvt2et+77rorjjvuuNh3331jxowZsfbaa0dExIwZM2LLLbeM7373u/GDH/wg+vfvH1/84hfjt7/9bd7zDz300PjJT34Su+++e5x11lmxwgorxJQpUzq9z+uvvx7bbrtt3HHHHXHUUUfFjBkzYr311ovDDjssfvSjHxX0Z7RkyZJ48803480334y//vWvcfPNN8d5550XO+ywQ4wbN66g1+jOQQcdFJlMpsc1yI444oj47Gc/GxERv/71r9u/ch8/8cQTY7vttosZM2bEl7/85Zg5c2ZMmjSpU4DzwgsvxN577x2f/exn49xzz43hw4fHoYcemhemzZ8/P3beeeeYO3dufPvb345jjz02fvWrX8WMGTM6je3Xv/51TJkyJYYMGRJnnXVW/Od//mc888wz8elPf7rTxhHLli2LSZMmxWqrrRY//OEPY8cdd4xzzz03LrnkkrzjDjvssDj22GNjzJgxcdZZZ8W3v/3tGDx4cDz44IPtx3z/+9+Pgw8+ONZff/0477zz4thjj40777wzdthhh3jnnXd6/XOPiNhnn33io48+ijPOOCN23333+PGPfxyHH354++MHHXRQPPHEE/HUU0/lPe/hhx+Ov/zlL50q4orRr1+/2H///eODDz6I+++/v/3+iy66KMaOHRv//u//Hueee26MGTMmvv71r7eHs8m4/vnPf8btt9+e95rz58+Pu+66q0/jAgAiIgMAUCWPPPJIJiIys2bNymQymUxbW1tmrbXWyhxzzDHtx9x+++2ZiMjcfPPNec/dfffdM+uss077z7/+9a8zra2tmfvuuy/vuIsvvjgTEZk//vGP7fdFRKa1tTXz9NNPdxrTBx98kPfz4sWLM5tssknmM5/5TPt9c+bMyURE5thjj8079tBDD81EROY73/lO+32HHXZYZs0118y8+eabecfut99+mWHDhnV6v+WNHTs2ExGdvrbbbrtOr/md73wnExGZf/zjH+33HXLIIZmVVlqp29d/7LHHMhGROe6443ocx7Rp0zJdfVS87777MhGRmTlzZt79t912W6f7k9/l3nvvbb/vjTfeyAwaNChzwgkntN937LHHZiIi86c//SnvuGHDhmUiIjNv3rxMJpPJvPvuu5lVVlkl87WvfS3vvefPn58ZNmxY3v2HHHJIJiIy3/3ud/OO3XLLLTNbb711+8933XVXJiIyRx99dKffta2tLZPJZDIvv/xypl+/fpnvf//7eY8/+eSTmf79+3e6f3nJf6c999wz7/6vf/3rmYjIPP7445lMJpN55513MoMHD86cdNJJeccdffTRmZVWWinz3nvv9fg+O+64Y2bjjTfu9vEbbrghExGZGTNmtN/X1d/HSZMm5f2/tmzZssxaa62V2XffffOOO++88zItLS2Zl156qcdxAQA9UzkHAFTNzJkzY+TIkbHzzjtHRLZlct99942rrrqqvdXwM5/5TKy++up5a6K9/fbbMWvWrLyKuGuvvTY23HDD2GCDDdqrzN588834zGc+ExERd999d95777jjjrHRRht1GtMKK6yQ9z4LFiyI7bffPh599NH2+5MW2K9//et5z/3GN76R93Mmk4nrrrsu9thjj8hkMnnjmjRpUixYsCDvdbuzzTbbxKxZs2LWrFlxyy23xPe///14+umnY88994wPP/yw1+f3ZMiQIRER8e6775b0/GuvvTaGDRsWn/3sZ/N+v6233jqGDBnS6c99o402iu2337795zXWWCPGjx8fL730Uvt9t956a2y77bbxyU9+Mu+4Aw88MO+1Zs2aFe+8807sv//+ee/dr1+/2GabbTq9d0TEkUcemffz9ttvn/fe1113XbS0tHS57mHSynv99ddHW1tb7LPPPnnvO2rUqFh//fW7fN+uTJs2Le/n5O/PrbfeGhHZ9eI+//nPx3//939HJpOJiGz139VXXx1Tp06NlVZaqaD36U5X/+1z//4vWLAg3nzzzdhxxx3jpZdeam9/bW1tjQMPPDBuuummvOfOnDkzPvWpT/W5mhMAmp0NIQCAqli2bFlcddVVsfPOO8e8efPa799mm23i3HPPjTvvvDMmTpwY/fv3j7322iuuvPLKWLRoUQwaNCiuv/76WLJkSV449/zzz8ef//znWGONNbp8vzfeeCPv5+4ChFtuuSW+973vxdy5c/PWqstdY+2VV16J1tbWTq+x/C6z//jHP+Kdd96JSy65pFPrZHfj6srqq68eu+66a/vPU6ZMifHjx8fee+8dv/jFLzqFgsV47733IiJi5ZVXLun5zz//fCxYsCBGjBjR5ePL/34f+9jHOh0zfPjwvPXpXnnlldhmm206Hbf8WmbPP/98RER7ALu85XegTdaP6+m9X3zxxRg9enSsuuqqXb5m8r6ZTKbbjTgK3f10+eevu+660dramteOe/DBB8fVV18d9913X+ywww5xxx13xOuvvx4HHXRQQe/Rk67+2//xj3+M73znOzF79uz44IMP8o5fsGBBDBs2rH1cZ511Vtxwww1x8MEHx3PPPRdz5syJiy++uM/jAoBmJ5wDAKrirrvuitdeey2uuuqquOqqqzo9PnPmzJg4cWJEROy3337xs5/9LH73u9/F1KlT45prrokNNtggb7H8tra22HTTTeO8887r8v3GjBmT93NuhVDivvvuiz333DN22GGHuPDCC2PNNdeMAQMGxC9/+cu48sori/4dkw0MvvSlL8UhhxzS5TGbbbZZ0a8bEbHLLrtERMS9997bp3AuWc9s+WCxUG1tbTFixIi8jTxyLR+G9evXr8vjksqwYt87IrvuXLJBRq7lN8vo7r1Led+Wlpb43e9+1+VrJhVpxcoNgBOTJk2KkSNHxhVXXBE77LBDXHHFFTFq1Ki8sLZUy/+3f/HFF2OXXXaJDTbYIM4777wYM2ZMDBw4MG699dY4//zz8zbk2GijjWLrrbeOK664Ig4++OC44oorYuDAgbHPPvv0eVwA0OyEcwBAVcycOTNGjBiRt9B84vrrr48bbrghLr744lhhhRVihx12iDXXXDOuvvrq+PSnPx133XVX/Md//Efec9Zdd914/PHHY5ddduky5CjEddddF4MHD47bb789Bg0a1H7/L3/5y7zjxo4dG21tbTFv3ry86qcXXngh77g11lgjVl555Vi2bFlZwpRcS5cujYiO6qdS/frXv46Wlpb2DR+6092f6brrrht33HFHbLfddl0GnqUYO3Zse1Vcrueee67Te0dEjBgxomx/vuuuu27cfvvt8dZbb3VbPbfuuutGJpOJcePGxcc//vGS3+v555/Pq7584YUXoq2trX1zkohsoHjAAQfE5ZdfHmeddVbceOON8bWvfa3PQeOyZcviyiuvjBVXXDE+/elPR0TEzTffHIsWLYqbbropr8Kxuzbdgw8+OI4//vh47bXX4sorr4wpU6bE8OHD+zQuAMBurQBAFXz44Ydx/fXXx+c+97nYe++9O30dddRR8e6778ZNN90UEdk1rvbee++4+eab49e//nUsXbq00w6s++yzT/ztb3+Ln//8512+3/vvv9/ruPr16xctLS3t691FRLz88stx44035h03adKkiIi48MIL8+7/yU9+0un19tprr7juuus67bgZkW17LdXNN98cEZFXPVisM888M37/+9/Hvvvu222LZiJZ32z5nUj32WefWLZsWZx++umdnrN06dKCdy7Ntfvuu8eDDz4YDz30UPt9//jHPzpV502aNCmGDh0aP/jBDzrtCps8p1h77bVXZDKZOO200zo9llT3feELX4h+/frFaaed1qniL5PJxD//+c+C3mv5YDr5+7Pbbrvl3X/QQQfF22+/HUcccUS89957fd4NddmyZXH00UfHn//85zj66KPb23+TwC/3d1qwYEGncDqx//77R0tLSxxzzDHx0ksv2aUVAMpE5RwAUHHJQvJ77rlnl49vu+22scYaa8TMmTPbQ7h99903fvKTn8R3vvOd2HTTTWPDDTfMe85BBx0U11xzTRx55JFx9913x3bbbRfLli2LZ599Nq655pq4/fbb4xOf+ESP45oyZUqcd955MXny5DjggAPijTfeiAsuuCDWW2+9eOKJJ9qP23rrrWOvvfaKH/3oR/HPf/4ztt1227jnnnviL3/5S0TkV5mdeeaZcffdd8c222wTX/va12KjjTaKt956Kx599NG444474q233ur1z+tvf/tbXHHFFRERsXjx4nj88cfjZz/7Way++uoFtbQuXbq0/fkfffRRvPLKK3HTTTfFE088ETvvvHO36+Hl2nrrrSMi4uijj45JkyZFv379Yr/99osdd9wxjjjiiDjjjDNi7ty5MXHixBgwYEA8//zzce2118aMGTNi77337vX1c33rW9+KX//61zF58uQ45phjYqWVVopLLrkkxo4dm/ffYejQoXHRRRfFQQcdFFtttVXst99+scYaa8Srr74av/3tb2O77baLn/70p0W998477xwHHXRQ/PjHP47nn38+Jk+eHG1tbXHffffFzjvvHEcddVSsu+668b3vfS9OPvnkePnll2Pq1Kmx8sorx7x58+KGG26Iww8/PL75zW/2+l7z5s2LPffcMyZPnhyzZ8+OK664Ig444IBOgeuWW24Zm2yySfumJ1tttVXBv8+CBQva/9t/8MEH8cILL8T1118fL774Yuy33355oerEiRNj4MCBsccee7QHgT//+c9jxIgR8dprr3V67TXWWCMmT54c1157bayyyioxZcqUgscFAPSgRrvEAgBNZI899sgMHjw48/7773d7zKGHHpoZMGBA5s0338xkMplMW1tbZsyYMZmIyHzve9/r8jmLFy/OnHXWWZmNN944M2jQoMzw4cMzW2+9dea0007LLFiwoP24iMhMmzaty9e49NJLM+uvv35m0KBBmQ022CDzy1/+MvOd73wns/zHpPfffz8zbdq0zKqrrpoZMmRIZurUqZnnnnsuExGZM888M+/Y119/PTNt2rTMmDFjMgMGDMiMGjUqs8suu2QuueSSXv+sxo4dm4mI9q/W1tbMiBEjMvvvv3/mhRdeyDs2Gec//vGP9vsOOeSQvOevuOKKmbXXXjuz1157Zf7nf/4ns2zZsl7HkMlkMkuXLs184xvfyKyxxhqZlpaWTn8el1xySWbrrbfOrLDCCpmVV145s+mmm2a+9a1vZf7+97/n/S5Tpkzp9No77rhjZscdd8y774knnsjsuOOOmcGDB2f+5V/+JXP66adnLr300kxEZObNm5d37N13352ZNGlSZtiwYZnBgwdn1l133cyhhx6aeeSRR/L+HFZaaaVO793Vf9ulS5dmzjnnnMwGG2yQGThwYGaNNdbI7Lbbbpk5c+bkHXfddddlPv3pT2dWWmmlzEorrZTZYIMNMtOmTcs899xzPf5ZJu/5zDPPZPbee+/MyiuvnBk+fHjmqKOOynz44YddPufss8/ORETmBz/4QY+vnWvHHXfM+28/ZMiQzPrrr5/50pe+lPn973/f5XNuuummzGabbZYZPHhwZu21186cddZZmcsuu6zLP/dMJpO55pprMhGROfzwwwseFwDQs5ZMpoTVeAEAiLlz58aWW24ZV1xxRRx44IG1Hg4pMmPGjDjuuOPi5Zdf7nLH21r5zW9+E1OnTo177703tt9++1oPBwBSQTgHAFCADz/8sNMGCIceemj8+te/jpdffrnT7rBQqkwmE5tvvnmsttpq3W7OUCuf+9zn4s9//nO88MILJW/EAgDks+YcAEABzj777JgzZ07svPPO0b9///jd734Xv/vd7+Lwww8XzFEW77//ftx0001x9913x5NPPhm/+c1vaj2kdldddVU88cQT8dvf/jZmzJghmAOAMlI5BwBQgFmzZsVpp50WzzzzTLz33nvxsY99LA466KD4j//4j+jf3/VO+u7ll1+OcePGxSqrrBJf//rX4/vf/36th9SupaUlhgwZEvvuu29cfPHF/s4DQBkJ5wAAAACgRlprPQAAAAAAaFbCOQAAAACoEYtFlElbW1v8/e9/j5VXXtkCuQAAAABNLpPJxLvvvhujR4+O1tbu6+OEc2Xy97//3U5tAAAAAOT53//931hrrbW6fVw4VyYrr7xyRGT/wIcOHVrj0QAAAABQSwsXLowxY8a0Z0bdEc6VSdLKOnToUOEcAAAAABERvS5/ZkMIAAAAAKgR4RwAAAAA1IhwDgAAAABqRDgHAAAAADUinAMAAACAGhHOAQAAAECNCOcAAAAAoEaEcwAAAABQI8I5AAAAAKgR4RwAAAAA1IhwDgAAAABqRDgHAAAAADUinAMAAACAGhHOAQAAAECNCOcAAAAAoEZqGs7de++9sccee8To0aOjpaUlbrzxxrzHW1pauvw655xz2o9Ze+21Oz1+5pln5r3OE088Edtvv30MHjw4xowZE2effXansVx77bWxwQYbxODBg2PTTTeNW2+9tSK/MwAAAAAkahrOvf/++7H55pvHBRdc0OXjr732Wt7XZZddFi0tLbHXXnvlHffd734377hvfOMb7Y8tXLgwJk6cGGPHjo05c+bEOeecE9OnT49LLrmk/ZgHHngg9t9//zjssMPisccei6lTp8bUqVPjqaeeqswvDgAAAAAR0ZLJZDK1HkREtkruhhtuiKlTp3Z7zNSpU+Pdd9+NO++8s/2+tddeO4499tg49thju3zORRddFP/xH/8R8+fPj4EDB0ZExLe//e248cYb49lnn42IiH333Tfef//9uOWWW9qft+2228YWW2wRF198cUHjX7hwYQwbNiwWLFgQQ4cOLeg5AAAAAKRToVlRw6w59/rrr8dvf/vbOOywwzo9duaZZ8Zqq60WW265ZZxzzjmxdOnS9sdmz54dO+ywQ3swFxExadKkeO655+Ltt99uP2bXXXfNe81JkybF7Nmzux3PokWLYuHChXlfAAAAAFCM/rUeQKH+67/+K1ZeeeX4whe+kHf/0UcfHVtttVWsuuqq8cADD8TJJ58cr732Wpx33nkRETF//vwYN25c3nNGjhzZ/tjw4cNj/vz57fflHjN//vxux3PGGWfEaaedVo5fDQAAAIAm1TDh3GWXXRYHHnhgDB48OO/+448/vv32ZpttFgMHDowjjjgizjjjjBg0aFDFxnPyySfnvffChQtjzJgxFXs/AAAAANKnIcK5++67L5577rm4+uqrez12m222iaVLl8bLL78c48ePj1GjRsXrr7+ed0zy86hRo9q/d3VM8nhXBg0aVNHwDwAAAID0a4g15y699NLYeuutY/PNN+/12Llz50Zra2uMGDEiIiImTJgQ9957byxZsqT9mFmzZsX48eNj+PDh7cfkbjKRHDNhwoQy/hYAAAAAkK+m4dx7770Xc+fOjblz50ZExLx582Lu3Lnx6quvth+zcOHCuPbaa+OrX/1qp+fPnj07fvSjH8Xjjz8eL730UsycOTOOO+64+NKXvtQevB1wwAExcODAOOyww+Lpp5+Oq6++OmbMmJHXknrMMcfEbbfdFueee248++yzMX369HjkkUfiqKOOquwfAAAAAABNrSWTyWRq9eZ/+MMfYuedd+50/yGHHBKXX355RERccsklceyxx8Zrr70W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AQAgHep+zbk//OEPMWLEiBg/fnz827/9W/zzn/9sf2z27NmxyiqrtAdzERG77rprtLa2xp/+9Kf2Y3bYYYcYOHBg+zGTJk2K5557Lt5+++32Y3bddde89500aVLMnj2723EtWrQoFi5cmPfVjIRzALWxfFurczAAADSmug7nJk+eHL/61a/izjvvjLPOOivuueee2G233WLZ/81I5s+fHyNGjMh7Tv/+/WPVVVeN+fPntx8zcuTIvGOSn3s7Jnm8K2eccUYMGzas/WvMmDF9+2UblHAOoPra2rJfEdacAwCARlfTttbe7Lfffu23N91009hss81i3XXXjT/84Q+xyy671HBkESeffHIcf/zx7T8vXLiwKQM64RxA9eUGcdpaAQCgsdV15dzy1llnnVh99dXjhRdeiIiIUaNGxRtvvJF3zNKlS+Ott95qX6du1KhR8frrr+cdk/zc2zHdrXUXkV0Lb+jQoXlfzUg4B1B9uedbba0AANDYGiqc++tf/xr//Oc/Y80114yIiAkTJsQ777wTc+bMaT/mrrvuira2tthmm23aj7n33ntjyZIl7cfMmjUrxo8fH8OHD28/5s4778x7r1mzZsWECRMq/Ss1POEcQPXlVs5pawUAgMZW03Duvffei7lz58bcuXMjImLevHkxd+7cePXVV+O9996LE088MR588MF4+eWX484774zPf/7zsd5668WkSZMiImLDDTeMyZMnx9e+9rV46KGH4o9//GMcddRRsd9++8Xo0aMjIuKAAw6IgQMHxmGHHRZPP/10XH311TFjxoy8ltRjjjkmbrvttjj33HPj2WefjenTp8cjjzwSRx11VNX/TBqNcA6g+nLPt9paAQCgsdU0nHvkkUdiyy23jC233DIiIo4//vjYcsst49RTT41+/frFE088EXvuuWd8/OMfj8MOOyy23nrruO+++2JQUiYQETNnzowNNtggdtlll9h9993j05/+dFxyySXtjw8bNix+//vfx7x582LrrbeOE044IU499dQ4/PDD24/51Kc+FVdeeWVccsklsfnmm8f//M//xI033hibbLJJ9f4wGpRwDqD6hHMAAJAeLZlMJlPrQaTBwoULY9iwYbFgwYKmWn9uxx0j7r03e3uttSL+939rOx6AZvD66xHJsqhXXx2x774RO+0UcffdNR0WAACQo9CsqKHWnKP+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MX369Ljkkkvaj3nggQdi//33j8MOOywee+yxmDp1akydOjWeeuqpyvziKZBM/rpqqzIxBKicrsK51tbOjwMAAI2hf++HVM5uu+0Wu+22W5ePDRs2LGbNmpV3309/+tP45Cc/Ga+++mp87GMfa79/5ZVXjlGjRnX5OjNnzozFixfHZZddFgMHDoyNN9445s6dG+edd14cfvjhERExY8aMmDx5cpx44okREXH66afHrFmz4qc//WlcfPHF5fhVU0dbK0BtdLXmXEtL9udly7S1AgBAo2moNecWLFgQLS0tscoqq+Tdf+aZZ8Zqq60WW265ZZxzzjmxNCcdmj17duywww4xcODA9vsmTZoUzz33XLz99tvtx+y66655rzlp0qSYPXt2t2NZtGhRLFy4MO+rmQjnAGqjq/Nv7s/OwQAA0FhqWjlXjI8++ihOOumk2H///WPo0KHt9x999NGx1VZbxaqrrhoPPPBAnHzyyfHaa6/FeeedFxER8+fPj3HjxuW91siRI9sfGz58eMyfP7/9vtxj5s+f3+14zjjjjDjttNPK9es1HOEcQG30FM4tWuQcDAAAjaYhwrklS5bEPvvsE5lMJi666KK8x44//vj225tttlkMHDgwjjjiiDjjjDNi0KBBFRvTySefnPfeCxcujDFjxlTs/eqNcA6gNrpqa839WVsrAAA0lroP55Jg7pVXXom77rorr2quK9tss00sXbo0Xn755Rg/fnyMGjUqXn/99bxjkp+Tdeq6O6a7dewiIgYNGlTR8K/eCecAakNbKwAApEtdrzmXBHPPP/983HHHHbHaaqv1+py5c+dGa2trjBgxIiIiJkyYEPfee28sWbKk/ZhZs2bF+PHjY/jw4e3H3HnnnXmvM2vWrJgwYUIZf5t06Smcy/mjBqDMhHMAAJAuNa2ce++99+KFF15o/3nevHkxd+7cWHXVVWPNNdeMvffeOx599NG45ZZbYtmyZe1rwK266qoxcODAmD17dvzpT3+KnXfeOVZeeeWYPXt2HHfccfGlL32pPXg74IAD4rTTTovDDjssTjrppHjqqadixowZcf7557e/7zHHHBM77rhjnHvuuTFlypS46qqr4pFHHolLLrmkun8gDUTlHEBtaGsFAIB0qWk498gjj8TOO+/c/nOyhtshhxwS06dPj5tuuikiIrbYYou85919992x0047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MU888URsv/32MXjw4BgzZkycffbZncZy7bXXxgYbbBCDBw+OTTfdNG699day/75poXIOoDaEcwAAkD41Defef//92HzzzeOCCy7o8vGzzz47fvzjH8fFF18cf/rTn2KllVaKSZMmxUcffdR+zIEHHhhPP/10zJo1K2655Za499574/DDD29/fOHChTFx4sQYO3ZszJkzJ84555yYPn16XHLJJe3HPPDAA7H//vvHYYcdFo899lhMnTo1pk6dGk899VTlfvkGJpwDqA1trQAAkD7dXHuvjt122y122223Lh/LZDLxox/9KE455ZT4/Oc/HxERv/rVr2LkyJFx4403xn777Rd//vOf47bbbouHH344PvGJT0RExE9+8pPYfffd44c//GGMHj06Zs6cGYsXL47LLrssBg4cGBtvvHHMnTs3zjvvvPYQb8aMGTF58uQ48cQTIyLi9NNPj1mzZsVPf/rTuPjii6vwJ9FYkuCtq8mhcA6gclTOAQBA+tTtmnPz5s2L+fPnx6677tp+37Bhw2KbbbaJ2bNnR0TE7NmzY5VVVmkP5iIidt1112htbY0//elP7cfssMMOMXDgwPZjJk2aFM8991y8/fbb7cfkvk9yTPI+XVm0aFEsXLgw76tZqJwDqA3hHAAApE/dhnPz58+PiIiRI0fm3T9y5Mj2x+bPnx8jRozIe7x///6x6qqr5h3T1Wvkvkd3xySPd+WMM86IYcOGtX+NGTOm2F+xYRUSzrW1Zb8AKJ9C21qFcwAA0DjqNpyrdyeffHIsWLCg/et///d/az2kqikknMs9DoDyKLRyzppzAADQOOo2nBs1alRERLz++ut597/++uvtj40aNSreeOONvMeXLl0ab731Vt4xXb1G7nt0d0zyeFcGDRoUQ4cOzftqFsI5gNrQ1goAAOlTt+HcuHHjYtSoUXHnnXe237dw4cL405/+FBMmTIiIiAkTJsQ777wTc+bMaT/mrrvuira2tthmm23aj7n33ntjyZIl7cfMmjUrxo8fH8OHD28/Jvd9kmOS9yGfcA6gNrS1AgBA+tQ0nHvvvfdi7ty5MXfu3IjIbgIxd+7cePXVV6OlpSWOPfbY+N73vhc33XRTPPnkk3HwwQfH6NGjY+rUqRERseGGG8bkyZPja1/7Wjz00EPxxz/+MY466qjYb7/9YvTo0RERccABB8TAgQPj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eSXuuOOO+OpXv9rjcdtss01ERLzwwgsRETFq1Kh4/fXX845Jfk7WqevumKFDh3ZZNRcRMWjQoBg6dGjeV9oJ56iGpDqupaWjpTVZZ07lHM2qmGUFll9zDgAAqG8NE8798pe/jBEjRsSUKVN6PG7u3LkREbHmmmtGRMSECRPiySefjDfeeKP9mFmzZsXQoUNjo402aj/mzjvvzHudWbNmxYQJE8r4GzS+YsK5JFQRzlGs3M0gkqUlkwo6lXM0q2LOv62tHf/vOAcDAED9a4hwrq2tLX75y1/GIYccEv1zZiYvvvhinH766TFnzpx4+eWX46abboqDDz44dthhh9hss80iImLixImx0UYbxUEHHRSPP/543H777XHKKafEtGnTYtD/zfiPPPLIeOmll+Jb3/pWPPvss3HhhRfGNddcE8cdd1xNft96pXKOasgN5xIq52h2xbS15h7nHAwAAPWvIcK5O+64I1599dX4yle+knf/wIED44477oiJEyfGBhtsECeccELstddecfPNN7cf069fv7jllluiX79+MWHChPjSl74UBx98cHz3u99tP2bcuHHx29/+NmbNmhWbb755nHvuufGLX/wiJk2aVLXfsREI56iGJIBLArkIlXNQTFtr7nHaWgEAoP41xIYQEydOjEwm0+n+MWPGxD333NPr88eOHRu33nprj8fstNNO8dhjj5U8xmYgnKMaVM5BZ8Wcf3OPcw4GAID61xCVc9QH4RzVoHIOOtPWCgAA6SWco2DCOaqhq8q55LbKOZqVtlYAAEgv4RwFE85RDT21taqco1lpawUAgPQSzlGwYtqqTAwpVU9trSrnaFbCOQAASC/hHAVTOUc1qJyDzpKLI9paAUiL//iPiMmTzRcAIhpkt1bqg3COakgCOBtCQAeVcwCkzUUXRbz9dsSf/xyx6aa1Hg1Abamco2DCOaohaV3tqnJOWyvNSjgHQNp88EH2+4cf1nYcAPVAOEfBhHNUQ0+7taqco1mV2tbqHAxAPWpr6/hcJ5wDEM5RhFLCuSVLKjce0qmrDSFUztHsSq2cs+YcAPUo9zOdcA5AOEcRkslhIZUbKucolco56ExbKwBpkhvOufgKIJyjCNpaqYaedmv14Y1mpa0VgDTJrZZTOQcgnKMIwjmqoau2VpVzNDttrQCkiXAOIJ9wjoIJ56gGlXPQmbZWANJE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+umnx0knnRTTp0+PgQMHxsUXXxzjxo2Lc889NyIiNtxww7j//vvj/PPPj0mTJlX1d61npYZzAwbkPx+6U8yGEBHZMG/FFSs7JqgHLo4AkBbCOYCu1X3l3PPPPx+jR4+OddZZJw488MB49dVXIyJizpw5sWTJkth1113bj91ggw3iYx/7WMyePTsiImbPnh2bbrppjBw5sv2YSZMmxcKFC+Ppp59uPyb3NZJjktfozqJFi2LhwoV5X2lmckilFVM5F2FNEpqHtlYA0iCTEc4BdKeuw7ltttkmLr/88rjtttvioosuinnz5sX2228f7777bsyfPz8GDhwYq6yySt5zRo4cGfPnz4+IiPnz5+cFc8njyWM9HbNw4cL4sId/Hc4444wYNmxY+9eYMWP6+uvWtVLbqkwOKVQhG0L07x/R2pp/PKSdtlYA0mDp0oi2tuzt5T/vJT+7+Ao0q7pua91tt93ab2+22WaxzTbbxNixY+Oaa66JFZa/3FJlJ598chx//PHtPy9cuDDVAZ3KOSqprS1iyZLs7Z4q51paso9/+KFwjubh/AtAGuTWPaicA8hX15Vzy1tllVXi4x//eLzwwgsxatSoWLx4cbzzzjt5x7z++uvta9SNGjWq0+6tyc+9HTN06NAeA8BBgwbF0KFD877SzOSQSsoN2noK5yJcWaX5OP8CkAa5wdvylXPCOaDZNVQ4995778WLL74Ya665Zmy99dYxYMCAuPPOO9sff+655+LVV1+NCRMmRETEhAkT4sknn4w33nij/ZhZs2bF0KFDY6ONNmo/Jvc1kmOS1yDL5JBKyg3nemprjegI71TO0SySttRS21qdfwGoB0nwNnhwthsil3AOaHZ1Hc5985vfjHvuuSdefvnleOCBB+Jf//Vfo1+/frH//vvHsGHD4rDDDovjjz8+7r777pgzZ058+ctfjgkTJsS2224bERETJ06MjTbaKA466KB4/PHH4/bbb49TTjklpk2bFoP+b4Z/5JFHxksvvRTf+ta34tlnn40LL7wwrrnmmjjuuONq+avXHeEclZRUwbW09P53TOUczaav519rzgFQD5LPbl1diPX5Dmh2db3m3F//+tfYf//945///GesscYa8elPfzoefPDBWGONNSIi4vzzz4/W1tbYa6+9YtGiRTFp0qS48MIL25/fr1+/uOWWW+Lf/u3fYsKE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LeL000+Pk046KaZPnx4DBw6Miy++OMaNGxfnnntuRERsuOGGcf/998f5558fkyZNqtwv2ADqbXK4/HpzubeFc42nHGvOtbVl/2715e8o1KOk2k1bKwCNSlsrQGHqunJueQsWLIiIiFVzy6YiYubMmbH66qvHJptsEieffHJ88MEH7Y/Nnj07Nt100xg5cmT7fZMmTYqFCxfG008/3X7MrrvumveakyZNitmzZ3c7lkWLFsXChQvzvtKokcK5pOWVxlGO3VojXFklnbS1AtDohHMAhWmYWpO2trY49thjY7vttotNNtmk/f4DDjggxo4dG6NHj44nnngiTjrppHjuuefi+uuvj4iI+fPn5wVzEdH+8/z583s8ZuHChfHhhx/GCl38a3LGGWfEaaedVtbfsR6VY0FylXN0py9trbnPWbQoYsiQ8owJ6kW9XRwBgGIJ5wAK0zDh3LRp0+Kpp56K+++/P+/+ww8/vP32pptuGmuuuWbssssu8eKLL8a6665bsfGcfPLJcfzxx7f/vHDhwhgzZkzF3q9W6m1y2FM49/bb2RbH1oaqB21ufamc69cv+7Vsmco50klbKwCNLvmMVsqGED7fAc2kIWKMo446Km655Za4++67Y6211urx2G222SYiIl544YWIiBg1alS8/vrrecckPyfr1HV3zNChQ7usmouIGDRoUAwdOjTvK40aIZxLupzb2iLeeafv70H19KVyLqLjw5sdW0mjcp5/I7LnSACoJpVzAIWp63Auk8nEUUcdFTfccEPcddddMW7cuF6fM3fu3IiIWHPNNSMiYsKECfHkk0/GG2+80X7MrFmzYujQobHRRhu1H3PnnXfmvc6sWbNiwoQJZfpNGlcjhHMDB3a0NGptbRzJRg4RpYdzyfNcWSWNyh3OqZ4DoNqEcwCFqetwbtq0aXHFFVfElVdeGSuvvHLMnz8/5s+fHx/+35n6xRdfjNNPPz3mzJkTL7/8ctx0001x8MEHxw477BCbbbZZRERMnDgxNtpoozjooIPi8ccfj9tvvz1OOeWUmDZtWgz6v5n9kUceGS+99FJ861vfimeffTYuvPDCuOaaa+K4446r2e9eL+otnEs2fcgN53J/Fs41jtxqt1LaWnOfp3KONCpHW6twDoBaEs4BFKauw7mLLrooFixYEDvttFOsueaa7V9XX311REQMHDgw7rjj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xx/PH2MS1KWdyjnombZWABpZudtaG31tqiSc23HHiE9+MmLatOzPX/96bT/DLr/eXMKmEI3l1FMjjjwy4sQTK/ceSeWccK5yhHN0qxKTwyVLCn9OqZtB5D6n3ivn7rqr55/TqpwbQiSvsXhx439wg4S2VgAaWTnDuba24uYQ9WbhwohHH83e3mGH7PfvfS9izTUjnn8+4owzaje25debSwjnGsstt2S//+pX2b9vlVCuttaI/E0h6CCco1u1rpxLgrWkCq4YjRLO3Xln9vtnPpP/c9qVs601t/pOaytpoa0VgEZWznAu9/Ua0QMPZAPGddaJWGut7H3DhkXMmJG9fcYZHS2D1dTWFvHgg9nby1fObbVV9rtNIerfCy9EvPRS9vb770f8+tflf49ly7IbQkSUt3LumWd8Ps0lnKNb9RLOpbVybvHijhL36dOzE+gXX+zYojrNytnWmhvwCedIC22tADSycmwIMXBgdm223NdrRPfck/2eVM0l9t47Yvfds1WBRx5Z/Q6QP/85u1bZSit1hCWJYcM6Fu1XPVffbr89+z35vHfRReX/uzRvXnbuOnhwxMc+1vfXW2ediBVXzBZsvPBC318vLYRzdKuclRu1Cufeead+J6QPP5y9urH66hHbbZddfyKiOdadK2fl3MCBHbffey/itdciHnss4rbbIi6/POKssyKOOy7igAOyFYoHHijEo/7V+uIIAPRFOTaEaGlJx9rCuevN5Wppibjgguyf0T33ZFsSqylZb+6Tn+z684bW1sZw223Z79/8ZjbwevrpiPvvL+97JJWd48eXJxtobY3YeOPsba2tHYRzdKvWk8O+hHNJK2wmE/H228U/vxqSFtadd86eoJLW1mZYd66ca861tHS8zlprRYwenS3F3223iC9/OeLb34740Y8i/vu/s8HnlVdG/OY3fX9fqKTkooK2VgAaUTnaWnOf36iVcx98kL0gH9G5ci4iYu21I77zneztE06IePPNqg2t2/XmEsK5+rd4cUdhxz77ZIsQIiIuvLC871PO9eYS1p3rTDhHt8oZzg0YkP+ahehLONe/f7YcO/d16k0SwiWhXO66c2nf2KCcba0R+aX4ra0Ro0ZFbL55xMSJEQcfnN256Ic/jNhrr+wx//M/5XlfqJRKXBxpa0v/uQWA+iCcy3rwwWzb6lprRYwb1/Uxxx8fsckm2TnLt75VvbF1t1NrQjhX//74x2wn1ogR2bnPv/1b9v7rrot4/fXyvU9SOVeO9eYSdmztrAwf+0mrWlfOvfVW9nsp4VxEtnpuwYKO16knH3zQcbVql12y3ydMyFaA/f3v2QU3x4+v3fgqKZMpb+VcRMR992XXKxgxIvv3pbtqo0ceyf5jdeut2Q95ff3ACJVSifNvRLYirxyvCQDdyWTKs+Zc7vMbNZxLWlp32KFj/bzlDRgQ8bOfZZe5+eUvIw49tOsqu3L65z8jnnsue3vbbbs+JtkU4uWXs8eXOiejcpL15iZNyhYobLll9r/ngw9GXHZZxMknl+d9KlE5J5zrTOUc3UraqspdudHWVthz+lI5l/u8eqyc++Mfs2XIa63VsdjqCitk/1GOSHdr6+LFHbfLVTk3eHD2iuOIET23AW69dcTYsdkrTMk/ZlCPytnWmnsO19oKQKUtXdrxeb9clXONuuZcd5tBLO9Tn4o4/PDs7SOOqPz6yMkurePHdz/XWmWViHXXzd5+9NHKjofSJOvNTZrUcV9SPXfxxeVZez2TqWzl3IsvZtcNRzhHDypZuVGIJFRL1o8rVj2Hc8l6c7vskn8VLbe1Na1yP2yUq3KuUC0tEV/4Qva21lbqWTnPv7kBX71ukANAeuRWuTVzW+uiRR0h2PKbQXTlzDOzF5qffTbinHMqO7be1ptLaG2tX/PnRzz+ePb2Zz/bcf8++2Tnz6++GvG73/X9fd54I7uGe0tLxPrr9/31EmusETFyZPb200+X73UbmXCOblUqnCu0ciPNlXNJZVzS0ppIwrm77y68wrDR/PGP2e+rrZa/02q17L139vvNN9u1lfpV6/MvAJQqN0jra5dEI4dzDz+crfgbMaKw5WqGD484//zs7e99L7tkS6X0tt5c4hOfyH4XztWf3/8++32rrbJ/xxKDB0d85SvZ2+XYGCKpmhs3rvxLAtkUIp9wjm7VcnK4eHFHeWvawrl33un4By4J4xKf+ETEkCHZdfKeeKLqQ6uKSy7Jfj/ooO7X3qikbbfN7ui6cGG6KxRpbNpaAWhUuevN9fWzXiOHc4WsN7e8/feP2HXX7AXkb36zMuNaujTioYeyt1XONa5kiZ7Jkzs/dsQR2e+33RYxb17f3qcS680lrDuXTzhHt2oZziWBWmtrdr2DUtRrOHfPPdmquPHjI/7lX/IfGzCgo+w9jevOvfZatmItIuJrX6vNGFpbI/71X7O3r7uuNmOA3pTz/Nua8y+9tlYAKq1cm0HkvkYjhnOFrjeXq6Ul4sc/zv7b/ZvfdIRo5fTkk9n1l4cN630NsWRTiHnz6nOTvWbV1tZROZe73lxivfUiJk7Mrhf3s5/17b0qsd5cQjiXTzhHtyq15lEx4dzw4fkTy2LUaziXVGstXzWXSPO6c7/8ZTYc+NSnIjbaqHbj2Guv7Pcbb8xubw/1ppzn39zXUTkHQKUlmzeUowWuUTeEWLq0YymXQtaby7XhhtkOk4iIU04p77giOtab23bb3udZNoWoT48+GvHmmxErr9x9a/LXv579fumlfVvKpxqVc088kQ0Sm51wjm6Vc3LY0tIR0BUTzvVly+5kI4l6u8qTuxlEV5Jw7t570xUctbVF/OIX2dvJblS1sv322UVI33qr46om1JNy7pad+zrCOQAqLalyK2c412iVc489lq1OGz48YpNNin/+d76T7aiZNav8n1ULXW8uobW1/iQtrZ/5TPbvSVemTIlYa61siNeXjfAqWTm30UbZgPif/8xucNHshHN0q5aVG0mg1pdwrh4r5+bPj3jmmWxYudNOXR+z2WbZsb/3XsQjj1R1eBV1113ZkvhhwyK++MXajqV//4ipU7O3tbZSj5LzZDnWnMt9HW2tAFSacK4jUNt++9K6gMaNi/jqV7O3/+M/yltVlFTOFRvOpWle0uiScK6rltZE//4dBREXXVTa+7z3XnbX14jKVM6tsELHDrBaW4Vz9KCW4Vw5KufqMZxL1pHbYovuf7fW1oidd87eTlNra7IRxJe+FLHiirUdS0RHa+v11wssqD/aWgFoVNacy98MolSnnJL9/f/4x+zC/uXw+usRL72ULRTYZpvCnqNyrr4sWNARsPYUzkVkA97+/bN/h0rZbPAvf8l+X2ONvs3Le2LduQ7CObpVD+Fc0ppainoO57pbby6RPJ6WTSHeeCO7vltE7TaCWN5nPpNtNXjjjY41QaBeaGsFoFE1+5pzy5ZF3Hdf9nZfwrnRoyOmTcvePuWU8lTPJaHOxhtnu1kKYVOI+nLXXdnPc+uvH7HOOj0fu+aaHRvhlVI9l6w3V4mW1oRwroNwjm6VO5xL/nFN/ifvSTkr5z78sH6utvW23lwiCeceeKB+xt4X//Vf2fXzPvnJiM03r/VosgYMiNhzz+xtra3Um0q1tQrnSItMJtti5e801J9mb2t96qmId96JGDIkYsst+/Za3/529nUefTTb7dFXyXpzn/pU4c8ZPrwjBLIpRO0V0tKa69/+Lfv9iisiFi4s7r2S9eYq0dKayN0UotkJ5+hWucO5Aw/Mfj/55N4/TJcjnFt55Y6xF1I998EH2RL0Su0UM29exMsvZ8e0/fY9H/vxj2evli1a1HGFq1FlMhE//3n2dr1UzSVyW1vb2mo7FshVqcplLdykxQ9+EPH//l/EkUfWeiTA8po9nEvWm9tuu77/O7766hHHHZe9/Z//2fd/x4tdby6htbU+ZDLFh3M77ZQN1957LxvQFaMalXObbZb9/swzLrgJ5+hWuSeHp5ySDdueeaZj187ulCOca2npeH5vJdiZTMTee2e3Ov/+90t/z54kVXPbbJO9AtaTlpaO6rpGX3funnsinn8++zvvt1+tR5Pvs5/Njuuvf4146KFajwY6aGuF7s2bF/G972VvX3pp41/EgrRp9nAuWW9uxx3L83onnJCtXvvznyOuvLL011m8OOLhh7O3i6mcixDO1Yvnn88Wewwc2P3mgstraemonrvoouIKUapROTduXMRKK2WLUl54oXLv0wiEc3Sr3G1Vq6wSMX36/2/vvsOjqPb/gb83bVMgCQIBEkKASCKKVCWCVKVdBUEvUkQC+aIXkKJylSJoQC9FetMLNlBBERCkKwoERMrVEKQXgSCBUERCQktI9vz++PxmS7K72U022ZC8X88zz87Ozp49OztnZ+Yzp8j8O+9IZ5a2uCI4B5j6rMuv5tzSpcCmTTL/7rvA4cOF+1xrtP7j8mvSqikt/c5pteZeeCH/oGRx8/UFunSReTZtpZKEzVqJbBsxQvqf8vaW50OHslYoUUlSlgeEUMo1g0GYCwoCRo6U+fHjpauYgti/XwIgFSuaRsh0FINzJYM2MEiLFs5dV8XGyoB8hw4BO3c69p7sbNOAEEVZc87DQ/pABNjvHINzZJOra84BwMCBQHQ0cOWKNEmxxVXBOUcGhfjrL1N18UqV5IA3YIBrT/SVcnwwCI02YuuvvzrfP0BJcfUqsHKlzGtDeZc0WtPWb78tuibNRM5is1Yi677/XgYY8vSUpj1BQdIHUn418omo+JTlASGOHZPrHF9faXrvKsOGAVWqyEirixYVLA2tv7lmzaQ2lTO0QSFOnwauXSvY51PhOdukVRMcDPTuLfOODgxx5oxcF/v7A+Hhzn2eszgohGBwjmwqiuCctzcwfbrMz54thd4arRlqcQTnRoyQAF29etK0MTAQ2LsXmDu3cJ9t7sgRGbrczw947DHH3hMRAURGysW0dgfuXvPll1KFvlEj0x23kqZTJ/ldzpwBkpLcnRsiwWatRHllZgLDh8v88OFyE+u99+T5W2+VrNHZicqystysVTtnb9ZMmh66SkCA/M8B8r9XkGBlQfubA6Q1Uq1aMs9BIdwjMxNISJB5Z4NzAPDKK/K4ciVw+XL+62v9zUVHS+22osRBIQSDc2STqy8ONU8/DbRrJ0Gb0aPzvq5U8dWc27xZAkg6ndx1r1XLFDwcO1buDrmC1m9cixaAXu/4+7QmsPdi01algI8+kvmSWmsOkJOdp56SeTZtpZKCzVqJ8po9W/rbqVIFiI+XZYMHy0n9339L37ZE5H5lOTinDQbhqv7mzA0cKDWYUlKABQucf39BRmo1x6at7rVzpwxgWLWqaRAFZzRuDDRtKrXh4uJsV5LRFEd/cxrt+7DmHJENRVFzDpBA2IwZ8rh8OfDLL5avZ2SYPlvrM66g7AXnbt40jfI2dKgM1AAAL70kd+Nv35bRRV3R1FELzjna35zmXu53btcuuePi7y/9zZVkbNpKJQ2btRJZOn/eVEtu6lRpzgrIvj1/vswvXMgaHUQlQVntc64o+pszp9dLv92AdA9044bj7z13ToJ6np4Fb277yCPyyOCce2j9zXXs6HyzZM3bb8t7N26UoNuoUbb7gS+OkVo1Ws2506ed269LGwbnyKaiCs4BEh0fMEDmR4wADAbTa1ogzddXAjuFYS84N3683DEID7ccoVWnk0EM/PwkKFbYfmyys01VkJ0Nzmmj8Pz+uzS9vZdoA0H07ClNhUuyp5+WpgfHj0sTZCJ3K6rgHGvO0b3qzTflplrz5sCLL1q+1qqV3ARSSm62mZ9TEFHxK6t9zp0+LTcSvL1NN/1drV8/4P77pV87Z7rg0Zq0NmggrUYKgjXn3Kug/c2Z69xZuvF54glpxTZ1qgwOsmBB3nPE4qw5V6mS1AgEimZgxnsFg3NkU1EG5wC5A16unPTztmyZabmrmrSap6H1YafZtw+YOVPmP/wQKF/e8vXISOA//5H5N96QA21B7dsnAzoEB0vfa86oUkX6wgOAbdsKnofilpYmtSKBkt2kVRMYCHToIPPaABZE7qTVcGOzViJpJvb113LzbP58633fTJsm5xS7dwNLlhR/HonIpKw2a9VqzTVtWvgKBrZ4ewMTJsj8tGlyzu2IwvQ3p9EGhTh1yvHPJde4cEGafOp0QPv2hUurQQPgp5+AdetMAzUOHizLtdp5ShVvzTmA/c4BDM6RHUUdnKtaFRgzRuZHjzYddF0ZnNOaxZrXnMvOlqarBgPQo4fcQbDm1Vfl4JqeLn9YBW3uqDVJbdOmYBfa92K/c0uXyu9Zr17R3Tl0te7d5ZH9zpU8WVlyQb5mjbtzUnzYrJVIZGdLbThAuqKwdZMrNNTU3GvkSNvNdIio6JXV4JzW31xRNGk116uXnGOnpZn6ys5PYfubAzgohDtt3iyPjzwitcwKS6eTa+CDB4F58+S3PXIE+Mc/ZLC8LVvkOOrhITXrigP7nWNwjuwo6uAcALz+ujQrPXfOVJOtKGrOmQfnZs+W6rwVKtivDu7pCXz2mdyhWrcO+OabguVB629O6z/OWe7ud27HDgmwde/uWJPP3ANBFLRPhOL2zDOyrx88CJw44e7ckObYMbnLO2wY0K0b0LevBMxLOzZrJRIffggcOiTHc61Guy2vviq1AC5dMtUsIaLiV1aDc1rNuaIYDMKch4epD87Zs6UvucxM6eg/JydvhYLbt+XaByhczTmATVvdxby/OVfy9pYbYH/8Afz73/L8hx9MtfNq13ZuMMPC0GrOMThHZEVxBOf8/IApU2R+8mTg4kVTE9SiCM6dPm26sz59ujQbteehh0yjvw0bJtV+nZGZKSPrAM73N6dp1UoOwidOyMG3uKSny5DbrVtL0+Nvv5U/zZdesp+PX3+V6si+vnn7BSrJKlQwBUIdrT134gSwYYP0g0SupZT0f9G4sdydDQqScrBkCdCwIbBnj7tzWLTYrJVIgmxvvy3zkyblP0iUj4/pptvcuWW73xoidyqKASFyciT4VFKdOyd9WXt6Fq52mqO6dpWBHW7elIoOvr7yH+jlJedLOp3kxdtbzqHu3pVWSzVrFu5zGZwrfjk5wI8/yryrg3OaChXk2vjoUdNAeQDw4INF83nWmAfnyuoAfQzOkU3FEZwDgN69pWbWzZtyEl5Ufc4ZDNIk5vZtGY01Ls6xNEaPlj+Lv/6Su/LO2L1bOrCtWrXg7fWDg02jIxVX7blNm6S6/H//K88HDACefVa24aefSvXm0aOBa9fyvlerNff88/JHfy8xH7XVFqWAn3+Wk6LoaKkSXr263G06dap48lnaXb4s23fwYCmv7dtLrc0dO4CICDn5bdFCatGU1maabNZKJF1fpKfLxaA2iFR+OnSQ41VOjtxUK6sn+ETuVBQDQpinWxJpteYaN87bl3VR0OmAGTPsB0ANBjmf0IKa3bsXvkWLFpz77bfCpUOOS0yUa9nAwKLvLigyUvrf3rFDWqtoXVAVh7p1JbB89apU2CmLGJwjm4orOKfTmZq0fvqpaeADVwbnDAbggw/kroNeDyxc6PjBycdH8uXhIR1Sr1vn+OdrwbQnnijcwbC4mrZevQrExgJPPSV3AGvXNo1Yu2qV9FfRsqWcHL3/vvyBT59uOllKTzcN7vHyy0Wb16LQrZv8zomJQHKy5WvZ2TLIRUyM1GZcu1aWV6smfX7MnClBy86dpeo5RwssmE2bpM+Jdeuk7M2aJdszNBR4/HEZubh3b7nwfvttCbT/+ae7c+16bNZKZd2ePcCiRTI/f75ztUhnzpQL1m3bgBUrXJenGzeki4t+/eRm3TffyP8PA4BkjVLS8mD4cBntsEsX4Msvy0Z/iK5s1moefCrupq1KSSsYR2jBuaLub85cy5Zy7p2RIfvVtWtyLn/litQ8Tk2VQe3OnZNWL86M7moLB4Uoftoore3aSU3I4tCyJfDFF8BjjxXP5wHyf6H1b1dWB4VgcC6XDz74ADVr1oSvry9iYmLwv//9z91ZcguDwRRcKOrgHCDVv3v0kIOg1plqfs1XHOHjI6O3AcCbb8pjfLzzHVs++qjUjAKkNo+jJ1aF7W9OYx6cK6qLgJUrperyl19KIPH11+WPsW1b0zrNmsnvs26dNPm9dk22a1QUsHixNDm8eVNOQlu0KJp8FqWQENNJ1apV8njjBjBnjuwzPXtKs11fX2DgQOkPLSVFmrb+4x/y22jzDzwg7yvJJ+G3bkkfJEuXSt8lixZJYNIdd6Zv35ZaLk89JSeU9erJtn7tNcuRGYOCJL9ffCFl++efZXQpbXTg0sLVzVoZnKN7SU6OaRCIuDjnLw5q1jTd7f/3vwvX9cDNmxLge/55OUb06iX/P3PnynxEhDQp69FDbibs3SuD2JQmN29K6wFyzB9/SJ+HUVFyQ2/ePOD4cWD9erkBGhIitcOXLi29fai6Mjin05kCdEUdnMvOlhphc+ZImQ4Lk89u3FhajGzZYvscSbt+Ker+5nLz9pbzocBAaW1z330yYEBIiLTcCQ2VFh5hYa7pB7piRVPTWA4KUTyKqr+5kqisDwqhU4r3+zTffPMNYmNjsWDBAsTExGD27NlYsWIFjh8/jpCQELvvTU9PR1BQEK5fv47AwMBiynHRuXtXAluABGCCg4v+M5OTJaCh3aFatAjo37/w6dasCZw9K/P168tBtyB3HW7dkiDAH3/IQAcLF9pfPyNDDpDZ2dIMrzB9PNy6JU1Es7KknzNXjpqTmioXQVow6sEHpaZgfhdDOTkSyHv7bVMfdDqdBKhmzABGjHBdHovT/PkSJGrUSA6CCxaY7gxWqiTb6pVXgMqV87735EmpoblokemEOyBATsZfeklOjPz8ZCquO1+A5OXoUWkaeuSIaT452Xqw19NTmuw2aGCa6teXWoKOnNgpJf8h3t6Orf/778ALL5gGHHn1VemLMr++ak6dAvr0kYthQC7i5841BeTdzWCQO9YnTsi+oU0ZGVIrtU4d03T//YC/v+m9bdsCCQlSE7Vnz8Ln5bnngNWrZX8eOLDw6RHZk50tzdNTU4ELF2RKTZXzidBQOR7WqiWPlSvn/Z/46CPZT4OCJKiRX/+w1ty+LTeRzpwB3noLmDjR8ffeuiW1eJcvl4DKrVum1yIjpQuE27elNvn+/Xmbi+v10h1F8+ZStoOC5DxKm7TnruiPy5UMBtleBw5YTqdOyf96SIgcC7RjQv360gypuDoLL4iMDGkelZpq6tc4JMQUrKha1TU3Qa5ckZqUS5aYjkmAHO+7dZP/4EOHZJ1jx0yv6/VyQ69HD6l5XxzNIYtDSIhsk99/N11sF0aFCnIudvSoXCu4yvXrUkt3507gl1/ktzMv79b4+cmN3A4dpNuNevXk/65qVfkvu3r13uvWxVndu0sXMFOnmio/UNFIS5Prj5wcOW+PiHB3jorWe+9J//CxscDnn7s7N67jaKyIwTkzMTExePTRRzF//nwAgMFgQHh4OIYNG4bRo0fbfW9pC87dvm26UMzIKL6L3dGjpbkkIM0Gu3QpfJqNG0vtIJ1ODsBNmxY8re3bgTZtZP6hh2Qb2Zr+/lv+VGrXdk1fZG3ayOcPG5Z/lXnzUq3NW1uWmgq8+6788Xt5SU2DsWOdO9G+fVsCUpMmyYWXj48EJFwxzLc7XLggJ+zm6tSR2hexsY7dBb5xQwKX8+fbHuHWy8sUqPP3N82bT76+eR+1eR8f2fY3bsh086b1x7Q0+/02VKwoAdnataV51u+/mwZlya1SJel/Ua+Xz759W+4ga/Pmk1JS4027kxsUZLogNZ+/fVtqFWRlyYnt4sXO3Rm8e1dqKEyaJJ95//3AyJESHLh50/aknXwHBMj/W0CA5bz5Mr3esSDjtWsSfNOCcX/84VwtxLAwU7Du+++lGcrKlZYd8xZUjx5S+6d/f7mgcAWDwfrvn3vZnTuyv/v4SMDWx8f65O0tk6enrK9N1p57uLDev1LyXXJyZL/JyTFN5s+zs00dbGv50Cbz51pn3K7k6JmaUpaTvWWOfIbBIGUsK8v+482b8j+jBeIuX3a8ab+fnwTptCkiApg2TS5w58yRJoEFtXat1FDy8QE+/ljKsz23bgEbN0rtcPPadrVqSRnq0UNu3Jj/H9y8KTf9du2SfmZ37bIcId4evd70nxgYKIGZcuUsH3Mv026cFlTu/7JLl0xBuIMH5bjhDE9PCZZowbrISFmulSttMn+u7Ys6nZQVrfN6bd78OZC3PFp7vHPH1IzPPBiXX61JT0+58aQF66pXl6laNcttnXu7ac+vX5cgxQ8/mIK0Hh4StOnTRwJz5gE3pWSgkuXLZTp+3PSar68E6mrUkBvV9qasLMmD9r9pPpn/n3p7y35mPvn6Wn/u4WH6new9at9fm7Tfy3waMED+/111Qzk0VH7TKVNk++T+XzOfsrMtj0G3blmfP39eAqa5//uCgyWw/vjjMtWqJbX0f/wR2LxZ8mGualWpJbljhwSu9+8v/Pct6SZPlpsebdqYajnbkvv3yb0/5d63zMt/7n3MfJkjiiLK4Yrah86kl5QkfSxHR1sG9kur776TfmMbNSpdNTMZnHNSVlYW/P39sXLlSnTr1s24vF+/fkhLS8OaNWss1s/MzESmWScE6enpCA8PLzXBuYwMOVEE5ABWXHd309PlIH75spwk1qtX+DS7dpUT9FdfleHGC2vYMAm6OOrll02DJBTGu+9Kk9yi0KSJ1JZr0KDgaVy7JmnUrQs8/bTr8uYOnTtL89SWLYE33pDnBbnYVkr6PJo3T07q3Dmqa2io/DYPPiiTNp+7BqBScsJ64IAE6rTpxImi7Ueva1e5eLZWI9ER27fL6MDFOaKxI7y8TLXkoqLksXx5Cdib16azNrgKIEGCzp0Ln4/YWAkYExUXT0+p8RYaKoGO0FAJQl24IHf/k5Plv8bWWWi9enJRUpiuNZSS49GmTc6/NyLCFJBr0sS5i8GTJyVQt2ePXMinpcl0/brpsaSefev1cvNRC7ZpU0CABJXMa9T9/rvt/66SpFw52QerVpUaTVeuyLHiwgXXDpLz6KMSkOvZUz4rP0rJue6KFVKj7uRJ1+WlpLhwQbZ9YUVHy3lIUahd2xSIa9HC1Cm9NUrJTdfNm+W8LiHBsqntsGGu6detpPvxR9fd6CPHDB8uN6xKu1On5PjfuLHUaHV1MNRdGJxz0oULFxAWFoZdu3ahWbNmxuUjR47E9u3bsde8jjqA8ePHY8KECXnSKS3BuTt35OCSnQ2MGuW6fo8cceKE3Bl45hnXpHf8uBxEX37ZNUHGnBy5YEhPlztw9iYPD6lxFR5e+M9NTZX+7hw9ETb/M9Pmcy/z8JC7tMOHF0/fgveKW7ekf50aNVybrlKmWkXmd29z39HV1rH3mJkpNe5y1/Qyf9SmyMjCN02/dUtOSA8flu9hraZf7lp/t2/LRaj5Ban5fFqa3Aho104Ca4U9AF+7JlXhT56UbeDvb6r9Zm1SylSTzl7tQ0f7jypXTmruaUG4OnWkJpAjZevqValpZx6w8/GREZNd0WfP//4nAX5X9ieo9QOk1ea0tR/4+sr/pnltK23K/Tw727I2jK3nrjxz0Wp5mtfSs1YjTjsOWqtRZz5fFP36abWMcrO1zHyytyw/Op1lzcbc89qjr69cgGtBuGrVJNCe37lDVpbUENWCdWfOyOPff0sz1EaN8s9jfs6ela4IHOnbS6eTAEvPnvJYVBcFBoOpZrM2ZWSYphs3rM9nZFjfvwpTiyQw0BSAa9BA/rccPR8wv5mjTSkp1mvE5X7U3p+7Jo21WjXmZdFWOfXxkWBw1aqmQJz2aKv1R06O1LZLSZHvkZJimi5eNAXucm838+ceHtKaoU8fCSAVlFKy/datk+Nt7tpuer18R/N5rQuJ/CbzGnfa+YO1eYPB/m9m/v9hrcaa+W+mlHSPMnlywbeJua+/lsHJtP9Ce5Onp2WLBFvzFSpIOS9M8DAzU2rLbt4sQYWpUwvXjc294u5d6eLnjz/yvmbvuGSvVpz5vmWvdp15LTtHOHrsdIQztdhdKTBQbvTXru3adEsi7TcuzthDcWBwzknOBudKe805IiIiIiIiIiIqOEeDc6wr8/9VqlQJnp6euHTpksXyS5cuoaqVuul6vR76ktwDLhERERERERERlXgu7rL43uXj44MmTZpgy5YtxmUGgwFbtmyxqElHRERERERERETkKqw5Z2bEiBHo168fHnnkETRt2hSzZ8/GzZs3ERcX5+6sERERERERERFRKcTgnJmePXviypUreOedd3Dx4kU0bNgQ33//PapUqeLurBERERERERERUSnEASFcxNFO/oiIiIiIiIiIqPRzNFbEPueIiIiIiIiIiIjchME5IiIiIiIiIiIiN2FwjoiIiIiIiIiIyE0YnCMiIiIiIiIiInITBueIiIiIiIiIiIjchME5IiIiIiIiIiIiN2FwjoiIiIiIiIiIyE0YnCMiIiIiIiIiInITBueIiIiIiIiIiIjchME5IiIiIiIiIiIiN2FwjoiIiIiIiIiIyE0YnCMiIiIiIiIiInITBueIiIiIiIiIiIjchME5IiIiIiIiIiIiN2FwjoiIiIiIiIiIyE0YnCMiIiIiIiIiInITBueIiIiIiIiIiIjchME5IiIiIiIiIiIiN2FwjoiIiIiIiIiIyE0YnCMiIiIiIiIiInITBueIiIiIiIiIiIjchME5IiIiIiIiIiIiN2FwjoiIiIiIiIiIyE0YnCMiIiIiIiIiInITBueIiIiIiIiIiIjchME5IiIiIiIiIiIiN2FwjoiIiIiIiIiIyE283J2B0kIpBQBIT093c06IiIiIiIiIiMjdtBiRFjOyhcE5F8nIyAAAhIeHuzknRERERERERERUUmRkZCAoKMjm6zqVX/iOHGIwGHDhwgWUL18eOp3O3dlxifT0dISHh+PcuXMIDAx0d3aIShyWEaL8sZwQ2ccyQmQfywiRfSwjJZtSChkZGQgNDYWHh+2e5VhzzkU8PDxQvXp1d2ejSAQGBrKQE9nBMkKUP5YTIvtYRojsYxkhso9lpOSyV2NOwwEhiIiIiIiIiIiI3ITBOSIiIiIiIiIiIjdhcI5s0uv1iI+Ph16vd3dWiEoklhGi/LGcENnHMkJkH8sIkX0sI6UDB4QgIiIiIiIiIiJyE9acIyIiIiIiIiIichMG54iIiIiIiIiIiNyEwTkiIiIiIiIiIiI3YXCOiIiIiIiIiIjITcp8cG7y5Ml49NFHUb58eYSEhKBbt244fvy4xTp37tzBkCFDULFiRZQrVw7//Oc/cenSJePrv//+O3r37o3w8HD4+fmhbt26mDNnjkUaO3fuxOOPP46KFSvCz88PDzzwAGbNmpVv/pRSeOedd1CtWjX4+fmhXbt2OHnypMU6EydORPPmzeHv74/g4GCHv/uBAwfQsmVL+Pr6Ijw8HFOnTrV4fdWqVXjkkUcQHByMgIAANGzYEF9++aXdNFNTU/HCCy8gKioKHh4eeO211/Ksc/fuXbz77ruIjIyEr68vGjRogO+//z7f/P7999/o06cPAgMDERwcjAEDBuDGjRtOfSdr8vt9r169ik6dOiE0NBR6vR7h4eEYOnQo0tPT8027NCiuMmLul19+gZeXFxo2bJhv/hwpI5rMzEw0bNgQOp0O+/fvt5tuUe3Ld+7cQf/+/fHwww/Dy8sL3bp1y7NO//79odPp8kwPPfSQ3bRr1qyZ5z1TpkyxWGf58uVo2LAh/P39ERERgWnTptlNM7dBgwZBp9Nh9uzZFsufeeYZ1KhRA76+vqhWrRr69u2LCxcuOJX2vayslpNVq1ahffv2qFy5MgIDA9GsWTP88MMPFuvs2LEDXbp0QWhoKHQ6Hb777rt88+tIugDwwQcfoGbNmvD19UVMTAz+97//2U03ISEBXbt2RbVq1YzHtaVLl+ZZb/bs2YiOjoafnx/Cw8Px+uuv486dO3bTzu8YNX78eKvlOiAgIN/tURqwjBR/GXFkm1uT37nUxx9/jJYtW6JChQqoUKEC2rVrl2/ZA4Dhw4ejSZMm0Ov1Vn8TR8tnacUy4vp9ecWKFXjggQfg6+uLhx9+GBs3bszz2R06dEDFihUdyivg2H66ePHiPP/1vr6++aadXxlJTk62ehzZs2dPvmmXBiwjpaeMAEBaWhqGDBmCatWqQa/XIyoqKs/nm0tOTsaAAQNQq1Yt+Pn5ITIyEvHx8cjKyrJYTymF6dOnIyoqCnq9HmFhYZg4cWK++S4Jynxwbvv27RgyZAj27NmDH3/8EXfv3kWHDh1w8+ZN4zqvv/461q1bhxUrVmD79u24cOECnnvuOePriYmJCAkJwZIlS3D48GGMHTsWY8aMwfz5843rBAQEYOjQodixYweOHj2KcePGYdy4cfjoo4/s5m/q1KmYO3cuFixYgL179yIgIAAdO3a0uEjIysrC888/j8GDBzv8vdPT09GhQwdEREQgMTER06ZNw/jx4y3yc99992Hs2LHYvXs3Dhw4gLi4OMTFxVm9QNJkZmaicuXKGDduHBo0aGB1nXHjxmHhwoWYN28ejhw5gkGDBuHZZ59FUlKS3Tz36dMHhw8fxo8//oj169djx44d+Ne//uXUd7Imv9/Xw8MDXbt2xdq1a3HixAksXrwYP/30EwYNGmQ33dKiuMqIJi0tDbGxsXjyyScdyp8jZUQzcuRIhIaGOpRuUe3LOTk58PPzw/Dhw9GuXTur68yZMwepqanG6dy5c7jvvvvw/PPP55vvd9991+K9w4YNM762adMm9OnTB4MGDcKhQ4fw4YcfYtasWVZ/B2tWr16NPXv2WN2Gbdu2xfLly3H8+HF8++23OHXqFLp37+5QuqVBWS0nO3bsQPv27bFx40YkJiaibdu26NKli0UZuHnzJho0aIAPPvjAoTQdTfebb77BiBEjEB8fj3379qFBgwbo2LEjLl++bDPdXbt2oX79+vj222+Nx7XY2FisX7/euM5XX32F0aNHIz4+HkePHsWnn36Kb775Bm+99ZbdPOd3jHrjjTcsymZqaioefPBBh8p1acAyUvxlxJFtnpsj51IJCQno3bs3tm3bht27dyM8PBwdOnTA+fPn8833//3f/6Fnz55WX3OkfJZmLCOu3Zd37dqF3r17Y8CAAUhKSkK3bt3QrVs3HDp0yLjOzZs30aJFC7z//vsO5VVL15H9NDAw0OL//uzZsw6lb6+MaH766SeLtJs0aeJw/u9lLCOlp4xkZWWhffv2SE5OxsqVK3H8+HF8/PHHCAsLs5nusWPHYDAYsHDhQhw+fBizZs3CggUL8pyfvfrqq/jkk08wffp0HDt2DGvXrkXTpk0dzr9bKbJw+fJlBUBt375dKaVUWlqa8vb2VitWrDCuc/ToUQVA7d6922Y6r7zyimrbtq3dz3r22WfViy++aPN1g8GgqlatqqZNm2ZclpaWpvR6vfr666/zrL9o0SIVFBRk9zM1H374oapQoYLKzMw0Lhs1apSKjo62+75GjRqpcePGOfQZrVu3Vq+++mqe5dWqVVPz58+3WPbcc8+pPn362EzryJEjCoD69ddfjcs2bdqkdDqdOn/+vFKqYN+poL/vnDlzVPXq1W2+XpoVdRnp2bOnGjdunIqPj1cNGjSwmxdnysjGjRvVAw88oA4fPqwAqKSkJAe+rXDlvmyuX79+qmvXrvmut3r1aqXT6VRycrLd9SIiItSsWbNsvt67d2/VvXt3i2Vz585V1atXVwaDwW7aKSkpKiwsTB06dCjfz1FKqTVr1iidTqeysrLsrldalcVyonnwwQfVhAkTrL4GQK1evdrpNK2l27RpUzVkyBDj85ycHBUaGqomT57sVLpPPfWUiouLMz4fMmSIeuKJJyzWGTFihHr88cdtpuHIMSq3/fv3KwBqx44dTuW3tGAZKfoyklvubW5NQc6lsrOzVfny5dXnn3/uUD4d+U00uctnWcIyUrh9uUePHurpp5+2WBYTE6MGDhyYZ90zZ84UOK9K5d1Pnbkms8bWb1LYfJY2LCP3bhn573//q2rXrl3o64SpU6eqWrVqGZ8fOXJEeXl5qWPHjhUqXXcp8zXncrt+/ToAqTUGSHT97t27FjVcHnjgAdSoUQO7d++2m46WhjVJSUnYtWsXWrdubXOdM2fO4OLFixafHRQUhJiYGLuf7Yjdu3ejVatW8PHxMS7r2LEjjh8/jmvXruVZXymFLVu24Pjx42jVqlWhPjszMzNP1W4/Pz/s3LnT+FyrDm6e3+DgYDzyyCPGZe3atYOHhwf27t3r8HdKSEiATqdDcnIygIL9vhcuXMCqVavs/nalWVGWkUWLFuH06dOIj493KC+OlpFLly7h5Zdfxpdffgl/f3+H0naEI/uyK3z66ado164dIiIijMtylxHNlClTULFiRTRq1AjTpk1DdnZ2vvlNSUkx3tHVmkwkJCQY1zEYDOjbty/efPPNfJvWAtK8b+nSpWjevDm8vb2d/bqlQlktJwaDARkZGXaPf65INysrC4mJiRbfycPDA+3atbP4Tv3790ebNm3spp17Gzdv3hyJiYnGZnqnT5/Gxo0b8dRTTxnXKcgxKrdPPvkEUVFRaNmypQNboPRhGSnaMmJN7m0O5C0jzp4fAsCtW7dw9+5di3THjx+PmjVrFvDbWObZ1dvqXsEy4ty+nNvu3bvztFDo2LGj09dQBTmOAMCNGzcQERGB8PBwdO3aFYcPH7Z4vTBl5JlnnkFISAhatGiBtWvXFiiN0oBl5N4tI2vXrkWzZs0wZMgQVKlSBfXq1cOkSZOQk5NjXMfWtY69dNetW4fatWtj/fr1qFWrFmrWrImXXnoJf//9t1PfyV0YnDNjMBjw2muv4fHHH0e9evUAABcvXoSPj0+evtyqVKmCixcvWk1n165d+Oabbyyas2iqV68OvV6PRx55BEOGDMFLL71kMz9a+lWqVHH4sx118eJFq+mafy4gO3y5cuXg4+ODp59+GvPmzUP79u0L9dkdO3bEzJkzcfLkSRgMBvz4449YtWoVUlNTjesEBQUhOjraIr8hISEW6Xh5eeG+++4z5teR7+Tv74/o6GhjwMCZ37d3797w9/dHWFgYAgMD8cknnxRiK9ybirKMnDx5EqNHj8aSJUvg5eXlUH4cKSNKKfTv3x+DBg2yuHB2BUf25cK6cOECNm3alOe/IncZAaSvkmXLlmHbtm0YOHAgJk2ahJEjR1rkd9WqVdiyZQsMBgNOnDiBGTNmAIAxz97e3oiOjrY4YXj//ffh5eWF4cOH283rqFGjEBAQgIoVK+LPP//EmjVrCvXd71VluZxMnz4dN27cQI8ePQqchiPp/vXXX8jJycn3+FitWjXUqFHDZrrLly/Hr7/+iri4OOOyF154Ae+++y5atGgBb29vREZGok2bNhbNJgpyjDJ3584dLF26FAMGDHBwC5QuLCNFX0Zys7bNgbxlxNHzQ3OjRo1CaGioxUVepUqVEBkZWeDvA1gvn2UFy4jz+7K1PLviGqogx5Ho6Gh89tlnWLNmDZYsWQKDwYDmzZsjJSXFuE5Byki5cuUwY8YMrFixAhs2bECLFi3QrVu3MhmgYxm5t8vI6dOnsXLlSuTk5GDjxo14++23MWPGDPznP/8xrmPtWsfcH3/8gXnz5mHgwIEW6Z49exYrVqzAF198gcWLFyMxMfGe6WqHwTkzQ4YMwaFDh7Bs2bICp3Ho0CF07doV8fHx6NChQ57Xf/75Z/z2229YsGABZs+eja+//hoAsHTpUpQrV844/fzzzwXOQ24PPfSQMd1//OMfTr23fPny2L9/P3799VdMnDgRI0aMsKhRUxBz5sxBnTp18MADD8DHxwdDhw5FXFwcPDxMu+Ozzz6LY8eOFepzrGnatCmOHTtmtz27LbNmzcK+ffuwZs0anDp1CiNGjHB5/kq6oiojOTk5eOGFFzBhwgRERUVZfV9By8i8efOQkZGBMWPG2FzHPF1n+hJ0ZF8urM8//xzBwcF5Bo6wVkZGjBiBNm3aoH79+hg0aBBmzJiBefPmITMzEwDw8ssvY+jQoejcuTN8fHzw2GOPoVevXgBgzHNYWBiOHTtm7JshMTERc+bMceju1ZtvvomkpCRs3rwZnp6eiI2NhVLKFZvhnlJWy8lXX32FCRMmYPny5XkCVYVRmHQnT56ML774wupr27ZtQ1xcHD7++GOLGqEJCQmYNGkSPvzwQ+zbtw+rVq3Chg0b8N577xnXKewxavXq1cjIyEC/fv0KnMa9jGWk+MuIrW1ur4w4YsqUKVi2bBlWr15tUTN76NCh2LJlS4HTtVU+ywqWEef35aJSkONIs2bNEBsbi4YNG6J169ZYtWoVKleujIULFxrXKUgZqVSpEkaMGIGYmBg8+uijmDJlCl588UWnB/cqDVhG7u0yYjAYEBISgo8++ghNmjRBz549MXbsWCxYsMC4jr1zrfPnz6NTp054/vnn8fLLL1ukm5mZiS+++AItW7ZEmzZt8Omnn2Lbtm0ODZDhdm5sUluiDBkyRFWvXl2dPn3aYvmWLVsUAHXt2jWL5TVq1FAzZ860WHb48GEVEhKi3nrrLYc+87333lNRUVFKKaXS09PVyZMnjdOtW7fUqVOnrLbtbtWqlRo+fHie9Gz1b5CcnGxMNyUlRSmlVN++ffP0dbV161YFQP3999828zxgwADVoUMHh76frX66NLdv31YpKSnKYDCokSNHqgcffNDmup9++qkKDg62WHb37l3l6empVq1apZQq2Hdy5vc19/PPPysA6sKFCzbXKW2Ksoxcu3ZNAVCenp7GSafTGZdt2bKlwGWka9euysPDwyJtLd3Y2FillLJI99KlS3m+uyv3ZXP59TlnMBjU/fffr1577TWH0svt0KFDCkCefheys7NVSkqKyszMVBs3blQA1OXLl62mMWvWLKXT6fJsPw8PDxUREWHzs8+dO6cAqF27dhUo7/eqslpOvv76a+Xn56fWr19vd/vAyf60bKWbmZmpPD0986QVGxurnnnmmXzTTUhIUAEBAWrhwoV5XmvRooV64403LJZ9+eWXys/PT+Xk5FhNz5FjlLknnnhCdevWLd98lkYsI8VTRszZ2ubWOHMuNW3aNBUUFGTR16Ij8uu/yV75LAtYRlyzL4eHh+fpH/edd95R9evXz7NuQfrTcnY/7d69u+rVq5dD6zrTL+P8+fNV1apVHVq3tGAZuffLSKtWrdSTTz5psUy7JjHv89Sa8+fPqzp16qi+ffvmOS975513lJeXl8WyW7duKQBq8+bNDufdXcp8cM5gMKghQ4ao0NBQdeLEiTyvax1Lrly50rjs2LFjeTqWPHTokAoJCVFvvvmmw589YcIEuxe3WseS06dPNy67fv26SweEMO+EccyYMfkOCBEXF6dat27t0GfkF9DQZGVlqcjISDVmzBib62idbf/222/GZT/88IPVASGc+U6O/r65bd++XQFQZ86cyff73euKo4zk5OSogwcPWkyDBw9W0dHR6uDBg+rGjRs285ZfGTl79qxFuj/88IMCoFauXKnOnTvn0DZw5b5sLr/g3LZt2xQAdfDgQYfSy23JkiXKw8PDbsC9b9++qlmzZjZf/+uvv/L8NqGhoWrUqFF2O1s9e/asAqC2bdtWoLzfa8pyOfnqq6+Ur6+v+u677+xvJOVc4CG/dJs2baqGDh1qfJ6Tk6PCwsLyHRBi27ZtKiAgIM9gLprGjRurkSNH5smLn5+fys7OtvoeR45RmtOnTyudTqfWrVtnN5+lDctI8ZeR/La5NY6eS73//vsqMDDQ7rmSLfYCD/mVz9KMZcS1+3KPHj1U586dLZY1a9bMJZ3dO7ufZmdnq+joaPX66687tL4zwbmXXnpJNWrUyKF173UsI6WnjIwZM0ZFRERYBNdmz56tqlWrZjfdlJQUVadOHdWrVy+r52TaNv3jjz+My7QBuI4fP+5Q3t2pzAfnBg8erIKCglRCQoJKTU01Trdu3TKuM2jQIFWjRg21detW9dtvv6lmzZpZXMwePHhQVa5cWb344osWaZjXRJk/f75au3atOnHihDpx4oT65JNPVPny5dXYsWPt5m/KlCkqODhYrVmzRh04cEB17dpV1apVS92+fdu4ztmzZ1VSUpKaMGGCKleunEpKSlJJSUkqIyPDZrppaWmqSpUqqm/fvurQoUNq2bJlyt/f3yKyPWnSJLV582Z16tQpdeTIETV9+nTl5eWlPv74Y7t51j6/SZMm6oUXXlBJSUnq8OHDxtf37Nmjvv32W3Xq1Cm1Y8cO9cQTT6hatWpZ3OVYtWpVnhPBTp06qUaNGqm9e/eqnTt3qjp16qjevXs79Z327t2roqOjjTUIlcr/992wYYP67LPP1MGDB9WZM2fU+vXrVd26de2O3FeaFFcZyc3RExNHyog5Zw4urtiXrTl8+LBKSkpSXbp0UW3atDF+Tm4vvviiiomJsZpG7jKya9cuNWvWLLV//3516tQptWTJElW5cmXjnTillLpy5Yr673//q44ePaqSkpLU8OHDla+vr9q7d69xnZSUFBUdHW2xLLfco7Xu2bNHzZs3TyUlJank5GS1ZcsW1bx5cxUZGanu3Lljd1uUFmW1nCxdulR5eXmpDz74wCLPaWlpxnUyMjKM+zgANXPmTJWUlKTOnj1bqHSXLVum9Hq9Wrx4sTpy5Ij617/+pYKDg9XFixeN64wePVr17dvX+Hzr1q3K399fjRkzxiLdq1evGteJj49X5cuXV19//bU6ffq02rx5s4qMjFQ9evQwrlOQY5Rm3LhxKjQ01Gagr7RiGSn+MuLINs9dRhw5l5oyZYry8fFRK1eutEjX/Lxz3rx5eUY9PnnypEpKSlIDBw5UUVFRxu+s1ZJwpHyWZiwjhduXc/vll1+Ul5eXmj59ujp69KiKj49X3t7eFjc8r169qpKSktSGDRsUALVs2TKVlJSkUlNTjesU5DgyYcIE9cMPP6hTp06pxMRE1atXL+Xr62txDlmQMrJ48WL11VdfqaNHj6qjR4+qiRMnKg8PD/XZZ5/Z3calBctI6Skjf/75pypfvrwaOnSoOn78uFq/fr0KCQlR//nPf4zr5D7XSklJUffff7968sknVUpKikXampycHNW4cWPVqlUrtW/fPvXbb7+pmJgY1b59e7vbuKQo88E5AFanRYsWGde5ffu2euWVV1SFChWUv7+/evbZZy12gvj4eKtpmNeKmzt3rnrooYeUv7+/CgwMVI0aNVIffvihzSYyGoPBoN5++21VpUoVpdfr1ZNPPpkn6tuvXz+rn59fjZXff/9dtWjRQun1ehUWFqamTJli8frYsWPV/fffr3x9fVWFChVUs2bN1LJly+xvUGV9m5pvi4SEBFW3bl2l1+tVxYoVVd++ffPULFi0aJHK3er66tWrqnfv3qpcuXIqMDBQxcXF5QlA5vedtJpI5jXe8vt9t27dqpo1a6aCgoKUr6+vqlOnjho1alS+AZjSorjKSG6OHggdKSPmnAnOuWJftiYiIsJq2ubS0tKUn5+f+uijj6ymkbuMJCYmqpiYGON+WrduXTVp0iSL4NiVK1fUY489pgICApS/v7968skn1Z49e6xuH3v/H7mDcwcOHFBt27ZV9913n9Lr9apmzZpq0KBBFkHw0q6slpPWrVtbzXO/fv2M62j/u/bWKUi6SsnFTY0aNZSPj49q2rRpnv25X79+FrW9bR0vzde5e/euGj9+vIqMjFS+vr4qPDxcvfLKKxb/+QU9RuXk5Kjq1as73P1FacIyUvxlxJFtnruMKJX/uZStY1h8fLxxnfj4+Dy/i608a+dkjpTP0oxlpHD7sjXLly9XUVFRysfHRz300ENqw4YNFq9r/+X29uWCHEdee+0147GpSpUq6qmnnlL79u2z+OyClJHFixerunXrGq8nmzZtqlasWGF3G5QmLCOlp4woJRULYmJilF6vV7Vr11YTJ060uHGZ+1zLVl5yn4+dP39ePffcc6pcuXKqSpUqqn///vfMTR6dUmWwt24iIiIiIiIiIqISgKO1EhERERERERERuQmDc0RERERERERERG7C4BwREREREREREZGbMDhHRERERERERETkJgzOERERERERERERuQmDc0RERERERERERG7C4BwREREREREREZGbMDhHRERERERERETkJgzOERERERERERERuQmDc0RERESUR//+/aHT6aDT6eDt7Y0qVaqgffv2+Oyzz2AwGBxOZ/HixQgODi66jBIRERHd4xicIyIiIiKrOnXqhNTUVCQnJ2PTpk1o27YtXn31VXTu3BnZ2dnuzh4RERFRqcDgHBERERFZpdfrUbVqVYSFhaFx48Z46623sGbNGmzatAmLFy8GAMycORMPP/wwAgICEB4ejldeeQU3btwAACQkJCAuLg7Xr1831sIbP348ACAzMxNvvPEGwsLCEBAQgJiYGCQkJLjnixIRERG5EYNzREREROSwJ554Ag0aNMCqVasAAB4eHpg7dy4OHz6Mzz//HFu3bsXIkSMBAM2bN8fs2bMRGBiI1NRUpKam4o033gAADB06FLt378ayZctw4MABPP/88+jUqRNOnjzptu9GRERE5A46pZRydyaIiIiIqGTp378/0tLS8N133+V5rVevXjhw4ACOHDmS57WVK1di0KBB+OuvvwBIn3OvvfYa0tLSjOv8+eefqF27Nv7880+EhoYal7dr1w5NmzbFpEmTXP59iIiIiEoqL3dngIiIiIjuLUop6HQ6AMBPP/2EyZMn49ixY0hPT0d2djbu3LmDW7duwd/f3+r7Dx48iJycHERFRVksz8zMRMWKFYs8/0REREQlCYNzREREROSUo0ePolatWkhOTkbnzp0xePBgTJw4Effddx927tyJAQMGICsry2Zw7saNG/D09ERiYiI8PT0tXitXrlxxfAUiIiKiEoPBOSIiIiJy2NatW3Hw4EG8/vrrSExMhMFgwIwZM+DhIV0ZL1++3GJ9Hx8f5OTkWCxr1KgRcnJycPnyZbRs2bLY8k5ERERUEjE4R0RERERWZWZm4uLFi8jJycGlS5fw/fffY/LkyejcuTNiY2Nx6NAh3L17F/PmzUOXLl3wyy+/YMGCBRZp1KxZEzdu3MCWLVvQoEED+Pv7IyoqCn369EFsbCxmzJiBRo0a4cqVK9iyZQvq16+Pp59+2k3fmIiIiKj4cbRWIiIiIrLq+++/R7Vq1VCzZk106tQJ27Ztw9y5c7FmzRp4enqiQYMGmDlzJt5//33Uq1cPS5cuxeTJky3SaN68OQYNGoSePXuicuXKmDp1KgBg0aJFiI2Nxb///W9ER0ejW7du+PXXX1GjRg13fFUiIiIit+ForURERERERERERG7CmnNERERERERERERuwuAcERERERERERGRmzA4R0RERERERERE5CYMzhEREREREREREbkJg3NERERERERERERuwuAcERERERERERGRmzA4R0RERERERERE5CYMzhEREREREREREbkJg3NERERERERERERuwuAcERERERERERGRmzA4R0RERERERERE5Cb/Dy6OJrEHbXhVAAAAAElFTkSuQmCC"/>
</div>
</div>
</div>
</div>
</div>
<div class="jp-Cell jp-MarkdownCell jp-Notebook-cell">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea"><div class="jp-InputPrompt jp-InputArea-prompt">
</div><div class="jp-RenderedHTMLCommon jp-RenderedMarkdown jp-MarkdownOutput" data-mime-type="text/markdown">
</div>
</div>
</div>
</div><div class="jp-Cell jp-CodeCell jp-Notebook-cell jp-mod-noOutputs">
<div class="jp-Cell-inputWrapper" tabindex="0">
<div class="jp-Collapser jp-InputCollapser jp-Cell-inputCollapser">
</div>
<div class="jp-InputArea jp-Cell-inputArea">
<div class="jp-InputPrompt jp-InputArea-prompt">In [ ]:</div>
<div class="jp-CodeMirrorEditor jp-Editor jp-InputArea-editor" data-type="inline">
<div class="cm-editor cm-s-jupyter">
<div class="highlight hl-ipython3"><pre><span></span> 
</pre></div>
</div>
</div>
</div>
</div>
</div>
</main>
</body>
</html>
