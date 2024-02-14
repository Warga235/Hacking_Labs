Exemples  de commandes Nmap avec des explications détaillées:

```markdown
# Commandes Nmap avec exemples

## 1. Commande de base
```bash
nmap [cible]
```
Effectue un balayage des 1000 ports les plus couramment utilisés sur la cible.

Exemple :
```bash
nmap 192.168.1.100
```

## 2. Balayage de tous les ports
```bash
nmap -p- [cible]
```
Analyse tous les ports de 1 à 65535 sur la cible.

Exemple :
```bash
nmap -p- 10.0.0.1
```

## 3. Balayage rapide
```bash
nmap -F [cible]
```
Effectue un balayage rapide en utilisant les 100 ports les plus couramment utilisés.

Exemple :
```bash
nmap -F 172.16.0.1
```

## 4. Détails sur les services et versions
```bash
nmap -sV [cible]
```
Détecte les versions des services en cours d'exécution sur les ports ouverts.

Exemple :
```bash
nmap -sV 192.168.0.1
```

## 5. Détection du système d'exploitation
```bash
nmap -O [cible]
```
Essaie de deviner le système d'exploitation des hôtes cibles.

Exemple :
```bash
nmap -O 10.10.0.1
```

## 6. Balayage de scripts
```bash
nmap -sC [cible]
```
Exécute les scripts de base pour la détection de services et la collecte d'informations.

Exemple :
```bash
nmap -sC 192.168.2.1
```

## 7. Balayage en mode furtif
```bash
nmap -sS [cible]
```
Utilise un balayage SYN pour éviter les logs d'activité.

Exemple :
```bash
nmap -sS 10.1.0.1
```

## 8. Balayage de version agressif
```bash
nmap -A [cible]
```
Combine l'analyse des services, la détection du système d'exploitation, la version et le script scanning.

Exemple :
```bash
nmap -A 192.168.1.1
```

## 9. Enregistrement de résultats dans un fichier
```bash
nmap -oN resultat_scan.txt [cible]
```
Enregistre les résultats du balayage dans un fichier texte.

Exemple :
```bash
nmap -oN scan_results.txt 10.0.0.1
```

## 10. Balayage avec le mode verbose
```bash
nmap -v [cible]
```
Fournit des détails verbeux pendant le balayage.

Exemple :
```bash
nmap -v 192.168.1.1
```

## 11. Balayage UDP
```bash
nmap -sU [cible]
```
Effectue un balayage des ports UDP sur la cible.

Exemple :
```bash
nmap -sU 192.168.1.1
```

## 12. Personnalisation du fichier de scripts
```bash
nmap --script [nom_script] [cible]
```
Exécute un script spécifique pendant le balayage.

Exemple :
```bash
nmap --script vuln 192.168.1.1
```

## 13. Balayage avec des hôtes aléatoires
```bash
nmap --randomize-hosts -iR 10
```
Sélectionne aléatoirement 10 hôtes à partir de la plage d'adresses spécifiée.

Exemple :
```bash
nmap --randomize-hosts -iR 5 192.168.0.1-50
```

## 14. Ignorer la résolution DNS
```bash
nmap -n [cible]
```
Désactive la résolution DNS pendant le balayage, accélérant le processus.

Exemple :
```bash
nmap -n 10.1.1.1
```

## 15. Utilisation de proxies pour le balayage
```bash
nmap --proxy [proxy_host:proxy_port] [cible]
```
Permet d'effectuer des balayages à travers un proxy.

Exemple :
```bash
nmap --proxy 192.168.1.100:8080 10.0.0.1
```

## 16. Balayage avec des paquets fragmentés
```bash
nmap -f [cible]
```
Divise les paquets pour contourner les systèmes de détection d'intrusion.

Exemple :
```bash
nmap -f 192.168.1.1
```

## 17. Balayage de plage IP
```bash
nmap 192.168.1.1-50
```
Vous pouvez spécifier une plage d'adresses IP pour analyser plusieurs hôtes.

Exemple :
```bash
nmap 192.168.1.1-10
```

## 18. Utilisation de NSE (Nmap Scripting Engine)
```bash
nmap --script [nom_script] [cible]
```
Permet l'exécution de scripts personnalisés pour l'analyse.

Exemple :
```bash
nmap --script http-enum 192.168.1.1
```

## 19. Balayage avec des intervalles de temps
```bash
nmap --scan-delay 10s --max-retries 2 [cible]
```
Ajoute un délai entre les scans pour éviter d'être détecté comme une attaque.

Exemple :
```bash
nmap --scan-delay 5s --max-retries 3 10.0.0.1
```

## 20. Balayage à partir d'une liste de hôtes
```bash
nmap -iL hote.txt
```
Lit les adresses IP à partir d'un fichier et les analyse.

Exemple :
```bash
nmap -iL hosts_list.txt
```

Ces exemples couvrent une gamme variée de scénarios d'utilisation de Nmap. Assurez-vous de comprendre les implications éthiques et de sécurité avant d'utiliser ces commandes dans des environnements réels. Consultez la documentation officielle de Nmap pour des informations plus détaillées sur chaque option.
