# Kundenprojekt MSSQL19 Installation

## Die Vorgaben meines Kunden waren: 
Installation von Microsoft SQL Server 2019 auf dem neuen Server, Konfiguration des Servers zur Optimierung für spezifische Anwendungsanforderungen und Anpassung an Best Practices für Sicherheit und Performance. Nach Abschluss der Installation ist die Einrichtung einer regelmäßigen Backup-Routine für alle Datenbanken erforderlich, sowie die Überprüfung der reibungslosen Verbindung zu bestehenden Anwendungen. Zudem muss eine detaillierte Dokumentation über alle durchgeführten Installationsschritte und Konfigurationseinstellungen für die internen Unterlagen angefertigt werden.

## Verwendete Technologien:
Debian 11 Minimal, MSSQL 2019, SSMS 19.3, Azure Data Studio 1.47

## OS Sicherheit und Linux Hardening:
- Einsetzen von Debian 11 Minimal und Nachinstallation benötigter Pakete, um die Angriffsfläche so gering wie möglich zu halten
- Installation von Apticron um bei Aktualisierungen benachrichtigt zu werden
- SSH absichern inkl. Port Änderung und Email-Notification bei Login
- Installation von fail2ban sowie ufw
- Installation sowie Konfiguration von Monit zur ständigen Überwachung
- Konstante Kontrolle mit lynis und tripwire















Verwendete Quellen:
- https://learn.microsoft.com/de-de/sql/linux/sql-server-linux-setup?view=sql-server-ver16
- https://learn.microsoft.com/de-de/sql/sql-server/editions-and-components-of-sql-server-2019?view=sql-server-ver16
- https://www.mssqltips.com/sqlservertip/4891/sql-server-installation-best-practices/
- https://www.bu.edu/csmet/files/2021/02/SQL-Server-2019-Installation-Guide.pdf
- https://www.thomas-krenn.com/de/wiki/Absicherung_eines_Debian_Servers
