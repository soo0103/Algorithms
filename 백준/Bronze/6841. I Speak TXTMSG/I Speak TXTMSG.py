form = {"CU": "see you",
        ":-)": "I’m happy",
        ":-(": "I’m unhappy",
        ";-)": "wink",
        ":-P": "stick out my tongue",
        "(~.~)": "sleepy",
        "TA": "totally awesome",
        "CCC": "Canadian Computing Competition",
        "CUZ": "because",
        "TY": "thank-you",
        "YW": "you’re welcome",
        "TTYL": "talk to you later"}

while 1:
    try:
        text = input()

        if text not in form:
            print(text)
        else:
            print(form[text])
    except:
        break