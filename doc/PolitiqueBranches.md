# Choix et politique des branches

La politique de gestion des branches est un aspect essentiel de la gestion du code source dans un projet. Voici notre choix de branches et la justification de notre politique de branche :

1. **main** : La branche "main" est notre branche principale et représente la version de production stable de notre projet. Cette branche contient uniquement le code qui a été testé, validé et prêt à être déployé en production. Elle est protégée et ne peut recevoir de modifications directes. Les mises à jour de cette branche se font via des pull requests provenant de la branche "develop".
2. **develop** : La branche "develop" est notre branche de développement principale. C'est là que le développement actif du projet a lieu. Toutes les fonctionnalités, les correctifs de bogues et les améliorations sont développés dans cette branche. Une fois qu'une fonctionnalité est considérée comme prête pour les tests, elle est fusionnée dans la branche "develop" via un pull request. La branche "develop" peut contenir du code en cours de développement et peut être déployée sur des environnements de test ou de préproduction pour des tests supplémentaires.
3. **features/metric_pull-request** : Cette branche est utilisée pour développer et tester la fonctionnalité liée aux métriques des pull requests. Les développeurs travaillent sur cette branche de manière isolée pour ajouter, modifier ou résoudre des problèmes liés aux métriques des pull requests. Une fois que la fonctionnalité est développée et testée localement, un pull request est créé pour fusionner les changements dans la branche "develop".
4. **features/DocumentationsMatt** : Cette branche est utilisée par un développeur nommé Matt pour travailler sur les améliorations de la documentation. Il peut ajouter, modifier ou réorganiser la documentation du projet sur cette branche. Lorsque les modifications sont terminées, Matt crée un pull request pour fusionner les changements dans la branche "develop".
5. **features/metrique_visualisation** : Cette branche est utilisée pour développer et tester la fonctionnalité de visualisation des métriques. Les développeurs travaillent sur cette branche pour ajouter, modifier ou résoudre des problèmes liés à la visualisation des métriques. Une fois que la fonctionnalité est prête, un pull request est créé pour fusionner les changements dans la branche "develop".

Notre politique de branche suit une approche de gestion du workflow Git basée sur les branches "main" et "develop". Les fonctionnalités sont développées dans des branches distinctes et fusionnées dans la branche "develop" via des pull requests. Cette approche permet une gestion efficace des fonctionnalités en cours de développement, en isolant les modifications et en facilitant la collaboration entre les membres de l'équipe. Les branches spécifiques telles que "features/metric_pull-request", "features/DocumentationsMatt" et "features/metrique_visualisation" permettent une organisation claire du travail et une séparation des responsabilités entre les développeurs travaillant sur différentes fonctionnalités.

En adoptant cette politique de branche, nous nous assurons que notre code reste propre, stable et prêt pour le déploiement en production. De plus, en utilisant des branches distinctes pour le développement de fonctionnalités spécifiques, nous facilitons la gestion des conflits et des tests unitaires pour chaque fonctionnalité avant leur intégration dans la branche principale de développement.