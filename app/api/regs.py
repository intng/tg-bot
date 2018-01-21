from app.postgres import regs
import json

def activate(token):
    if regs.check_reg(token):
        res = regs.check_reg()
        return json.dumps({'activated': True, 'user': {'id': res[1], 'name': res[2], 'surname': res[3]}})
    else:
        pass