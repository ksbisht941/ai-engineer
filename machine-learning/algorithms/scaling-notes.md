**1. When is feature scaling required?**

* When features have **different units or ranges** (e.g., age vs income)
* When using **distance-based algorithms** → KNN, K-Means, SVM
* When using **gradient-based models** → Linear/Logistic Regression, Neural Networks
* When you want **faster convergence** in training
* Not critical for **tree-based models** → Decision Trees, Random Forest, XGBoost

---

**2. When to use Normalization (Min-Max Scaling)?**

* When you need values in a **fixed range** (usually 0 to 1)
* When data has **no significant outliers**
* When using models sensitive to scale like:

  * Neural Networks
  * KNN
* When distribution is **not Gaussian** and you just care about bounds

---

**3. When to use Standardization (Z-score Scaling)?**

* When data is **approximately Gaussian (normal distribution)**
* When dataset has **outliers** (more robust than normalization)
* When using models assuming centered data:

  * Linear Regression
  * Logistic Regression
  * SVM
  * PCA
* When you want features with **mean = 0 and std = 1**

---

**Shortcut memory:**

* **Normalization → bounded (0–1), no outliers**
* **Standardization → centered, handles outliers, works for most models**
* **Tree models → ignore scaling**
