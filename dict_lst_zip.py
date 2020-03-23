l1=['1','2','3','4']
l2=['a','b','c','d']

def complst(l1,l2):
    if l1==l2:
        return "same elements"
    return dict(zip(l1,l2))
print("Result:",complst(l1,l2))
