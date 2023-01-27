from textblob.classifiers import NaiveBayesClassifier

#tag data sets 
dataset = [
            ("Pogi", "positive"),
            ("ganda", "positive"),
            ("maganda", "positive"),
            ("Magaling", "positive"),
            ("Mabait", "positive"),
            ("Matino", "positive"),
            ("Nakabibighani", "positive"),
            ("Bayani", "positive"),
            ("Matalino", "positive"),
            ("Maniwala", "positive"),
            ("Pahimakas", "positive"),
            ("Tadhana", "positive"),
            ("Magkaugnay", "positive"),
            ("Marahuyo", "positive"),
            ("Mutya", "positive"),
            ("Tinatangi", "positive"),
            ("Dayang", "positive"),
            ######## NEGATIVE
            ("tanga", "negative"),
            ("bobo", "negative"),
            ("hindi marunong", "negative"),
            ("hindi nag tuturo", "negative"),
            ("sakit ", "negative"),
            ("nakaktakot", "negative"),
            ("uto uto", "negative"),
            ("hindi namamansin", "negative"),
            ("nagagalit", "negative"),
            ("panget", "negative"),
        ######## NEURAL
            ("I am neutral on this item.", "neutral")
        ]


cl = NaiveBayesClassifier(dataset)
print(cl.classify("ang ganda ng aso"))
print(cl.accuracy(dataset))
