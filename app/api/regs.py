from app.postgres import regs
import json

def activate(token):
    if regs.check_reg(token):
        res = regs.check_reg(token)
        if res[1] != None:
            regs.del_reg(token)
            return json.dumps({'activated': True, 'user': {'id': res[1], 'name': res[2], 'surname': res[3]}})
        else:
            return json.dumps({'activated': False})
    else:
        regs.new_reg(token)
        return json.dumps({'activated': False, 'created': True})
