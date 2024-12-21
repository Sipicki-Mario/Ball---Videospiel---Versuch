Sehr geehrte Damen und Herren,

für dieses Projekt brauchen Sie "pygame".
Hiermit zeige ich Ihnen, wie Sie es installieren.

Erstmal werde ich es einfach und dann ausführlicher erklären.

Einfach erklärt:

Um pygame mit pip3 zu installieren, folge diesen einfachen Schritten:
          1. Öffnen Sie das Terminal oder die Eingabeaufforderung / Command Prompt (Win + R).
          2. Geben Sie den folgenden Befehl ein und drücken Sie Enter:
                                          
                                          pip3 install pygame
                     

Danach sollten Sie die Installation in python überprüfen, indem Sie folgenden Code eingeben:

                                          import pygame
                                          pygame.init()
                                          print(pygame.__version__)


Wenn keine Fehler angezeigt werden und die Versionsnummer erscheint, wurde pygame erfolgreich installiert.







Ausführlicher erklärt / Ausführliche Erklärung:

Schritt 1: Sicherstellen, dass python und pip3 installiert sind.
           Python-Version überprüfen: Überprüfen Sie zuerst, ob python3 und pip3 auf Ihrem System installiert sind, indem Sie die folgenden Befehle in Ihrem Terminal oder der Eingabeaufforderung / Command Prompt (Win + R) ausführen:

                   python3 --version
                   pip3 --version

Wenn python3 installiert ist, sollten Sie eine Versionsnummer sehen (z. B. Python 3.x.x). Falls dies nicht der Fall ist, laden Sie python3 von python.org herunter und installieren Sie es.



Schritt 2: pip3 installieren (falls nicht bereits installiert)
           Wenn pip3 nicht installiert ist, können Sie es mit dem folgenden Befehl in Ihrem Terminal oder der Eingabeaufforderung / Command Prompt (Win + R) installieren:

           python3 -m ensurepip --upgrade



Schritt 3: pygame mit pip3 installieren.
           Um pygame mit pip3 zu installieren, führen Sie diesen Befehl in Ihrem Terminal oder der Eingabeaufforderung / Command Prompt (Win + R) aus:

           pip3 install pygame

Dies wird die neueste Version von pygame für python3 herunterladen und installieren.



Schritt 4: Installation überprüfen.
             Um zu überprüfen, ob pygame korrekt installiert wurde, öffnen Sie eine python3-Shell und versuchen Sie, pygame zu importieren:

             python3

Geben Sie dann in der python-Shell ein:

             import pygame
             pygame.init()
             print(pygame.__version__)

Wenn Pygame korrekt / richtig installiert wurde, sollte die Versionsnummer von pygame angezeigt werden, was eine erfolgreiche Installation bestätigt.



Fehlerbehebung (Windows-spezifische Probleme): Wenn Sie Windows verwenden und auf Probleme stoßen, stellen Sie sicher, dass die neuesten Microsoft Visual C++ Build Tools installiert sind.
                                               Diese können Sie auf / von https://visualstudio.microsoft.com/visual-cpp-build-tools/ herunterladen.



Vielen Dank im Voraus für das Lesen und Ansehen meiner Projekte!

Mit freundlichen Grüßen

Mario Sipicki
