
elemendid = []

# lisame ELEMENT juurde

def lisa_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
            nimetused.append(nimetus)
            nimetused.append(list(element.values())[0])
    if nimetus in nimetused:
        print("Elemendid {} on juba olemas".format(nimetus))
    else:
        elemendid.append({'nimetus':nimetus, 'hind':hind, 'kogus':kogus})




# lisame ELEMENDID KORRAGE juurde
def lisa_elemendid(elemendid_nimekiri):
    global elemendid
    elemendid = elemendid_nimekiri
# loeme ELEMENDID korraga, aga nii, et tagastame iga kord üks element

def loe_elemendid():
    global elemendid
    loetud_elemendid = []
    for element in elemendid:
        loetud_elemendid.append(element)
    return loetud_elemendid



# loeme KONKREETNE ELEMENT
def loe_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
            nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Elemendid {} ei eksisteeri".format(nimetus)
    else:
        return elemendid[nimetused.index(nimetus)]

# uuendame KONKREETSE elemendi
def uuenda_element(nimetus, hind, kogus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Elementi {} ei saa uuendada, kuna ta ei eksisteeri".format(nimetus)
    else:
        elemendid[nimetused.index(nimetus)] = {'nimetus':nimetus, 'hind':hind, 'kogus':kogus}

# kustutame KONKREETSE elemendi
def kustuta_element(nimetus):
    global elemendid
    nimetused = []
    for element in elemendid:
        nimetused.append(list(element.values())[0])
    if nimetus not in nimetused:
        return "Elementi {} ei saa uuendada, kuna ta ei eksisteeri".format(nimetus)
    else:
        elemendid.remove(elemendid[nimetused.index(nimetus)])

# kustutame KÕIK elemendid
def kustutaKÕIK_elemendid():
    global elemendid
    elemendid.clear()

def main():

    # loome katse andmestik
    katse_elemendid = [
            {'nimetus': 'leib', 'hind': 0.80, 'kogus': 20},
            {'nimetus': 'piim', 'hind': 0.50, 'kogus': 15},
            {'nimetus': 'vein', 'hind': 5.60, 'kogus': 5},
    ]

    # testime elementide lisamist.
    lisa_elemendid(katse_elemendid)
    #print(elemendid)

    lisa_element('kohupiim', 0.80, 15)
    #print(elemendid)

    lisa_element('vein', 0.80, 5)
    #print(elemendid)

    loe_elemendid()
    #print(elemendid)

    #uuenda_element("vein", 10.0, 10)
    #print(loe_element("vein"))

    #kustuta_element("vein")
    kustutaKÕIK_elemendid()
    print(loe_elemendid())

    #print(loe_element('vein'))
#käivitamine
if __name__ == '__main__':
     main()


