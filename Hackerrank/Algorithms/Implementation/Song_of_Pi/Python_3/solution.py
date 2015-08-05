value_pi = "31415926535897932384626433833"
n = int(input())
for i in range(0,n):
    sentence = input()
    words = sentence.split(' ')
    value_of_song = []
    for word in words:
        size_word = len(word)
        value_of_song.append(str(size_word))
    value_of_song = ''.join(value_of_song)
    if value_of_song == value_pi[0:len(value_of_song)]:
        print("It's a pi song.")
    else:
        print("It's not a pi song.")
