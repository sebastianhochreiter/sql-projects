# Kundenprojekt bestehende SQL Server Instanz automatisierte Integrity Checks


**Vorgaben des Kunden:**
1. **Zeitfenster für die Wartung:** Der Kunde gibt an, dass die Wartung außerhalb der Geschäftszeiten erfolgen muss, um die Produktivität nicht zu beeinträchtigen.
2. **Fehlerbehandlung:** Der Kunde erwartet klare Protokollierung und Benachrichtigungen im Falle von Fehlern während des CheckDB-Prozesses.
3. **Compliance-Anforderungen:** Es gibt spezifische Compliance-Anforderungen, die berücksichtigt werden müssen, konkret: regelmäßige Datenüberprüfungen nach PCI-DSS (Payment Card Industry Data Security Standard).

**Verwendete Technologien:**
1. **SQL Server Agent:** Dies ist ein SQL Server-Dienst, der Aufträge planen und automatisieren kann. Es wird verwendet, um den CheckDB-Job zu planen und zu automatisieren.
2. **SQL Server Management Studio (SSMS):** SSMS wird verwendet, um den CheckDB-Job zu erstellen und zu konfigurieren.
3. **Transact-SQL (T-SQL):** T-SQL wird verwendet, um den eigentlichen CheckDB-Befehl zu erstellen und in einem SQL Server-Agentenjob auszuführen.

**Monitoring & Logging:**
1. **SQL Server-Agent-Protokolle:** Überwache die Ausführungsprotokolle des SQL Server-Agents, um sicherzustellen, dass der CheckDB-Job gemäß Zeitplan ausgeführt wird. Überprüfe auf Fehlermeldungen oder Warnungen.
2. **SQL Server-Fehlerprotokolle:** Überwache die SQL Server-Fehlerprotokolle, um Fehler während des CheckDB-Prozesses zu erfassen und zu analysieren.
3. **Benachrichtigungen:** Konfiguriere Benachrichtigungen im SQL Server-Agenten, um bei erfolgreicher oder fehlgeschlagener Ausführung des CheckDB-Jobs E-Mails an Administratoren zu senden.
4. **Protokollierung:** Protokolliere detaillierte Informationen über die Ausführung des CheckDB-Jobs, einschließlich Startzeit, Endzeit, Dauer und Ergebnisse. Dies kann in einer speziellen Datenbanktabelle oder in Textdateien erfolgen.
5. **Health Checks:** Verwende Überwachungstools von Drittanbietern oder eingebaute SQL Server-Überwachungsfunktionen, um die allgemeine Gesundheit der Datenbank zu überwachen und sicherzustellen, dass CheckDB erfolgreich durchgeführt wurde.

Durch die Berücksichtigung dieser Punkte können Kundenanforderungen erfüllt und eine zuverlässige und effiziente regelmäßige Überprüfung der Datenbankintegrität mit dem CheckDB-Prozess gewährleistet werden.


## Dokumentation
- Sämtliche Änderungen und Verbesserungen wurden, wie vom Kunden gewünscht, als Textdatei nach Abschluss der Arbeiten versandt.















Verwendete Quellen:
- https://www.bsasoftware.com/wp-content/uploads/2017/08/sqlservermaintenance.pdf
- https://www.mssqltips.com/sqlservertutorial/2210/maintenance-tasks-for-sql-server/
- https://ola.hallengren.com/sql-server-index-and-statistics-maintenance.html
- https://learn.microsoft.com/en-us/sql/relational-databases/maintenance-plans/maintenance-plans?view=sql-server-ver16
- https://learn.microsoft.com/de-de/sql/t-sql/database-console-commands/dbcc-checkdb-transact-sql?view=sql-server-ver16
