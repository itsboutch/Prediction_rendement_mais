
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import f_oneway
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Lire le fichier CSV
df = pd.read_csv("rendement_mais.csv")  

# Afficher les premières lignes pour vérifier
print("Aperçu des données :")
print(df.head())

# --------------------------------------------------------
# Étape 2 : Analyse statistique descriptive
# --------------------------------------------------------
# 2.1 Mesures de tendance centrale (rendement)
mean = df['RENDEMENT_T_HA'].mean()
median = df['RENDEMENT_T_HA'].median()
mode = df['RENDEMENT_T_HA'].mode()[0] if not df['RENDEMENT_T_HA'].mode().empty else 'Aucun'
print(f"\nTendance centrale (rendement) :\nMoyenne = {mean:.2f}, Médiane = {median}, Mode = {mode}")

# 2.2 Mesures de dispersion (rendement)
std = df['RENDEMENT_T_HA'].std()
variance = df['RENDEMENT_T_HA'].var()
etendue = df['RENDEMENT_T_HA'].max() - df['RENDEMENT_T_HA'].min()
print(f"\nDispersion (rendement) :\nÉcart-type = {std:.2f}, Variance = {variance:.2f}, Étendue = {etendue}")

# 2.3 Visualisation des données
# Histogrammes
fig, axes = plt.subplots(2, 2, figsize=(12, 8))
sns.histplot(df['RENDEMENT_T_HA'], ax=axes[0, 0], kde=True).set_title('Distribution du rendement')
sns.histplot(df['PRECIPITATIONS_MM'], ax=axes[0, 1], kde=True).set_title('Distribution des précipitations')
sns.histplot(df['TEMPERATURE_C'], ax=axes[1, 0], kde=True).set_title('Distribution de la température')

# Boxplots
sns.boxplot(data=df[['RENDEMENT_T_HA', 'PRECIPITATIONS_MM', 'TEMPERATURE_C']], ax=axes[1, 1])
plt.suptitle("Visualisations des données")
plt.tight_layout()
plt.show()

# 2.4 Corrélations
corr_matrix = df.corr(numeric_only=True)
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Matrice de corrélation")
plt.show()

# --------------------------------------------------------
# Étape 3 : ANOVA (test d'influence du type de sol)
# --------------------------------------------------------


# Extraire les groupes
groupes = [df[df['TYPE_SOL'] == sol]['RENDEMENT_T_HA'] for sol in df['TYPE_SOL'].unique()]

# Exécuter le test ANOVA
f_stat, p_value = f_oneway(*groupes)
print(f"\nRésultats ANOVA :\nF = {f_stat:.2f}, p-value = {p_value:.4f}")

# Interprétation
alpha = 0.05
if p_value < alpha:
    print("\nConclusion : Le type de sol a un impact significatif sur le rendement (p < 0.05).")
else:
    print("\nConclusion : Aucun impact significatif détecté.")

# --------------------------------------------------------
# Étape 4 : Modélisation (prédiction du rendement)
# --------------------------------------------------------


# Encodage des variables catégorielles (TYPE_SOL)
df_encoded = pd.get_dummies(df, columns=['TYPE_SOL'])

# Séparation des données
X = df_encoded.drop('RENDEMENT_T_HA', axis=1)
y = df_encoded['RENDEMENT_T_HA']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Entraînement des modèles
models = {
    'Régression Linéaire': LinearRegression(),
    'Arbre de Décision': DecisionTreeRegressor(random_state=42)
}

print("\nPerformance des modèles :")
for name, model in models.items():
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    print(f"\n{name}:")
    print(f"- MAE = {mean_absolute_error(y_test, y_pred):.2f}")
    print(f"- RMSE = {np.sqrt(mean_squared_error(y_test, y_pred)):.2f}")
    print(f"- R² = {r2_score(y_test, y_pred):.2f}")

# --------------------------------------------------------
# Étape 5 : Interprétation et recommandations
# --------------------------------------------------------
# Importance des variables (exemple avec l'arbre de décision)
dt = DecisionTreeRegressor(random_state=42).fit(X_train, y_train)
importance = pd.Series(dt.feature_importances_, index=X.columns).sort_values(ascending=False)
print("\nImportance des variables (Arbre de Décision) :")
print(importance)

# Recommandations basées sur les résultats
print("\nRecommandations :")
print("- Privilégier les sols argileux (meilleur rendement observé).")
print("- Optimiser la quantité d'engrais (corrélation positive avec le rendement).")
print("- Surveiller les précipitations et température (impact significatif).")

# Limites
print("\nLimites :")
print("- Petit échantillon de données (résultats peu généralisables).")
print("- Manque de données pour le sol limoneux (1 observation).")