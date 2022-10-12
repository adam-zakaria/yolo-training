def remove_persons_from_detections():
    f = 'remove_test.txt'
    with open(f, encoding='latin-1') as fx:
        ls = ""
        for l in fx:
            if l.split()[0] == '0': continue
            else: 
                print(l)
                ls += l
            #l = ' '.join(l) + '\n'
    with open(f, 'w', encoding='latin-1') as fy:
        fy.write(ls)
    return
remove_persons_from_detections()