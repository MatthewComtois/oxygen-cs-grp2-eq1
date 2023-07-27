# Création de l’application

Ce document explique les différents choix technologiques faits lors de ce projet

## Choix technologie de l'API

### signalrcore Python
C'est la technologie de base qui était déjà implémentée. Donc, nous avons seulement
continué à l'utiliser.

## Choix technologie de Base de données

### MySQL
Pour le choix de la base de données, nous étions recommandés d'utiliser des bases de 
données relationnelles tels que  PostgreSQL et MySQL. Ayant déjà utilisé MySQL, nous 
avons décidé d'aller avec ce choix. Aussi, nous avions trouvé de la documentation 
pour facilement intégrer une base de données MySQL à un projet en python. Aussi, en
utilisant MySQL, nous uniformisons les bases de données utilisées à travers les 
applications.

## Choix de la suite de test

### Pytest
Ayant déjà utilisé Pytest pour le projet de métrics et voulant garder une uniformité,
nous avons décidé de rester avec Pytest pour la suite de test.

## Choix technologiques pour la conteneurisation de l'application

### Docker
Docker est le standard dans l'industrie pour ce qui est de la conteneurisation 
d'application. C'était donc un choix assez facile à faire. De plus, il est indiqué
dans le laboratoire d'utiliser Docker. En utilisant Docker, nous pouvons aussi
déployé nos images sur Docker hub, ce qui est nécessaire pour la partie d'intégration
continue. Pour ce qui est de la creation de l'image et du build de l'image, nous 
utilisons aussi des fichiers ".dockerignore" et "docker-compose.yml" pour faciliter
le tout et reduire la taille de nos images.

## Choix technologiques pour le déploiement des container de l'application

### Kubernetes
Kubernetes permet de facilement déployer des conteneurs Docker. Il permet aussi de 
facilement faire la gestion et de gérer la gestion de mise en échelle de ces conteneurs.
Nous l'avons choisi primordialement, car c'est la technologie qui est demandée lors du 
laboratoire. Cependant, même si ce choix ne nous était pas imposé, nous aurions quand
même choisi d'utiliser Kubernetes. Nous utilisons différents fichiers de type yaml pour
automatiser la création des pods, des déploiements, des services, des secrets et des
config-map. Nous avons fait cela autant pour la base de données que pour l'application
en soi.

## Choix technologiques pour l'intégration continue

### Pre-commit
Pre-commit permet de facilement générer le fichier de Pre-commit avec une seule 
commande. Ceci permet de facilement uniformiser les pre-commit git hook 
automatisant sa génération.

### Pylint
Étant donné que c'est la technologie recommandée dans le laboratoire et qu'il y a 
beaucoup de documentation pour l'utilisation de Pylint pour les pre-commit et les 
Github Actions, nous avons décidé de choisir cette technologie. Pylint permet 
d'exécuter facilement les étapes de linting et d'analyse de code.

### Black 21.9b0
Étant donné que c'est la technologie recommandée dans le laboratoire et qu'il y a 
beaucoup de documentation pour l'utilisation de Black pour les pre-commit et les 
Github Actions, nous avons décidé de choisir cette technologie. Black permet de 
valider le formatage du code.

### Pytest
Ceci est seulement la même suite de tests que nous utilisons déjà dans le logiciel.
Donc, il est normal que nous continuions à l'utiles pour exécuter les tests lors du
pre-commit git hook.

### Github Action
Nous utilisons les Github Action pour facilement valider la qualité du code,
tester le code, construire l'image Docker et la "push" sur DockerHub lorsque nous 
poussons du code sur notre repo Github ou même quand on créer un pull-request. Les 
Github Action sont un aussi un standard dans l'industrie. C'est une bonne manière 
pour s'assurer la qualité du code présent dans le repo. Aussi, les Github Action 
permettent d'exécuter des actions de manière conditionnelle, ce qui est parfait pour
l'implémentation que nous devions faire.

### Docker Hub
Docker Hub permet de facilement faire la gestion et le partage d'image Docker. C'est 
semblable à github. Étant donné que nous utilisons déjà Docker et que nous devions 
déployer nos images sur Docker hub, nous n'avions pas vraiment le choix de l'utiliser.

## Choix technologiques pour le déploiement continu

### Github Action
Étant donné que nous ont utilisait déjà des Github Action pour l'intégration en
continu, nous avons décidé de continué à l'utiliser pour le déploiement en continu.
Il est aussi pratique de voir à un seul endroit, github, si notre intégration et 
notre déploiement à fonctionner. 