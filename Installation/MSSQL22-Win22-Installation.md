# Kundenprojekt MSSQL22 in Windows Server 2022 Installation

## Die Vorgaben meines Kunden waren: 
- Zweck der Installation: Unterstützung einer geschäftskritischen Anwendung mit hohen Verfügbarkeits- und Leistungsanforderungen.
- Datenschutz: Einhaltung spezifischer Datenschutzstandards (konkret DSGVO, spezielle Richtlinien besonders schutzwürdiger, medizinischer Daten).
- Zugriffskontrolle: Sichere Zugriffssteuerung für Administratoren und Endbenutzer der Anwendung.
- Disaster Recovery: Vorgaben für Wiederherstellungszeiten (RTO) und Datenverlusttoleranzen (RPO).

## Verwendete Technologien:
- Betriebssystem: Windows Server 2022.
- Datenbank-Software: Microsoft SQL Server 2022.
- Überwachungs- und Verwaltungstools: SQL Server Management Studio (SSMS), Performance Monitor, Extended Events, SQL Server Agent.
- Sicherheitswerkzeuge: Windows Defender, SSL/TLS für Verschlüsselung, SQL Server Audit.
- Proof of Concept Erstellung mit VMware Workstation 17 Player

## OS Sicherheit und Linux Hardening:
- Netzwerksicherheit:
  - Konfiguration der Windows-Firewall, um nur spezifische Ports zuzulassen (u.a. Ändern des Default Ports 1433).
  - Einsatz von IPSec für sichere Remote-Verbindungen.
    
- Authentifizierung und Zugriffssteuerung:
  - Einsatz der gemischten Authentifizierung (Windows-Authentifizierung und SQL-Authentifizierung).
  - Verwendung von starken Passwörtern für alle Accounts.
  - Prinzip der minimalen Rechte für Benutzer und Dienste.
  - Einrichtung von Rollenbasiertem Zugriff (RBAC).
 
- Datenverschlüsselung:
  - Transparent Data Encryption (TDE) zum Schutz der Ruhe-Daten.
  - SSL/TLS zur Verschlüsselung der Datenübertragung.

- Überwachung und Auditing:
  - Konfiguration des SQL Server Audits, um Zugriffe und sicherheitsrelevante Ereignisse zu protokollieren.

## Performance des SQL Servers
- Anpassung der Größe und des Wachstums der Datenbankdateien und Logs.
- Einsatz von In-Memory OLTP für hochperformante Transaktionsverarbeitung, falls benötigt.
- Planung und Beratung bezüglich Hardware-Kauf und physische Installation in Firma
- Analyse vorheriger Datenbanken um den Workflow der Applikation zu verstehen
- Optimierung alter Queries bezüglich Zeit und Ressourcennutzung
- Anpassung Max Memory, Cost Threshold & Max Degree of Parallelism, Erweiterung TempDB
- Automatisierung Indexwartung



## Dokumentation
- Ausführliche Dokumentation aller getätigten Schritte im firmeninternen Sharepoint














Verwendete Quellen:
- https://learn.microsoft.com/de-de/windows-server/get-started/editions-comparison-windows-server-2022?tabs=full-comparison
