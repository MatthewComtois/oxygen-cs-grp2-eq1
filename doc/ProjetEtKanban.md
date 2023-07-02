# Création d’un projet et du tableau Kanban dans GitHub

## Choix des colonnes Kanban
Pour les choix de colonnes, nous avons décidé de seulement aller avec les cinq colonnes de base, soit
Backlog, À faire, En cours, Revue, Terminée. Notre résonnement primaire est que si on complique trop 
le kanban, lors de la période d'adoption, les gens vont être moins portés à l'utiliser correctement. 
Quand nous allons voir que le tableau Kanban sera une contrainte à l'atteinte de nos objectifs 
de devops, nous allons pouvoir ajouter plus de colonnes pour avoir plus d'information. Par exemple, on 
pourrait diviser chaque colonne présente actuellement pour savoir si une tâche est en cours ou en attentes.

## Choix de l'automatisation
Comme mentionné dans l'énoncé du laboratoire, nous devions créer deux déclencheurs, soit un sur la colonne
Backlog lors de l'ouverture d'une tâche et un sur la colonne Terminée lors de la fermeture d'une tâche. 
Nous avons donc ajouté ses deux worckflow. Quand une tâche est créée, elle est automatiquement mise dans la
colonne Backlog. Quand une tâche est fermée, elle est automatiquement mise dans la colonne Terminée.