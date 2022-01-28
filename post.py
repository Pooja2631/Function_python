post=input("enter the postname...")
def disco():
    if post=='disco':
        return"deepti\n1.displine\n2.fill the attendence sheet"

def fc():
    if post=='fc':
        return "neha\n1.mange the kicthen\n2.order the vegetable"

def hc():
    if post=='hc':
        return"karisha\n1.care the ill person\n2.giving honey water"

def tmp():
    if post=='tmp':
        return"anisha\n1.assing the mentor\n2.mange the academic"

def it():
    if post=='it':
        return"nishu\n1.mange the net\n2.giving laptop"

def outreach():
    if post=='outreach':
        return"chandni  \n1.post photo in facebook\n2.who got job mange the farewall"
    
def main_fun():
    if post=='disco':
        print(disco())
    if post=='fc':
        print(fc())
    if post=='hc':
        print(hc())
    if post=='tmp':
        print(tmp())
    if post=='it':
        print(it())
    if post=='outreach':
        print(outreach())
main_fun()