import os
import pandas as pd
import glob

data_files_path = "../simpo"


# kuangalia niko na files ngapi
csv_files = glob.glob(os.path.join(data_files_path, '*.csv'))
files = []
for file in csv_files:
    files.append(file)
print(f"Uko na files {len(files)} kwa folder yako")

# nataka kujua kila file iko na towns ngapi
def angalia_towns_ngapi(data_files_path):
    for file in os.listdir(data_files_path):
        file_path = os.path.join(data_files_path, file)
        files_ziko = pd.read_csv(file_path)
        column_ya_towns = files_ziko["Town"]
        towns = column_ya_towns.unique()
        print(f"{file} iko na towns {len(towns)}")


# document iko na towns kidogo ni 149, kumaanisha kila document iko na
# the 149 towns. hizi ndo nitatumia kwa analysis yangu
# unda list iko na towns za kwanza 149 zenye ziko kwa kila document
# natumia document ya january 2022 prices ju hio iko na 149 towns
# since kila file iko na towns tofauti, nataka kuangalia kwa files
# zote nione ni towns gani ziko kwa kila file

def tafuta_towns_common(data_files_path):
    # kuangalia majina za towns ziko kwa kila document
    # list ya towns ziko kwa kila document
    towns_common = []
    for file in os.listdir(data_files_path):
        file_path = os.path.join(data_files_path, file)
        files_ziko = pd.read_csv(file_path)
        towns = files_ziko["Town"].unique()
        # kwa kila document nachukua towns zote
        # alafu naziweka kwa list
        towns_common.append(list(towns))
        # hii list naiweka kwa list ingine
        # at the end nakua na list iko na list ya towns

    # ndo nifanye operation na hizi towns, zinahitaji kuwa kwa set
    # naweka list empty ya kuhold hizi sets
    town_sets = []
    for town in towns_common:
        # naloop throuh ile list iko na list ya towns kwa kila document
        town = set(town)
        # kila list inachenjiwa inakua set
        town_sets.append(town)
        # alafu naweka kila set kwa list ya sets

    # after tumeweka towns za kila fila kwa set yake,
    # nataka kuangalia ni towns gani na ngapi ziko kwa kila file
    # at the end ntachukua towns zenye ziko kwa kila file na data yake
    # towns zenye haziyuko kwa files zote nizidrop

    # nachukua file ya kwanza kwa list ya towns zote naitumia kama
    # base file ya kucompare towns ziko kwa files zote
    list_ya_towns = towns_common[0]
    # naconvert hii list kuwa set ndo iwe rahisi kucompre
    set_ya_towns = set(list_ya_towns)

    # nataka kucompare towns zote kwa files zote so naloop kwa zote
    for i in range(1, len(town_sets)):
        # after looping naangalia values gani ziko kwa files zote
        common_town = set_ya_towns.intersection(town_sets[i])

    # nachukua hizi values(towns) naziweka kwa list ndo ntatumia
    # kuchukua data nataka
    comm_nms = list(common_town)
    # sasa tuko na majina ya towns zenye ziko kwa files zote
    print(len(comm_nms))
    return comm_nms


# hapa sasa ni kuweka hizi towns kwa file ya super, diesel na kerosene
# ndo niweke data

def unda_files_safi():
    comm_nms = tafuta_towns_common(data_files_path)
    # hapa naunda files tatu, moja ya super,
    # moja ya diesel na moja ya kerosene
    # kwa kila izi files naweka column moja ya towns
    # zenye nimepata ziko commb kwa kila document

    # iongeze kwa file ya super
    file_ya_super = pd.read_csv("super_prices.csv")
    file_ya_super["town"] = comm_nms
    super_file_path = "super_prices.csv"
    file_ya_super.to_csv(super_file_path, index=False)

    # iongeze kwa file ya diesel
    file_ya_diesel = pd.read_csv('diesel_prices.csv')
    file_ya_diesel["town"] = comm_nms
    diesel_file_path = "diesel_prices.csv"
    file_ya_diesel.to_csv(diesel_file_path, index=False)

    # iongeze kwa file ya kerosene
    file_ya_kerosene = pd.read_csv("kerosene_prices.csv")
    file_ya_kerosene["town"] = comm_nms
    kerosene_file_path = "kerosene_prices.csv"
    file_ya_kerosene.to_csv(kerosene_file_path, index=False)

    # at the end nakuwa na files tatu in this order
    # super_prices.csv
    # town
    #
    # diesel_prices.csv
    # town
    # kerosene_prices.csv
    # town
    # hizi files ziko na towns zote common


# sasa nataka kuchukua data yote ya super kwa files zite niweke kwa file ya super
# same for diesel na kerosene

