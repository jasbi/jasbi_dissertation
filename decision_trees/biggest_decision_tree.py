from sklearn import tree
from sklearn.utils import shuffle
import pandas as pd
from collections import Counter
import graphviz
import numpy as np
from matplotlib import pyplot as plt


# Speech Act to Numbers
def speech_act_to_float(string):
    if string in acts:
        return acts[string]
    elif len(acts.keys()) == 0:
        acts[string] = 0
        return acts[string]
    else:
        acts[string] = max(acts.values()) + 1
        return acts[string]


# Speech Act to Numbers
def consistency_to_float(string):
    if string in cons:
        return cons[string]
    elif len(cons.keys()) == 0:
        cons[string] = 0
        return cons[string]
    else:
        cons[string] = max(cons.values()) + 1
        return cons[string]


def utterance_type_to_float(string):
    if string in uts:
        return uts[string]
    elif len(uts.keys()) == 0:
        uts[string] = 0
        return uts[string]
    else:
        uts[string] = max(uts.values()) + 1
        return uts[string]


def syn_level_to_float(string):
    if string in syns:
        return syns[string]
    elif len(syns.keys()) == 0:
        syns[string] = 0
        return syns[string]
    else:
        syns[string] = max(syns.values()) + 1
        return syns[string]


def connective_meaning_to_float(string):
    if string in cons:
        return cons[string]
    elif len(cons.keys()) == 0:
        cons[string] = 0
        return cons[string]
    else:
        cons[string] = max(cons.values()) + 1
        return cons[string]


def annotation_to_float(string):
    if string in anns:
        return anns[string]
    elif len(anns.keys()) == 0:
        anns[string] = 0
        return anns[string]
    else:
        anns[string] = max(anns.values()) + 1
        return anns[string]


# THE WORKHORSE
# Step 1: Builds decision tree of depth 2 using 200 training data points
# Step 2: Predict the exclusivity of 200 examples using 200 testing data points
# Step 3: Count number of true positives, false positives, false negatives, and true negatives
# Step 4: Report that information
def clf_accuracy(train, test):
    clf = tree.DecisionTreeClassifier(max_depth=6)
    clf = clf.fit(train[0],train[1])
    actual = test[1].values.flatten().tolist()
    predicted = clf.predict(test[0])
    accuracy = actual == predicted
    fp = 0 # False positive
    fn = 0 # False negative
    for index, a in enumerate(predicted):
        b = actual[index]
        if a and not b:
            fp += 1
        if not a and b:
            fn += 1
    c = Counter(accuracy)
    n = float(len(accuracy))
    return clf, c[True]/n, c[False]/n, fp / n, fn / n


# Prints a pretty decision tree plot
def print_plot(clf,i):
    dot_data = tree.export_graphviz(clf, out_file=None,
                                    feature_names=['consistency','intonation','annotation','speech_act'],
                                    class_names=['AND', 'XOR', 'NOR', 'IOR', 'NPQ', 'XNOR'],
                                    filled=True, rounded=True,
                                    special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render('plots/'+str(i))

# IMPORT DATA
all_data = pd.read_csv("providence_merged.csv")
data = all_data[['speech_act','consistency', 'utterance_type','intonation','syn_level','connective_meaning','annotation']]

# CONVERT DATA TEXT TO INT
acts = {}
data['speech_act'] = data['speech_act'].apply(speech_act_to_float)
print acts
cons = {}
data['consistency'] = data['consistency'].apply(consistency_to_float)
uts = {}
data['utterance_type'] = data['utterance_type'].apply(utterance_type_to_float)
syns = {}
data['syn_level'] = data['syn_level'].apply(syn_level_to_float)
cons = {}
data['connective_meaning'] = data['connective_meaning'].apply(connective_meaning_to_float)
anns = {}
data['annotation'] = data['annotation'].apply(annotation_to_float)

# Define some containers
# These are useful containers for tracking our data as we run randomization
c = 300
sums = []
fpt = 0
fnt = 0
aa = []
clfs = []
maxxx = 100
maxx = 301

# RANDOMIZATION
# Step 1: Shuffle the exclusive and inclusive examples
# Step 2: Select up to 25 exclusive and up to 25 inclusive examples for training
# Step 3: Select  exclusive and 100 inclusive examples for testing
# Step 4: Run the "Clf_accuracy" function on this training and testing data
# Step 5: Add this data to the containers
while c < maxx:
    cc = 0
    sum = 0
    if c % 10 == 0:
        print c
    while cc < maxxx:
        shuffled = shuffle(data)
        train   = shuffled.iloc[:c]
        test    = shuffled.iloc[c:]
        tr = [train[['consistency', 'intonation','annotation','speech_act']],train['connective_meaning']]
        te = [test[['consistency','intonation','annotation','speech_act']],test['connective_meaning']]
        clf, a, b, fp, fn = clf_accuracy(tr, te)
        if c == maxx - 1:
            aa.append(a)
            clfs.append(clf)
            fpt += fp
            fnt += fn
        sum += a
        cc+=1
    sums.append(sum/maxxx)
    c+=1

# Print final avg accuracy, avg false positive rate, avg false negative rate
print sum/maxxx
print fpt/maxxx
print fnt/maxxx

# Print max accuracy, plot most accurate tree
print max(aa)
val = np.argmax(aa)
print_plot(clfs[val],0)

# sums.insert(0, 0.5)
# print sums
# plt.plot(range(0,maxx,1),sums,label='tree performance')
# plt.plot(range(0,maxx,1),[0.8]*maxx,'--g')
# axes = plt.gca()
# axes.set_ylim([0.5,1])
# plt.xlabel('Number of Examples')
# plt.ylabel('Accuracy')
# plt.show()