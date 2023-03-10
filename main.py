from AB import AB

arbreFromInit = AB(10,AB(5,3,AB(8,AB(6,None,7))),12)
# arbreFromInit.afficher()

arbreFromPrefix = AB.initFromPrefix([20,10,8,50,40])
arbreFromPrefix.afficher()