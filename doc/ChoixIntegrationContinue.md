# Choix pipeline d'intégration continue

Ce document explique les différents choix reliés à l'implémentation du pipeline d'intégration continue

## Pre-commit hook
Pour le pre-commit hook, nous utilisons l'outil pre-commit pour généré automatiquement et uniformiser 
les pre-commit hook entre nos différents appareils. Pour ce qui est du pre-commit hook en tant que tel,
il commence par valider le formatage du code à l'aide de Black. Ensuite, il exécute les étapes de 
linting et d'analyse de code à l'aide de Pylint. À la fin, il exécute les tests. Si une des étapes ne
passe pas, le commit n'est pas exécuté.

## Github Action
Nous avons décidé d'exécuter notre Github Actions à chaque fois qu'un push ou qu'un pull request est 
exécuté sur la branch "main" et "develop". La raison pour ne pas le faire sur toutes nos branches est 
que nous utilisons déjà le pre-commit hook sur nos branches locales et ses branches là sont ensuite merge 
dans "develop". Ensuite, nous mergeons seleument "develop" dans "main". Donc, toutes les branches 
devrons passer par le Github Action.

Pour ce qui est du Github actions en tant que telles, nous commençons par exécuté les tests. Si les tests
passent, le Github Action continue, sinon, elle s'arrête là. Ensuite, on exécute les différentes étapes
de validations de code tel que Pylint et Black comme dans notre Pre-commit Hook. Aussi, seulement si 
l'événement qui à déclencher l'action est un push dans la branche "main", on build l'image Docker et on
pousse ensuite l'image sur Docker Hub avec deux tags, soit "latest" et le numéro de build de Github.