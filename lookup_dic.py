
reveresd_array = []
lookup_reverse_dic_CODE = {}
lookup_dic_CODE = {}



def create_dic_code():
    global lookup_reverse_dic_CODE
    global lookup_dic_CODE
    with open ('phrase.csv') as  reveresd_array:
     for row in reveresd_array:
        replace_with, phrase = row
        # Now print fetched result
        lookup_dic_CODE.update({replace_with: [phrase]})
        lookup_reverse_dic_CODE.update({phrase: [replace_with]})
    cursor.close()
    return


def reverse_replace(_token_):
    global lookup_dic_CODE
    for item in lookup_dic_CODE.items():
        _token_ = str.replace(_token_, item[0], item[1][0])

    return _token_
