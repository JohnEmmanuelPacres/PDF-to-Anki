import genanki
import random

def build_deck(flashcards, deck_name):
    #1 Create a unique model ID
    deck_id = random.randrange(1 << 30, 1 << 31)

    #2 Define the model for flashcards
    my_model = genanki.Model(
        1607392319,
        'Simple Flashcard Model',
        fields=[
            {'name': 'Question'},
            {'name': 'Answer'},
        ],
        templates=[
            {
                'name' : 'Card 1',
                'qfmt' : '{{Question}}',
                'afmt' : '{{FrontSide}}<hr id="answer">{{Answer}}',
            },
        ],
        # design
        css="""
        .card {
            font-family: arial;
            font-size: 20px;
            text-align: center;
            color: black;
            background-color: white;
        }
        """
    )

        #3 Create the deck
    my_deck = genanki.Deck(deck_id, deck_name)

        # 4 Add notes to the deck
    for card in flashcards:
        #Ensure we have data for both sides
        if 'front' in card and 'back' in card:
            note = genanki.Note(
                model = my_model,
                fields = [card['front'], card['back']]
            )
        my_deck.add_note(note)
        
        # 5 Save the deck to a file
    output_filename = f"{deck_name.replace(' ', '_')}.apkg"
    genanki.Package(my_deck).write_to_file(output_filename)

    return output_filename