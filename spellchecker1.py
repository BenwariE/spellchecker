from spellchecker import SpellChecker
def input_text():
    input_text = input('eneter your text')
    return autocorrectword(input_text)
def autocorrectword(input_tex):
    words = input_text.split()
    corrected_words =[]
    for word in words :
        spell = SpellChecker()
        
        if spell.unknown(word):
            corrected_word= spell.candidates(word)
            corrected_words.append(corrected_word.pop())
        else:
            corrected_words.append(word)  
        corrected_text = ''.join(corrected_words)
        return print(corrected_text) 
if __name__ == '__main__':
    input_text()
    
 