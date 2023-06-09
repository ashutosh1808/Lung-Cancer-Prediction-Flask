import pickle

with open("lc.model","rb") as f:
	model=pickle.load(f)

age=float(input("enter age: "))
alc=int(input("(alc): 1-no, 2 yes: "))
pp=int(input("(pp): 1-no, 2 yes: "))
cd=int(input("(cd): 1-no, 2 yes: "))
d=[[age,alc,pp,cd]]
res=model.predict(d)
print(res)