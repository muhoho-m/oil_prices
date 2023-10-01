import pandas as pd
import numpy as np

# load files zenye tuna analize
file_ya_super = pd.read_csv('super_m.csv')
file_ya_diesel = pd.read_csv("diesel_m.csv")
file_ya_kerosene = pd.read_csv("kerosene_m.csv")

super_file_path = "super_m.csv"
diesel_file_path = "diesel_m.csv"
kerosene_file_path = "kerosene_m.csv"

"""Function ya kuangalia data iko na outliers"""


def detect_outliers(data):
    outliers = []
    # outliers zitakua zile ziko beyond two standard deviations
    threshold = 2
    mean = np.mean(data)
    std = np.std(data)
    for i in data:
        z_score = (i - mean) / std
        if np.abs(z_score) > threshold:
            outliers.append(i)
    return outliers


def maelezo_ya_super_file(file_path, file):
    # naanalize data ya kila mwezi
    # niko na data ya kutoka jan 22 hadi july 2023
    # nataka kuona trends ziko kwa data
    data_super = file.describe()
    """1. Bei imepanda kutoka wapi hadi wapi na by how much"""
    for mwezi in data_super.columns:
        print(f"Super sold at {file[mwezi].mean():.2f} Ksh for the month of {mwezi}.")

    bei_ya_jan22 = data_super["jan22"].mean()
    bei_ya_jun23 = data_super["jun23"].mean()
    diff_ya_bei = bei_ya_jun23 - bei_ya_jan22
    print(f"Kwa miezi kumi na tisa, bei ya mafuta imepanda na shillingi {diff_ya_bei:.2f}")

    """2. Towns gani ziko na bei ya juu kila time"""
    """natafuta ooutlier wa kila mwezi
    alafu naziweka ka dictionary with key[month], values[list[outlier_values]]"""
    print("\n")
    # chukua data ya kila mwezi
    data_ya_jan22 = file["jan22"]
    # angalia bei za juu kwa kila town hio mwezi
    # weka hizo bei kwa list
    outliers_za_jan22 = detect_outliers(data_ya_jan22)
    print(f"Bei za juu January 2022 \n{outliers_za_jan22}")

    print("\n")
    data_ya_feb22 = file["feb22"]
    outliers_za_feb22 = detect_outliers(data_ya_feb22)
    print(f"Bei za juu February 2022 \n{outliers_za_feb22}")

    print("\n")
    data_ya_mar22 = file["mar22"]
    outliers_za_mar22 = detect_outliers(data_ya_mar22)
    print(f"Bei za juu March 2022 \n{outliers_za_mar22}")

    print("\n")
    data_ya_apr22 = file["apr22"]
    outliers_za_apr22 = detect_outliers(data_ya_apr22)
    print(f"Bei za juu April 2022 \n{outliers_za_apr22}")

    print("\n")
    data_ya_may22 = file["may22"]
    outliers_za_may22 = detect_outliers(data_ya_may22)
    print(f"Bei za juu May 2022 \n{outliers_za_may22}")

    print("\n")
    data_ya_jun22 = file["jun22"]
    outliers_za_jun22 = detect_outliers(data_ya_jun22)
    print(f"Bei za juu June 2022 \n{outliers_za_jun22}")

    print("\n")
    data_ya_jul22 = file["jul22"]
    outliers_za_jul22 = detect_outliers(data_ya_jul22)
    print(f"Bei za juu July 2022 \n{outliers_za_jul22}")

    print("\n")
    data_ya_aug22 = file["aug22"]
    outliers_za_aug22 = detect_outliers(data_ya_aug22)
    print(f"Bei za juu August 2022 \n{outliers_za_aug22}")

    print("\n")
    data_ya_sep22 = file["sep22"]
    outliers_za_sep22 = detect_outliers(data_ya_sep22)
    print(f"Bei za juu September 2022 \n{outliers_za_sep22}")

    print("\n")
    data_ya_oct22 = file["oct22"]
    outliers_za_oct22 = detect_outliers(data_ya_oct22)
    print(f"Bei za juu October 2022 \n{outliers_za_oct22}")

    print("\n")
    data_ya_nov22 = file["nov22"]
    outliers_za_nov22 = detect_outliers(data_ya_nov22)
    print(f"Bei za juu November 2022 \n{outliers_za_nov22}")

    print("\n")
    data_ya_dec22 = file["dec22"]
    outliers_za_dec22 = detect_outliers(data_ya_dec22)
    print(f"Bei za juu December 2022 \n{outliers_za_dec22}")

    print("\n")
    data_ya_jan23 = file["jan23"]
    outliers_za_jan23 = detect_outliers(data_ya_jan23)
    print(f"Bei za juu January 2023 \n{outliers_za_jan23}")

    print("\n")
    data_ya_feb23 = file["feb23"]
    outliers_za_feb23 = detect_outliers(data_ya_feb23)
    print(f"Bei za juu February 2023 \n{outliers_za_feb23}")

    print("\n")
    data_ya_mar23 = file["mar23"]
    outliers_za_mar23 = detect_outliers(data_ya_mar23)
    print(f"Bei za juu March 2023 \n{outliers_za_mar23}")

    print("\n")
    data_ya_apr23 = file["apr23"]
    outliers_za_apr23 = detect_outliers(data_ya_apr23)
    print(f"Bei za juu April 2023 \n{outliers_za_apr23}")

    print("\n")
    data_ya_may23 = file["may23"]
    outliers_za_may23 = detect_outliers(data_ya_may23)
    print(f"Bei za juu May 2023 \n{outliers_za_may23}")

    print("\n")
    data_ya_jun23 = file["jun23"]
    outliers_za_jun23 = detect_outliers(data_ya_jun23)
    print(f"Bei za juu June 2023 \n{outliers_za_jun23}")

    print("\n")
    data_ya_jul23 = file["jul23"]
    outliers_za_jul23 = detect_outliers(data_ya_jul23)
    print(f"Bei za juu July 2023 \n{outliers_za_jul23}")

    # weka hao outliers kwa list
    # chukua bei za kila town per mwezi

    data_ya_towns = pd.read_csv(file_path, index_col="town")

    # data ya Janury
    jan22 = {}
    feb22 = {}
    mar22 = {}
    apr22 = {}
    may22 = {}
    jun22 = {}
    jul22 = {}
    aug22 = {}
    sep22 = {}
    oct22 = {}
    nov22 = {}
    dec22 = {}
    jan23 = {}
    feb23 = {}
    mar23 = {}
    apr23 = {}
    may23 = {}
    jun23 = {}
    jul23 = {}

    # data ya Janury
    for town, data in data_ya_towns.iterrows():
        # data ya kila mwezi
        # naweka data ya kila mwezi per month kwa dictionary
        jan22[town] = data[0]
        feb22[town] = data[1]
        mar22[town] = data[2]
        apr22[town] = data[3]
        may22[town] = data[4]
        jun22[town] = data[5]
        jul22[town] = data[6]
        aug22[town] = data[7]
        sep22[town] = data[8]
        oct22[town] = data[9]
        nov22[town] = data[10]
        dec22[town] = data[11]
        jan23[town] = data[12]
        feb23[town] = data[13]
        mar23[town] = data[14]
        apr23[town] = data[15]
        may23[town] = data[16]
        jun23[town] = data[17]
        jul23[town] = data[18]

    # naweka list ya towns ndo nicompare badae
    # kila town enye iko na value more thn minimum iko kwa
    # list ya outliers per month inachukuliwa

    print("\n")
    print(f"In the month of january 2022, towns with the highest prices were:")
    towns_za_jan22 = []
    for towni, price in jan22.items():
        if price >= min(outliers_za_jan22):
            towns_za_jan22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of february 2022, towns with the highest prices were:")
    towns_za_feb22 = []
    for towni, price in feb22.items():
        if price >= min(outliers_za_feb22):
            towns_za_feb22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of March 2022, towns with the highest prices were:")
    towns_za_mar22 = []
    for towni, price in mar22.items():
        if price >= min(outliers_za_mar22):
            towns_za_mar22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of April 2022, towns with the highest prices were:")
    towns_za_apr22 = []
    for towni, price in apr22.items():
        if price >= min(outliers_za_apr22):
            towns_za_apr22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of May 2022, towns with the highest prices were:")
    towns_za_may22 = []
    for towni, price in may22.items():
        if price >= min(outliers_za_may22):
            towns_za_may22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of June 2022, towns with the highest prices were:")
    towns_za_jun22 = []
    for towni, price in jun22.items():
        if price >= min(outliers_za_jun22):
            towns_za_jun22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of July 2022, towns with the highest prices were:")
    towns_za_jul22 = []
    for towni, price in jul22.items():
        if price >= min(outliers_za_jul22):
            towns_za_jul22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of August 2022, towns with the highest prices were:")
    towns_za_aug22 = []
    for towni, price in aug22.items():
        if price >= min(outliers_za_aug22):
            towns_za_aug22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of September 2022, towns with the highest prices were:")
    towns_za_sep22 = []
    for towni, price in sep22.items():
        if price >= min(outliers_za_sep22):
            towns_za_sep22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of October 2022, towns with the highest prices were:")
    towns_za_oct22 = []
    for towni, price in oct22.items():
        if price >= min(outliers_za_oct22):
            towns_za_oct22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of November 2022, towns with the highest prices were:")
    towns_za_nov22 = []
    for towni, price in nov22.items():
        if price >= min(outliers_za_nov22):
            towns_za_nov22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of December 2022, towns with the highest prices were:")
    towns_za_dec22 = []
    for towni, price in dec22.items():
        if price >= min(outliers_za_dec22):
            towns_za_dec22.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of january 2023, towns with the highest prices were:")
    towns_za_jan23 = []
    for towni, price in jan23.items():
        if price >= min(outliers_za_jan23):
            towns_za_jan23.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of february 2023, towns with the highest prices were:")
    towns_za_feb23 = []
    for towni, price in feb23.items():
        if price >= min(outliers_za_feb23):
            towns_za_feb23.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of March 2023, towns with the highest prices were:")
    towns_za_mar23 = []
    for towni, price in mar23.items():
        if price >= min(outliers_za_mar23):
            towns_za_mar23.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of April 2023, towns with the highest prices were:")
    towns_za_apr23 = []
    for towni, price in apr23.items():
        if price >= min(outliers_za_apr23):
            towns_za_apr23.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of May 2023, towns with the highest prices were:")
    towns_za_may23 = []
    for towni, price in may23.items():
        if price >= min(outliers_za_may23):
            towns_za_may23.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of June 2023, towns with the highest prices were:")
    towns_za_jun23 = []
    for towni, price in jun23.items():
        if price >= min(outliers_za_jun23):
            towns_za_jun23.append(towni)
            print(f"{towni}  Ksh: {price}")

    print("\n")
    print(f"In the month of July 2023, towns with the highest prices were:")
    towns_za_jul23 = []
    for towni, price in jul23.items():
        if price >= min(outliers_za_jul23):
            towns_za_jul23.append(towni)
            print(f"{towni}  Ksh: {price}")

    # naweka list ya kila mwezi ya towns kwa list moja
    towns_za_bei_ghali = [towns_za_jan22, towns_za_feb22, towns_za_mar22, towns_za_apr22, towns_za_may22,
                          towns_za_jun22, towns_za_jul22, towns_za_aug22, towns_za_sep22, towns_za_oct22,
                          towns_za_nov22, towns_za_dec22, towns_za_jan23, towns_za_feb23, towns_za_mar23,
                          towns_za_apr23, towns_za_may23, towns_za_jun23, towns_za_jul23]

    # eka towns zote kwa list moja
    list_towns_za_bei_ghali = []
    for towns_za_bei in towns_za_bei_ghali:
        for town in towns_za_bei:
            list_towns_za_bei_ghali.append(town)

    # angalia towns ngapi zimekua na bei ya juu throughout the period
    towns_uniq = np.unique(list_towns_za_bei_ghali)
    list_ya_towns_uniq = list(towns_uniq)
    print("\n")
    print(f"Towns zimekua na bei ya juu all through ni {len(list_ya_towns_uniq)}")

    # angalia kila town imekua na bei ya juu mara ngapi throughout the period
    print(f"\n")
    print(f"HOW MANY TIMES HAS EACH TOWN HAD A PRICE OFF THE SCALE?")
    from collections import Counter
    count_towns = Counter(list_towns_za_bei_ghali)
    for kila_town, mara_imetajwa in count_towns.items():
        print(f"{kila_town} imekua na bei ya juu miezi {mara_imetajwa}")

    # angalia towns gani zimekua ma bei ya juu mara mingi kabisaa
    print("\n")
    print(f"TOWNS GANI ZIMEKUA NA BEI YA JUU MARA MINGI")
    for high_town, mara_imetajwa in count_towns.items():
        if mara_imetajwa > 10:
            print(f"{high_town} imekua na bei ya juu mara {mara_imetajwa}")

    # kama bei ya hio town ya hiomwezi iko kwa list ya outliers then
    # hio town iko na bei ya juu
    # weka hizo towns kwa list per mwezi
    # tafuta towns zenye ziko kwa list ya kila mwezi
    # and that makes towns zenye ziko na bei ya juu kila time

    """3. Block gani ya mwaka kuna bei ziliongezeka kuliko zingine. 
    Jan-Mar, Apr-Jun, Jul-Sep, Oct-Dec"""

    print(f"Behaviour ya bei over periods of three months time.")
    mean_ya_data = file.describe()
    mean_jan_mar22 = (mean_ya_data["jan22"].mean() +
                      mean_ya_data["feb22"].mean() +
                      mean_ya_data["mar22"].mean()) / 3

    mean_apr_jun22 = (mean_ya_data["apr22"].mean() + mean_ya_data["may22"].mean() + mean_ya_data["jun22"].mean()) / 3
    mean_jul_sep22 = (mean_ya_data["jul22"].mean() + mean_ya_data["aug22"].mean() + mean_ya_data["sep22"].mean()) / 3
    mean_oct_dec22 = (mean_ya_data["oct22"].mean() + mean_ya_data["nov22"].mean() + mean_ya_data["dec22"].mean()) / 3
    mean_jan_mar23 = (mean_ya_data["jan23"].mean() + mean_ya_data["feb23"].mean() + mean_ya_data["mar23"].mean()) / 3
    mean_apr_jun23 = (mean_ya_data["apr23"].mean() + mean_ya_data["may23"].mean() + mean_ya_data["jun23"].mean() +
                      mean_ya_data["jul23"].mean()) / 4

    print("")
    print(f"Petrol prices from:")
    print(f"January to March 2022: Ksh {mean_jan_mar22:.2f}")
    print(f"April to June 2022: Ksh {mean_apr_jun22:.2f}")
    print(f"July to September 2022: Ksh {mean_jul_sep22:.2f}")
    print(f"October to December 2022: Ksh {mean_oct_dec22:.2f}")
    print(f"January to March 2023: Ksh {mean_jan_mar23:.2f}")
    print(f"April to June 2023: Ksh {mean_apr_jun23:.2f}")

    """Naangalia vile bei ya mafuta over certain period of time."""
    block_ya_kwanza = mean_apr_jun22 - mean_jan_mar22  # 14.88
    block_ya_pili = mean_jul_sep22 - mean_apr_jun22  # 10.89
    block_ya_tatu = mean_oct_dec22 - mean_jul_sep22  # 8.97
    block_ya_nne = mean_jan_mar23 - mean_oct_dec22  # -2.25
    block_ya_tano = mean_apr_jun23 - mean_jan_mar23  # 6.76
    diff = [block_ya_kwanza, block_ya_pili, block_ya_tatu, block_ya_nne, block_ya_tano]

    print("")
    print(f"The highest rise in fuel in blocks of three months"
          f" happened during March 2022 and June 2022 with a jump of {max(diff):.2f} Ksh")
    print("")
    print(f"There was a drop of fuel prices between the periods of"
          f" October-December 2022 and January-March 2023 by {block_ya_nne:.2f} Ksh")
    print("")
    print(f"The margins for fuel increament is decreasing in blocks of three months")


maelezo_ya_super_file(diesel_file_path, file_ya_diesel)

print("\n")
print("FINDINGS ZA SUPER PRICES")
print(f"Bungoma na Thika ndo towns zimekua na bei ya juu for the longest time"
      f" being na bei ya juu for 16 of 19 months each")
print("")
print(f"Iten, Kilifi, Eldoret, Muhoroni, Kainuk na Lomut zinafuata with them"
      f" being na bei ya juu for 15 of 19 months")
print("")
print(f"Lungalunga inafuata na 14 na Makuyu na 12 of the 19 months each")
print("")
print(f"It is worth to note that most of the towns ziko na bei ya juu most of the time ni zenye"
      f" ziko interior.")
print("")

"""1. Bei imepanda kutoka wapi hadi wapi na by how much"""

"""2. Towns gani ziko na bei ya juu kila time."""

"""3. Block gani ya mwaka kuna bei ziliongezeka kuliko zingine in spans of three months. 
Jan-Mar, Apr-Jun, Jul-Sep, Oct-Dec"""
