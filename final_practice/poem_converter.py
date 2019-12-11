import re

class Poem_Converter:
    def __init__(self, converter):
        self.dict = converter
        self.original = None
        self.converted = None

    def Read_and_Convert(self, poem):
        self.original = poem
        poem = re.sub('\s*[,\.!\?]\s*','\n', poem)
        for k in self.dict:
            if isinstance(self.dict[k], int):
                poem = re.sub('\s^\n+'+k, k, poem)
                poem = re.sub(k, ' ' * self.dict[k] + k, poem)
            if isinstance(self.dict[k], str):
                poem = re.sub(k, self.dict[k], poem)
        self.converted = poem

    def Show_Poem(self, b):
        if b:
            print(self.converted)
        else:
            print(self.original)

if __name__ == "__main__":
    # poem = 'Two roads diverged in a yellow wood , And sorry I could not travel both . And be one traveler , long I stood . And looked down one as far as I could . To where it bent in the undergrowth .'
    poem = 'Scatter , as from an unextinguishd hearth . Ashes and sparks , my words among mankind ! Be through my lips to unawakend earth The trumpet of a prophecy! O Wind , If Winter comes , can Spring be far behind ?'
     
    # poem = 'This is a test, and anothertest, and a big                        test.'
    # layout_dictionary = {'test':3}

    # layout_dictionary = {'I': '>///<', 'it': '^o^', 'And':3}
    layout_dictionary = {'my': 'ORZ', 'of': '<(__)>', 'as':7} 

    c = Poem_Converter(layout_dictionary)
    c.Read_and_Convert(poem)
    c.Show_Poem(True)

