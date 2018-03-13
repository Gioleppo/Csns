from BurglaryModel import *

print("Experiment A")
modelA = BurglaryModel(128, 128, 0.2, 0.56, 0.019)
for i in range(730):
    modelA.step()
    print(str(modelA.avgA)  + "\t" + str(modelA.varA))

print("----------------------------------")
print("Experiment B")
modelB = BurglaryModel(128, 128, 0.2, 5.6, 0.002)
for i in range(730):
    modelB.step()
    print(str(modelB.avgA) + "\t" + str(modelB.varA))

print("----------------------------------")
print("Experiment c")
modelC = BurglaryModel(128, 128, 0.3, 0.56, 0.019)
for i in range(730):
    modelC.step()
    print(str(modelC.avgA) + "\t" + str(modelC.varA))

print("----------------------------------")
print("Experiment D")
modelD = BurglaryModel(128, 128, 0.3, 5.6, 0.002)
for i in range(730):
    modelD.step()
    print(str(modelD.avgA) + "\t" + str(modelD.varA))