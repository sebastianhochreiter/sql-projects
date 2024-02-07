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
- Planung und Beratung bezüglich Hardware-Kauf und physische Installation in Firma
- Analyse vorheriger Datenbanken um den Workflow der Applikation zu verstehen
- Optimierung alter Queries bezüglich Zeit und Ressourcennutzung
- Anpassung Max Memory, Cost Threshold & Max Degree of Parallelism, Erweiterung TempDB
- Automatisierung Indexwartung

## Backups
- Anlegen Server Agents für automatische Sicherung NICHT möglich, da Linux System
- Aktivierung von SQL Server Agent und Erstellung Job für automatische Sicherung
- Tägliche Sicherung in der Nacht in diesem Fall völlig ausreichend
- Email-Notificatin falls Sicherung fehlschlägt

## Dokumentation
- Ausführliche Dokumentation aller getätigten Schritte im firmeninternen Jira und Confluence














Verwendete Quellen:
- https://learn.microsoft.com/de-de/sql/linux/sql-server-linux-setup?view=sql-server-ver16
- https://learn.microsoft.com/de-de/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver16
- https://www.mssqltips.com/sqlservertip/4891/sql-server-installation-best-practices/
- https://www.bu.edu/csmet/files/2021/02/SQL-Server-2019-Installation-Guide.pdf
- https://www.thomas-krenn.com/de/wiki/Absicherung_eines_Debian_Servers
- https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-run-sql-server-agent-job?view=sql-server-ver16
- https://www.sqlskills.com/blogs/paul/wait-statistics-or-please-tell-me-where-it-hurts/