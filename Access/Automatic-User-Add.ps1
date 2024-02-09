# Skript für meinen Kunden
Mein Kunde hatte mehr als 2500 Mitarbeiter in einem Excel File. Die Mitarbeiter sollten automatisiert mit PowerShell einem MSSQL Server hinzugefügt werden

# Pfad zur Excel-Datei
$excelPath = "x\Nutzer.xlsx"

# Importieren der Benutzer aus der Excel-Datei
$users = Import-Excel -Path $excelPath

# Servername
$serverName = "yyy\MSSQLSERVER01"

# Durchlaufen aller Benutzer und Erstellen der Logins und Benutzer in SQL Server
foreach ($user in $users) {
    # SQL-Befehl zum Erstellen eines neuen Logins
    $sqlLoginCommand = "CREATE LOGIN [$($user.Benutzername)] WITH PASSWORD = N'$($user.Passwort)', CHECK_POLICY = OFF;"

    # SQL-Befehl zum Erstellen eines Benutzers in der Datenbank `master` und Zuweisen einer Rolle
    $sqlUserCommand = @"
USE [master];
CREATE USER [$($user.Benutzername)] FOR LOGIN [$($user.Benutzername)];
EXEC sp_addrolemember '$($user.Zugang)', '$($user.Benutzername)';
"@

    # Ausführen der SQL-Befehle
    try {
        Invoke-Sqlcmd -ServerInstance $serverName -Query $sqlLoginCommand
        Invoke-Sqlcmd -ServerInstance $serverName -Query $sqlUserCommand
        Write-Host "Login und Benutzer für $($user.Benutzername) wurden erfolgreich erstellt."
    } catch {
        Write-Error "Fehler beim Erstellen von Login oder Benutzer für $($user.Benutzername): $_"
    }
}

