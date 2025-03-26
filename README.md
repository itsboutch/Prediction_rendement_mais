# Prediction_rendement_mais
# Projet d'Analyse de Rendement du Maïs 🌽

*Ce README résume les résultats du projet et permet de comparer les calculs manuels avec les résultats Python.*

---

## **Aperçu du Projet**
**Objectif** : Prédire le rendement du maïs (en t/ha) en fonction de facteurs comme le type de sol, les précipitations, ou la quantité d'engrais.  

**Jeu de données** :  
- Variables explicatives : `SURFACE_HA`, `TYPE_SOL`, `ENGRAIS_KG_HA`, `PRECIPITATIONS_MM`, `TEMPERATURE_C`.  
- Variable cible : `RENDEMENT_T_HA`.  

---

## **Résultats Clés**

### 1. Statistiques Descriptives
- **Moyenne du rendement** : `7.38 t/ha`  
- **Écart-type** : `2.57`  
- **Étendue** : `8.99 t/ha`  

### 2. Test ANOVA (Type de Sol)
- **Statistique F** : `1.36`  
- **p-value** : `0.2582`  
- **Conclusion** : Aucun impact significatif du type de sol détecté *(p > 0.05)*.  

### 3. Performance des Modèles
| Modèle              | MAE   | RMSE  | R²     |
|---------------------|-------|-------|--------|
| Régression Linéaire | 2.10  | 2.46  | -0.03  |
| Arbre de Décision   | 2.66  | 3.30  | -0.85  |

### 4. Importance des Variables (Arbre de Décision)
1. `ENGRAIS_KG_HA` (31.9%)  
2. `PRECIPITATIONS_MM` (29.2%)  
3. `TEMPERATURE_C` (19.8%)  

---

## **Comparaison Calculs Manuel vs Code**
  
| Étape       | Calcul Manuel (Photo) | Résultat Code | Commentaire |
|-------------|-----------------------|---------------|-------------|
| ANOVA       | ![ANOVA](IMG_8226.jpg) | `F=1.36, p=0.258` | Résultats incohérents |
- C'est normal parce que l'ensemble de données est très différent de l'ensemble du sujet de TD ( Que 5 valeurs )
---

## **Visualisations** 
1. **Histogrammes** :  
   ![Histogramme Rendement](Figure_1.png)  
2. **Heatmap des Corrélations** :  
   ![Heatmap](Figure_2_heatmap.png)  
3. **Boxplots** :  
   ![Boxplots](box_plot.png)  

--- 

## Interprétation des graphiques 📊

### Figure 1 : Distributions des variables clés

#### **Rendement (RENDEMENT_T_HA)**  
- Distribution centrée entre **8 et 10 t/ha**, avec un pic à **8 t/ha**.  
- Quelques valeurs extrêmes (4–6 t/ha et 12 t/ha) pouvant refléter des parcelles sous-optimales ou très productives.  

#### **Température (TEMPERATURE_C)**  
- Plage dominante : **20°C à 24°C**, typique d'un climat tempéré.  
- Peu de valeurs extrêmes (<16°C ou >28°C), suggérant un environnement stable.  

#### **Précipitations (PRECIPITATIONS_MM)**  
- Concentration entre **80 mm et 120 mm**, avec un maximum à **100–120 mm**.  
- Valeurs <80 mm pourraient indiquer des épisodes de sécheresse ponctuels.  

---

### Figure 2 : Matrice de corrélation  
- Corrélations globalement **très faibles** (proches de **0**) entre les variables.  
- Aucun lien linéaire fort détecté entre :  
  - Température et rendement (`TEMPERATURE_C` : **0.01**)  
  - Précipitations et rendement (`PRECIPITATIONS_MM` : **0.03**)  
  - Surface et rendement (`SURFACE_HA` : **1.00**, corrélation attendue car variable redondante).  

🔍 **Implications** :  
- D'autres facteurs non mesurés (sols, pratiques agricoles) pourraient expliquer les variations de rendement.  
- Une analyse des **interactions entre variables** ou des modèles non linéaires serait pertinente.  
