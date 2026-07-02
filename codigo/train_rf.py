#!/usr/bin/env python3
import json, pickle, numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (confusion_matrix, accuracy_score,
    precision_recall_fscore_support)
import os
A=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),"artifacts"); os.makedirs(A,exist_ok=True)
d=np.load(A+"/data.npz"); meta=pickle.load(open(A+"/meta.pkl","rb"))
classes=meta["classes"]; feat=meta["feature_cols"]
Xtr,Xte,ytr,yte=d["X_tr"],d["X_te"],d["y_tr"],d["y_te"]
rf=RandomForestClassifier(n_estimators=200, random_state=42, n_jobs=-1, class_weight="balanced")
rf.fit(Xtr,ytr)
yp=rf.predict(Xte)
acc=accuracy_score(yte,yp)
P,R,Fs,_=precision_recall_fscore_support(yte,yp,labels=range(len(classes)),zero_division=0)
mp,mr,mf,_=precision_recall_fscore_support(yte,yp,average="macro",zero_division=0)
cm=confusion_matrix(yte,yp,labels=range(len(classes)))
perclass={classes[i]:{"precision":float(P[i]),"recall":float(R[i]),"f1":float(Fs[i])} for i in range(len(classes))}
imp=sorted(zip(feat, rf.feature_importances_), key=lambda x:-x[1])
out={"model":"RandomForest","accuracy":float(acc),"macro_precision":float(mp),
     "macro_recall":float(mr),"macro_f1":float(mf),"per_class":perclass,
     "confusion_matrix":cm.tolist(),"classes":classes,
     "feature_importance":[[c,float(v)] for c,v in imp]}
json.dump(out, open(A+"/rf_results.json","w"), indent=2, ensure_ascii=False)
with open(A+"/rf_model.pkl","wb") as fh: pickle.dump(rf, fh)
print("RF acc=%.4f macroF1=%.4f"%(acc,mf))
for c in classes: print("  %-15s P=%.3f R=%.3f F1=%.3f"%(c,perclass[c]["precision"],perclass[c]["recall"],perclass[c]["f1"]))
print("TOP10:", [c for c,_ in imp[:10]])
print("OK rf")
