def calc_Percentage(rec):
    if not rec:
        return "Cannot calculate Empty Record!"
    else:
        return (rec[3] + rec[4] + rec[5] + rec[6] + rec[7]) / 5
