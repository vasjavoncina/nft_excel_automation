import json

class NFT:

    def __init__(self, name, background, head, armor, helmet, left_hand, right_hand):
        self.name = name
        self.background = background
        self.head = head
        self.armor = armor
        self.helmet = helmet
        self.left_hand = left_hand
        self.right_hand = right_hand
        
class NFTJI:

    def __init__(self):
        self.nfts = []
        self.nfts_in_names = {}


    def v_slovar(self):
        return {
            "nfts":[
                {
                    "name": nft.name,
                    "background": nft.background,
                    "head": nft.head,
                    "armor": nft.armor,
                    "helmet": nft.helmet,
                    "left hand": nft.left_hand,
                    "right hand": nft.right_hand
                }
                for nft in self.nfts
            ]
        }

    def add_nft(self, name, background, head, armor, helmet, left_hand, right_hand):
        if name not in self.nfts_in_names:
            new = NFT(name, background, head, armor, helmet, left_hand, right_hand)
            self.nfts.append(new)
            self.nfts_in_names[name] = new
            return new

    @classmethod
    def iz_slovarja(cls, nft_slovar):
        nfts = cls()
        for nft in nft_slovar["nfts"]:
            nov_nft = nfts.add_nft(
                nft["name"],
                nft["background"],
                nft["head"],
                nft["armor"],
                nft["helmet"],
                nft["left hand"],
                nft["right hand"]
                )
        return nfts


    def shrani_stanje(self, ime_datoteke):
        with open(ime_datoteke, "w") as datoteka:
            json.dump(self.v_slovar(), datoteka, ensure_ascii=False, indent=4)


    @classmethod
    def nalozi_stanje(cls, ime_datoteke):
        with open(ime_datoteke) as datoteka:
            slovar_s_nftji = json.load(datoteka)
        return cls.iz_slovarja(slovar_s_nftji)