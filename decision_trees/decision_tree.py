from sklearn import tree
from sklearn.utils import shuffle
import pandas as pd
from collections import Counter
import graphviz
import numpy as np
from matplotlib import pyplot as plt

# Convert Text to Numbers
def exclusion_to_float(string):
    if string == 'EXC':
        return 1
    else:
        return 0

# Convert Text to Numbers
def utterance_to_float(string):
    if string == 'Declarative':
        return 0
    elif string == 'Interrogative':
        return 1
    elif string == 'Imperative':
        return 2
    else:
        return 2

# Convert Text to Numbers
def exclusivity_to_float(string):
    if string != 'EX' and string != 'IN':
        print string
    if string == 'EX':
        return 1
    else:
        return 0

# Convert Text to Numbers
def synlevel_to_float(string):
    if string == 'SUB':
        return 1
    else:
        return 0

# THE WORKHORSE
# Step 1: Builds decision tree of depth 2 using 200 training data points
# Step 2: Predict the exclusivity of 200 examples using 200 testing data points
# Step 3: Count number of true positives, false positives, false negatives, and true negatives
# Step 4: Report that information
def clf_accuracy(train, test):
    clf = tree.DecisionTreeClassifier(max_depth=2)
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
                                    feature_names=['consistency','intonation','syn_level'],
                                    class_names=['IN', 'EX'],
                                    filled=True, rounded=True,
                                    special_characters=True)
    graph = graphviz.Source(dot_data)
    graph.render('plots/'+str(i))

# IMPORT DATA
alex_data = pd.read_csv("../2_annotated_data/ProvidenceData-alex.csv")
lily_data = pd.read_csv("../2_annotated_data/ProvidenceData-lily.csv")
will_data = pd.read_csv("../2_annotated_data/ProvidenceData-will.csv")
vio_data  = pd.read_csv("../2_annotated_data/ProvidenceData-vio.csv")
naima_data  = pd.read_csv("../2_annotated_data/ProvidenceOR-Naima.csv")
all_data = pd.concat([alex_data, lily_data, will_data, vio_data, naima_data])
data = all_data[['exclusion','intonation','utterance_type','syn_level','exclusivity']]

# CONVERT DATA TEXT TO INT
data['exclusion'] = data['exclusion'].apply(exclusion_to_float)
data['syn_level'] = data['syn_level'].apply(synlevel_to_float)
data['utterance_type'] = data['utterance_type'].apply(utterance_to_float)
data['exclusivity'] = data['exclusivity'].apply(exclusivity_to_float)

# SORT DATA BY EXCLUSIVITY
exx = data[data['exclusivity'] == 1]
inn = data[data['exclusivity'] == 0]

# Define some containers
# These are useful containers for tracking our data as we run randomization
c = 1
sums = []
fpt = 0
fnt = 0
aa = []
clfs = []
maxxx = 100

# RANDOMIZATION
# Step 1: Shuffle the exclusive and inclusive examples
# Step 2: Select up to 25 exclusive and up to 25 inclusive examples for training
# Step 3: Select  exclusive and 100 inclusive examples for testing
# Step 4: Run the "Clf_accuracy" function on this training and testing data
# Step 5: Add this data to the containers
while c < 101:
    cc = 0
    sum = 0
    print c
    while cc < maxxx:
        shuffled = shuffle(data)
        train   = shuffled.iloc[:c]
        test    = shuffled.iloc[c:c+300]
        tr = [train[['exclusion','intonation']],train['exclusivity']]
        te = [test[['exclusion','intonation']],test['exclusivity']]
        clf, a, b, fp, fn = clf_accuracy(tr, te)
        if c == 100:
            aa.append(a)
            clfs.append(clf)
        sum += a
        fpt += fp
        fnt += fn
        cc+=1
    sums.append(sum/maxxx)
    c+=1

# Print avg accuracy, avg false positive rate, avg false negative rate
print sum/100
print fpt/100
print fnt/100

# Print max accuracy, plot most accurate tree
print max(aa)
val = np.argmax(aa)
print_plot(clfs[val],0)

sums.insert(0, 0.5)
print sums
plt.plot(range(0,101,1),sums,label='tree performance')
plt.plot(range(0,101,1),[0.8]*101,'--g')
axes = plt.gca()
axes.set_ylim([0.5,1])
plt.xlabel('Number of Examples')
plt.ylabel('Accuracy')
plt.show()