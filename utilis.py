def segmentation (sales):
    if sales<=3:
        return "bas"
    elif 3>sales<=50:
        return "moyen"
    elif 3>sales<=100:
        return "haut"
    else:
        return "tres haut"