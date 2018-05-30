import string
import naive_bayes_classifier



def recommendations():
    classified = [
        "what's up?",
        "Your son is in hospital, recall us please $100 call award"
    ]
    f = open('spam.txt', encoding='utf-8', newline='')
    text = f.read()
    X_train = []
    y_train = []
    X_test = []
    lines = text.split('\n')
    for message in  lines :
        buff = message.split('\t', 1)
        X_train.append(buff[1])
        y_train.append(message.split('\t', 1)[0])
    for message in classified:
        X_test.append(message)

    model = naive_bayes_classifier.NaiveBayesClassifier(0.05)
    model.fit(X_train, y_train)
    y = model.predict(X_test)

    print(y)

recommendations()