def weka_data_kwa_clean_files():
    # kwanza nichukue file moja nitoe towns za comparison
    file_ya_kerosene = pd.read_csv("kerosene_prices.csv")
    towns_nataka = file_ya_kerosene["town"].unique()

    # naweka hizi towns kwa list
    list_ya_towns_nataka = []
    for t in towns_nataka:
        list_ya_towns_nataka.append(t)

    # tuweke data ya super kutokakwa files zote kwa file ya super
    # kuloop kwa files zote kwanza
    for file in os.listdir(data_files_path):
        # kwanza natoa jina ya file ndo ntatumia kama label kwa clean document
        jina_ya_column = os.path.splitext(file)[0]
        file_path = os.path.join(data_files_path, file)
        # soma file
        files_ziko = pd.read_csv(file_path)

    # nahitaji kuwa na files zote ndo niziweke data
    # na path ya files zote ndo kusave data after kupopulate
    super_file_path = "super_prices.csv"
    diesel_file_path = "diesel_prices.csv"
    kerosene_file_path = "kerosene_prices.csv"

    file_ya_super = pd.read_csv("super_prices.csv")
    file_ya_diesel = pd.read_csv("diesel_prices.csv")

    # nataka kuloop kwa kila file, nichukue data ya super, diesel na
    # kerosene kwa zile towns ziko kwa kila document na niziweke kwa
    # files za kila commodity
    data_nataka_kwa_file = files_ziko[files_ziko["Town"].isin(list_ya_towns_nataka)]

    # kuongeza kwa super
    file_ya_super[jina_ya_column] = data_nataka_kwa_file["Super"]
    # jina ya file tunatoa data ndo itakua column head kwa file naweka data
    file_ya_super.to_csv(super_file_path, index=False)

    # ongeza ya diesel
    file_ya_diesel[jina_ya_column] = data_nataka_kwa_file["Diesel"]
    file_ya_diesel.to_csv(diesel_file_path, index=False)

    # ongeza ya kerosene
    file_ya_kerosene[jina_ya_column] = data_nataka_kwa_file["Kerosene"]
    file_ya_kerosene.to_csv(kerosene_file_path, index=False)

    # after hii operation ntakua na files tatu na data inakaa ivi
    # super_prices
    # town jan22 feb22 mar22 apr22 jun22  ... aug23

    # diesel_prices
    # town jan22 feb22 mar22 apr22 jun22  ... aug23

    # kerosene_prices
    # town jan22 feb22 mar22 apr22 jun22  ... aug23

    # kila file itakua na data ya commodity yake ya kila mwezi


file_ya_super = pd.read_csv("super_prices.csv")
file_ya_diesel = pd.read_csv("diesel_prices.csv")
file_ya_kerosene = pd.read_csv("kerosene_prices.csv")

# sasa niko  na files zote na data yote, wacha tuone data inakaa aje
def angalia_summary_ya_data():
    print(file_ya_super.describe())
    print(file_ya_diesel.describe())
    print(file_ya_kerosene.describe())


# kwanza kufill empty slots
# naona bado kuna empty slots kwa files
# nazifil na mode of the column since nliangalia file na
# prices in a month zinakaribia kufanana across multiple towns
def jaza_empty_cells():
    # nikifill empty slots ntaunda file ingine ya
    # kila commodity na nisave ikiwa na all slots filles
    super_zimejazwa = file_ya_super.fillna(file_ya_super.mode().iloc[0])
    jina_ya_super = "super_m.csv"
    super_zimejazwa.to_csv(jina_ya_super, index=False)

    diesel_zimejazwa = file_ya_diesel.fillna(file_ya_diesel.mode().iloc[0])
    jina_ya_diesel = "diesel_m.csv"
    diesel_zimejazwa.to_csv(jina_ya_diesel, index=False)

    kerosene_zimejazwa = file_ya_kerosene.fillna(file_ya_kerosene.mode().iloc[0])
    jina_ya_kerosene = "kerosene_m.csv"
    kerosene_zimejazwa.to_csv(jina_ya_kerosene, index=False)

    # after this ntakua na files zingine tatu
    # super_m.csv
    # Town jan22 feb22 mar22 apr22 jun22  ... aug23

    # diesel_m.csv
    # Town jan22 feb22 mar22 apr22 jun22  ... aug23

    # kerosene_m.csv
    # Town jan22 feb22 mar22 apr22 jun22  ... aug23
    # na sasa the data is cleaned and ready for analysis


"""kwanza angalia kwa files zote uone ni towns ngapi ziko kwa kila file
take these towns and create three files, super, diesel and kerosene
enda kwa files zote tena
using the created file towns, chukua data ya super, diesel na kerosene for the 19 files
and place them in their respective files
tumia jina ya file kama header ya column for each commodity
like kama file ya "mar22.csv", chukua the mar22 and use it as a header for that particular datapoint
final files

After this, I have data like:
super_prices.csv
Town jan22 feb22 mar22 apr22 jun22  ... aug23

diesel_prices.csv
Town jan22 feb22 mar22 apr22 jun22  ... aug23

kerosene_prices.csv
Town jan22 feb22 mar22 apr22 jun22  ... aug23
"""