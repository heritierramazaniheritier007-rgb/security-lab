\# security-lab



Python Security Tools for lab practice - offensive and defensive.



!\[Python](https://img.shields.io/badge/Python-3.11+-blue)

!\[Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux-green)

!\[Status](https://img.shields.io/badge/Status-Active-brightgreen)



\---



\## Avertissement legal



Ce projet est destine \*\*uniquement a l'apprentissage en laboratoire isole\*\*

(VMs VirtualBox, reseau prive). Toute utilisation sur des systemes sans

autorisation ecrite est \*\*illegale\*\* et peut entrainer des poursuites penales.



L'auteur decline toute responsabilite en cas d'usage malveillant.



\---



\## Structure du projet





\---



\## Installation



\### Windows



```powershell

pip install pynput



\### Linux

pip3 install --user pynput



\# Windows

python keyloggers/keylogger\_v4.py



\# Linux

python3 keyloggers/keylogger\_v4.py



\# Windows

type %APPDATA%\\Microsoft\\Windows\\Logs\\.cache\_sys.log



\# Linux

cat /tmp/.cache\_sys.log



\# Detection de fichiers caches suspects

python3 detect\_keyloggers/detect\_v1.py



\# Detection de processus Python suspects (Linux uniquement, root conseille)

sudo python3 detect\_keyloggers/detect\_v2.py







\---



\## Competences demontrees



\- Programmation Python (modules, exceptions)

\- Manipulation fichiers cross-platform (`pathlib`, `os`, `sys`)

\- Hooks clavier avec `pynput`

\- Lecture de `/proc` (Linux systeme)

\- Detection comportementale (fichiers + processus)

\- Git (init, add, commit, push, .gitignore)

\- Securite offensive et defensive en environnement isole



\---



\## Auteur



\*\*Heritier Ramazani Christian\*\*

\- GitHub : \[@heritierramazaniheritier007-rgb](https://github.com/heritierramazaniheritier007-rgb)

\- Localisation : Lubumbashi, RDC





