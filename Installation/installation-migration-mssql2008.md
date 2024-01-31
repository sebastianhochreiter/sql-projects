# Kundenprojekt MSSQL2008R2 Migration und Installation MSSQL2019

## Die Vorgaben meines Kunden waren: 
Installation von Microsoft SQL Server 2019 auf dem neuen Server, Konfiguration des Servers zur Optimierung für spezifische Anwendungsanforderungen und Anpassung an Best Practices für Sicherheit und Performance. 
Es sollten die Datenbanken inklusive Stored Procedures von einem alten Windows Server mit MSSQL2008 R2 zu einem neueren Server migriert werden.

## Verwendete Technologien:
Debian 11 Minimal (12 hat aktuell keine Kompatibilität mit MSSQL19), MSSQL 2019, MSSQL 2008R2 SSMS 19.3, Azure Data Studio 1.47

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

## Migration
- Konkrete Kompatibilitätsprüfung der Datenbanken, Stored Procedures
- Anpassung der vorhandenen Stored Proccedures
- Anpassung des Kompatibilitätslevels

## Testing nach Migration
- Funktionalitätstests
  - Sample Testing spezifischer Datensätze
  - Stored Procedure Testing inkl. Trigger
  - Anwendungsintegration, CRUD-Testing
- Leistungstests
  - Benchmarking mit Benchmark Factory for Databases
  - Manuelle Abfrageleistungsprüfung
  - Neuerstellung Indizes, da alte nicht kompatibel waren
- Sicherheitstests
  - Prüfung Zugriffskontrolle mit Power Usern
  - Sichtung Audit-Logs
  - Einholung Feedback von User
 



Verwendete Quellen:
- https://www.quest.com/products/benchmark-factory/
- https://www.mssqltips.com/sqlservertip/5346/migrate-sql-server-database-from-windows-to-sql-server-on-linux-in-cloud-part-3/
- https://learn.microsoft.com/en-us/sql/database-engine/install-windows/install-sql-server?view=sql-server-ver16
- https://www.databasedesign-resource.com/sql-server-installation-methods.html
- https://www.thomas-krenn.com/de/wiki/Absicherung_eines_Debian_Servers
- https://learn.microsoft.com/en-us/sql/linux/sql-server-linux-run-sql-server-agent-job?view=sql-server-ver16
- https://www.sqlskills.com/blogs/paul/wait-statistics-or-please-tell-me-where-it-hurts/
