BASE = {'record_id':'w3-001','repo':'Admissible-Existence/ECAT-ICAT','boundary':'w3','declared':True,'mapped':True,'scoped':True,'status':'READY','ready':True,'reason':'ready','timestamp':'2026-06-16T00:00:00Z'}

def item(**changes):
    x = dict(BASE)
    x.update(changes)
    return x

FIXTURES = [
    {'id':'ready','expected':'READY','record':item()},
    {'id':'declared','expected':'INCOMPLETE','record':item(declared=False,status='INCOMPLETE',ready=False)},
    {'id':'mapped','expected':'INCOMPLETE','record':item(mapped=False,status='INCOMPLETE',ready=False)},
    {'id':'scoped','expected':'INCOMPLETE','record':item(scoped=False,status='INCOMPLETE',ready=False)},
    {'id':'blocked','expected':'BLOCKED','record':item(status='READY',ready=False)},
]
