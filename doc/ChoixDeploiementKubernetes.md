# Choix relié au fichier de Kubernetes

Ce document explique les différents choix reliés à l'implémentation et la création des fichiers de Kubernetes.

## Application oxygen-cs
Pour les variables d'environnement, nous avons créé deux fichiers. Un fichier, "oxygencs-secret.yaml" sert à 
inscrire les variables que nous voulons protégées. C'est pourquoi les variables doivent être inscrites en Base 64.
Ensuite, il y a le fichier "oxygencs-config-map.yaml". C'est dans ce fichier qu'on nous indiquons les variables 
d'environnement qui sont moins critique ou que nous n’avons pas nécessairement besoin de garder en secrets.

Pour le déploiement de oxygen-cs, nous avons créé un fichier. Le fichier "oxygencs-deployment.yaml" permet de 
créer et déployer automatiquement l'image avec le tag "latest" se trouvant sur Docker Hub. Il va aussi chercher 
les variables que nous avons définies dans les différents fichiers de "Secret" et de "ConfigMap". 

## Base de données
Pour les variables d'environnement, nous avons créé un fichier pour les secrets nommé "mysql-secret.yaml". C'est
dans ce fichier que nous définissent l'utilisateur et le mot de passe que nous voulons utiliser pour la 
connexion à la base de données. Encore une fois, c'est pour des raisons de sécurité que nous les mettons dans 
des secrets de Kubernetes. Aussi, ils doivent être inscrits dans le fichier en Base 64.

Pour la base de données, nous avons décidé de faire deux fichiers. Un fichier qui permet de créer le pods de la
base de données, soit "mysql-pod.yaml. Ce fichier permet d'aller chercher l'image de la base de données et la 
déployer sur Kubernetes en tant que pod. Ensuite, nous avons aussi créé un fichier "msql-service.yaml" qui 
permet de créer le service de la base de données. Ceci permet, en autre, notre autre pods de communiquer avec
la base de données.