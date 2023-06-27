# LOG-680 : Template for Oxygen-CS

![image](./doc/wheel.png)

This Python application continuously monitors a sensor hub and manages HVAC (Heating, Ventilation, and Air Conditioning) system actions based on received sensor data.

It leverages `signalrcore` to maintain a real-time connection to the sensor hub and utilizes `requests` to send GET requests to a remote HVAC control endpoint.

This application uses `pipenv`, a tool that aims to bring the best of all packaging worlds to the Python world.

## Requierements

- Python 3.8+
- pipenv

## Getting Started

1. Clone the repository :

```
git clone https://github.com/your-username/sensor-hub-monitor.git
cd sensor-hub-monitor
```

2. Install the project's dependencies :

```
pipenv install
```

3. Ajouter les git hook:
```
pip install pytest pylint pre-commit
pre-commit install
```


## Setup

You need to setup the following variables inside the Main class:

- HOST: The host of the sensor hub and HVAC system.
- TOKEN: The token for authenticating requests.
- TICKETS: The number of tickets.
- T_MAX: The maximum allowed temperature.
- T_MIN: The minimum allowed temperature.
- DATABASE: The database connection details.

## Running the Program

After setup, you can start the program with the following command:

```
pipenv run start
```

## Logging

The application logs important events such as connection open/close and error events to help in troubleshooting.

## To Implement

There are placeholders in the code for sending events to a database and handling request exceptions. These sections should be completed as per the requirements of your specific application.


## Wiki

répertoire contenant la documentation dans différents fichiers en format Markdown. Ces fichiers contiennent toutes lesdiverses informations pertinentes au projet.

### Création d’un projet et du tableau Kanban dans GitHub
[Explication des choix des colonnes Kanban et des automatisations](doc/ProjetEtKanban.md)  
### Création des étiquettes
[Explication des choix des étiquettes](doc/ChoixLabel.md)  
### Ajout des modèles 
[Explication du choix du modèle de nouvelle fonctionnalité](doc/ModelNewFeature.md)
[Explication du choix du modèle de correction de bogue](doc/ModelBugFix.md)
[Explication du choix du modèle de nouvelle documentation](doc/ModelDoc.md)
[Explication des choix des modèles Pull Request](doc/ModelPullRequest.md)  
### Création des milestones
[Explication des choix des milestones](doc/ChoixMilestone.md)  
### Politiques de branches 
[Explication des choix de la politique de branche](doc/PolitiqueBranches.md)  
### Création de l’application
[Explication des choix des technologies utilisées pour l’API](doc/ChoixTechnologiques.md)   
### Base de données
[Explication du choix de la DB et le lien avec l’API](doc/ChoixTechnologiques.md)  
### Tests et démonstration 
[Explication des choix de notre suite de test](doc/ChoixTechnologiques.md)  
### Conteneurisation de l'applications 
[Explication des choix technologiques pour la conteneurisation de l'application](doc/ChoixTechnologiques.md)  
### Intégration Continue
[Explication des choix technologiques pour l'intégration continue](doc/ChoixTechnologiques.md)  
### Création des tags de Docker
[Explication des choix pour les tags de Docker](doc/ChoixTagDockerHub.md) 

## License

MIT

## Contact

For more information, please feel free to contact the repository owner.
