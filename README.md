# SFM-Selenium-Handler
Usado para facilitar a manipulação do sistema de gestão de chão de fábrica utilizada pela empresa

Com funções de fácil utilização que buscam os xpaths dos elementos

Exemplo:


SFM = WSFM(driver, "usuario1", "senha123")

SFM.abrir("pareto-events-labor-report")

SFM.esperar_apagar_texto("//input[contains(@class, 'form-control input-daterange')]")

SFM.esperar_escrever("//input[contains(@class, 'form-control input-daterange')]", f"{ontem} até {ontem}", True)

SFM.esperar_clicar("//a[text()='Atualizar']")

SFM.esperar_clicar("//a[text()='Filtrar']") 

SFM.esperar_clicar("//a[text()='Filtrar'][1]")

SFM.esperar_clicar("//button[contains(@ng-click, 'export')]") 

sleep(2)

SFM.abrir("efficiency-by-employee-report")

SFM.esperar_escrever("//input[contains(@id, 'dateInitialField')]", ontem, True)

SFM.esperar_escrever("//input[contains(@id, 'dateFinishedField')]", hoje, True)

SFM.esperar_apagar_texto("//input[contains(@id, 'sectionComboboxhierarchy')]")

SFM.esperar_escrever("//input[contains(@id, 'sectionComboboxhierarchy')]", "Secao Caldeiraria Montagem", True)

SFM.esperar_clicar("//span[text()='Gerar relatório']")

SFM.esperar_clicar("//span[text()='Exportar']")

sleep(2)
