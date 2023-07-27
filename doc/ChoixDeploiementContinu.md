# Choix pipeline de déploiement continu

Ce document explique les différents choix reliés à l'implémentation du pipeline de déploiement continue

## Github Action
Nous avons décidé d'exécuter notre Github Actions de déploiement à chaque fois qu'un push est exécuté 
sur la branche "main" et que le "build" de l'image Docker à fonctionner. La raison est que nous voulons 
seulement déployer l'image sur Kubernetes si une nouvelle image a été "build" et "push" sur Docker Hub. 

Pour ce qui est du Github actions en tant que telles, nous commençons par aller chercher le fichier de 
config que nous avons enregistré en Base 64 dans les secrets de Github. Nous faisons en sorte que le 
fichier de Config soit utilisé par Kubernetes. Nous indiquons ensuite quel contexte utiliser. On finit
par faire le déploiement de l'image construit lors de cette Github Action.