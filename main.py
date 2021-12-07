from os import path
import re
from openpyxl import load_workbook
from model import NFTJI, NFT
from excel import *
##################################################################################

def g(niz):
    return f'\033[0;92m{niz}\033[0m'
def b(niz):
    return f'\033[1;94m{niz}\033[0m'
def r(niz):
    return f'\033[1;91m{niz}\033[0m'

def open_json(file):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read().strip()
        name_sample = r'"name": "(.*)?",'
        name_match = re.findall(name_sample, text)
        attr_sample = r'"attributes": \[((.|\n)*)\]'
        attr_match = re.findall(attr_sample, text)
        attrs = attr_match[0][0].split('"')
        
        name = name_match[0]
        background = attrs[7]
        head = attrs[15]
        body = attrs[23]
        armor = attrs[31]
        helmet = attrs[39]
        left_hand = attrs[47]
        right_hand = attrs[55]

        return name, background, head, body, armor, helmet, left_hand, right_hand


def dodaj_nft(file_name):
    name, background, head, body, armor, helmet, left_hand, right_hand= open_json(file_name)
    nftji.add_nft(name, background, head, body, armor, helmet, left_hand, right_hand)



def extract_json_files(path):
    '''set to 9000 nft files'''
    for i in range(9000):
        file_name = path + str(i) + ".json"
        dodaj_nft(file_name)
    #nftji.shrani_stanje(DATA)

def get_list_of_values(trait):
    traits = [trait]
    for nft in nftji.nfts:
        traits.append(NFT.return_trait(nft, trait))
    return traits


def values_dictionary(trait):
    dict = {}
    list_of_values = get_list_of_values(trait)[1:]
    for value in list_of_values:
        if value not in dict:
            dict[value] = 1
        else:
            dict[value] += 1
    return dict


def excel_bulker(path, all_traits):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = len(all_traits)
    wb = load_workbook(path)
    names_list = get_list_of_values(all_traits[0])
    fill_the_name_column(wb, letters[0], names_list)

    nft_probability_list = []

    for i in range(1, l):
        dictionary_of_values = values_dictionary(all_traits[i])
        values_list = get_list_of_values(all_traits[i])
        probability_list = fill_the_attribute_column(wb, letters[i], values_list, dictionary_of_values)
        nft_probability_list.append(probability_list)
    
    fill_the_object_rarity_column(wb, letters[l], nft_probability_list)

    save_excel_file(wb, path)

def excel_columns_fix(excel_path, all_traits):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    l = len(all_traits)
    for letter in letters[:l+1]:
        set_column_width(excel_path, letter)

###########################################################################
#DATA = "shramba.json"
#try:
#    nftji = NFTJI.nalozi_stanje(DATA)
#except FileNotFoundError:
#    nftji = NFTJI()
###########################################################################

def main(json_path, all_traits, excel_path):
    extract_json_files(json_path)
    print(b("files extracted!"))
    excel_bulker(excel_path, all_traits)
    excel_columns_fix(excel_path, all_traits)
    

    print(g("excel workbook filled!"))

###########################################################################

'''variables:'''

jpath = "jsons/"
traits = ["name", "background", "head", "body", "armor", "helmet", "left hand", "right hand"]
excel = "excel_file/NFT.xlsx"

'''program'''

nftji = NFTJI()

try:
    main(jpath, traits, excel)
    print(b("Done"))
except FileNotFoundError:
    print(r("files missing"))

