exitUser = '!-[Завершение работы программы пользователем]-!'
text = ''

def actionsWithFile():
    actionWithFile = input('Что делать дальше?\n1 - Вывести содержимое\n2 - Записать текст\n3 - Закрыть файл: ')
    if actionWithFile == '1':
        global startOpenFile
        print(*startOpenFile)
        actionsWithFile()
    if actionWithFile == '2':
        inputText = input('Введите текст: ')
        startOpenFile.write(inputText)
        systemPrint("Успеx")
        startOpenFile.close()
        startOpenFile = open(fileNameEdited, 'r+', encoding="utf-8")
        print(*startOpenFile)
        actionsWithFile()
    if actionWithFile == '3':
        startOpenFile.close()
        systemPrint('Файл был успешно закрыт')
        start()

def systemPrint(text):
    print('!-[' + text + ']-!')

def start():
    startActions = input('Открыть, создать или выйти из программы? [1 / 2 / 3] ')

    if startActions == '1':  # open file
        global fileNameEdited
        global startOpenFile
        fileName = input('Путь к файлу: ')
        fileNameEdited = fileName.replace('"', '')
        # fileNameEdited = fileNameEdited.replace('\\', '/')
        startOpenFile = open(fileNameEdited, 'r+', encoding="utf-8")
        actionsWithFile()
    if startActions == '2':  # create file
        fileName = input('Введите название создаваемого файла (без расширения): ')
        startOpenFile = open(fileName + '.txt', 'w+', encoding="utf-8")
        startOpenFile.close()
        print('!-[Файл создан в одной деректории с PyFileManager]-!')
        start()
    if startActions == '3':  # exit the program
        systemPrint('Завершение...')
        exit(exitUser)

start()