import argparse

import enviro_design
from card_design import Cards

def get_args():
    parser = argparse.ArgumentParser(description='make decck')
    parser.add_argument(
        '-n',
        '--name',
        default='card',
        help='card',
    )
    return parser.parse_args()
# mae a new card and add it to a new deck
def main():
    args = get_args()
    new_card = Cards.make_card(args.name)
    new_deck = Cards.make_deck(args.name)
    Cards.add_card_to_deck(new_deck, new_card)
    print(f'new_card = {new_card}')
    print(f"number of cards:", len(Cards.self.deck))
    print("here are the cards:" + str(Cards.cards))     
    

if __name__ == '__main__':
    
    main()