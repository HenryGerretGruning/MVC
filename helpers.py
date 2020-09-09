elemendid = []

# lisame ELEMENT juurde

def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        if nimetus in element.values():
            nimetused.append(nimetus)
    if nimetus in nimetused:
        print("Elemendid {} on juba olemas".format(nimetus))
    else:
        elemendid.append({'nimetus':nimetus, 'hind':hind, 'kogus':kogus})




# lisame ELEMENDID KORRAGE juurde
def lisa_elemendid(elemendid_nimekiri):
    global elemendid
    elemendid = elemendid_nimekiri

def main():

    # loome katse andmestik
    katse_elemendid = [
            {'nimetus': 'leib', 'hind': 0.80, 'kogus': 20},
            {'nimetus': 'piim', 'hind': 0.50, 'kogus': 15},
            {'nimetus': 'vein', 'hind': 5.60, 'kogus': 5},
    ]

    # testime elementide lisamist.
    lisa_elemendid(katse_elemendid)
    print(elemendid)

    lisa_element('kohupiim', 0.80, 15)
    print(elemendid)

    lisa_element('leib', 0.80, 5)
    print(elemendid)


# käivitamine
if __name__ == '__main__':
     main()