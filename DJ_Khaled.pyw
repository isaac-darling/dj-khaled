#DJ Khaled
#Isaac Darling
#2020 07
import inflect , time , sys , os

with open(__file__) as f:
    this = f.readlines()[:-1]

try:
    limit = int(sys.argv[1])
    this = [f"    limit = {limit}\n" if "limit = int" in i and "this" not in i else i for i in this]
except IndexError or ValueError:
    sys.exit()

base = os.path.basename(__file__)
engine = inflect.engine()

def condition():
    dir = [i for i in os.listdir(os.getcwd()) if "Another-One" in i]
    count = len(dir)
    return count < limit

if "Another-One" not in base and condition():
    with open("_Another-One_.pyw" , "w") as f:
        new = f"{os.getcwd()}/{f.name}"
        name = os.path.basename(f.name)
        num = len(name[:name.find("Another")])
        f.writelines(this)
        f.write(f"#this is the {engine.number_to_words(engine.ordinal(num))} one")
elif condition():
    with open(f"_{base[:-4]}_.pyw" , "w") as f:
        new = f"{os.getcwd()}/{f.name}"
        name = os.path.basename(f.name)
        num = len(name[:name.find("Another")])
        f.writelines(this)
        f.write(f"#this is the {engine.number_to_words(engine.ordinal(num))} one")

time.sleep(3/2)
os.startfile(new)
#this is the root