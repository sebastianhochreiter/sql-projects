# Kundenprojekt MSSQL19 Installation

## Die Vorgaben meines Kunden waren: 
Installation von Microsoft SQL Server 2019 auf dem neuen Server, Konfiguration des Servers zur Optimierung für spezifische Anwendungsanforderungen und Anpassung an Best Practices für Sicherheit und Performance. Nach Abschluss der Installation ist die Einrichtung einer regelmäßigen Backup-Routine für alle Datenbanken erforderlich, sowie die Überprüfung der reibungslosen Verbindung zu bestehenden Anwendungen. Zudem muss eine detaillierte Dokumentation über alle durchgeführten Installationsschritte und Konfigurationseinstellungen für die internen Unterlagen angefertigt werden.

## Verwendete Technologien:
Debian 11 Minimal (12 hat aktuell keine Kompatibilität mit MSSQL19), MSSQL 2019, SSMS 19.3, Azure Data Studio 1.47

## OS Sicherheit und Linux Hardening:
- Einsetzen von Debian 11 Minimal und Nachinstallation benötigter Pakete, um die Angriffsfläche so gering wie möglich zu halten
- Installation von Apticron um bei Aktualisierungen benachrichtigt zu werden
- SSH absichern inkl. Port Änderung und Email-Notification bei Login
- Installation von fail2ban sowie ufw
- Installation sowie Konfiguration von Monit zur ständigen Überwachung
- Konstante Kontrolle mit lynis und tripwire

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
