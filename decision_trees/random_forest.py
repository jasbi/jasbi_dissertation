from sklearn.ensemble import RandomForestClassifier as rfc
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_curve, auc
import pandas as pd
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

# IMPORT DATA
all_data = pd.read_csv("providence_merged.csv")
data = all_data[['speech_act','consistency', 'utterance_type','intonation','syn_level','connective_meaning','annotation']]

# CONVERT DATA TEXT TO INT
acts = {}
data['speech_act'] = data['speech_act'].apply(speech_act_to_float)
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

# Select input and target
X = data[['consistency', 'intonation','annotation','speech_act']]
y = np.squeeze(data[['connective_meaning']])

# TREE DEPTH
# Random Forest Classification
# n_samples = 50
# max_depth = 15
# depths = range(1,max_depth+1)
# scores = []
# for i in depths:
#     mean = 0
#     for j in range(n_samples):
#         clf = rfc(max_depth=i,max_features=None)
#         clf.fit(X,y)
#         mean += clf.score(X,y)
#     scores.append(mean/n_samples)
# plt.plot(depths,scores)
# plt.xlabel('max_depth')
# plt.ylabel('self score')
# plt.title('Evaluation of Tree Depth on Tree Accuracy')
# plt.show()

# TRAINING SIZE
# trains = range(1,301)
# scores = []
# for t in trains:
#     X_train, X_test, y_train, y_test = train_test_split(X,y,train_size=t)
#     clf = rfc(n_estimators=500,max_depth=8,max_features=None)
#     clf.fit(X_train,y_train)
#     scores.append(clf.score(X_test,y_test))
# plt.plot(trains,scores)
# plt.xlabel('number of training samples')
# plt.ylabel('test score')
# plt.title('Effect of Training Size on Tree Accuracy')
# plt.show()

# # N Estimators
# trains = range(1,100)
# scores = []
# for t in trains:
#     mean = 0
#     for i in range(30):
#         X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=100)
#         clf = rfc(n_estimators=t,max_depth=8,max_features=None)
#         clf.fit(X_train,y_train)
#         mean += clf.score(X_test,y_test)
#     scores.append(mean/30)
# plt.plot(trains,scores)
# plt.xlabel('number of estimators')
# plt.ylabel('test score')
# plt.title('Effect of N-Estimators Size on Tree Accuracy')
# plt.show()

# ROC Curve

for i in range(30):
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=100)
    clf = rfc(n_estimators=50,max_depth=8,max_features=None)
    clf.fit(X_train,y_train)
    probs = clf.predict_proba(X_test)[:,1]
    fpr, tpr = roc_curve(y_test,probs)
    plt.plot(fpr, tpr)
plt.xlabel('false positive rate')
plt.ylabel('true positive rate')
plt.title('ROC Curve')
plt.show()
