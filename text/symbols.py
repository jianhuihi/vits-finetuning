'''
Defines the set of symbols used in text input to the model.
'''

'''# japanese_cleaners
_pad        = '_'
_punctuation = ',.!?-'
_letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧ↓↑ '
'''

'''# japanese_cleaners2
_pad        = '_'
_punctuation = ',.!?-~…'
_letters = 'AEINOQUabdefghijkmnoprstuvwyzʃʧʦ↓↑ '
'''

'''# korean_cleaners
_pad        = '_'
_punctuation = ',.!?…~'
_letters = 'ㄱㄴㄷㄹㅁㅂㅅㅇㅈㅊㅋㅌㅍㅎㄲㄸㅃㅆㅉㅏㅓㅗㅜㅡㅣㅐㅔ '
'''

'''# chinese_cleaners
_pad        = '_'
_punctuation = '，。！？—…'
_letters = 'ㄅㄆㄇㄈㄉㄊㄋㄌㄍㄎㄏㄐㄑㄒㄓㄔㄕㄖㄗㄘㄙㄚㄛㄜㄝㄞㄟㄠㄡㄢㄣㄤㄥㄦㄧㄨㄩˉˊˇˋ˙ '
'''

# zh_ja_mixture_cleaners
# _pad        = '_'
# _punctuation = ',.!?-~…'
# _letters = 'AEINOQUabdefghijklmnoprstuvwyzʃʧʦɯɹəɥ⁼ʰ`→↓↑ '

_pad        = '_'
_punctuation = '，。！？—…'
# Mandarin pinyin letters
_letters = 'a b c d e f g h i j k l m n o p q r s t u v w x y z zh ch sh ai ei ui ao ou iu ie üe er an en in un ün ang eng ing ong'
letter_list = _letters.split(' ')
letter_list.append(' ')


# 需要注意的是，在汉语拼音中，字母ü 通常在没有声母的情况下被写作v，比如说"绿"被拼写为"lv"。


# Export all symbols:
symbols = [_pad] + list(_punctuation) + list(letter_list)

print(len(symbols))

print(symbols)

# Special symbol ids
SPACE_ID = symbols.index(" ")