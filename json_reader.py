from os import name
import re
from model import NFTJI

##################################################################################



##################################################################################

def odpri_json(file):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read().strip()
        name_sample = r'"name": "(.*)?",'
        name_match = re.findall(name_sample, text)
        attr_sample = r'"attributes": \[((.|\n)*)\]'
        attr_match = re.findall(attr_sample, text)
        attrs = attr_match[0][0].split('"')
        
        
        name = name_match[0]
        background = attrs[7]
        head = attrs[23]
        armor = attrs[39]
        helmet = attrs[47]
        left_hand = attrs[71]
        right_hand = attrs[79]
        
        return name, background, head, armor, helmet, left_hand, right_hand



def dodaj_nft(file_name):
    name, background, head, armor, helmet, left_hand, right_hand = odpri_json(file_name)
    shramba.add_nft(name, background, head, armor, helmet, left_hand, right_hand)





def main():
    
    #for i in range(1, 10001):
    #    file_name = str(i) + ".json"
    #    dodaj_nft(file_name)
    
    file_name = str(1) + ".json"
    dodaj_nft(file_name)
    shramba.shrani_stanje(DATA)
    



DATA = "shramba.json"

try:
    shramba = NFTJI.nalozi_stanje(DATA)
except FileNotFoundError:
    shramba = NFTJI()


main()