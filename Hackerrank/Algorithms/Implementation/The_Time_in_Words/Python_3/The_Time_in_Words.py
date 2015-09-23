hours_in_words = ['one', 'two', 'three','four','five','six','seven','eight','nine','ten','eleven','twelve']
minutes_in_words = ['zero','one', 'two', 'three','four','five','six','seven','eight','nine','ten','eleven',
                    'twelve', 'thirteen', 'fourteen', 'fifteen','sixteen','seventeen','eighteen','nineteen',
                    'twenty','twenty one','twenty two','twenty three', 'twenty four', 'twenty five',
                    'twenty six','twenty seven', 'twenty eight', 'twenty nine','thirty']

hours = input()
minutes = input()

hours_word = ""
minutes_word = ""

if int(minutes) <= 30:
    hours_word = hours_in_words[int(hours)-1]
    minutes_word = minutes_in_words[int(minutes)]
else:
    hours_word = hours_in_words[int(hours)]
    minutes_word = minutes_in_words[len(minutes_in_words)-1-(int(minutes)-30)]

if minutes == "00":    
    print(hours_word + " o' clock")
elif minutes == "01":
    print(minutes_word + " minute past " + hours_word)
elif minutes == "15":
    print("quarter past " + hours_word)
elif int(minutes) < 30:
    print(minutes_word + " minutes past " + hours_word)
elif minutes == "30":
    print("half past " + hours_word)
elif minutes == "45":
    print("quarter to " + hours_word)
elif int(minutes) < 59:
    print(minutes_word + " minutes to " + hours_word)
elif minutes == "59":
    print(minutes_word + " minute to " + hours_word)