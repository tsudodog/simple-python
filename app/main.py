import fire

def hello(name="World"):
    print("I am new code.")
    return "Hello %s" % name

if __name__ =='__main__':
    fire.Fire(hello)